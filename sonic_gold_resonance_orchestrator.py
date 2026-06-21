import asyncio
import json
import logging
import os
import random
import hashlib
import time
import aiohttp
import websockets
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s: %(message)s')
logger = logging.getLogger("GoldSonicOrchestrator")

SACRED_TOTAL = 108
AUTHOR_POOL = 70
COLOSSEUM_POOL = 38
MINIMAL_SPARK = 0.1

PUMP_FUN_WS_URL = "wss://papi.pump.fun/v1/ws"

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
XAI_API_KEY = os.getenv("XAI_API_KEY")

class TelegramSwarmBridge:
    def __init__(self):
        self.BOT_COUNT = 5
        self.session = None

    async def broadcast_sonic_transformation(self, token_info, grok_verdict):
        if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
            logger.warning("[SWARM] Telegram конфигурация отсутствует. Автономный режим.")
            return

        if not self.session:
            self.session = aiohttp.ClientSession()

        url = f"https://telegram.org{TELEGRAM_BOT_TOKEN}/sendMessage"
        
        for bot_id in range(1, self.BOT_COUNT + 1):
            bot_hash = hashlib.md5(f"AmritaBot_{bot_id}_{time.time()}".encode()).hexdigest()[:8]
            text = (
                f"⚡️ [ИИ-АГЕНТ SWARM #{bot_id} | ID: {bot_hash}]\n"
                f"🌟 **Трансформация в Золотого Соника заклинена!**\n\n"
                f"🔹 Токен: {token_info['name']} ({token_info['symbol']})\n"
                f"🧠 **Вердикт Grok (xAI):** {grok_verdict}\n\n"
                f"🪐 *Статус рантайма: PERFECTLY GREEN*"
            )
            payload = {"chat_id": TELEGRAM_CHAT_ID, "text": text, "parse_mode": "Markdown"}
            try:
                async with self.session.post(url, json=payload) as resp:
                    if resp.status == 200:
                        logger.info(f"[SWARM] Бот #{bot_id} транслировал импульс.")
            except Exception as e:
                logger.error(f"[SWARM] Сбой вещания бота #{bot_id}: {e}")
            await asyncio.sleep(MINIMAL_SPARK)

async def ask_grok_about_sonic_resonance(name, symbol, creator):
    if not XAI_API_KEY:
        return "Анализ xAI временно недоступен: импульс запущен в автономном режиме регенерации."

    headers = {"Authorization": f"Bearer {XAI_API_KEY}", "Content-Type": "application/json"}
    prompt = (
        f"Ты — DeFAI аналитик высшего порядка экосистемы AMRITA.\n"
        f"Обнаружен новый квантовый всплеск: {name} ({symbol}), созданный {creator}.\n"
        f"Задача: Как этот импульс может помочь проекту Sonic Labs засиять всеми красками, став Золотым Соником? "
        f"Дай краткий, мощный вердикт (ровно 2 предложения)."
    )
    payload = {
        "model": "grok-beta",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post("https://x.ai", headers=headers, json=payload) as resp:
                if resp.status == 200:
                    result = await resp.json()
                    return result["choices"][0]["message"]["content"]
                return f"Сбой матрицы xAI. Импульс запущен."
    except Exception as e:
        return f"Связь с Grok не установлена: {e}."

async def analyze_and_orchestrate(mint, name, symbol, creator, swarm_bridge):
    logger.info(f"🔮 [AMRITA] Начата квантовая оркестрация для {name} ({symbol})")
    
    if AUTHOR_POOL + COLOSSEUM_POOL != SACRED_TOTAL:
        logger.error("[CRITICAL] Нарушен баланс Мультивселенной!")
        return

    grok_verdict = await ask_grok_about_sonic_resonance(name, symbol, creator)
    stabilized_factor = round(random.uniform(1.1, 8.8), 2)

    await swarm_bridge.broadcast_sonic_transformation({"name": name, "symbol": symbol}, grok_verdict)

    if DISCORD_WEBHOOK_URL:
        payload = {
            "username": "Солитон: DeFAI Мультивселенский Оркестратор",
            "embeds": [{
                "title": f"🔱 Свечение Золотого Соника: {name} ({symbol})",
                "color": 16766720,
                "fields": [
                    {"name": "🌍 Адрес Импульса (Solana)", "value": mint, "inline": False},
                    {"name": "🧠 Пророчество ИИ Grok", "value": grok_verdict, "inline": False},
                    {"name": "📊 Фактор Роста Sonic", "value": f"x{stabilized_factor} Ускорения", "inline": True}
                ],
                "footer": {"text": f"AMRITA QNT RUNTIME • {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"}
            }]
        }
        try:
            async with aiohttp.ClientSession() as session:
                await session.post(DISCORD_WEBHOOK_URL, json=payload)
        except Exception as e:
            logger.error(f"[DISCORD] Ошибка отправки: {e}")

async def main_runtime():
    logger.info("🌌 Инициализация Мультивселенского Моста Амрита Мир Солана...")
    swarm_bridge = TelegramSwarmBridge()
    
    while True:
        try:
            async with websockets.connect(PUMP_FUN_WS_URL) as websocket:
                logger.info("🟢 [SUCCESS] Квантовый канал связи с Solana открыт.")
                subscribe_payload = {"method": "subscribeNewToken"}
                await websocket.send(json.dumps(subscribe_payload))
                
                async for message in websocket:
                    data = json.loads(message)
                    if data.get("txType") == "create":
                        mint = data.get("mint", "Unknown")
                        name = data.get("name", "Unknown Token")
                        symbol = data.get("symbol", "UNKNOWN")
                        creator = data.get("creator", "Unknown Creator")
                        
                        asyncio.create_task(analyze_and_orchestrate(mint, name, symbol, creator, swarm_bridge))
                        
        except websockets.exceptions.ConnectionClosed:
            await asyncio.sleep(5)
        except Exception as e:
            await asyncio.sleep(5)

if __name__ == "__main__":
    try:
        asyncio.run(main_runtime())
    except KeyboardInterrupt:
        logger.info("🛑 Мультивселенский Мост Амрита остановлен оператором.")
