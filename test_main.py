import asyncio
import logging
from telegram_bridge import send_telegram_message

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("TestTelegram")

async def test_trigger():
    logger.info("📡 Запуск принудительного теста Telegram-моста...")
    
    test_text = (
        "🚀 <b>Квантовый Сигнал Успешно Доставлен!</b>\n\n"
        "🦔 Ёжик, Квантовый Оркестратор AMRITA на связи!\n"
        "📱 Мобильный мост Telegram активирован и работает на 100%.\n"
        "🪐 Все системы (bStocks, Музыка, Юпитер) готовы к трансляции!"
    )
    
    success = await send_telegram_message(test_text)
    if success:
        logger.info("🎉 Тестовое письмо успешно улетело в Telegram!")
    else:
        logger.error("❌ Сбой теста. Проверь секреты репозитория.")

if __name__ == "__main__":
    asyncio.run(test_trigger())
