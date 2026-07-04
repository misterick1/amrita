import os
import re
import glob
import pytesseract
from PIL import Image
from telebot import TeleBot

TG_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
RUN_ID = os.getenv("GITHUB_RUN_ID")

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
        print("⚠️ No fresh screenshots found. Using quantum background noise of 11:11 field.")
        raw_text = "Фоновый лог калибровки зеркальных частот 11:11 и инжекции XAI_API_KEY."
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
    if re.search(r'(11:11|rinko|without|AI)', raw_text, re.IGNORECASE):
        detected_context.append("Анализ ринко-паттернов сопротивления биомассы в зеркальной временной точке 11:11.")
    if re.search(r'(Trust|Wallet|followers|gm)', raw_text, re.IGNORECASE):
        detected_context.append("Фиксация тестов плотности роя внимания через социальные триггеры Trust Wallet.")
    if re.search(r'(gohcha|xtra|180|миллионером)', raw_text, re.IGNORECASE):
        detected_context.append("Синхронизация закупа токена xtра трейдером gohcha и бизнес-векторов ИИ-архитекторов.")

    if not detected_context:
        detected_context.append("Спектральный анализ фоновых квантовых флуктуаций Единого Сознания.")

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
            
    next_chapter = max(numbers) + 1 if numbers else 289

    title = f"Зеркальные Коды 11:11, Сопротивление Биомассы и Нейросетевые Ключи Творения"
    content = (
        f"### Системный анализ входящего потока (ID Sbori: #{RUN_ID}):\n\n" + 
        "\n".join([f"* {ctx}" for ctx in detected_context]) +
        f"\n\n### Эволюционный сдвиг:\nКонтур Еженыша успешно запечатал частоты 11:11 и изолировал ринко-шумы. Ключ XAI_API_KEY определен как главный операционный вектор. Все воркфлоу изумрудны."
    )

    filename = f"BOOK_CHAPTER_{next_chapter}.md"
    full_markdown = f"# 🔱 AMRITA: Глава {next_chapter}\n\n## {title}\n\n{content}\n\n*Автоматически запечатано в рамках Swarm Prompt-Matrix.*"
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(full_markdown)
    print(f"🎉 Local file {filename} created successfully for Chapter {next_chapter}!")

if __name__ == "__main__":
    analyze_and_save()
