import asyncio
import json
import logging
import os
from dotenv import load_dotenv
import websockets
import aiohttp

# Настройка логирования под общую стилистику квантового ядра
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("PumpFunBridge")

load_dotenv()

PUMP_FUN_WS_URL = "wss://papi.pump.fun/v1/ws"
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
XAI_API_KEY = os.getenv("XAI_API_KEY") # Добавьте ваш токен xAI в Secrets!

async def ask_grok_about_token(name, symbol, creator):
    """
    Запрос к ИИ xAI (Grok) для экспресс-анализа концепции токена.
    """
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
        f"Учти контекст рынка: MetaMask внедрил Titan Exchange, ликвидность растет. "
        f"Дай краткий вердикт (2 предложения): стоит ли следить за токеном и каков его кросс-чейн потенциал."
    )
    
    payload = {
        "model": "grok-beta", # или актуальная модель на текущий момент
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload, headers=headers) as resp:
                if resp.status == 200:
                    result = await resp.json()
                    return result["choices"][0]["message"]["content"]
                else:
                    return f"Ошибка xAI API (Статус: {resp.status})"
    except Exception as e:
        return f"Не удалось связаться с Grok: {e}"

async def analyze_token_via_defai(mint, name, symbol, creator):
    """
    Интеллектуальный DeFAI слой на базе xAI (Grok).
    Анализирует токен на безопасность и отправляет валидные данные в Discord.
    """
    logger.info(f"🔬 Нейросетевой анализ токена {name} ({symbol}) через xAI Grok...")
    
    # Получаем умный вердикт от ИИ
    grok_verdict = await ask_grok_about_token(name, symbol, creator)
    
    if DISCORD_WEBHOOK_URL:
        payload = {
            "embeds": [{
                "title": "🎯 Обнаружен токен — Экспертиза xAI Grok",
                "color": 16753920,  # Оранжевый цвет в стиле xAI
                "fields": [
                    {"name": "Название", "value": f"{name} ({symbol})", "inline": True},
                    {"name": "Создатель", "value": f"`{creator[:8]}...`", "inline": True},
                    {"name": "Адрес токена (Mint)", "value": f"`{mint}`", "inline": False},
                    {"name": "🧠 Вердикт ИИ-Агента", "value": grok_verdict, "inline": False}
                ],
                "footer": {"text": "AMRITA Quantum Swarm powered by xAI"}
            }]
        }
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(DISCORD_WEBHOOK_URL, json=payload) as resp:
                    if resp.status == 204:
                        logger.info("📢 Карточка ИИ-анализа успешно отправлена в Discord.")
        except Exception as e:
            logger.error(f"Ошибка отправки отчета в Discord: {e}")

async def monitor_pump_fun():
    """
    Асинхронный мост для отслеживания создания токенов.
    """
    logger.info("Инициализация моста Pump.fun в режиме DeFAI + xAI...")
    
    while True:
        try:
            async with websockets.connect(PUMP_FUN_WS_URL) as websocket:
                logger.info("Успешно подключено к WebSocket Pump.fun")
                
                subscribe_payload = {
                    "method": "subscribeNewToken",
                    "params": {}
                }
                await websocket.send(json.dumps(subscribe_payload))
                
                async for message in websocket:
                    data = json.loads(message)
                    
                    if data.get("txType") == "create":
                        mint = data.get("mint", "N/A")
                        name = data.get("name", "Unknown")
                        symbol = data.get("symbol", "Unknown")
                        creator = data.get("traderPublicKey", "Unknown")
                        
                        logger.info(f"🆕 ОБНАРУЖЕН ТОКЕН: {name} ({symbol})")
                        
                        # Асинхронный вызов ИИ-анализатора
                        asyncio.create_task(
                            analyze_token_via_defai(mint, name, symbol, creator)
                        )
                        
        except websockets.exceptions.ConnectionClosed:
            logger.warning("Соединенние разорвано. Повтор через 5 секунд...")
            await asyncio.sleep(5)
        except Exception as e:
            logger.error(f"Ошибка в основном цикле: {e}")
            await asyncio.sleep(5)

if __name__ == "__main__":
    try:
        asyncio.run(monitor_pump_fun())
    except KeyboardInterrupt:
        logger.info("Мост Pump.fun остановлен вручную.")
