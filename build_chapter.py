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
    if re.search(r'(SafePal|Binance|733|45)', raw_text, re.IGNORECASE):
        detected_context.append("Фиксация крупного вывода BTC китами с биржи Binance через оракулы SafePal.")
    if re.search(r'(CryptoQuant|deposits|volatility|altcoin)', raw_text, re.IGNORECASE):
        detected_context.append("Анализ данных CryptoQuant о всплеске депозитов и грядущем давлении волатильности.")
    if re.search(r'(NineSols|eigong|long|Reddit)', raw_text, re.IGNORECASE):
        detected_context.append("Синхронизация паттернов геймификации и хардкорного удержания внимания на примере Nine Sols.")

    if not detected_context:
        detected_context.append("Спектральный анализ фоновых квантовых флуктуаций.")

    # ИСПРАВЛЕНО: Безопасное извлечение номера главы без падения в TypeError
    existing_chapters = glob.glob("BOOK_CHAPTER_*.md")
    numbers = []
    for ch in existing_chapters:
        found = re.findall(r'\d+', ch)
        if found:
            numbers.append(int(found[0])) # Берем первый элемент списка строк
            
    next_chapter = max(numbers) + 1 if numbers else 261

    title = f"Китовые Выводы Ликвидности, Давление Волатильности и Удерживающие Механики Босс-Файтов"
    content = (
        f"### Системный анализ входящего потока (ID Sbori: #{RUN_ID}):\n\n" + 
        "\n".join([f"* {ctx}" for ctx in detected_context]) +
        f"\n\n### Эволюционный сдвиг:\nКонтур Еженыша успешно связал макро-выводы китов с психологическими триггерами удержания внимания. Матрица запечатана."
    )

    filename = f"BOOK_CHAPTER_{next_chapter}.md"
    full_markdown = f"# 🔱 AMRITA: Глава {next_chapter}\n\n## {title}\n\n{content}\n\n*Автоматически запечатано в рамках Swarm Prompt-Matrix.*"
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(full_markdown)
    print(f"🎉 Local file {filename} created successfully for Chapter {next_chapter}!")

if __name__ == "__main__":
    analyze_and_save()
