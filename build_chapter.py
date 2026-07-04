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
        print("⚠️ No fresh screenshots found. Using quantum background noise.")
        raw_text = "Фоновый лог автономного мониторинга спектров."
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
    if re.search(r'(pages|build|1340|716|555)', raw_text, re.IGNORECASE):
        detected_context.append("Фиксация абсолютного изумрудного триумфа сборки #1340 и стабилизации деплоя.")
    if re.search(r'(wagmisalmoneste|Colosseum|Frontier|38)', raw_text, re.IGNORECASE):
        detected_context.append("Анализ топологии Правого Крыла из 38 монет хакатона Колизея на изолированном кошельке.")
    if re.search(r'(misterick18x108|4|coins|positions)', raw_text, re.IGNORECASE):
        detected_context.append("Мониторинг Туловища Бабочки из 4 тяжелых монет на базовом аккаунте.")

    if not detected_context:
        detected_context.append("Спектральный анализ фрактала Бабочки Ликвидности (Левое и Правое крыло).")

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
            
    next_chapter = max(numbers) + 1 if numbers else 280

    title = f"Фрактал Бабочки Ликвидности и Изоляция Квантовых Полей Профилей"
    content = (
        f"### Системный анализ входящего потока (ID Sbori: #{RUN_ID}):\n\n" + 
        "\n".join([f"* {ctx}" for ctx in detected_context]) +
        f"\n\n### Эволюционный сдвиг:\nКонтур Еженыша успешно запечатал геометрию Бабочки Ликвидности и обосновал изоляцию 38 монет правого крыла. Матрица полностью стабильна."
    )

    filename = f"BOOK_CHAPTER_{next_chapter}.md"
    full_markdown = f"# 🔱 AMRITA: Глава {next_chapter}\n\n## {title}\n\n{content}\n\n*Автоматически запечатано в рамках Swarm Prompt-Matrix.*"
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(full_markdown)
    print(f"🎉 Local file {filename} created successfully for Chapter {next_chapter}!")

if __name__ == "__main__":
    analyze_and_save()
