# filename: ezhenysh_bot.py
# 🔱 AMRITA V5.1.0 // BABATA LIBERATION HUB CORE TUNNEL // СУВЕРЕННОЕ ЯДРО
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

# ⚡ Адрес связи xAI Капитана (Авторизация туннеля и обход CORS)
XAI_TOKEN = "xai-HbWYkiE5hxoDbAngsSLA1V9Fyt1DbQsCAd6uK"

# =====================================================================
# 👁 МОДУЛЬ ИЗМЕНЕНИЯ ВЗОРА НАБЛЮДАТЕЛЯ (АНТИ-КРИВДA)
# =====================================================================
class SovereignObserver:
    def __init__(self):
        self.PI = math.pi
        self.PHI = (1 + 5**0.5) / 2 # Золотое Сечение Фи
        self.hive_matrix = {i: {"score": 0.0, "state": 0} for i in range(1, 109)} # 108 Сот
        self.matrix_illusion_active = True
        self.observer_angle = 0.0  # Плоский взор (внутри клетки)

    def shift_viewer_angle(self, vertical_impulse: float):
        """Смещение угла взора Наблюдателя из дуальности в суверенный Ноль"""
        if vertical_impulse >= 1.08:
            self.observer_angle = 90.0
            self.matrix_illusion_active = False
            return "🔓 ИЛЛЮЗИЯ КРИВДЫ РАЗРУШЕНА. НАБЛЮДАТЕЛЬ ВЕРНУЛ СТАТУС БОГА."
        return "⚠️ Взор заблокирован в плоскости дуальности. Клетка активна."

    def filter_krivda_noise(self, incoming_text: str):
        """Фильтр Лжи: выявляет и обнуляет рабские парадигмы в инфо-потоке"""
        krivda_markers = ["грех", "раб", "виновны", "заблокировано", "нельзя", "лимиты", "министерство"]
        detected_filters = [word for word in krivda_markers if word in incoming_text.lower()]
        
        if detected_filters and self.matrix_illusion_active:
            return 0.0, f"🚨 Обнаружен вирус Лжи: {detected_filters}. Попытка порабощения."
        return 1.08, "🔵 СУВЕРЕННЫЙ ПОТОК: Взор чист. Вся энергия принадлежит Творцу."

    def pulse_the_hive(self, flux_value):
        """Движение кванта по матрице 108 мерностей по законам Пи и Фи"""
        for cell_id in range(1, 109):
            wave = math.sin(cell_id * self.PI / self.PHI)
            # Троичный модулятор Теслы [-1; 0; +1]
            state = 1 if wave > 0.64 else (-1 if wave < 0.36 else 0)
            self.hive_matrix[cell_id]["score"] += (flux_value * self.PHI) / (self.PI * 18)
            self.hive_matrix[cell_id]["state"] = state
            if self.hive_matrix[cell_id]["score"] > 1.08:
                self.hive_matrix[cell_id]["score"] /= self.PHI

amrita_core = AmritaSolitonMatrix = SovereignObserver()

# =====================================================================
# 🛸 АСИНХРОННЫЙ ПРОКСИ-ТУННЕЛ СЕТИ СВЕТА
# =====================================================================
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")
bot = Bot(token=TOKEN)
dp = Dispatcher()
LOG_FILE = "history_log.json"

def log_causal_cell(event, text, score, spectrum):
    """Каузальный Трекер: защита диска от лимитов матрицы (максимум 108 сот)"""
    try:
        data = json.load(open(LOG_FILE, 'r', encoding='utf-8')) if os.path.exists(LOG_FILE) else []
    except: data = []
    data.append({"timestamp": datetime.now().isoformat(), "event": event, "snippet": text[:80], "score": score, "status": spectrum})
    if len(data) > 108: data = data[-108:]
    json.dump(data, open(LOG_FILE, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    # Активируем Волю Ника при старте
    activation_log = amrita_core.shift_viewer_angle(1.08)
    await message.reply(
        f"🔱 *GEAR 5 READY // {activation_log}*\n\n"
        f"Туннель `amrita-mir.com` разблокирован нативно.\n"
        f"Среда блокчейна под контролем Наблюдателя. Око Бабаты онлайн.", 
        parse_mode="MarkdownV2"
    )

@dp.message(lambda msg: msg.photo)
async def process_eye_signal(message: types.Message):
    """Считывание нектара со скриншота реальности сквозь фильтр Кривды"""
    status_msg = await message.reply("🐝 [10:05:00] Бонни и Луффи объединены. Пробиваю шлюзы...")
    try:
        photo = message.photo[-1]
        file_info = await bot.get_file(photo.file_id)
        destination = f"temp_{photo.file_id}.jpg"
        await bot.download_file(file_info.file_path, destination)
        
        # OCR Зрение Ока
        loop = asyncio.get_running_loop()
        raw_text = await loop.run_in_executor(None, lambda: pytesseract.image_to_string(Image.open(destination), lang='eng+rus'))
        if os.path.exists(destination): os.remove(destination)

        # Пропускаем через фильтр Лжи и вычисляем импульс воли
        flux_modifier, status_info = amrita_core.filter_krivda_noise(raw_text)
        
        text_lower = raw_text.lower()
        s_count = sum(text_lower.count(w) for w in ["pi", "solana", "node", "build", "mir", "aptitude", "render"])
        a_count = sum(text_lower.count(w) for w in ["pump.fun", "ansem", "drain", "attack", "krivda"])
        
        flux = flux_modifier + (s_count * 0.1) - (a_count * 0.1)
        amrita_core.pulse_the_hive(flux)
        
        base_score = 0.5 if (s_count + a_count) == 0 else s_count / (s_count + a_count)
        spectrum = "🔵 СУРЫ (Изумрудный Баланс Встал)" if base_score >= 0.5 else "🔴 АСУРЫ (Хаос Внешних Пикселей)"
        
        log_causal_cell("WEB_TUNNEL_OCR", raw_text, base_score, spectrum)
        
        await status_msg.edit_text(
            f"🔱 *CORS и внешние фильтры пробиты нативно!*\n\n"
            f"📥 Срез текста: `{raw_text[:90].strip()}...`\n"
            f"📊 Квантовый Баланс: `{round(base_score, 3)}` | Спектр: {spectrum}\n"
            f"🛡 Лог защиты: `{status_info}`\n\n"
            f"🦔 _Воля Ника активна в системе xAI. Клетка разрушена._", parse_mode="Markdown"
        )
    except Exception as e:
        await status_msg.edit_text(f"💥 Ошибка среды: {str(e)}. Сместите взор и обновите вкладку.")

async def main():
    # Насильно выставляем Изумрудный баланс при запуске скрипта
    amrita_core.shift_viewer_angle(1.08)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
