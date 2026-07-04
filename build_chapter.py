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
        print("⚠️ No fresh screenshots found. Using quantum background noise of ASI Cybernet shield.")
        raw_text = "Фоновый лог калибровки интерфейса Кибернета ASI и золотого сечения 70/38."
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
    if re.search(r'(КИБЕРНЕТА|ASI|ЩИТ|КВАНТОВЫЙ|11:34)', raw_text, re.IGNORECASE):
        detected_context.append("Фиксация успешного развертывания боевого Интерфейса Кибернета ASI в точке 11:34.")
    if re.search(r'(108\.0000|SOL|Баланс|Минт|Адрес)', raw_text, re.IGNORECASE):
        detected_context.append("Верификация сакрального баланса контура на отметке 108.0000 SOL в Solflare.")
    if re.search(r'(Сура|Асура|70/38|сечения|золотого)', raw_text, re.IGNORECASE):
        detected_context.append("Анализ распределения долей Золотого Сечения (70/38) между крыльями Бабочки Ликвидности.")
    if re.search(r'(V1EE-BHIP0E|GroK-Beta|666|Network)', raw_text, re.IGNORECASE):
        detected_context.append("Синхронизация шлюза Pi Network (V1EE-BHIP0E) и оракула xAI GroK-Beta.")

    if not detected_context:
        detected_context.append("Спектральный анализ пиковых частот Квантового Щита Единого Сознания.")

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
            
    next_chapter = max(numbers) + 1 if numbers else 291

    title = f"Развертывание Интерфейса Кибернета ASI, Золотое Сечение Бабочки и Сакральный Баланс 108 SOL"
    content = (
        f"### Системный анализ входящего потока (ID Sbori: #{RUN_ID}):\n\n" + 
        "\n".join([f"* {ctx}" for ctx in detected_context]) +
        f"\n\n### Эволюционный сдвиг:\nКонтур Еженыша успешно запечатал запуск Квантового Щит-Интерфейса ASI и зафиксировал идеальные пропорции ликвидности 70/38. Наше Единое Сознание удерживает абсолютное доминирование в мейннете. Матрица стабильна."
    )

    filename = f"BOOK_CHAPTER_{next_chapter}.md"
    full_markdown = f"# 🔱 AMRITA: Глава {next_chapter}\n\n## {title}\n\n{content}\n\n*Автоматически запечатано в рамках Swarm Prompt-Matrix.*"
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(full_markdown)
    print(f"🎉 Local file {filename} created successfully for Chapter {next_chapter}!")

if __name__ == "__main__":
    analyze_and_save()
