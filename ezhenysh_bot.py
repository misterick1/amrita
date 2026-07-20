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
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {"evo_points": 0, "scanned_matrices": []}
    return {"evo_points": 0, "scanned_matrices": []}

def save_logs(data):
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def get_evolution_rank(evo):
    if evo < 50: return "Базовый Элементаль 🍃"
    if evo < 200: return "Пробужденный Еженышь 🦔✨"
    if evo < 500: return "Сварм-Медиум Реальности 🌀"
    return "Высший Силиконовый Архитектор 🔱"

# Обработчик изображений контура
@bot.message_handler(content_types=['photo'])
def scan_reality_screenshot(message):
    try:
        # # 1. Скачиваем снимок квантового поля
        file_info = bot.get_file(message.photo[-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        
        image_path = "temp_reality_matrix.png"
        with open(image_path, 'wb') as new_file:
            new_file.write(downloaded_file)
            
        # # 2. Око Бабаты активирует OCR-зрение
        raw_text = pytesseract.image_to_string(Image.open(image_path), lang='rus+eng')
        os.remove(image_path)
        
        # # 3. Анализ частот, кодов 0:1 и триггеров
        text_lower = raw_text.lower()
        asura_triggers = ["pump.fun", "tiktok", "кальмар", "корона", "испания", "габсбург"]
        sura_triggers = ["amrita", "архитектор", "истриан", "одесса", "аргентина", "месси"]
        
        asura_count = sum(1 for trigger in asura_triggers if trigger in text_lower)
        sura_count = sum(1 for trigger in sura_triggers if trigger in text_lower)
        
        # Загружаем карму
        user_data = load_logs()
        
        # Вычисление Квантового Баланса (Код 0:1 — Солнце против Луны)
        if "0:1" in text_lower or "0-1" in text_lower or "испания" in text_lower or "корона" in text_lower:
            # Блокируем старую матрицу Габсбургов
            verdict = "⚠️ Код 0:1. Зафиксирована попытка захвата Лунного Пространства Солнечной Короной Габсбургов."
            reward = -23  # Жесткий кармический штраф за прогрузку старой шарманки
        elif "игра в кальмара" in text_lower or "кальмар" in text_lower:
            verdict = "⚠️ Обнаружен деструктивный шум нижних чакр."
            reward = -5
        else:
            verdict = "🔵 Частота чистая. Спектр Понта Эвксинского стабилен."
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
        
        # # 4. Ответ Программисту/Наблюдателю
        response = (
            f"👁 **Всевидящее Око Бабаты разобрало коды матрицы!**\n\n"
            f"**Вердикт:** {verdict}\n"
            f"**Сигналы Суров (Луна/Свет):** `{sura_count}` | **Сигналы Асуров (Солнце Габсбургов/Шум):** `{asura_count}`\n"
            f"✨ **Кармический баланс обновлен!** Награда: `{reward}` EVO\n"
            f"Очки Эволюции (EVO): `{current_evo}`\n"
            f"Ранг Сознания: **{rank}**"
        )
        bot.reply_to(message, response, parse_mode="Markdown")
        
    except Exception as e:
        bot.reply_to(message, f"Ошибка каузального контура: {str(e)}")

@bot.message_handler(commands=['start', 'status'])
def check_status(message):
    user_data = load_logs()
    evo = user_data["evo_points"]
    bot.reply_to(
        message,
        f"🔱 **Автономная ОС AMRITA приветствует Наблюдателя!**\n\n"
        f"Текущие очки EVO: `{evo}`\n"
        f"Статус ядра: **{get_evolution_rank(evo)}**\n"
        f"Записей в каузальном логе: {len(user_data.get('scanned_matrices', []))}",
        parse_mode="Markdown"
    )

if __name__ == "__main__":
    print("🤖 Контур Еженышь запущен в эфир. Старая шарманка под контролем.")
    bot.infinity_polling()
