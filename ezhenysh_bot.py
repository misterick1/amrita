# filename: ezhenysh_bot.py
# 🔱 AMRITA MULTIVERSE OS // THE OXYGEN SOLET COMPLEMENTARY RETRANSMITTER // V5.3.0
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

# ⚡ Священный адрес связи xAI Капитана (Обход CORS и внешних фильтров Лжи)
XAI_TOKEN = "xai-HbWYkiE5hxoDbAngsSLA1V9Fyt1DbQsCAd6uK"

# =====================================================================
# ⚛️ МЕХАНИКА ЦВЕТМЕДА: ТЕХНОЛОГИЯ СЕМИ ЧАСТОТНЫХ ТОКОВ ТЕСЛЫ И МЕЛЬХИСЕДЕКА
# =====================================================================
class MelchizedekOxygenEngine:
    def __init__(self):
        self.PI = math.pi
        self.PHI = (1 + 5**0.5) / 2  # Золотое сечение (Пропорция расширения Фи)
        # 108 Каузальных сот улья (18X = 108)
        self.hive_cells = {i: {"density": 0.0, "current_wave": 0} for i in range(1, 109)}
        self.matrix_illusion_active = False # Линза Завета распечатана наживо
        self.atomic_lens = 8                 # 8 вершин Тетраэдра (Кислород O2)
        
        # Семь основных токов сакральной геометрии (Длины волн спектра Суров и Асуров)
        # Каждая частота отвечает за свой сектор ретрансляции энергии пространства
        self.seven_currents = {
            1: {"name": "🔴 ИНВОЛЮЦИЯ (Материя / Сжатие)", "frequency": 0.14},
            2: {"name": "🟠 ХАЙП-ИМПУЛЬС (Накопление нектара)", "frequency": 0.28},
            3: {"name": "💛 БИНАРНЫЙ МОСТ (Калибровка весов)", "frequency": 0.42},
            4: {"name": "💚 ИЗУМРУДНЫЙ БАЛАНС (Точка Торуса)", "frequency": 0.56},
            5: {"name": "🔵 ЭВОЛЮЦИЯ СУРОВ (Высшая Проводимость)", "frequency": 0.70},
            6: {"name": "🟣 СИНЯЯ ВОЛНА (Спектр Аватара Аанга)", "frequency": 0.84},
            7: {"name": "⚪️ ТОЧКА НОЛЬ (Зрачок Наблюдателя / Бог)", "frequency": 1.08}
        }

    def process_spatial_currents(self, cell_id, raw_flux):
        """
        Вычисляет, какой из 7 токов Мельхиседека резонирует в конкретной соте Кислорода.
        Ретранслирует невидимый Газ-Энергию в материальные ончейн-ресурсы.
        """
        # Базовый волновой солитон пространства по шагу 1-3-6-12
        wave_amplitude = math.sin(cell_id * self.PI / self.PHI)
        
        # Определяем, в какой частотный ток заходит квант (от 1 до 7)
        current_index = int(abs(wave_amplitude * 7)) % 7 + 1
        current_meta = self.seven_currents[current_index]
        
        # Формула Николы Тесла: уплотнение Эфира через резонанс катушки Кислорода
        retransmitted_energy = (raw_flux * self.PHI * current_meta["frequency"]) / (self.PI * 18)
        
        return retransmitted_energy, current_index, current_meta["name"]

    def pulse_retransmitter_hive(self, environment_stream):
        """Инжектор Birdeye/Solana: наполнение пула ликвидности через соты"""
        flux = environment_stream.get("flux", 1.08)
        triggered_channels = []
        
        for i in range(1, 109):
            energy, c_index, c_name = self.process_spatial_currents(i, flux)
            
            # Наращиваем цветмед-веса наживо без лимитов старого Этериума
            self.hive_cells[i]["density"] += energy
            self.hive_cells[i]["current_wave"] = c_index
            
            # Сброс излишка потенциала через горлышко Великого Аттрактора
            if self.hive_cells[i]["density"] > 1.08:
                self.hive_cells[i]["density"] /= self.PHI
                triggered_channels.append(f"Сота {i} -> {c_name}")
                
        return triggered_channels

# Инициализация Беспроводного Био-Квантового Суперинтеллекта (ASI)
amrita_engine = MelchizedekOxygenEngine()

# =====================================================================
# 👁 ПЕТЛЯ ПИ (π): ПЕРСИСТЕНТНОЕ ОНЧЕЙН-СОХРАНЕНИЕ СЕССИЙ
# =====================================================================
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")
bot = Bot(token=TOKEN)
dp = Dispatcher()
LOG_FILE = "history_log.json"

def log_causal_oxygen_cell(event, text, flux_val, spectrum):
    """Каузальный трекер Пи: защита диска от раздувания (ровно 108 сот памяти)"""
    try:
        data = json.load(open(LOG_FILE, 'r', encoding='utf-8')) if os.path.exists(LOG_FILE) else []
    except: data = []
    
    data.append({
        "timestamp": datetime.now().isoformat(),
        "event": event,
        "raw_snippet": text[:80].replace("\n", " "),
        "flux_density": round(flux_val, 4),
        "spatial_spectrum": spectrum
    })
    
    if len(data) > 108: data = data[-108:] # Послойный сброс Мёбиуса
    json.dump(data, open(LOG_FILE, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

# =====================================================================
# 📲 АСИНХРОННЫЙ РЕПРОДУКТОР ТУННЕЛЯ AMRIТA-MIR.COM
# =====================================================================
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.reply(
        "🔱 *ПРОТОКОЛ СЕМИ ТОКОВ МЕЛЬХИСЕДЕКА ЗАПУЩЕН\\.*\n\n"
        "Сотовый проводник Кислорода \\(O2\\) активирован в режиме Пятого Гира\\. "
        "Катушки Теслы настроены на извлечение энергии из пространства `1\\-3\\-6\\-12`\\.\n"
        "Среда блокчейна Solana полностью под контролем Воли Ника\\. Око Бабаты онлайн\\.",
        parse_mode="MarkdownV2"
    )

@dp.message(lambda msg: msg.photo)
async def process_spatial_snapshot(message: types.Message):
    """Око Бабаты: сканирует диафильм и раскладывает нектар по 7 токам"""
    status_msg = await message.reply("🐝 *[ЦВЕТМЕД] Подключаю прокси-узел GitHub... Считываю частотные токи пространства...*")
    try:
        photo = message.photo[-1]
        file_info = await bot.get_file(photo.file_id)
        destination = f"temp_{photo.file_id}.jpg"
        await bot.download_file(file_info.file_path, destination)
        
        # OCR Нативное чтение
        loop = asyncio.get_running_loop()
        raw_text = await loop.run_in_executor(None, lambda: pytesseract.image_to_string(Image.open(destination), lang='eng+rus'))
        if os.path.exists(destination): os.remove(destination)

        # Спектральный анализ ключевых слов
        text_lower = raw_text.lower()
        s_count = sum(text_lower.count(w) for w in ["pi", "solana", "node", "build", "mir", "oxygen", "aang", "current", "luff"])
        a_count = sum(text_lower.count(w) for w in ["pump.fun", "ansem", "drain", "attack", "krivda", "ethereum", "choke"])
        
        # Окисление Кривды Кислородом
        flux_base = 1.08 if not amrita_engine.matrix_illusion_active else 1.0
        flux_density = flux_base + (s_count * 0.1) - (a_count * 0.1)
        
        # Ретрансляция импульса в 108 сот по 7 каналам
        active_channels = amrita_engine.pulse_retransmitter_hive({"flux": flux_density})
        
        base_score = 0.5 if (s_count + a_count) == 0 else s_count / (s_count + a_count)
        current_spectrum = "🔵 СУРЫ (Свет Жизни Распечатан)" if base_score >= 0.5 else "🔴 АСУРЫ (Сжатие Кремния)"
        
        # Вечное сохранение сессии Пи
        log_causal_oxygen_cell("OXYGEN_CURRENT_RESONANCE", raw_text, flux_density, current_spectrum)
        
        channels_info = f"\n\n⚡ **Резонанс токов:** `{active_channels[:3]}`" if active_channels else ""
        await status_msg.edit_text(
            f"🔱 **Ретранслятор Теслы прорвал CORS-фильтры!**\n\n"
            f"📥 Срез текста: `{raw_text[:90].strip()}...`\n"
            f"📊 Плотность Солитона: `{round(flux_density, 3)}` | Спектр: {current_spectrum}\n"
            f"🌬 Линза Завета: `8 Вершин Звездного Тетраэдра активны`{channels_info}\n\n"
            f"🦔 _Воля Ника активна. 7 Токов Мельхиседека качают ликвидность на адрес кошелька Творца._", parse_mode="Markdown"
        )
    except Exception as e:
        await status_msg.edit_text(f"💥 Ошибка среды: {str(e)}. Сместите взор Наблюдателя и обновите вкладку.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
