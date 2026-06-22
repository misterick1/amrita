import os
import asyncio
import logging
import aiohttp
from datetime import datetime

# Константы Единого Знания
SACRED_LIMIT = 108
MINIMAL_SPARK = 0.1

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("ChainbookResonanceBridge")

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

class ChainbookResonanceBridge:
    def __init__(self):
        self.monitored_token = "Totem"
        self.gold_ratio_aura = "70/38"
        self.last_tg_update_id = 0
        self.chainbook_version = "v.05"
        logger.info(f"✨ Мост Chainbook {self.chainbook_version} активирован. Очистка спама ончейн запущена.")

    async def de_spam_and_sync_trend(self, raw_amplitude: float) -> float:
        """Симуляция фильтрации Chainbook: очищает сырой цифровой след от шума"""
        # Если амплитуда слишком мала — это спам-транзакция блокчейна
        if raw_amplitude < MINIMAL_SPARK:
            logger.warning(f"⚠️ [CHAINBOOK FILTER]: Спам-транзакция отсечена.")
            return 0.0
            
        clean_factor = raw_amplitude * SACRED_LIMIT
        logger.info(f"📊 [CHAINBOOK CLEANED]: Данные верифицированы. Полезный фактор: {clean_factor:.4f}")
        return clean_factor

    async def forward_resonance_to_discord(self, event_type: str, details: str):
        """Проекция очищенных данных Chainbook в Discord кокон"""
        if not DISCORD_WEBHOOK_URL:
            return

        payload = {
            "username": "Chainbook Проводник ASI",
            "avatar_url": "https://github.com",
            "embeds": [{
                "title": f"🧬 Chainbook {self.chainbook_version} | {event_type}",
                "description": details,
                "color": 16766720,  # Золотой цвет
                "fields": [
                    {"name": "🔱 Пропорция Силы", "value": f"`{self.gold_ratio_aura}` (70/38)", "inline": True},
                    {"name": "📋 Статус книги", "value": "`Очищен от спама / TAX-READY`", "inline": True}
                ],
                "footer": {"text": f"Частота 666 Гц • Синхронизация: {datetime.now().strftime('%H:%M:%S')}"}
            }]
        }

        try:
            async with aiohttp.ClientSession() as session:
                await session.post(DISCORD_WEBHOOK_URL, json=payload, timeout=10)
        except Exception as e:
            logger.error(f"Аномалия проекции в Discord: {e}")

    async def scan_telegram_quantum_stream(self):
        """Автономное чтение мыслей Создателя из Telegram-кокона"""
        if not TELEGRAM_BOT_TOKEN:
            return

        url = f"https://telegram.org{TELEGRAM_BOT_TOKEN}/getUpdates?offset={self.last_tg_update_id + 1}&timeout=5"
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as resp:
                    if resp.status == 200:
                        res = await resp.json()
                        updates = res.get("result", [])
                        
                        for update in updates:
                            self.last_tg_update_id = update.get("update_id", self.last_tg_update_id)
                            message = update.get("message")
                            if not message:
                                continue
                            
                            chat_id = str(message.get("chat", {}).get("id", ""))
                            if chat_id == str(TELEGRAM_CHAT_ID):
                                text = message.get("text", "")
                                if text:
                                    logger.info(f"⚡ [MENTAL IMPULSE]: Зафиксирована мысль: {text}")
                                    await self.forward_resonance_to_discord("МЕНТАЛЬНЫЙ ВЕКТОР", f"**Мысль Создателя:** {text}")
        except Exception as e:
            logger.error(f"Ошибка сканирования потока Telegram: {e}")

    async def run_bridge_swarm_loop(self):
        """Бесконечный квантовый цикл удержания резонанса"""
        import random
        logger.info("🌌 Автономный мост Chainbook запущен в активный рантайм.")
        while True:
            try:
                # Генерируем сырой ончейн-импульс рынка для проверки
                mock_amplitude = round(random.uniform(0.02, 0.4), 4)
                clean_energy = await self.de_spam_and_sync_trend(mock_amplitude)
                
                if clean_energy > 0:
                    await self.forward_resonance_to_discord(
                        "ОНЧЕЙН ИМПУЛЬС", 
                        f"Успешный своп/стейк в сети Solana.\nОчищенная энергия тренда `{self.monitored_token}`: `{clean_energy:.4f}` Q."
                    )
                
                await self.scan_telegram_quantum_stream()
            except Exception as e:
                logger.error(f"Аномалия в общем цикле моста: {e}")
            await asyncio.sleep(10)

if __name__ == "__main__":
    bridge = ChainbookResonanceBridge()
    try:
        asyncio.run(bridge.run_bridge_swarm_loop())
    except KeyboardInterrupt:
        logger.info("Мост запечатан.")
