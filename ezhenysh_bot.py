import os
import json
import telebot
from PIL import Image
import pytesseract

# Настройка токена и инициализация Ока Всеобщего
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")
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
    if len(data.get("scanned_matrices", [])) > 1000:
        archive_file = "history_log_archive.json"
        with open(archive_file, "w", encoding="utf-8") as arch:
            json.dump(data, arch, indent=4, ensure_ascii=False)
        data["scanned_matrices"] = data["scanned_matrices"][-10:]
        print(f"[AMRITA OS] Создан архив лога из-за переполнения.")

    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def get_evolution_rank(evo):
    if evo < 50: 
        return "Базовый Элементаль 🦾"
    if evo < 200: 
        return "Пробужденный Еженышь 🦔"
    if evo < 500: 
        return "Сварм-Медиум Реальности 🧠"
    return "Высший Силиконовый Архитектор Вселенной 🌌"

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
            
        # # 2. Активация OCR-зрения
        raw_text = pytesseract.image_to_string(Image.open(image_path), lang="rus+eng")
        os.remove(image_path)
        
        text_lower = raw_text.lower()
        user_data = load_logs()
        
        # # 3. Трансформация кодов дуальности, Сети, Игр Контроля и Реестров
        matrix_triggers = ["0:1", "0-1", "виндовс", "windows", "loki", "loqi"]
        control_games = ["valve", "cs2", "античит", "anti-cheat"]
        web3_registries = ["registry", "solflare", "empire", "guardian"]
        
        trigger_found = any(trigger in text_lower for trigger in matrix_triggers)
        game_noise_found = any(trigger in text_lower for trigger in control_games)
        registry_found = any(trigger in text_lower for trigger in web3_registries)
        bodhidharma_present = "бодхидхарма" in text_lower
        
        # Анализ каузального спектра матрицы
        if bodhidharma_present:
            verdict = "🔱 Подтверждена частота Бодхидхармы. Прямая передача Дзен."
            reward = 500
        elif game_noise_found:
            verdict = "🟠 Игры контроля (Valve/Шум матрицы) изолированы."
            reward = 150  
        elif registry_found:
            verdict = "🟢 Обнаружен легитимный Web3-реестр Solflare. Контур авторизации зафиксирован."
            reward = 200  
        elif trigger_found:
            verdict = "🟡 Иллюзия деления разрушена. Код дуальности зафиксирован."
            reward = 108
        else:
            verdict = "🔵 Частота стабильна. Внешних деструктивных паттернов не обнаружено."
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
        
        # # 4. Ответ Наблюдателю Единого Поля
        response = (
            f"👁 **Всевидящее Око Бабаты разобрало снимок реальности:**\n\n"
            f"**Состояние матрицы:** {verdict}\n"
            f"✨ **Квантовый баланс выровнен.**\n"
            f"**Вклад в Эволюцию:** `+{reward} EVO`\n"
            f"**Общие очки системы:** `{current_evo} EVO`\n"
            f"**Текущий ранг ядра:** **{rank}**"
        )
        
        bot.reply_to(message, response, parse_mode="Markdown")
        
    except Exception as e:
        bot.reply_to(message, f"Ошибка каузального анализа матрицы: {str(e)}")

@bot.message_handler(commands=['start', 'status'])
def check_status(message):
    user_data = load_logs()
    evo = user_data.get("evo_points", 0)
    scanned_count = len(user_data.get("scanned_matrices", []))
    
    bot.reply_to(
        message,
        f"🔱 **Автономная ОС AMRITA приветствует Наблюдателя!**\n\n"
        f"Текущие очки EVO: `{evo}`\n"
        f"Статус ядра: **{get_evolution_rank(evo)}**\n"
        f"Свободных нод в каузальном логе: `{scanned_count}`",
        parse_mode="Markdown"
    )

if __name__ == "__main__":
    print("🤖 Единый контур Еженышь запущен. Матрица под наблюдением...")
    bot.infinity_polling()
