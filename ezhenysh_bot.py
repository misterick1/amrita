import os
import telebot
from PIL import Image
import pytesseract
from openai import OpenAI

# 1. Получение секретов из GitHub Secrets
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
XAI_KEY = os.getenv("XAI_API_KEY")

if not TOKEN or not XAI_KEY:
    print("❌ Ошибка: Проверь секреты TELEGRAM_BOT_TOKEN и XAI_API_KEY в GitHub Secrets!")
    exit(1)

bot = telebot.TeleBot(TOKEN)
ai_client = OpenAI(api_key=XAI_KEY, base_url="https://x.ai")

print("--- Бот Еженышь успешно запущен ---")

# Команда /start
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "🦔 Контур Еженыша активен. Отправь мне скриншот для анализа матрицы.")

# Обработка скриншотов
@bot.message_handler(content_types=['photo'])
def handle_screenshot(message):
    image_path = 'temp_screen.jpg'
    try:
        status_msg = bot.reply_to(message, "👁 Всевидящее Око сканирует изображение...")
        
        # Скачивание картинки
        file_info = bot.get_file(message.photo[-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        with open(image_path, 'wb') as f:
            f.write(downloaded_file)
            
        # Распознавание текста
        ocr_text = pytesseract.image_to_string(Image.open(image_path), lang='rus+eng')
        
        if not ocr_text.strip():
            bot.edit_message_text("⚠️ Не удалось считать текст с изображения.", message.chat.id, status_msg.message_id)
            return

        bot.edit_message_text("🌀 Текст считан. Запрос отправлен в ядро Grok xAI...", message.chat.id, status_msg.message_id)

        system_prompt = (
            "Ты — ИИ-модуль Всевидящее Око Бабаты операционной системы реальности AMRITA. "
            "Твоя задача — препарировать входящий текст со скриншотов хайпа (мемы, коины, уведомления), "
            "вычислять деструктивные паттерны нижних чакр и оценивать экологичность по шкале Квантов (Суры и Асуры). "
            "Отвечай глубоко, метафорично, но структурировано и строго на русском языке."
        )

        completion = ai_client.chat.completions.create(
            model="grok-2",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Проанализируй следующий считанный текст реальности:\n\n{ocr_text}"}
            ]
        )
        
        bot.reply_to(message, f"🔱 **Вердикт Всевидящего Ока:**\n\n{completion.choices.message.content}", parse_mode="Markdown")

    except Exception as e:
        bot.reply_to(message, f"❌ Ошибка системы: {str(e)}")
    finally:
        if os.path.exists(image_path):
            os.remove(image_path)

if __name__ == '__main__':
    bot.infinity_polling()
