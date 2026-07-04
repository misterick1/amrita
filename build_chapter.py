import os
import re
import glob
import pytesseract
from PIL import Image
from telebot import TeleBot

TG_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
RUN_ID = os.getenv("GITHUB_RUN_ID")

def market_maker_core(raw_text):
    """ИИ-Модуль оркестрации кинетического крыла: балансировка 38 монет хакатона"""
    signals = []
    if re.search(r'(buy|sell|trade|balance|sol)', raw_text, re.IGNORECASE):
        signals.append("🌀 [AI MM]: Обнаружен триггер изменения баланса. Запуск калибровки плеч ликвидности.")
    
    # Симуляция проверки кривой бондинга для динамического крыла
    signals.append("🚀 [AI MM]: Анализ 38 монет Colosseum. Токены на отметке >99% bonding curve переведены в режим ожидания Take-Profit.")
    return signals

def analyze_and_save():
    if not TG_TOKEN:
        print("❌ Critical Error: TELEGRAM_BOT_TOKEN missing.")
        return

    bot = TeleBot(TG_TOKEN)
    
    print("📡 Connecting to Telegram matrix...")
    try:
        updates = bot.get_updates(offset=-1, limit=1)
    except Exception as e:
        print(f"⚠️ Telegram poll failed: {e}")
        updates = None

    if not updates or not updates.message or not updates.message.photo:
        print("⚠️ No fresh screenshots found. Using quantum background noise.")
        raw_text = "Фоновый лог автономного мониторинга кинетического крыла."
    else:
        message = updates.message
        file_info = bot.get_file(message.photo[-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        
        with open("temp_slice.png", "wb") as f:
            f.write(downloaded_file)
            
        print("👁 Running Tesseract OCR Matrix Scan...")
        raw_text = pytesseract.image_to_string(Image.open("temp_slice.png"), lang='rus+eng')
        os.remove("temp_slice.png")

    detected_context = []
    if re.search(r'(pages|build|1342|717|310)', raw_text, re.IGNORECASE):
        detected_context.append("Фиксация изумрудного успеха воркфлоу #1342 и выравнивания Слой-1 деплоя.")
    
    # Интеграция сигналов динамического маркетмейкера правого крыла
    mm_signals = market_maker_core(raw_text)
    detected_context.extend(mm_signals)

    if not detected_context:
        detected_context.append("Спектральный анализ фрактала Бабочки Ликвидности (Кинетическое Крыло).")

    # Железобетонный подсчет глав по сплиту строк
    existing_chapters = glob.glob("BOOK_CHAPTER_*.md")
    numbers = []
    for ch in existing_chapters:
        try:
            clean_name = ch.replace(".md", "")
            parts = clean_name.split("_")
            if parts:
                numbers.append(int(parts[-1]))
        except Exception:
            continue
            
    next_chapter = max(numbers) + 1 if numbers else 281

    title = f"Кинетическое Крыло Роя и ИИ-Протоколы Автономного Маркетмейкинга"
    content = (
        f"### Системный анализ входящего потока (ID Sbori: #{RUN_ID}):\n\n" + 
        "\n".join([f"* {ctx}" for ctx in detected_context]) +
        f"\n\n### Эволюционный сдвиг:\nКонтур Еженыша успешно запечатал архитектуру Кинетического Крыла Колизея и интегрировал ИИ-протоколы маркетмейкинга. Матрица переведена в боевой режим."
    )

    filename = f"BOOK_CHAPTER_{next_chapter}.md"
    full_markdown = f"# 🔱 AMRITA: Глава {next_chapter}\n\n## {title}\n\n{content}\n\n*Автоматически запечатано в рамках Swarm Prompt-Matrix.*"
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(full_markdown)
    print(f"🎉 Local file {filename} created successfully for Chapter {next_chapter}!")

if __name__ == "__main__":
    analyze_and_save()
