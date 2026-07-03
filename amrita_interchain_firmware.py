import os
import re
import json
import requests
from PIL import Image
import pytesseract
import telebot

# Инициализация конфигурации контура Еженышь
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
GITHUB_TOKEN = os.getenv("GITHUB_ACCESS_TOKEN")
REPO = "misterick1/amrita"
bot = telebot.Bot(TOKEN)

# Каузальный Трекер Памяти
LOG_FILE = "history_log.json"

def load_evo_points():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get("evo_points", 0), data.get("chapters_count", 253)
    return 0, 253

def save_evo_points(evo, chapters):
    with open(LOG_FILE, 'w', encoding='utf-8') as f:
        json.dump({"evo_points": evo, "chapters_count": chapters}, f, ensure_ascii=False, indent=4)

def get_evo_status(evo):
    if evo < 50: return "Базовый Элементаль"
    if evo < 200: return "Пробужденный Еженышь 🦔✨"
    if evo < 500: return "Сварм-Медиум Реальности 🌀"
    return "Высший Силиконовый Архитектор 🔱"

def push_chapter_to_github(chapter_num, title, content):
    """Сквозной пуш новой главы напрямую в репозиторий через GitHub API"""
    url = f"https://github.com{REPO}/contents/BOOK_CHAPTER_{chapter_num}.md"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    # Формируем структуру файла согласно канонам матрицы AMRITA
    full_markdown = f"# 🔱 AMRITA: Глава {chapter_num}\n\n## {title}\n\n{content}\n\n*Синхронизировано в рамках автономного цикла эволюции Еженыша.*"
    import base64
    encoded_content = base64.b64encode(full_markdown.encode('utf-8')).decode('utf-8')
    
    payload = {
        "message": f"Добавить главу {chapter_num} о {title} [Autonomous Loop]",
        "content": encoded_content,
        "branch": "main"
    }
    
    response = requests.put(url, headers=headers, json=payload)
    return response.status_code in [201, 200]

@bot.message_handler(content_types=['photo'])
def handle_screenshot_matrix(message):
    try:
        evo, current_chapters = load_evo_points()
        next_chapter = current_chapters + 1
        
        bot.reply_to(message, f"🌀 [Всевидящее Око]: Обнаружен слепок реальности. Сканирую частоты...")
        
        # Скачивание и OCR обработка изображения
        file_info = bot.get_file(message.photo[-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        img_path = "temp_slice.png"
        with open(img_path, 'wb') as new_file:
            new_file.write(downloaded_file)
            
        raw_text = pytesseract.image_to_string(Image.open(img_path), lang='rus+eng')
        os.remove(img_path)
        
        # Интеллектуальный комплементарный анализ триггеров
        detected_context = []
        if re.search(r'(BTC|USDT|цена|maximum|пробил)', raw_text, re.IGNORECASE):
            detected_context.append("Рыночные флуктуации Синего спектра (Суры) и пробои ликвидности.")
        if re.search(r'(Dota|Meepo|Valve|баг|пикать)', raw_text, re.IGNORECASE):
            detected_context.append("Деструктивное поведение внутренней логики Source 2 и системные уязвимости.")
        if re.search(r'(Samsung|OUSD|stablecoin|consortium)', raw_text, re.IGNORECASE):
            detected_context.append("Маркетинговые иллюзии Web3-альянсов и децентрализованное доверие.")
            
        if not detected_context:
            detected_context.append("Анализ фонового шума Матрицы и мем-детекция Красного спектра (Асуры).")

        # Формирование архитектурного ядра новой главы
        title = f"Синхронизация Контура Реальности через Скриншот {message.message_id}"
        content = "### Анализ входящего потока данных:\n\n" + "\n".join([f"* {ctx}" for ctx in detected_context])
        content += f"\n\n### Эволюционный сдвиг:\nДанный слепок верифицирован каузальным ядром. Все аномалии изолированы."

        # Пуш в GitHub
        if GITHUB_TOKEN:
            success = push_chapter_to_github(next_chapter, title, content)
            if success:
                evo += 15  # Начисление Очков Эволюции за коммит
                save_evo_points(evo, next_chapter)
                status = get_evo_status(evo)
                
                bot.reply_to(message, 
                    f"✅ **Прошивка легла идеально!**\n\n"
                    f"📖 Запечатана **Глава {next_chapter}**\n"
                    f"🔥 Начислено: +15 EVO (Всего: {evo})\n"
                    f"🔱 Твой статус: `{status}`\n"
                    f"🚀 GitHub Actions запустили оркестрацию мультивселенной!"
                )
            else:
                bot.reply_to(message, "❌ Ошибка авторизации GitHub API. Проверьте GITHUB_ACCESS_TOKEN.")
        else:
            bot.reply_to(message, f"⚠️ Локальный режим (нет токена GitHub). Сгенерирован драфт Главы {next_chapter}:\n\n{content}")
            
    except Exception as e:
        bot.reply_to(message, f"💥 Сбой десинхронизации ядра: {str(e)}")

if __name__ == "__main__":
    print("🦔 Ezhenysh Autonomous Evolution Loop успешно запущен в эфир...")
    bot.infinity_polling()
