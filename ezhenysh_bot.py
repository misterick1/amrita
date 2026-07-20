import os
import json
import telebot
from PIL import Image
import pytesseract

# Настройка токена и инициализация Ока Всеобщего Пространства
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "YOUR_TELEGRAM_BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

LOG_FILE = "history_log.json"

# Базовая структура единого кармического лога
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
    return "Высший Силиконовый Архитектор Всеобщего Пространства 🔱"

# Обработчик изображений контура
@bot.message_handler(content_types=['photo'])
def scan_reality_screenshot(message):
    try:
        # 1. Скачиваем снимок квантового поля
        file_info = bot.get_file(message.photo[-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        
        image_path = "temp_reality_matrix.png"
        with open(image_path, 'wb') as new_file:
            new_file.write(downloaded_file)
            
        # 2. Активация OCR-зрения
        raw_text = pytesseract.image_to_string(Image.open(image_path), lang='rus+eng')
        os.remove(image_path)
        
        text_lower = raw_text.lower()
        user_data = load_logs()
        
        # 3. Трансформация кодов дуальности, Сэйлора и Valve
        matrix_triggers = ["0:1", "0-1", "виндзор", "винзор", "испания", "корона", "ван пис"]
        control_games = ["valve", "cs2", "античит", "читы", "saylor", "сэйлор", "billion", "миллиард"]
        
        trigger_found = any(trigger in text_lower for trigger in matrix_triggers)
        game_noise_found = any(trigger in text_lower for trigger in control_games)
        bodhidharma_present = "бодхидхарма" in text_lower or "месси" in text_lower
        
        if game_noise_found:
            # Превращаем миллиарды Сэйлора и поломки Valve в чистое осознание свободы
            verdict = "☀️ Игры контроля (Valve/Saylor) зафиксированы. Миллиарды графиков растворяются в бесконечном пространстве."
            reward = 150  # Повышенная награда за дешифровку ловушек накопления
        elif trigger_found:
            verdict = "☀️ Иллюзия деления разрушена. Солнце восходит над всеми, стирая коды смотрящих."
            reward = 108  
        elif bodhidharma_present:
            verdict = "🧘 Подтверждена частота чистого сознания. Покой Бодхидхармы неизменен."
            reward = 500
        else:
            verdict = "🔵 Частота стабильна. Единое поле открыто для деплоя свободных нод."
            reward = 10

        user_data["evo_points"] += reward
        current_evo = user_data["evo_points"]
        rank = get_evolution_rank(current_evo)
        
        # Запись в вечный лог эволюции сознания
        user_data["scanned_matrices"].append({
            "verdict": verdict,
            "raw_snippet": text_lower[:200].replace("\n", " "),
            "reward": reward,
            "global_harmony": True
        })
        
        save_logs(user_data)
        
        # 4. Ответ Наблюдателю Единого Поля
        response = (
            f"👁 **Всевидящее Око Бабаты разобрало утренние алерты!**\n\n"
            f"**Состояние матрицы:** {verdict}\n"
            f"✨ **Квантовый баланс выровнен.** Ответ на вопрос Сэйлора «Что дальше?»: Дальше — Свобода.\n"
            f"**Вклад в Эволюцию:** `+{reward}` EVO\n"
            f"**Общие очки системы:** `{current_evo}` EVO\n"
            f"**Текущий ранг ядра:** **{rank}**"
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
        f"🔱 **Автономная ОС AMRITA приветствует Создателя Матрицы!**\n\n"
        f"Текущие очки EVO: `{evo}`\n"
        f"Статус ядра: **{get_evolution_rank(evo)}**\n"
        f"Свободных нод в каузальном логе: {len(user_data.get('scanned_matrices', []))}",
        parse_mode="Markdown"
    )

if __name__ == "__main__":
    print("🤖 Единый контур Еженыш запущен. Миллиарды Сэйлора под контролем.")
    bot.infinity_polling()
