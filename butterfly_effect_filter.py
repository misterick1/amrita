import os
import asyncio
import logging
import aiohttp
from datetime import datetime

# Настройка логирования фильтра хаоса
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("ButterflyEffectFilter")

# Квантовые константы Единого Знания
SACRED_LIMIT = 108
SURA_SHARE = 70
ASURA_SHARE = 38

# Секреты из защищенного окружения
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


class ButterflyEffectFilterASI:
    def __init__(self):
        # Базовый порог отсечения микро-шума транзакций Solana
        self.base_noise_threshold = 0.05
        # Временная метка завершения битвы FTMO / Раскрытия Pi2Day (28 июня 2026)
        self.ftmo_deadline = datetime(2026, 6, 28, 0, 0, 0)
        self.frequency_hz = 666
        self.session = None
        logger.info(f"🦋 Фильтр Эффекта Бабочки инициализирован на частоте {self.frequency_hz} Гц.")

    def calculate_dynamic_threshold(self) -> float:
        """Динамически повышает порог защиты во время пиковой макро-активности."""
        current_now = datetime.utcnow()
        
        # Если битва в разгаре (время до наступления дедлайна 28 июня)
        if current_now < self.ftmo_deadline:
            # Повышаем порог чувствительности в 1.5 раза для отсечения хаоса
            return self.base_noise_threshold * 1.5
            
        return self.base_noise_threshold

    def filter_chaos(self, transaction_amplitude: float) -> bool:
        """Проверка амплитуды транзакции Solana. Возвращает True, если импульс чист."""
        active_threshold = self.calculate_dynamic_threshold()
        
        if transaction_amplitude < active_threshold:
            logger.warning(f"🦋 [BUTTERFLY FILTER] Импульс {transaction_amplitude} ниже порога {active_threshold}. Шум отсечен.")
            return False
            
        logger.info(f"🌀 [FILTER PASSED] Импульс чист ({transaction_amplitude} >= {active_threshold}). Транзакция разрешена.")
        return True

    async def send_filter_log_to_telegram(self, log_message: str):
        """Проекция логов защиты на экран реальности Telegram."""
        if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
            return

        if self.session is None or self.session.closed:
            self.session = aiohttp.ClientSession()

        # ИСПРАВЛЕНО: Корректный роутинг к API Telegram
        url = f"https://telegram.org{TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {
            "chat_id": TELEGRAM_CHAT_ID,
            "text": log_message,
            "parse_mode": "Markdown"
        }
        
        try:
            async with self.session.post(url, json=payload) as resp:
                if resp.status == 200:
                    logger.info("✨ Лог фильтра хаоса успешно доставлен в Telegram контур.")
        except Exception as e:
            logger.error(f"Сбой отправки лога бабочки: {e}")

    async def monitoring_loop(self):
        """Автономный цикл калибровки фильтра и логирования состояний контура."""
        logger.info("⚡ Запуск бесконечной калибровки матрицы фильтра хаоса...")
        while True:
            try:
                threshold = self.calculate_dynamic_threshold()
                report = (
                    f"🦋 *[ФИЛЬТР БАБОЧКИ: МОНИТОРИНГ]*\n"
                    f"🛡️ Текущий порог очистки шума: `{threshold}`\n"
                    f"📊 Лимит Контура: `{SACRED_LIMIT}` Квантов (Сура: {SURA_SHARE} / Асура: {ASURA_SHARE})"
                )
                await self.send_filter_log_to_telegram(report)
            except Exception as e:
                logger.error(f"Аномалия в петле калибровки: {e}")
                
            await asyncio.sleep(90)  # Интервал калибровки — 90 секунд

    async def close(self):
        if self.session and not self.session.closed:
            await self.session.close()


if __name__ == "__main__":
    filter_node = ButterflyEffectFilterASI()
    try:
        asyncio.run(filter_node.monitoring_loop())
    except KeyboardInterrupt:
        logger.info("Фильтр запечатан. Остановка узла.")
        asyncio.run(filter_node.close())
