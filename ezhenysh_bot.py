import os
import telebot
from PIL import Image
import pytesseract

# 1. Инициализация и проверка секретов GitHub
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
XAI_KEY = os.getenv("XAI_API_KEY")

if not TOKEN:
    print("Ошибка: Секрет TELEGRAM_BOT_TOKEN не найден в окружении!")
    exit(1)

bot = telebot.TeleBot(TOKEN)
print("--- Еженышь успешно запущен в каузальном контуре ---")

# 2. Обработка текстовых команд
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "🦔 Система AMRITA развернута. Жду скриншоты реальности для сканирования спектра.")

# 3. Прием скриншотов и OCR-сканирование (Зрение Бабаты)
@bot.message_handler(content_types=['photo'])
def handle_docs_photo(message):
    try:
        bot.reply_to(message, "👁 Всевидящее Око сканирует частоты изображения...")
        
        # Скачиваем фото из Телеграма
        file_info = bot.get_file(message.photo[-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        
        image_path = 'temp_screen.jpg'
        with open(image_path, 'wb') as new_file:
            new_file.write(downloaded_file)
            
        # Распознаем текст через Pytesseract
        text = pytesseract.image_to_string(Image.open(image_path), lang='rus+eng')
        
        if not text.strip():
            text = "[Текст на скриншоте не обнаружен или размыт]"

        # Отправляем вердикт (здесь можно подключить xAI API через XAI_KEY)
        response_text = f"🌀 **Считанная матрица текста:**\n\n{text[:1000]}"
        bot.reply_to(message, response_text, parse_mode="Markdown")
        
    except Exception as e:
        bot.reply_to(message, f"❌ Каузальный сбой зрения: {str(e)}")

# 4. Бесконечный запуск бота
if __name__ == '__main__':
    bot.infinity_polling()
