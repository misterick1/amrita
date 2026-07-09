import os
import telebot
import requests
import base64
from multiverse_synthesizer import MultiverseQuantumSynthesizer

# Считывание секретов из репозитория GitHub
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
XAI_KEY = os.getenv("XAI_API_KEY")

if not TOKEN or not XAI_KEY:
    print("❌ Критическая ошибка: Проверь секреты TELEGRAM_BOT_TOKEN и XAI_API_KEY!")
    exit(1)

bot = telebot.TeleBot(TOKEN)
synthesizer = MultiverseQuantumSynthesizer()

print("--- Всевидящее Око Кибернет Амрита Мир успешно обновлено ---")

# Кнопки главного меню для управления с телефона
def get_main_keyboard():
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_status = telebot.types.KeyboardButton("🔱 Статус Мультивселенной (6 Слоев)")
    btn_links = telebot.types.KeyboardButton("🌀 Синтез Недостающих Связей")
    markup.add(btn_status, btn_links)
    return markup

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_text = (
        "🦔 Операционная система реальности AMRITA активирована.\n\n"
        "Контур автоматического парсинга писем Ghost, новостей и уведомлений запущен.\n"
        "Отправь мне скриншот или скопированный текст новости для моментального анализа ядра."
    )
    bot.send_message(message.chat.id, welcome_text, reply_markup=get_main_keyboard())

# Обработка входящего СКОПИРОВАННОГО ТЕКСТА (новости, логи, фиды)
@bot.message_handler(content_types=['text'], func=lambda message: message.text not in ["🔱 Статус Мультивселенной (6 Слоев)", "🌀 Синтез Недостающих Связей"])
def handle_raw_text_feed(message):
    try:
        status_msg = bot.reply_to(message, "🌀 Лог перехвачен. Ядро Grok-2 анализирует текстовые частоты...")
        
        system_prompt = (
            "Ты — аналитическое ядро операционной системы реальности AMRITA. "
            "Перед тобой входящий текстовый поток (новость, лог, email от Ghost или уведомление). "
            "Твоя задача — препарировать этот текст: вычленить Асуры (крахи бирж, скам, фишинг, паника) "
            "и Суры (цифровизация активов, стейблкоины корпораций вроде Sony/Hyundai, интеграция Ghost). "
            "Дай четкую структурированную оценку на русском языке и начисли кармические очки EVO (от +5 до +25) за фиксацию импульса."
        )

        headers = {
            "Authorization": f"Bearer {XAI_KEY}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": "grok-2",
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Разбери входящий поток:\n\n{message.text}"}
            ]
        }

        xai_response = requests.post("https://x.ai", headers=headers, json=payload)
        res_json = xai_response.json()
        
        if "choices" in res_json:
            verdict = res_json["choices"]["message"]["content"]
            bot.edit_message_text(f"🔱 **Каузальный вердикт потока:**\n\n{verdict}", message.chat.id, status_msg.message_id)
        else:
            bot.edit_message_text(f"❌ Сбой ядра ИИ: {str(res_json)}", message.chat.id, status_msg.message_id)

    except Exception as e:
        bot.reply_to(message, f"❌ Ошибка текстового контура: {str(e)}")

# Обработка текстовых кнопок меню (Статус и Синтез)
@bot.message_handler(func=lambda message: message.text in ["🔱 Статус Мультивселенной (6 Слоев)", "🌀 Синтез Недостающих Связей"])
def handle_menu_commands(message):
    try:
        if message.text == "🔱 Статус Мультивселенной (6 Слоев)":
            status_msg = bot.reply_to(message, "⏳ Опрашиваю блокчейн-ноды и реестры акций...")
            matrix = synthesizer.get_multiverse_balances()
            
            response = "📊 **МАТРИЦА БАЛАНСОВ АМРИТА:**\n\n"
            for chain, info in matrix["blockchain_layers"].items():
                response += f"🔹 **{chain}**: {info['balance']} ({info['role']})\n"
            
            response += "\n📈 **6_СЛОЙ: ЦИФРОВЫЕ АКЦИИ КОРПОРАЦИЙ:**\n"
            for stock, s_info in matrix["corporate_equity_layer_6"]["assets"].items():
                response += f"🏢 **{stock}** ({s_info['ticker']}): {s_info['total_shares_issued'] if 'total_shares_issued' in s_info else s_info['volume_usd']} на {s_info['blockchain']}\n"
                
            bot.edit_message_text(response, message.chat.id, status_msg.message_id, parse_mode="Markdown")

        elif message.text == "🌀 Синтез Недостающих Связей":
            status_msg = bot.reply_to(message, "🧠 Запускаю квантовый синтезатор ИИ...")
            matrix = synthesizer.get_multiverse_balances()
            verdict = synthesizer.synthesize_missing_links(matrix)
            bot.edit_message_text(f"🔱 **ВЕРДИКТ МУЛЬТИВСЕЛЕННОЙ:**\n\n{verdict}", message.chat.id, status_msg.message_id)
            
    except Exception as e:
        bot.reply_to(message, f"❌ Ошибка каузального контура: {str(e)}")

# Обработка входящих скриншотов
@bot.message_handler(content_types=['photo'])
def handle_screenshot(message):
    try:
        status_msg = bot.reply_to(message, "👁 Ядро Grok сканирует визуальную матрицу скриншота...")
        
        file_info = bot.get_file(message.photo[-1].file_id)
        file_url = f"https://telegram.org{TOKEN}/{file_info.file_path}"
        response = requests.get(file_url)
        
        if response.status_code != 200:
            bot.edit_message_text("❌ Ошибка загрузки медиафайла Telegram.", message.chat.id, status_msg.message_id)
            return

        base64_image = base64.b64encode(response.content).decode('utf-8')

        headers = {
            "Authorization": f"Bearer {XAI_KEY}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": "grok-2-vision-1212",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": (
                                "Ты — ИИ-модуль Всевидящее Око Операционной Системы AMRITA. "
                                "Изучи этот скриншот смартфона. Найди на нем все уведомления. "
                                "Вычисли деструктивные FOMO-паттерны (крипта, пампы, щиткоины, котировки, крахи бирж) "
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
            verdict = res_json["choices"]["message"]["content"]
            bot.reply_to(message, f"🔱 **Вердикт Всевидящего Ока:**\n\n{verdict}")
        else:
            bot.reply_to(message, f"❌ Сбой ответа ядра ИИ: {str(res_json)}")

    except Exception as e:
        bot.reply_to(message, f"❌ Ошибка контура: {str(e)}")

if __name__ == '__main__':
    bot.infinity_polling()
