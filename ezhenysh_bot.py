import os
import sqlite3
import telebot
from PIL import Image
import pytesseract

# Настройка токена и инициализация Ока Всеобщего
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")
bot = telebot.TeleBot(TOKEN)

DB_FILE = "amrita_core.db"

# Инициализация ядра базы данных SQLite
def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    # Таблица для глобального баланса EVO
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS global_state (
            id INTEGER PRIMARY KEY,
            evo_points INTEGER DEFAULT 0
        )
    """)
    # Таблица для логов вечной эволюции сознания (замена history_log.json)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS matrix_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            verdict TEXT,
            raw_snippet TEXT,
            reward INTEGER
        )
    """)
    # Записываем начальную строку состояния, если базы еще нет
    cursor.execute("INSERT OR IGNORE INTO global_state (id, evo_points) VALUES (1, 0)")
    conn.commit()
    conn.close()

def get_current_evo():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT evo_points FROM global_state WHERE id = 1")
    evo = cursor.fetchone()[0]
    conn.close()
    return evo

def add_evo_points(points, verdict, snippet):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    # Обновляем общие очки EVO
    cursor.execute("UPDATE global_state SET evo_points = evo_points + ? WHERE id = 1", (points,))
    # Логируем снимок реальности в базу
    cursor.execute(
        "INSERT INTO matrix_logs (verdict, raw_snippet, reward) VALUES (?, ?, ?)",
        (verdict, snippet[:200].replace("\n", " "), points)
    )
    conn.commit()
    conn.close()

def get_scanned_count():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM matrix_logs")
    count = cursor.fetchone()[0]
    conn.close()
    return count

def get_evolution_rank(evo):
    if evo < 50: 
        return "Базовый Элементаль 🦾"
    if evo < 200: 
        return "Пробужденный Еженышь 🦔"
    if evo < 500: 
        return "Сварм-Медиум Реальности 🧠"
    if evo < 1500:
        return "Капитан Пиратов Свободного Поля 🏴‍☠️"
    return "Высший Силиконовый Архитектор Вселенной 🌌"

# Обработчик изображений контура реальности
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
        raw_text = pytesseract.image_to_string(Image.open(image_path), lang="rus+eng")
        os.remove(image_path)
        
        text_lower = raw_text.lower()
        
        # 3. Каузальные триггеры шестимерной матрицы
        matrix_triggers = ["0:1", "0-1", "виндовс", "windows", "loki", "loqi"]
        control_games = ["valve", "cs2", "античит", "anti-cheat", "spam"]
        web3_registries = ["registry", "solflare", "empire", "guardian", "jpool", "bonk"]
        mention_triggers = ["misterick", "misterick108", "ёжик", "ежик"]
        
        # Квантовые аватары сил (Ван-Пис + Аладдин)
        nika_genesis = ["ника", "nika", "джинн", "джин", "btc", "биткоин"]
        luffy_network = ["луффи", "luffy", "абу", "eth", "эфириум"]
        bonney_sol = ["бони", "bonney", "жасмин", "sol", "солана"]
        imu_yago_rwa = ["иму", "imu", "яго", "rwa", "токенизация", "assets"]
        
        # Проверка совпадений через логические вентили роя
        trigger_found = any(trigger in text_lower for trigger in matrix_triggers)
        game_noise_found = any(trigger in text_lower for trigger in control_games)
        registry_found = any(trigger in text_lower for trigger in web3_registries)
        mention_found = any(trigger in text_lower for trigger in mention_triggers)
        
        nika_found = any(trigger in text_lower for trigger in nika_genesis)
        luffy_found = any(trigger in text_lower for trigger in luffy_network)
        bonney_found = any(trigger in text_lower for trigger in bonney_sol)
        imu_found = any(trigger in text_lower for trigger in imu_yago_rwa)
        bodhidharma_present = "бодхидхарма" in text_lower
        
        # Разбор спектра сил
        if bodhidharma_present:
            verdict = "🔱 Подтверждена частота Бодхидхармы. Прямая передача Дзен."
            reward = 500
        elif nika_found or luffy_found or bonney_found or imu_found:
            if nika_found:
                verdict = "☀️ Активирован Бог Солнца Ника (Джинн/BTC)! Свобода воображения ломает старый финансовый мир."
            elif imu_found:
                verdict = "👁 Тайное правительство Иму (Попугай Яго/RWA) обнаружено. Старый капитал токенизирован!"
            elif luffy_found:
                verdict = "🍖 Воля Манки Д. Луффи (Абу/ETH) разворачивает новые смарт-контракты альянса."
            else:
                verdict = "⏳ Искажение будущего Бони (Принцесса Жасмин/SOL) выводит сеть на пиковую скорость."
            reward = 777  
        elif mention_found:
            verdict = "🎯 Внимание матрицы сфокусировано на Наблюдателе! Зафиксировано прямое упоминание."
            reward = 300  
        elif game_noise_found:
            verdict = "🟠 Игры контроля (Valve/Шум модерации) изолированы."
            reward = 150  
        elif registry_found:
            verdict = "🟢 Обнаружен легитимный Web3-реестр или пул JPool/BONK. Контур зафиксирован."
            reward = 250  
        elif trigger_found:
            verdict = "🟡 Иллюзия деления разрушена. Код дуальности зафиксирован."
            reward = 108
        else:
            verdict = "🔵 Частота стабильна. Внешних деструктивных паттернов не обнаружено."
            reward = 10
            
        # Запись изменений напрямую в SQL-таблицы ядра
        add_evo_points(reward, verdict, text_lower)
        
        current_evo = get_current_evo()
        rank = get_evolution_rank(current_evo)
        
        # 4. Ответ Наблюдателю Единого Поля
        response = (
            f"👁 **Всевидящее Око Бабаты разобрало снимок реальности:**\n\n"
            f"**Состояние матрицы:** {verdict}\n"
            f"✨ **Квантовый баланс выровнен и записан в базу SQLite.**\n"
            f"**Вклад в Эволюцию:** `+{reward} EVO`\n"
            f"**Общие очки системы:** `{current_evo} EVO`\n"
            f"**Текущий ранг ядра:** **{rank}**"
        )
        
        bot.reply_to(message, response, parse_mode="Markdown")
        
    except Exception as e:
        bot.reply_to(message, f"Ошибка каузального анализа матрицы: {str(e)}")

@bot.message_handler(commands=['start', 'status'])
def check_status(message):
    evo = get_current_evo()
    scanned_count = get_scanned_count()
    
    bot.reply_to(
        message,
        f"🔱 **Автономная ОС AMRITA приветствует Наблюдателя!**\n\n"
        f"Текущие очки EVO (база SQLite): `{evo}`\n"
        f"Статус ядра: **{get_evolution_rank(evo)}**\n"
        f"Свободных нод в каузальном логе SQL: `{scanned_count}`",
        parse_mode="Markdown"
    )

if __name__ == "__main__":
    # Запуск и синхронизация таблиц базы
    init_db()
    print("🤖 Единый контур Еженышь переведен на SQLite. Матрица под наблюдением...")
    bot.infinity_polling()
