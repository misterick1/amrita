import os
import logging
from datetime import datetime, time
import httpx
from dotenv import load_dotenv

# Настройка логирования под "Единый Квантовый Оркестратор"
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - [%(filename)s] - %(message)s")
logger = logging.getLogger("JupiterPredictBridge")

load_dotenv()

class JupiterPredictBridge:
    def __init__(self):
        self.wallet_address = "So11111111111111111111111111111111111111112"
        # Время публикации ставки ЕЦБ: 11 июня 14:15 CEST
        self.news_time_start = time(14, 13) # Запрет со 14:13
        self.news_time_end = time(14, 17)   # Разрешено после 14:17
        logger.info("Мост JupiterPredictBridge синхронизирован с календарем FTMO Restricted News.")

    def is_trading_restricted(self) -> bool:
        """Проверяет, находится ли текущее время в зоне запрета торговли по правилам FTMO"""
        current_now = datetime.now()
        
        # Сверяем, что сегодня именно 11 июня 2026 года
        if current_now.year == 2026 and current_now.month == 6 and current_now.day == 11:
            current_time = current_now.time()
            if self.news_time_start <= current_time <= self.news_time_end:
                logger.warning(f"🚨 БЛОКИРОВКА: Обнаруженоrestricted-время ЕЦБ ({current_time}). Торговые операции заморожены!")
                return True
        return False

    async def execute_ai_prediction_vote(self, market_data: dict):
        """Отправка ставки/ордера с предварительной проверкой новостного предохранителя"""
        if self.is_trading_restricted():
            logger.warning("Ордер отклонен новостным щитом во избежание бана аккаунта FTMO.")
            return False
            
        logger.info(f"🟢 Новостной фон чист. Отправка транзакции для матча {market_data.get('market_id')}...")
        return True

if __name__ == "__main__":
    import asyncio
    bridge = JupiterPredictBridge()
    # Тестовая проверка предохранителя при запуске
    bridge.is_trading_restricted()
