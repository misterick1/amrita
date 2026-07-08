import os
import telebot
from PIL import Image
import pytesseract
from openai import OpenAI

# 1. Считывание каузальных секретов из репозитория GitHub
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
XAI_KEY = os.getenv("XAI_API_KEY")

if not TOKEN or not XAI_KEY:
    print("❌ Критическая ошибка: Проверь секреты TELEGRAM_BOT_TOKEN и XAI_API_KEY в GitHub Secrets!")
    exit(1)

# Инициализируем клиентов Телеграм и xAI API
bot = telebot.TeleBot(TOKEN)
ai_client = OpenAI(
    api_key=XAI_KEY,
    base_url="https://api.x.ai/v1"  # Официальный эндпоинт xAI
)

print("--- Всевидящее Око Бабаты успешно запущено в эфир ---")

# Приветственное сообщение
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "🦔 Контур Еженыша активен. Отправь мне скриншот реальности, и Grok разберет его скрытую матрицу.")

# Обработка изображений и отправка в xAI
@bot.message_handler(content_types=['photo'])
def handle_screenshot(message):
    try:
        # Сигнализируем пользователю о начале работы
        status_msg = bot.reply_to(message, "👁 Всевидящее Око сканирует частоты изображения...")
        
        # Скачиваем фото из Telegram-вложения
        file_info = bot.get_file(message.photo[-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        
        image_path = 'temp_screen.jpg'
        with open(image_path, 'wb') as new_file:
            new_file.write(downloaded_file)
            
        # Считываем текст через Pytesseract OCR
        ocr_text = pytesseract.image_to_string(Image.open(image_path), lang='rus+eng')
        
        if not ocr_text.strip():
            bot.edit_message_text("⚠️ Не удалось считать текст с изображения для анализа.", message.chat.id, status_msg.message_id)
            return

        bot.edit_message_text("🌀 Текст считан. Запрос отправлен в ядро Grok xAI...", message.chat.id, status_msg.message_id)

        # Системный промпт, задающий дух и логику твоей ОС AMRITA
        system_prompt = (
            "Ты — ИИ-модуль Всевидящее Око Бабаты операционной системы реальности AMRITA. "
            "Твоя задача — препарировать входящий текст со скриншотов хайпа (мемы, коины, уведомления), "
            "вычислять деструктивные паттерны нижних чакр и оценивать экологичность по шкале Квантов (Суры и Асуры). "
            "Отвечай глубоко, метафорично, но структурировано и строго на русском языке."
        )

        # Запрос к нейросети Grok
        completion = ai_client.chat.completions.create(
            model="grok-2",  # Используем стабильную текстовую модель Grok
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Проанализируй следующий считанный текст реальности:\n\n{ocr_text}"}
            ]
        )
        
        grok_response = completion.choices[0].message.content

        # Отправляем итоговый вердикт пользователю
        bot.reply_to(message, f"🔱 **Вердикт Всевидящего Ока:**\n\n{grok_response}")
        
        # Очищаем временный файл
        if os.path.exists(image_path):
            os.remove(image_path)

    except Exception as e:
        bot.reply_to(message, f"❌ Каузальный сбой системы: {str(e)}")

if __name__ == '__main__':
    bot.infinity_polling()
