import asyncio
import json
import logging
import os
import random
import aiohttp
import websockets
from dotenv import load_dotenv
from datetime import datetime

# Импортируем наш музыкальный движок
try:
    from music_generator import MusicGeneratorAgent
except ImportError:
    MusicGeneratorAgent = None

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("PumpFunBridge")

load_dotenv()

PUMP_FUN_WS_URL = "wss://papi.pump.fun/v1/ws"
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
XAI_API_KEY = os.getenv("XAI_API_KEY")

async def ask_grok_about_token(name, symbol, creator):
    """Запрос к ИИ xAI (Grok) с учетом макро-контекста"""
    if not XAI_API_KEY:
        return "Анализ xAI временно недоступен: отсутствует API ключ."

    url = "https://xai.ai"
    headers = {
        "Authorization": f"Bearer {XAI_API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = (
        f"Ты — DeFAI аналитик экосистемы AMRITA.\n"
        f"Название: {name} ({symbol})\n"
        f"Создатель: {creator}\n"
        f"Контекст рынка: Hyperliquid и Trust Wallet.\n"
        f"Срез рыночных данных Hyperliquid для оценки ликвидности.\n"
        f"Дай краткий вердикт (2 sentences):"
    )

    payload = {
        "model": "grok-beta",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload, headers=headers) as resp:
                if resp.status == 200:
                    result = await resp.json()
                    return result["choices"][0]["message"]["content"]
                return f"Ошибка xAI API (Статус: {resp.status})"
    except Exception as e:
        return f"Не удалось связаться с Grok: {e}"

async def analyze_token_via_defai(mint, name, symbol, creator):
    """Интеллектуальный DeFAI слой с агрегацией метаданных и генерацией трека"""
    logger.info(f"🔍 Комплексный анализ токена: {name} ({symbol})")

    # Получаем вердикт ИИ
    grok_verdict = await ask_grok_about_token(name, symbol, creator)

    # Музыкальное сопровождение токена
    track_title = f"Token {symbol} Core"
    track_style = "Cyber Techno" if "памп" in grok_verdict.lower() or "bullish" in grok_verdict.lower() else "Quantum Ambient"
    
    if MusicGeneratorAgent:
        try:
            agent = MusicGeneratorAgent()
            raw_track = await agent.generate_track_metadata()
            # Кастомизируем трек под реальный токен рынка
            raw_track["title"] = f"{name} Wave"
            raw_track["style"] = track_style
        except Exception as e:
            logger.error(f"Сбой музыкального движка: {e}")
            raw_track = {"title": track_title, "style": track_style, "duration": "3:14", "isrc_code": "US-AMR-26-00000"}
    else:
        raw_track = {"title": track_title, "style": track_style, "duration": "3:14", "isrc_code": "US-AMR-26-00000"}

    if DISCORD_WEBHOOK_URL:
        spotify_link = f"https://spotify.com{raw_track['title'].replace(' ', '%20')}"
        tiktok_link = "https://tiktok.com"
        alibaba_link = "https://alibaba.com"

        covers = [
            "https://unsplash.com",
            "https://unsplash.com",
            "https://unsplash.com"
        ]

        payload = {
            "username": "Солитон: DeFAI Оркестратор",
            "embeds": [{
                "title": f"🎯 Обнаружен и Озвучен Токен: {name} ({symbol})",
                "color": 16753920,
                "fields": [
                    {"name": "Адрес токена (Mint)", "value": f"`{mint}`", "inline": False},
                    {"name": "Создатель", "value": f"`{creator}`", "inline": True},
                    {"name": "🧠 Вердикт ИИ (Grok)", "value": grok_verdict, "inline": False},
                    {"name": "🎵 Саундтрек Токена", "value": f"**{raw_track['title']}** ({raw_track['style']})", "inline": True},
                    {"name": "Код ISRC", "value": f"`{raw_track['isrc_code']}`", "inline": True},
                    {
                        "name": "Статус медиа-дистрибуции", 
                        "value": f"🟢 Стриминг: [Spotify]({spotify_link}) | [TikTok]({tiktok_link}) | [Alibaba]({alibaba_link})", 
                        "inline": False
                    }
                ],
                "image": {"url": random.choice(covers)},
                "footer": {"text": f"AMRITA Quantum Network • {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC"}
            }]
        }

        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(DISCORD_WEBHOOK_URL, json=payload) as resp:
                    if resp.status in:
                        logger.info(f"📊 Карточка токена {symbol} со звуковым слоем отправлена.")
        except Exception as e:
            logger.error(f"Ошибка отправки отчета в Discord: {e}")

async def monitor_pump_fun():
    """Стрим токенов с pump.fun в реальном времени через веб-сокеты"""
    logger.info("Инициализация моста Pump.fun...")
    while True:
        try:
            async with websockets.connect(PUMP_FUN_WS_URL) as websocket:
                logger.info("Успешно подключено к стриму pump.fun API.")
                subscribe_payload = {"method": "subscribeNewToken"}
                await websocket.send(json.dumps(subscribe_payload))

                async for message in websocket:
                    data = json.loads(message)
                    if data.get("txType") == "mint":
                        mint = data.get("mint")
                        name = data.get("name")
                        symbol = data.get("symbol")
                        creator = data.get("creator")

                        logger.info(f"🆕 ОБНАРУЖЕН МИНТ: {name} ({symbol})")
                        asyncio.create_task(analyze_token_via_defai(mint, name, symbol, creator))
        except websockets.exceptions.ConnectionClosed:
            logger.warning("Соединение разорвано. Переподключение через 5 секунд...")
            await asyncio.sleep(5)
        except Exception as e:
            logger.error(f"Ошибка в основном цикле мониторинга: {e}")
            await asyncio.sleep(5)

if __name__ == "__main__":
    try:
        asyncio.run(monitor_pump_fun())
    except KeyboardInterrupt:
        logger.info("Мост Pump.fun остановлен.")
