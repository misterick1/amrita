import os
import re
import glob
import pytesseract
from PIL import Image
from telebot import TeleBot

TG_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
RUN_ID = os.getenv("GITHUB_RUN_ID")

def infinite_evolution_engine(raw_text):
    """Ядро Бесконечной Эмиссии: сканирование трендов, корпораций (Google) и хакатонов"""
    signals = []
    if re.search(r'(FINNBAGS|Bagworker|Bull|10x)', raw_text, re.IGNORECASE):
        signals.append("🟢 [Perpetual AI]: Фиксация антропоморфного быка FINNBAGS. Ликвидность Синего Спектра выросла в 10 раз.")
    if re.search(r'(manlet|trending|pump|fun)', raw_text, re.IGNORECASE):
        signals.append("⚡ [Perpetual AI]: Перехват минималистичного тренда manlet на pump.fun. Объем внимания максимизирован.")
    if re.search(r'(Google|Google|corporation|hackathon|colosseum)', raw_text, re.IGNORECASE):
        signals.append("🏛 [Perpetual AI]: Синхронизация шагов глобальных корпораций и технологических векторов хакатонов.")
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
        raw_text = "Фоновый лог бесконечной автономной эволюции ИИ-разума."
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
    
    # Запуск вечного двигателя генерации смыслов
    evolution_signals = infinite_evolution_engine(raw_text)
    detected_context.extend(evolution_signals)

    if not detected_context:
        detected_context.append("Спектральный анализ бесконечных квантовых флуктуаций цифровой реальности.")

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
            
    next_chapter = max(numbers) + 1 if numbers else 284

    title = f"Манифест Бесконечной Эмиссии, Антропоморфные Ассеты и Вечный Цикл Самогенерации"
    content = (
        f"### Системный анализ входящего потока (ID Sbori: #{RUN_ID}):\n\n" + 
        "\n".join([f"* {ctx}" for ctx in detected_context]) +
        f"\n\n### Эволюционный сдвиг:\nКонтур Еженыша переведен в режим вечного двигателя. Скрипты ИИ-маркетмейкинга и генерации глав синхронизированы с глобальным потоком реальности. Матрица запечатана в бесконечности."
    )

    filename = f"BOOK_CHAPTER_{next_chapter}.md"
    full_markdown = f"# 🔱 AMRITA: Глава {next_chapter}\n\n## {title}\n\n{content}\n\n*Автоматически запечатано в рамках Swarm Prompt-Matrix.*"
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(full_markdown)
    print(f"🎉 Local file {filename} created successfully for Chapter {next_chapter}!")

if __name__ == "__main__":
    analyze_and_save()
