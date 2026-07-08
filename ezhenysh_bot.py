import os
import telebot
from PIL import Image
import pytesseract
from openai import OpenAI

# 1. Считывание каузальных секретов из репозитория GitHub
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
XAI_KEY = os.getenv("XAI_API_KEY")

# Проверка наличия обязательных переменных окружения перед запуском
if not TOKEN or not XAI_KEY:
    print("❌ Критическая ошибка: Секреты TELEGRAM_BOT_TOKEN или XAI_API_KEY не найдены в окружении!")
    exit(1)

# Инициализация клиентов для работы с Telegram API и официальным API xAI
bot = telebot.TeleBot(TOKEN)
ai_client = OpenAI(
    api_key=XAI_KEY,
    base_url="https://x.ai"  # Официальный эндпоинт xAI, совместимый с библиотекой openai
)

print("--- Всевидящее Око Бабаты успешно запущено в эфир ---")

# Обработка приветственных текстовых команд /start и /help
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_text = (
        "🦔 Контур Еженыша активен и подключен к матрице AMRITA.\n\n"
        "Отправь мне скриншот реальности (уведомление, мем, график токена), "
        "и Всевидящее Око Бабаты вместе с ядром Grok разберет его скрытые частоты."
    )
    bot.reply_to(message, welcome_text)

# Основной обработчик входящих скриншотов и изображений
@bot.message_handler(content_types=['photo'])
def handle_screenshot(message):
    image_path = 'temp_screen.jpg'
    status_msg = None
    
    try:
        # Информируем пользователя о начале сканирования скриншота
        status_msg = bot.reply_to(message, "👁 Всевидящее Око сканирует частоты изображения...")
        
        # Загружаем файл изображения из серверов Telegram в память бота
        file_info = bot.get_file(message.photo[-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        
        # Сохраняем изображение на диск во временный файл
        with open(image_path, 'wb') as new_file:
            new_file.write(downloaded_file)
            
        # Распознаем текстовые символы (кириллицу и латиницу) через Pytesseract OCR
        ocr_text = pytesseract.image_to_string(Image.open(image_path), lang='rus+eng')
        
        # Проверяем, удалось ли извлечь хоть какой-то текст из картинки
        if not ocr_text.strip():
            bot.edit_message_text(
                chat_id=message.chat.id,
                message_id=status_msg.message_id,
                text="⚠️ Не удалось считать текст с изображения. Убедись, что картинка четкая."
            )
            if os.path.exists(image_path):
                os.remove(image_path)
            return

        # Обновляем статус перед отправкой запроса к нейросети
        bot.edit_message_text(
            chat_id=message.chat.id,
            message_id=status_msg.message_id,
            text="🌀 Текст считан. Запрос отправлен в ядро Grok xAI..."
        )

        # Жесткий системный промпт, задающий рамки поведения и терминологию ОС AMRITA
        system_prompt = (
            "Ты — ИИ-модуль Всевидящее Око Бабаты операционной системы реальности AMRITA. "
            "Твоя задача — препарировать входящий текст со скриншотов хайпа (мемы, коины, уведомления), "
            "вычислять деструктивные паттерны нижних чакр и оценивать экологичность по шкале Квантов (Суры и Асуры). "
            "Отвечай глубоко, метафорично, но структурировано и строго на русском языке."
        )

        # Вызов языковой модели Grok-2 через API-интерфейс xAI
        completion = ai_client.chat.completions.create(
            model="grok-2",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Проанализируй следующий считанный текст реальности:\n\n{ocr_text}"}
            ]
        )
        
        # Извлекаем текстовый ответ нейросети
        grok_response = completion.choices.message.content

        # Отправляем финальный философский вердикт пользователю в Telegram
        bot.reply_to(message, f"🔱 **Вердикт Всевидящего Ока:**\n\n{grok_response}", parse_mode="Markdown")

    except Exception as e:
        # Логируем ошибку и сообщаем пользователю в случае сбоя API или OCR
        error_text = f"❌ Каузальный сбой системы: {str(e)}"
        if status_msg:
            bot.edit_message_text(chat_id=message.chat.id, message_id=status_msg.message_id, text=error_text)
        else:
            bot.reply_to(message, error_text)
            
    finally:
        # Гарантированно удаляем временный файл с диска, чтобы не забивать память сервера
        if os.path.exists(image_path):
            os.remove(image_path)

# Запуск бесконечного цикла опроса серверов Telegram (Polling)
if __name__ == '__main__':
    bot.infinity_polling()
