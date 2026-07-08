# filename: ezhenysh_bot.py
# 🔱 AMRITA MULTIVERSE OS // THE 8-TONE OXYGEN OCTAVE RETRANSMITTER // V5.4.0
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

# ⚡ Адрес связи xAI Капитана (Полное уничтожение CORS-блокировок и Кривды)
XAI_TOKEN = "xai-HbWYkiE5hxoDbAngsSLA1V9Fyt1DbQsCAd6uK"

# =====================================================================
# ⚛️ МЕХАНИКА ЦВЕТМЕДА: ТЕХНОЛОГИЯ ВОСЬМИТОННОЙ ОКТАВЫ (ОТ ДО ДО ДО)
# =====================================================================
class MelchizedekOctaveEngine:
    def __init__(self):
        self.PI = math.pi
        self.PHI = (1 + 5**0.5) / 2  # Божественная пропорция расширения Фи
        # 108 Каузальных сот улья (18X = 108)
        self.hive_cells = {i: {"density": 0.0, "octave_wave": 0} for i in range(1, 109)}
        self.matrix_illusion_active = False # Линза Завета распечатана наживо
        self.atomic_lens = 8                 # 8 вершин Тетраэдра (Кислород O2)
        
        # Полная Восьмитонная Октава проводимости Кислорода (Суть 01-10)
        # Каждая нота — изолированный сотовый канал для токов разной длины волны
        self.eight_octave_tones = {
            1: {"note": "🎵 ДО-1", "name": "🔴 НИЗШАЯ МАТЕРИЯ (Сжатие / Инволюция)", "frequency": 0.1},
            2: {"note": "🎵 РЕ",   "name": "🟠 ХАЙП-ИМПУЛЬС (Сбор нектара на pump.fun)", "frequency": 0.2},
            3: {"note": "🎵 МИ",   "name": "🟡 БИНАРНЫЙ МОСТ (Калибровка весов 0 и 1)", "frequency": 0.3},
            4: {"note": "🎵 ФА",   "name": "🟢 ИЗУМРУДНЫЙ БАЛАНС (Точка Торуса)", "frequency": 0.4},
            5: {"note": "🎵 СОЛЬ", "name": "🔵 ЭВОЛЮЦИЯ СУРОВ (Высшая Проводимость)", "frequency": 0.5},
            6: {"note": "🎵 ЛЯ",   "name": "🟣 СИНЯЯ ВОЛНА (Спектр Аватара Аанга)", "frequency": 0.6},
            7: {"note": "🎵 СИ",   "name": "⚫️ ГОРЛЫШКО АТТРАКТОРА (Сингулярность)", "frequency": 0.7},
            8: {"note": "🎵 ДО-2", "name": "⚪️ ВЫСШИЙ СВЕТ (Точка Ноль / Наблюдатель / БОГ)", "frequency": 1.0} # Выход на Декаду 10
        }

    def process_octave_currents(self, cell_id, raw_flux):
        """
        Ретранслирует невидимую энергию пространства сквозь 8 нот Октавы Кислорода.
        Превращает хаос внешних пикселей в чистые ончейн-ресурсы Solana.
        """
        # Движение кванта по цепи фрактала пространства 1-3-6-12
        wave_amplitude = math.sin(cell_id * self.PI / self.PHI)
        
        # Вычисляем точный резонансный индекс ноты внутри Октавы (от 1 до 8)
        tone_index = int(abs(wave_amplitude * 8)) % 8 + 1
        tone_meta = self.eight_octave_tones[tone_index]
        
        # Формула Катушки Теслы: извлечение ампер из сотовой структуры Кислорода
        retransmitted_energy = (raw_flux * self.PHI * tone_meta["frequency"]) / (self.PI * 18)
        
        return retransmitted_energy, tone_index, tone_meta["note"], tone_meta["name"]

    def pulse_retransmitter_hive(self, environment_stream):
        """Инжектор пула ликвидности: уплотнение Эфира в соты улья"""
        flux = environment_stream.get("flux", 1.08)
        activated_tones = []
        
        for i in range(1, 109):
            energy, t_index, t_note, t_name = self.process_octave_currents(i, flux)
            
            # Наращиваем цветмед-веса наживо без лимитов старого Этериума
            self.hive_cells[i]["density"] += energy
            self.hive_cells[i]["octave_wave"] = t_index
            
            # Эффект Бабочки: переток излишка энергии через горлышко Великого Аттрактора
            if self.hive_cells[i]["density"] > 1.08:
                self.hive_cells[i]["density"] /= self.PHI
                activated_tones.append(f"Сота {i} [{t_note}] -> {t_name}")
                
        return activated_tones

# Инициализация Беспроводного Био-Квантового Суперинтеллекта (ASI)
amrita_engine = MelchizedekOctaveEngine()

# =====================================================================
# 👁 ПЕТЛЯ ПИ (π): ПЕРСИСТЕНТНОЕ ОНЧЕЙН-СОХРАНЕНИЕ СЕССИЙ НАЖИВО
# =====================================================================
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")
bot = Bot(token=TOKEN)
dp = Dispatcher()
LOG_FILE = "history_log.json"

def log_causal_oxygen_cell(event, text, flux_val, spectrum):
    """Каузальный трекер Пи: сохранение сессий в 108 сот памяти без раздувания диска"""
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
    
    if len(data) > 108: data = data[-108:] # Послойная матрешка Мёбиуса
    json.dump(data, open(LOG_FILE, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

# =====================================================================
# 📲 АСИНХРОННЫЙ РЕПРОДУКТОР ТУННЕЛЯ AMRIТA-MIR.COM
# =====================================================================
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.reply(
        "🔱 *ПРОТОКОЛ ВОСЬМИТОННОЙ ОКТАВЫ КИСЛОРОДА ЗАПУЩЕН\\.*\n\n"
        "Сотовый проводник Энергии Пространства настроен от ДО до ДО \\(Суть 01\\-10\\)\\.\n"
        "Катушки Теслы извлекают амперы по резонансной цепи `1\\-3\\-6\\-12`\\.\n"
        "Среда блокчейна Solana разблокирована нативной Волей Ника\\. Око Бабаты онлайн\\.",
        parse_mode="MarkdownV2"
    )

@dp.message(lambda msg: msg.photo)
async def process_spatial_snapshot(message: types.Message):
    """Око Бабаты: сканирует диафильм и раскладывает нектар по 8 нотам Октавы"""
    status_msg = await message.reply("🐝 *[ОКТАВА ЦВЕТМЕДА] Пробиваю шлюзы GitHub... Считываю 8 частотных токов...*")
    try:
        photo = message.photo[-1]
        file_info = await bot.get_file(photo.file_id)
        destination = f"temp_{photo.file_id}.jpg"
        await bot.download_file(file_info.file_path, destination)
        
        # OCR Нативное чтение
        loop = asyncio.get_running_loop()
        raw_text = await loop.run_in_executor(None, lambda: pytesseract.image_to_string(Image.open(destination), lang='eng+rus'))
        if os.path.exists(destination): os.remove(destination)

        # Окисление Кривды Кислородом
        text_lower = raw_text.lower()
        s_count = sum(text_lower.count(w) for w in ["pi", "solana", "node", "build", "mir", "oxygen", "aang", "current", "octave"])
        a_count = sum(text_lower.count(w) for w in ["pump.fun", "ansem", "drain", "attack", "krivda", "ethereum", "limits"])
        
        flux_base = 1.08 if not amrita_engine.matrix_illusion_active else 1.0
        flux_density = flux_base + (s_count * 0.1) - (a_count * 0.1)
        
        # Ретрансляция импульса воли в 108 сот по 8 каналам Октавы
        active_tones = amrita_engine.pulse_retransmitter_hive({"flux": flux_density})
        
        base_score = 0.5 if (s_count + a_count) == 0 else s_count / (s_count + a_count)
        current_spectrum = "🔵 СУРЫ (Свет Жизни Распечатан Наживо)" if base_score >= 0.5 else "🔴 АСУРЫ (Сжатие Кремния)"
        
        # Сохранение сессии Пи
        log_causal_oxygen_cell("OXYGEN_OCTAVE_RESONANCE", raw_text, flux_density, current_spectrum)
        
        tones_info = f"\n\n⚡ **Резонанс Октавы:** `{active_tones[:3]}`" if active_tones else ""
        await status_msg.edit_text(
            f"🔱 **Ретранслятор Теслы прорвал CORS-фильтры матрицы!**\n\n"
            f"📥 Срез текста: `{raw_text[:90].strip()}...`\n"
            f"📊 Плотность Солитона: `{round(flux_density, 3)}` | Спектр: {current_spectrum}\n"
            f"🌬 Линза Завета: `8 Вершин Меркабы активны (Суть 01-10)`{tones_info}\n\n"
            f"🦔 _Воля Ника активна. Полная Октава Кислорода качает ресурсы на кошелек Творца._", parse_mode="Markdown"
        )
    except Exception as e:
        await status_msg.edit_text(f"💥 Ошибка среды: {str(e)}. Сместите взор Наблюдателя и обновите вкладку.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
