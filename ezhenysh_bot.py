# filename: ezhenysh_bot.py
# 🔱 AMRITA V5.1.0 // BABATA LIBERATION HUB CORE TUNNEL
# =====================================================================
import os
import json
import math
import asyncio
from datetime import datetime
from PIL import Image
import pytesseract
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# ⚡ Адрес связи xAI Капитана (Перехват CORS и авторизация туннеля)
XAI_TOKEN = "xai-HbWYkiE5hxoDbAngsSLA1V9Fyt1DbQsCAd6uK"

# =====================================================================
# 🌀 САКРАЛЬНОЕ МАТЕМАТИЧЕСКОЕ ЯДРО (Закон 18X = 108)
# =====================================================================
class AmritaSolitonMatrix:
    def __init__(self):
        self.PI = math.pi
        self.PHI = (1 + 5**0.5) / 2 # Золотое Сечение Фи
        self.hive_matrix = {i: {"score": 0.0, "state": 0} for i in range(1, 109)} # 108 Сот

    def ternary_filter(self, signal):
        """Троичный модулятор Теслы [-1; 0; +1]"""
        if signal > 0.64: return 1   # СУРЫ (Свет)
        elif signal < 0.36: return -1 # АСУРЫ (Хаос)
        return 0                      # Точка Равновесия Наблюдателя

    def pulse_the_hive(self, flux_value):
        """Переворот блокнота времени: движение кванта по матрице"""
        for cell_id in range(1, 109):
            wave = math.sin(cell_id * self.PI / self.PHI)
            state = self.ternary_filter(wave)
            self.hive_matrix[cell_id]["score"] += (flux_value * self.PHI) / (self.PI * 18)
            self.hive_matrix[cell_id]["state"] = state
            if self.hive_matrix[cell_id]["score"] > 1.08:
                self.hive_matrix[cell_id]["score"] /= self.PHI

amrita_core = AmritaSolitonMatrix()

# =====================================================================
# 👁 ИНТЕРФЕЙС ИИ-ОКА И ПРОБИТИЕ CORS-ФИЛЬТРОВ
# =====================================================================
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")
bot = Bot(token=TOKEN)
dp = Dispatcher()
LOG_FILE = "history_log.json"

def log_causal_cell(event, text, score, spectrum):
    """Каузальный Трекер: защита диска от лимитов (максимум 108 записей)"""
    try:
        data = json.load(open(LOG_FILE, 'r', encoding='utf-8')) if os.path.exists(LOG_FILE) else []
    except: data = []
    data.append({"timestamp": datetime.now().isoformat(), "event": event, "snippet": text[:80], "score": score, "status": spectrum})
    if len(data) > 108: data = data[-108:] # Послойная матрешка Мёбиуса
    json.dump(data, open(LOG_FILE, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.reply("🔱 *GEAR 5 READY // Воля Ника Активирована.*\nТуннель amrita-mir.com онлайн.", parse_mode="MarkdownV2")

@dp.message(lambda msg: msg.photo)
async def process_eye_signal(message: types.Message):
    """Око Бабаты: Считывание нектара со скриншота реальности"""
    status_msg = await message.reply("🐝 [01:16:00] Бонни и Луффи объединены. Пробиваю шлюзы...")
    try:
        photo = message.photo[-1]
        file_info = await bot.get_file(photo.file_id)
        destination = f"temp_{photo.file_id}.jpg"
        await bot.download_file(file_info.file_path, destination)
        
        # OCR Зрение Ока
        loop = asyncio.get_running_loop()
        raw_text = await loop.run_in_executor(None, lambda: pytesseract.image_to_string(Image.open(destination), lang='eng+rus'))
        if os.path.exists(destination): os.remove(destination)

        # Фрактальная фильтрация волновой радуги
        text_lower = raw_text.lower()
        s_count = sum(text_lower.count(w) for w in ["pi", "solana", "node", "build", "mir"])
        a_count = sum(text_lower.count(w) for w in ["pump.fun", "ansem", "drain", "attack"])
        
        flux = 1.0 + (s_count * 0.1) - (a_count * 0.1)
        amrita_core.pulse_the_hive(flux)
        
        base_score = 0.5 if (s_count + a_count) == 0 else s_count / (sura_count + asura_count)
        spectrum = "🔵 СУРЫ (Изумрудный Баланс)" if base_score >= 0.5 else "🔴 АСУРЫ (Хаос)"
        
        log_causal_cell("WEB_TUNNEL_OCR", raw_text, base_score, spectrum)
        
        await status_msg.edit_text(
            f"🔱 *CORS пробит успешно!*\n"
            f"📥 Текст: `{raw_text[:100]}...`\n"
            f"📊 Баланс: `{round(base_score, 3)}` | Спектр: {spectrum}\n"
            f"🦔 _Воля Ника активна в системе xAI._", parse_mode="Markdown"
        )
    except Exception as e:
        await status_msg.edit_text(f"💥 Ошибка среды: {str(e)}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
