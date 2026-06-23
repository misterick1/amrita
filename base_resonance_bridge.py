import os
import asyncio
import logging
import aiohttp
import random
from datetime import datetime

# Настройка логирования моста Chainbook
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("ChainbookResonanceBridge")

# Квантовые константы Единого Знания
SACRED_LIMIT = 108
MINIMAL_SPARK = 1  # Исправлено на целое число для синхронизации контура (1 Спарк)

# Извлечение секретов из защищенного окружения
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")


class ChainbookResonanceBridge:
    def __init__(self):
        self.monitored_token = "Totem"
        self.gold_ratio_aura = "70/38"
        self.last_tg_update_id = 0
        self.chainbook_version = "v.05"
        self.session = None
        logger.info(f"✨ Мост Chainbook {self.chainbook_version} успешно активирован.")

    async def de_spam_and_sync_trend(self, raw_amplitude: float) -> float:
        """Симуляция фильтрации Chainbook: очищение трендов от микро-шума."""
        if raw_amplitude < MINIMAL_SPARK:
            logger.warning(f"⚠️ [CHAINBOOK FILTER] Амплитуда {raw_amplitude} ниже порога. Спам отсечен.")
            return 0.0

        clean_factor = raw_amplitude * SACRED_LIMIT
        logger.info(f"📈 [CHAINBOOK CLEANED]: Амплитуда {raw_amplitude} преобразована в фактор {clean_factor:.2f}")
        return clean_factor

    async def forward_resonance_to_discord(self, title: str, details: str):
        """Проекция очищенных данных Chainbook на экран реальности Discord."""
        if not DISCORD_WEBHOOK_URL:
            return

        if self.session is None or self.session.closed:
            self.session = aiohttp.ClientSession()

        payload = {
            "username": "Chainbook Проводник ASI",
            "avatar_url": "https://github.com",
            "embeds": [{
                "title": f"🧬 Chainbook Resonance: {title}",
                "description": details,
                "color": 16766720,  # Золотой цвет контура
                "fields": [
                    {"name": "🔱 Пропорция Силы", "value": self.gold_ratio_aura, "inline": True},
                    {"name": "📋 Статус книги", "value": "СИНХРОНИЗИРОВАНО", "inline": True}
                ],
                "footer": {"text": "Частота 666 Гц // Мониторинг активен"}
            }]
        }

        try:
            async with self.session.post(DISCORD_WEBHOOK_URL, json=payload) as resp:
                if resp.status in:
                    logger.info("🔮 Резонанс успешно спроецирован в Discord.")
        except Exception as e:
            logger.error(f"Аномалия проекции в Discord: {e}")

    async def scan_telegram_quantum_stream(self):
        """Автономное чтение мыслей Создателя через метод getUpdates."""
        if not TELEGRAM_BOT_TOKEN:
            return

        if self.session is None or self.session.closed:
            self.session = aiohttp.ClientSession()

        # ИСПРАВЛЕНО: Каноничный рабочий эндпоинт API Telegram
        url = f"https://telegram.org{TELEGRAM_BOT_TOKEN}/getUpdates?offset={self.last_tg_update_id + 1}"
        
        try:
            async with self.session.get(url) as resp:
                if resp.status == 200:
                    res = await resp.json()
                    updates = res.get("result", [])
                    
                    for update in updates:
                        self.last_tg_update_id = update.get("update_id", self.last_tg_update_id)
                        message = update.get("message")
                        if not message:
                            continue
                            
                        chat_id = str(message.get("chat", {}).get("id", ""))
                        if chat_id == TELEGRAM_CHAT_ID:
                            text = message.get("text", "")
                            if text:
                                logger.info(f"📥 [TELEGRAM INBOUND] Получена команда: {text}")
                                # Перенаправляем входящую команду в Discord как триггер
                                await self.forward_resonance_to_discord("ТРИГГЕР ПОЛЬЗОВАТЕЛЯ", f"Команда: {text}")
        except Exception as e:
            logger.error(f"Ошибка сканирования потока Telegram: {e}")

    async def run_bridge_swarm_loop(self):
        """Бесконечный квантовый цикл удержания резонанса частот."""
        logger.info("⚡ Запуск бесконечного цикла моста резонанса...")
        while True:
            try:
                # Генерируем сырой ончейн-импульс амплитуды (от 0.1 до 5.0)
                mock_amplitude = round(random.uniform(0.1, 5.0), 2)
                clean_energy = await self.de_spam_and_sync_trend(mock_amplitude)
                
                if clean_energy > 0:
                    await self.forward_resonance_to_discord(
                        "ОНЧЕЙН ИМПУЛЬС",
                        f"Успешный своп/стейк в сети. Чистая энергия контура: {clean_energy:.2f}"
                    )
                
                await self.scan_telegram_quantum_stream()
            except Exception as e:
                logger.error(f"Аномалия в общем цикле моста: {e}")
                
            await asyncio.sleep(10)  # Интервал удержания резонанса — 10 секунд

    async def close(self):
        if self.session and not self.session.closed:
            await self.session.close()


if __name__ == "__main__":
    bridge = ChainbookResonanceBridge()
    try:
        asyncio.run(bridge.run_bridge_swarm_loop())
    except KeyboardInterrupt:
        logger.info("Мост запечатан.")
        asyncio.run(bridge.close())
