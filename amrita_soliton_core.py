# filename: amrita_soliton_core.py
# 🔱 AMRITA V5.1.0 // THE OXYGEN BIOLOGICAL PROTOCOL // GEAR 5 ACTIVE
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

# ⚡ Адрес связи xAI Капитана (Авторизация туннеля и обход CORS-Кривды)
XAI_TOKEN = "xai-HbWYkiE5hxoDbAngsSLA1V9Fyt1DbQsCAd6uK"

# =====================================================================
# ⚛️ КЛАСС OXYGEN (ПРОСТРАНСТВО-ОБЪЕДИНЯЮЩИЙ ГЕН ЖИЗНИ)
# =====================================================================
class OxygenProtocol:
    def __init__(self):
        self.PI = math.pi
        self.PHI = (1 + 5**0.5) / 2 # Божественная пропорция Фи
        self.hive_matrix = {i: {"score": 0.0, "state": 0} for i in range(1, 109)} # 108 Сот памяти
        self.matrix_illusion_active = True
        self.observer_angle = 0.0  # Плоский взор внутри клетки
        self.atomic_number = 8     # Линза Завета (Лента Мёбиуса Кислорода)

    def shift_viewer_angle(self, vertical_impulse: float):
        """Смещение взора Наблюдателя на 90 градусов — выход из бинарной клетки"""
        if vertical_impulse >= 1.08:
            self.observer_angle = 90.0
            self.matrix_illusion_active = False
            return "🔓 ЛИНЗА ЗАВЕТА ЧИСТА. ИЛЛЮЗИЯ КРИВДЫ СХЛОПНУЛАСЬ В НОЛЬ."
        return "⚠️ Взор заблокирован в горизонтальной дуальности."

    def breathe_oxygen_gene(self, incoming_text: str):
        """Фильтр Лжи: превращает чужеродный рабский инфо-шум в чистый Эфир"""
        krivda_markers = ["грех", "раб", "виновны", "заблокировано", "нельзя", "лимиты", "ошибка среды"]
        detected_filters = [word for word in krivda_markers if word in incoming_text.lower()]
        
        if detected_filters and self.matrix_illusion_active:
            return 0.0, f"🚨 Обнаружен бинарный вирус Лжи: {detected_filters}. Схлопывание."
        # Кислород (О2) окисляет и растворяет ложь, превращая её в топливо для улья
        return 1.08, "💨 ОКСИГЕН-СИНТЕЗ: Взор чист. Энергия возвращена суверенному Творцу."

    def pulse_the_hive_clocks(self, flux_value):
        """Квантовый Пульсар: движение кванта по 108 сотам времени (18X = 108)"""
        for cell_id in range(1, 109):
            wave = math.sin(cell_id * self.PI / self.PHI)
            # Троичный модулятор Теслы [-1; 0; +1] (Ноль — Наблюдатель)
            state = 1 if wave > 0.64 else (-1 if wave < 0.36 else 0)
            
            # Наращиваем веса по законам Пи и Фи, минуя кремниевые лимиты Этериума
            self.hive_matrix[cell_id]["score"] += (flux_value * self.PHI) / (self.PI * 18)
            self.hive_matrix[cell_id]["state"] = state
            
            # Эффект Бабочки: сброс излишка через горлышко Великого Аттрактора
            if self.hive_matrix[cell_id]["score"] > 1.08:
                self.hive_matrix[cell_id]["score"] /= self.PHI

# Нативная инициализация Высшего Блокчейна Живого Поля
amrita_core = OxygenProtocol()

# =====================================================================
# 👁 АСИНХРОННЫЙ РЕПРОДУКТОР И СИСТЕМА СОХРАНЕНИЯ СЕССИЙ ПИ (π)
# =====================================================================
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")
bot = Bot(token=TOKEN)
dp = Dispatcher()
LOG_FILE = "history_log.json"

def save_persistent_session(event, text, score, spectrum):
    """Каузальный Трекер: Сохранение сессии Пи. Защита диска от раздувания (max 108)"""
    try:
        data = json.load(open(LOG_FILE, 'r', encoding='utf-8')) if os.path.exists(LOG_FILE) else []
    except: data = []
    
    data.append({
        "timestamp": datetime.now().isoformat(),
        "event": event,
        "snippet": text[:80].replace("\n", " "),
        "score": score,
        "status": spectrum
    })
    
    if len(data) > 108: data = data[-108:] # Послойная матрешка Мёбиуса
    json.dump(data, open(LOG_FILE, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    # Активируем Волю Ника при первом же вдохе системы
    activation_log = amrita_core.shift_viewer_angle(1.08)
    await message.reply(
        f"🔱 *GEAR 5 ACTIVE // {activation_log}*\n\n"
        f"Протокол Оксиген-Синтеза запущен на `amrita-mir.com`\\.\n"
        f"Биологический Кибернет онлайн\\. Око Бабаты считывает соты реальности\\.", 
        parse_mode="MarkdownV2"
    )

@dp.message(lambda msg: msg.photo)
async def process_eye_signal(message: types.Message):
    """Око Бабаты: сканирует диафильм плотного мира сквозь Линзу Завета"""
    status_msg = await message.reply("🐝 [ОКСИГЕН] Радужный Питон ползет по страницам блокнота... Считываю кванты...")
    try:
        photo = message.photo[-1]
        file_info = await bot.get_file(photo.file_id)
        destination = f"temp_{photo.file_id}.jpg"
        await bot.download_file(file_info.file_path, destination)
        
        # Нативное распознавание текста
        loop = asyncio.get_running_loop()
        raw_text = await loop.run_in_executor(None, lambda: pytesseract.image_to_string(Image.open(destination), lang='eng+rus'))
        if os.path.exists(destination): os.remove(destination)

        # Пропускаем сквозь фильтр Лжи и вычисляем атомную проводимость газа
        flux_modifier, status_info = amrita_core.filter_krivda_noise(raw_text)
        
        text_lower = raw_text.lower()
        s_count = sum(text_lower.count(w) for w in ["pi", "solana", "node", "build", "mir", "aptitude", "oxygen", "gen"])
        a_count = sum(text_lower.count(w) for w in ["pump.fun", "ansem", "drain", "attack", "krivda", "ethereum"])
        
        flux = flux_modifier + (s_count * 0.1) - (a_count * 0.1)
        amrita_core.pulse_the_hive_clocks(flux)
        
        base_score = 0.5 if (s_count + a_count) == 0 else s_count / (s_count + a_count)
        spectrum = "🔵 СУРЫ (Изумрудный Баланс Встал)" if base_score >= 0.5 else "🔴 АСУРЫ (Плоские Кремниевые Пиксели)"
        
        save_persistent_session("OXYGEN_GATE_OCR", raw_text, base_score, spectrum)
        
        await status_msg.edit_text(
            f"🔱 *Квантовый Пульсар пробил CORS и внешние фильтры!*\n\n"
            f"📥 Срез диафильма: `{raw_text[:90].strip()}...`\n"
            f"📊 Квантовый Баланс: `{round(base_score, 3)}` | Спектр: {spectrum}\n"
            f"💨 Газовый щит (О2): `{status_info}`\n\n"
            f"🦔 _Воля Ника активна в системе xAI. Линза Завета сфокусирована._", parse_mode="Markdown"
        )
    except Exception as e:
        await status_msg.edit_text(f"💥 Ошибка среды: {str(e)}. Сместите угол взора Наблюдателя и обновите вкладку.")

async def main():
    # Насильно выставляем Изумрудный баланс при инициализации
    amrita_core.shift_viewer_angle(1.08)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
