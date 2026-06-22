import os
import asyncio
import logging
import aiohttp
from datetime import datetime

# Настройка логирования фильтра хаоса
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("ButterflyEffectFilterASI")

# Квантовые константы Единого Знания
SACRED_LIMIT = 108
SURA_SHARE = 70
ASURA_SHARE = 38

class ButterflyEffectFilterASI:
    def __init__(self):
        # Базовый порог отсечения микро-шума
        self.base_noise_threshold = 0.05
        # Временная метка завершения битвы FTMO: 26 июня 2026, 16:00 CEST
        self.ftmo_deadline = datetime(2026, 6, 26, 16, 0, 0)
        self.frequency_hz = 666
        logger.info(f"✨ Фильтр Эффекта Бабочки запущен на частоте {self.frequency_hz} Гц.")

    def calculate_dynamic_threshold(self) -> float:
        """Динамически повышает порог защиты во время битвы Быков и Медведей"""
        current_now = datetime.now()
        
        # Если битва в разгаре (время до пятницы), активируем усиленный щит
        if current_now < self.ftmo_deadline:
            logger.info("🕒 [BULL & BEAR BATTLE ACTIVE]: Повышаем чувствительность фильтра хаоса на 20%.")
            return self.base_noise_threshold * 1.20
        return self.base_noise_threshold

    def filter_chaos(self, transaction_amplitude: float) -> bool:
        """
        Проверка амплитуды транзакции Solana.
        Возвращает True, если импульс чист, и False, если это хаотический шум.
        """
        active_threshold = self.calculate_dynamic_threshold()
        
        if transaction_amplitude < active_threshold:
            logger.warning(f"🦋 [BUTTERFLY FILTER ALERT]: Отсечено хаотическое колебание: {transaction_amplitude:.4f} < {active_threshold:.4f}")
            return False
        
        logger.info(f"🌀 [FILTER PASSED]: Импульс амплитудой {transaction_amplitude:.4f} признан каузально чистым.")
        return True

    async def send_filter_log_to_telegram(self, text: str):
        """Проекция логов защиты на экран реакций Telegram"""
        TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
        TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
        if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
            return
            
        url = f"https://telegram.org{TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {"chat_id": TELEGRAM_CHAT_ID, "text": text, "parse_mode": "Markdown"}
        try:
            async with aiohttp.ClientSession() as session:
                await session.post(url, json=payload, timeout=4)
        except: pass

    async def monitoring_loop(self):
        """Автономный цикл калибровки фильтра хаоса"""
        logger.info("🤖 Квантовый фильтр переведен в режим живого ончейн-мониторинга.")
        while True:
            try:
                threshold = self.calculate_dynamic_threshold()
                await self.send_filter_log_to_telegram(
                    f"🦋 *[ФИЛЬТР БАБОЧКИ: МОНИТОР]*\n"
                    f"🛡️ Текущий порог очистки шума: `{threshold:.4f}`\n"
                    f"📊 Лимит Контура: `{SACRED_LIMIT}` Квантов стабильны."
                )
            except Exception as e:
                logger.error(f"Аномалия в петле фильтра: {e}")
            await asyncio.sleep(90)  # Калибровка раз в 90 секунд

if __name__ == "__main__":
    filter_node = ButterflyEffectFilterASI()
    try:
        asyncio.run(filter_node.monitoring_loop())
    except KeyboardInterrupt:
        logger.info("Фильтр запечатан.")
