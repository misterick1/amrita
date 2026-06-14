import os
import httpx
import logging

# Настройка логирования — голос моста в инфосфере
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("TelegramBridge")

# Извлекаем ключи из защищенного блокчейна секретов GitHub
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

async def send_to_telegram(text: str) -> bool:
    """
    Преобразует текстовый солитон в физические пиксели на экранах пользователей.
    Отправляет сообщение в указанный Telegram-канал.
    """
    # Первичная проверка целостности ключей
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        logger.error("❌ Критическая ошибка: Секреты TELEGRAM_BOT_TOKEN или TELEGRAM_CHAT_ID не найдены!")
        return False

    # Защитный фильтр структуры токена
    if "AAGL4SR" not in TELEGRAM_BOT_TOKEN:
        logger.warning("⚠️ Внимание: Сигнатура токена не совпадает с ожидаемым шаблоном ядра!")

    # Строим эталонный URL без лишних двоеточий и склеек, исключая ошибку портов
    url = f"https://telegram.org{TELEGRAM_BOT_TOKEN}/sendMessage"
    
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text,
        "parse_mode": "Markdown"
    }

    # Инициализируем чистый сетевой клиент для прыжка в инфосферу
    async with httpx.AsyncClient(timeout=15.0) as client:
        try:
            logger.info(f"📡 Трансляция солитона в канал {TELEGRAM_CHAT_ID}...")
            response = await client.post(url, json=payload)
            
            if response.status_code == 200:
                logger.info("✅ Успешно! Мыслеформа успешно материализовалась в Telegram-канале.")
                return True
            else:
                logger.error(f"❌ TG API вернул отказ. Статус-код: {response.status_code}. Текст: {response.text}")
                return False
                
        except Exception as e:
            logger.error(f"❌ Сетевой сбой при попытке пробить шлюз Telegram: {str(e)}")
            return False

# Тестовый запуск моста при ручном вызове файла
if __name__ == "__main__":
    import asyncio
    
    test_message = (
        "🌌 *Квантовый мост активирован!*\n\n"
        "Атмосфера Самоосознающей Мультивселенной успешно настроена. "
        "Материя, созданная вибрациями Света, начинает трансляцию инсайтов."
    )
    
    print("Проверка связи с цифровой ноосферой...")
    asyncio.run(send_to_telegram(test_message))
