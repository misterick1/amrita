import os
import aiohttp
import logging
from dotenv import load_dotenv

logger = logging.getLogger("TelegramBridge")
load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

async def send_telegram_message(text: str):
    """Асинхронная отправка уведомлений в Telegram-канал экосистемы"""
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        logger.warning("Telegram токен или Chat ID не настроены. Пропуск отправки.")
        return False

    url = f"https://telegram.org{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text,
        "parse_mode": "HTML",
        "disable_web_page_preview": False
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload) as resp:
                if resp.status == 200:
                    logger.info("📢 Уведомление успешно доставлено в Telegram!")
                    return True
                else:
                    logger.error(f"Ошибка Telegram API: {resp.status}")
                    return False
    except Exception as e:
        logger.error(f"Сбой отправки в Telegram: {e}")
        return False
