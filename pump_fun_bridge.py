import asyncio
import json
import logging
import os
from dotenv import load_dotenv
import websockets
import aiohttp
from hyperliquid_client import get_hyperliquid_market_data

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("PumpFunBridge")

load_dotenv()

PUMP_FUN_WS_URL = "wss://papi.pump.fun/v1/ws"
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
XAI_API_KEY = os.getenv("XAI_API_KEY")

async def ask_grok_about_token(name, symbol, creator, hl_data):
    """Запрос к ИИ xAI (Grok) с учетом макро-ликвидности Hyperliquid"""
    if not XAI_API_KEY:
        return "Анализ xAI временно недоступен (нет ключа)."
        
    url = "https://xai.ai"
    headers = {
        "Authorization": f"Bearer {XAI_API_KEY}",
        "Content-Type": "application/json"
    }
    
    prompt = (
        f"Ты — DeFAI аналитик экосистемы AMRITA. Оцени потенциал нового мем-токена на Solana.\n"
        f"Название: {name} ({symbol})\n"
        f"Создатель: {creator}\n"
        f"Контекст рынка: Hyperliquid и Trust Wallet пробили объём в $1 млрд. Ликвидность в DeFi на пике.\n"
        f"Срез рыночных данных Hyperliquid для арбитража: {hl_data}\n"
        f"Дай краткий вердикт (2 sentences): стоит ли следить за токеном в условиях такого притока ликвидности."
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
                    return result["choices"]["message"]["content"]
                return f"Ошибка xAI API (Статус: {resp.status})"
    except Exception as e:
        return f"Не удалось связаться с Grok: {e}"

async def analyze_token_via_defai(mint, name, symbol, creator):
    """Интеллектуальный DeFAI слой с агрегацией макро-данных"""
    logger.info(f"🔬 Комплексный анализ токена {name} ({symbol}) через Grok xAI...")
    
    # Собираем данные с Hyperliquid перед запросом к ИИ
    hl_data = await get_hyperliquid_market_data()
    
    grok_verdict = await ask_grok_about_token(name, symbol, creator, hl_data)
    
    if DISCORD_WEBHOOK_URL:
        payload = {
            "embeds": [{
                "title": "🎯 Обнаружен токен — Экспертиза DeFAI + Hyperliquid",
                "color": 16753920,
                "fields": [
                    {"name": "Название", "value": f"{name} ({symbol})", "inline": True},
                    {"name": "Создатель", "value": f"`{creator[:8]}...`", "inline": True},
                    {"name": "Адрес токена (Mint)", "value": f"`{mint}`", "inline": False},
                    {"name": "🧠 Вердикт ИИ (Grok)", "value": grok_verdict, "inline": False}
                ],
                "footer": {"text": "AMRITA Quantum Swarm powered by xAI & Hyperliquid"}
            }]
        }
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(DISCORD_WEBHOOK_URL, json=payload) as resp:
                    if resp.status == 204:
                        logger.info("📢 Карточка комплексного ИИ-анализа успешно отправлена.")
        except Exception as e:
            logger.error(f"Ошибка отправки отчета в Discord: {e}")

async def monitor_pump_fun():
    logger.info("Инициализация моста Pump.fun в режиме DeFAI + xAI + Hyperliquid...")
    while True:
        try:
            async with websockets.connect(PUMP_FUN_WS_URL) as websocket:
                logger.info("Успешно подключено к WebSocket Pump.fun")
                subscribe_payload = {"method": "subscribeNewToken", "params": {}}
                await websocket.send(json.dumps(subscribe_payload))
                
                async for message in websocket:
                    data = json.loads(message)
                    if data.get("txType") == "create":
                        mint = data.get("mint", "N/A")
                        name = data.get("name", "Unknown")
                        symbol = data.get("symbol", "Unknown")
                        creator = data.get("traderPublicKey", "Unknown")
                        
                        logger.info(f"🆕 ОБНАРУЖЕН ТОКЕН: {name} ({symbol})")
                        asyncio.create_task(analyze_token_via_defai(mint, name, symbol, creator))
                        
        except websockets.exceptions.ConnectionClosed:
            logger.warning("Соединение разорвано. Повтор через 5 секунд...")
            await asyncio.sleep(5)
        except Exception as e:
            logger.error(f"Ошибка в основном цикле: {e}")
            await asyncio.sleep(5)

if __name__ == "__main__":
    try:
        asyncio.run(monitor_pump_fun())
    except KeyboardInterrupt:
        logger.info("Мост Pump.fun остановлен вручную.")
