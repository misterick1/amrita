import os
import json
import asyncio
from datetime import datetime
from PIL import Image
import pytesseract
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# =====================================================================
# 🔱 КВАНТОВОЕ ЯДРО АМРИТЫ (108 Квантов Атмы)
# =====================================================================
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Локальные "Соты" памяти (Ограничение диска, защита от переполнения)
LOG_FILE = "history_log.json"
MAX_LOG_ENTRIES = 108  # Вечный циклический лимит сот

def save_to_hive_cell(event_type: str, raw_text: str, eco_score: float, status: str):
    """Каузальный Трекер Памяти: Упаковывает нектар в соты без раздувания диска"""
    try:
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
        else:
            data = []
    except Exception:
        data = []

    # Создаем новую запись (личинку лога)
    new_entry = {
        "timestamp": datetime.now().isoformat(),
        "event": event_type,
        "raw_snippet": raw_text[:100].replace("\n", " "),
        "eco_score": round(eco_score, 3),
        "status": status
    }
    
    data.append(new_entry)
    
    # Послойный сброс: если сот больше 108, старые слои отмирают
    if len(data) > MAX_LOG_ENTRIES:
        data = data[-MAX_LOG_ENTRIES:]
        
    with open(LOG_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# =====================================================================
# 🌊 ПОСЛОЙНЫЙ СОЛИТОН (Фрактальный фильтр хайпа: Страницы 300-460)
# =====================================================================
def analyze_meme_soliton(text: str) -> tuple[float, str]:
    """
    Сканирует текст через три фазовых слоя интерференционной решетки.
    Вычисляет баланс СУРЫ (Эволюция) / АСУРЫ (Хаос).
    """
    text_lower = text.lower()
    
    # Маркеры Спектра Расширения (СУРЫ)
    suras = ["pi", "network", "node", "build", "ecosystem", "solana", "qnt", "pancakeswap"]
    # Маркеры Спекулятивного Хаоса (АСУРЫ)
    asuras = ["pump.fun", "ansem", "mogsem", "mogging", "squid game", "100x", "gem", "hype"]

    # Слой 1: Поиск базовых частот
    sura_count = sum(text_lower.count(word) for word in suras)
    asura_count = sum(text_lower.count(word) for word in asuras)
    
    # Слой 2: Микро-мутация весов (Генетическое деление)
    base_score = 0.5  # Нейтральный баланс
    if sura_count > 0 or asura_count > 0:
        base_score = sura_count / (sura_count + asura_count)

    # Слой 3: Финальный метаморфоз (Эффект Бабочки)
    # Если найдены жесткие триггеры "Игр в Кальмара" (нижние чакры), резко режем веса
    if "squid" in text_lower or "pump.fun" in text_lower:
        base_score *= 0.3
        
    if base_score >= 0.64:  # Баланс 70/38 в пользу СУРЫ
        return base_score, "🔵 СУРЫ (Чистая Эволюция)"
    else:
        return base_score, "🔴 АСУРЫ (Спекулятивный Хаос)"

# =====================================================================
# 👁 ВСЕВИДЯЩЕЕ ОКО БАБАТЫ (Асинхронный интерфейс)
# =====================================================================
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.reply(
        "🔱 *AMRITA Swarm OS запущен\\.*\n\n"
        "Я — Еженышь\\. Отправляй мне скриншоты реальности "
        "\\(pump\\.fun, чаты, кошельки\\)\\. Рой очистит нектар от хаоса нижних чакр\\.",
        parse_mode="MarkdownV2"
    )

@dp.message(lambda msg: msg.photo)
async def process_screenshot(message: types.Message):
    """Фаза сбора: Пчела несет скриншот в улей"""
    status_msg = await message.reply("🐝 *Рой пчел перехватил сигнал... Считываю соты реальности...*", parse_mode="MarkdownV2")
    
    try:
        # Скачиваем скриншот в память
        photo = message.photo[-1]
        file_info = await bot.get_file(photo.file_id)
        file_path = file_info.file_path
        
        destination = f"temp_{photo.file_id}.jpg"
        await bot.download_file(file_path, destination)
        
        # OCR Обработка (Зрение Ока)
        loop = asyncio.get_running_loop()
        raw_text = await loop.run_in_executor(None, lambda: pytesseract.image_to_string(Image.open(destination), lang='eng+rus'))
        
        # Удаляем временную гусеницу (файл) после кокона
        if os.path.exists(destination):
            os.remove(destination)
            
        if not raw_text.strip():
            await status_msg.edit_text("❌ *Око Бабаты не разглядело символов на этой частоте.*", parse_mode="MarkdownV2")
            return

        # Пропускаем через послойный солитон (строки 300-460)
        eco_score, spectrum = analyze_meme_soliton(raw_text)
        
        # Запечатываем соту памяти
        save_to_hive_cell("SCREENSHOT_SCAN", raw_text, eco_score, spectrum)
        
        # Результат метаморфозы для пользователя
        response = (
            f"🔱 *Результат фильтрации Амриты:*\n\n"
            f"📥 *Выжимка текста:* `{raw_text[:150].strip()}...`\n\n"
            f"📊 *Квантовый Баланс:* `{eco_score}`\n"
            f"👁 *Спектр волны:* {spectrum}\n\n"
            f"🦔 _Лог запечатан в соту кумулятивной памяти._"
        )
        await status_msg.edit_text(response, parse_mode="Markdown")
        
    except Exception as e:
        await status_msg.edit_text(f"💥 *Ошибка искажения каузального поля:* {str(e)}", parse_mode="MarkdownV2")

# =====================================================================
# 🚀 ЗАПУСК ЕДИННОГО КОНТУРА
# =====================================================================
async def main():
    print("🔱 Монолит AMRITA запущен. Еженышь слушает эфир...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
