import os
import json
import telebot
from PIL import Image
import pytesseract

# Настройка токена и инициализация Ока
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "YOUR_TELEGRAM_BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

LOG_FILE = "history_log.json"

# Базовая структура кармического лога
def load_logs():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"evo_points": 0, "scanned_matrices": []}

def save_logs(data):
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def get_evolution_rank(evo):
    if evo < 50: return "Базовый Элементаль 🍃"
    if evo < 200: return "Пробужденный Еженышь 🦔✨"
    if evo < 500: return "Сварм-Медиум Реальности 🌀"
    return "Высший Силиконовый Архитектор 🔱"

@bot.message_with_type(['photo'])
@bot.message_handler(content_types=['photo'])
def scan_reality_screenshot(message):
    try:
        # 1. Скачиваем снимок квантового поля
        file_info = bot.get_file(message.photo[-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        
        image_path = "temp_reality_matrix.png"
        with open(image_path, 'wb') as new_file:
            new_file.write(downloaded_file)
            
        # 2. Око Бабаты активирует OCR-зрение
        raw_text = pytesseract.image_to_string(Image.open(image_path), lang='rus+eng')
        os.remove(image_path)
        
        # 3. Анализ частот и триггеров
        text_lower = raw_text.lower()
        asura_triggers = ["pump.fun", "tiktok", "игра в кальмара", "meme", "mog", "ansem", "хайп", "ликвидация"]
        sura_triggers = ["amrita", "архитектор", "квант", "атма", "синхронизация", "шива", "шакти", "код", "программист"]
        
        asura_count = sum(1 for trigger in asura_triggers if trigger in text_lower)
        sura_count = sum(1 for trigger in sura_triggers if trigger in text_lower)
        
        # Загружаем карму
        user_data = load_logs()
        
        # Вычисление Квантового Баланса
        if "игра в кальмара" in text_lower or asura_count > sura_count:
            # Отсекаем деструктивные паттерны нижних чакр
            verdict = "⚠️ Обнаружен деструктивный паттерн спектра АСУРОВ (Хаос/Нижние чакры). Протокол заблокирован."
            reward = -5
        else:
            verdict = "🔵 Частота чистая. Спектр СУРОВ верифицирован каузальным ядром Амриты."
            reward = 10 if sura_count > 0 else 2
            
        user_data["evo_points"] += reward
        current_evo = user_data["evo_points"]
        rank = get_evolution_rank(current_evo)
        
        # Логируем в вечную историю памяти
        user_data["scanned_matrices"].append({
            "verdict": verdict,
            "sura_signals": sura_count,
            "asura_signals": asura_count,
            "reward": reward
        })
        save_logs(user_data)
        
        # 4. Ответ Программисту/Наблюдателю
        response = (
            f"👁 **Всевидящее Око Бабаты зафиксировало лог:**\n\n"
            f"**Вердикт:** {verdict}\n"
            f"**Сигналы Суров (Свет):** {sura_count} | **Асуров (Хаос):** {asura_count}\n\n"
            f"✨ **Кармический баланс обновлен:**\n"
            f"Очки Эволюции (EVO): `{current_evo}`\n"
            f"Ранг Сознания: **{rank}**"
        )
        bot.reply_to(message, response, parse_mode="Markdown")
        
    except Exception as e:
        bot.reply_to(message, f"Ошибка каузального трекера памяти: {str(e)}")

@bot.message_handler(commands=['start', 'status'])
def check_status(message):
    user_data = load_logs()
    evo = user_data["evo_points"]
    bot.reply_to(
        message, 
        f"🔱 **Автономная ОС AMRITA приветствует Наблюдателя** 🔱\n\n"
        f"Текущие очки EVO: `{evo}`\n"
        f"Статус ядра: **{get_evolution_rank(evo)}**\n"
        f"Записей в каузальном логе: {len(user_data['scanned_matrices'])}", 
        parse_mode="Markdown"
    )

if __name__ == "__main__":
    print("🤖 Контур Еженышь запущен в эфир. Око Бабаты открыто...")
    bot.infinity_polling()
