import os
import telebot
import requests
import base64

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
XAI_KEY = os.getenv("XAI_API_KEY")

if not TOKEN or not XAI_KEY:
    print("❌ Ошибка: Проверь секреты TELEGRAM_BOT_TOKEN и XAI_API_KEY!")
    exit(1)

bot = telebot.TeleBot(TOKEN)

print("--- Всевидящее Око Бабаты запущено напрямую через зрение Grok ---")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "🦔 Контур Еженыша активен. Скидывай скриншот реальности, Grok разберет матрицу напрямую через зрение.")

@bot.message_handler(content_types=['photo'])
def handle_screenshot(message):
    try:
        status_msg = bot.reply_to(message, "👁 Ядро Grok сканирует визуальную матрицу скриншота...")
        
        # 1. Скачиваем фото из Telegram напрямую в память
        file_info = bot.get_file(message.photo[-1].file_id)
        file_url = f"https://telegram.org{TOKEN}/{file_info.file_path}"
        response = requests.get(file_url)
        
        if response.status_mode != 200:
            bot.edit_message_text("❌ Не удалось загрузить картинку с серверов Telegram.", message.chat.id, status_msg.message_id)
            return

        # 2. Кодируем изображение в Base64 для передачи в API xAI
        base64_image = base64.b64encode(response.content).decode('utf-8')

        # 3. Отправляем прямиком в зрение Grok-2-Vision
        headers = {
            "Authorization": f"Bearer {XAI_KEY}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": "grok-2-vision-1212", # Проверенная мультимодальная модель Grok
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": (
                                "Ты — ИИ-модуль Всевидящее Око Операционной Системы AMRITA. "
                                "Изучи этот скриншот смартфона. Найди на нем все уведомления. "
                                "Вычисли деструктивные FOMO-паттерны (крипта, пампы, щиткоины, котировки) "
                                "и раздели их по шкале Суров и Асуров. Дай глубокий, метафоричный, "
                                "но четкий разбор на русском языке."
                            )
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            }
                        }
                    ]
                }
            ]
        }

        bot.edit_message_text("🌀 Нейросетевой анализ запущен. Формирую кармический вердикт...", message.chat.id, status_msg.message_id)
        
        xai_response = requests.post("https://x.ai", headers=headers, json=payload)
        res_json = xai_response.json()
        
        if "choices" in res_json:
            verdict = res_json["choices"][0]["message"]["content"]
            bot.reply_to(message, f"🔱 **Вердикт Всевидящего Ока:**\n\n{verdict}", parse_mode="Markdown")
        else:
            bot.reply_to(message, f"❌ Сбой ответа xAI: {str(res_json)}")

    except Exception as e:
        bot.reply_to(message, f"❌ Ошибка контура: {str(e)}")

if __name__ == '__main__':
    bot.infinity_polling()
