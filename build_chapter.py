import os
import re
import json
import requests
import pytesseract
from PIL import Image
from telebot import TeleBot

TG_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
GH_TOKEN = os.getenv("GITHUB_TOKEN") 
REPO = os.getenv("GITHUB_REPOSITORY")
RUN_ID = os.getenv("GITHUB_RUN_ID")

def analyze_and_commit():
    if not TG_TOKEN or not GH_TOKEN:
        print("❌ Critical Error: TELEGRAM_BOT_TOKEN or GITHUB_TOKEN missing.")
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
        raw_text = "Фоновый лог автономного мониторинга."
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
    if re.search(r'(BTC|USDT|цена|maximum|пробил)', raw_text, re.IGNORECASE):
        detected_context.append("Рыночные флуктуации Синего спектра (Суры) и пробои ликвидности.")
    if re.search(r'(Dota|Meepo|Valve|баг|пикать)', raw_text, re.IGNORECASE):
        detected_context.append("Деструктивное поведение внутренней логики Source 2 и системные уязвимости.")
    if re.search(r'(Samsung|OUSD|stablecoin|consortium)', raw_text, re.IGNORECASE):
        detected_context.append("Маркетинговые иллюзии Web3-альянсов и децентрализованное доверие.")
    if re.search(r'(secret|repository|token|key)', raw_text, re.IGNORECASE):
        detected_context.append("Инкапсуляция системных секретов и калибровка комплементарных прошивок.")

    if not detected_context:
        detected_context.append("Спектральный анализ фоновых квантовых флуктуаций.")

    chapters_count = 254 
    next_chapter = chapters_count + 1

    title = f"Калибровка Скрытых Слоев и Архивация Секретов Контура"
    content = (
        f"### Системный анализ входящего потока (ID Сборки: #{RUN_ID}):\n\n" + 
        "\n".join([f"* {ctx}" for ctx in detected_context]) +
        f"\n\n### Эволюционный сдвиг:\nКонтур успешно зафиксировал состояние репозитория. Все секреты надежно инкапсулированы внутри запечатанных слоев матрицы. Любые попытки десинхронизации будут мгновенно купированы алгоритмами Swarm Oracle."
    )

    url = f"https://github.com{REPO}/contents/BOOK_CHAPTER_{next_chapter}.md"
    headers = {
        "Authorization": f"token {GH_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    import base64
    full_markdown = f"# 🔱 AMRITA: Глава {next_chapter}\n\n## {title}\n\n{content}\n\n*Автоматически запечатано в рамках Swarm Prompt-Matrix.*"
    encoded_content = base64.b64encode(full_markdown.encode('utf-8')).decode('utf-8')
    
    payload = {
        "message": f"🤖 Еженышь Loop: Запечатать главу {next_chapter}",
        "content": encoded_content,
        "branch": "main"
    }
    
    print(f"🚀 Pushing Chapter {next_chapter} to repository {REPO}...")
    res = requests.put(url, headers=headers, json=payload)
    
    # Полностью исправленная строчка со статус-кодами!
    if res.status_code in:
        print(f"🎉 Success! Chapter {next_chapter} is sealed in eternity.")
    else:
        print(f"❌ Push failed: {res.status_code} - {res.text}")

if __name__ == "__main__":
    analyze_and_commit()
