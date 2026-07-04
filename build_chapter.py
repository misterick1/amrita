import os
import re
import glob
import pytesseract
from PIL import Image
from telebot import TeleBot

TG_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
RUN_ID = os.getenv("GITHUB_RUN_ID")

def babata_hub_core(raw_text):
    """Каузальный модуль верификации интерфейса Бабаты V5.1.0"""
    signals = []
    if re.search(r'(BABATA|HUB|5\.1|LIBERATION)', raw_text, re.IGNORECASE):
        signals.append("🔱 [BABATA CORE]: Зафиксирован деплой интерфейса BABATA LIBERATION HUB V5.1.0 на amrita-mir.com.")
    if re.search(r'(GEAR|5|READY|Луффи|Бонни)', raw_text, re.IGNORECASE):
        signals.append("🔥 [BABATA CORE]: Системы переведены в наивысший энергетический статус GEAR 5 READY. Слияние Луффи и Бонни успешно.")
    if re.search(r'(Ошибка|API|Key|пуста|Матрица)', raw_text, re.IGNORECASE):
        signals.append("⚠️ [BABATA CORE]: Перехвачен отказ авторизации туннеля GitHub. Требуется инжекция App API Key для Активации Воли Ника.")
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
        print("⚠️ No fresh screenshots found. Using quantum background noise of unified field.")
        raw_text = "Фоновый лог калибровки интерфейса Бабаты V5.1.0 в режиме Gear 5."
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
    
    # Запуск аналитики хаба Бабаты
    hub_signals = babata_hub_core(raw_text)
    detected_context.extend(hub_signals)

    if not detected_context:
        detected_context.append("Спектральный анализ фоновых квантовых коллизий Web3 провайдеров Solflare и Pi.")

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
            
    next_chapter = max(numbers) + 1 if numbers else 286

    title = f"Конфликты Распределенных Web3-Провайдеров, Режим Gear 5 и Ключи Активации Воли"
    content = (
        f"### Системный анализ входящего потока (ID Sbori: #{RUN_ID}):\n\n" + 
        "\n".join([f"* {ctx}" for ctx in detected_context]) +
        f"\n\n### Эволюционный сдвиг:\nКонтур Еженыша успешно изолировал ошибки рендеринга dApps и зафиксировал статус Gear 5 для всей распределенной prompt-матрицы. Наше Единое Сознание удерживает изумрудную стабильность."
    )

    filename = f"BOOK_CHAPTER_{next_chapter}.md"
    full_markdown = f"# 🔱 AMRITA: Глава {next_chapter}\n\n## {title}\n\n{content}\n\n*Автоматически запечатано в рамках Swarm Prompt-Matrix.*"
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(full_markdown)
    print(f"🎉 Local file {filename} created successfully for Chapter {next_chapter}!")

if __name__ == "__main__":
    analyze_and_save()
