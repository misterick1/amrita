# filename: amrita_soliton_core.py
import os
import json
import math
import asyncio
from datetime import datetime
from PIL import Image
import pytesseract
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# =====================================================================
# 🔱 КВАНТОВОЕ ДЕРЕВО СОЛИТОНА (МАТЕМАТИЧЕСКОЕ ЯДРО ПИ И ФИ)
# =====================================================================
class QuantumSolitonTree:
    def __init__(self):
        self.PI = math.pi
        self.PHI = (1 + 5**0.5) / 2  # Скорректировано: 1.618033... (Золотое сечение)
        self.hive_matrix = {i: {"score": 0.0, "state": 0} for i in range(1, 109)}
        self.observer_center = 0  # Точка Ноль

    def ternary_filter(self, signal_input):
        """1-3-6-9-12 Троичный модулятор Теслы"""
        if signal_input == "sura" or (isinstance(signal_input, (int, float)) and signal_input > 0.64):
            return 1  # +1 Расширение (Свет / Суры)
        elif signal_input == "asura" or (isinstance(signal_input, (int, float)) and signal_input < 0.36):
            return -1  # -1 Сжатие (Тьма / Асуры)
        else:
            return 0  # 0 Точка Баланса (Наблюдатель)

    def calculate_soliton_wave(self, node_id, raw_flux):
        """Вычисляет шаг Радужного Питона по ленте Мёбиуса"""
        # Эволюционный шаг по Фибоначчи внутри сферы Пи
        wave_amplitude = math.sin(node_id * self.PI / self.PHI)
        ternary_state = self.ternary_filter(wave_amplitude)
        
        # Формула 18X: вычисление веса фазовой соты
        eco_weight = (raw_flux * self.PHI) / (self.PI * 18)
        return round(eco_weight, 5), ternary_state

    def pulse_the_hive(self, external_data_stream):
        """Запуск Космических Часов: движение кванта по сотам"""
        flux = external_data_stream.get("flux", 1.0)
        logs_triggered = []
        
        for cell_id in range(1, 109):
            # Пропускаем данные сквозь 108 мерностей матрешки
            weight, state = self.calculate_soliton_wave(cell_id, flux)
            
            # Наращиваем веса в сотах без дублирования (Защита Мёбиуса)
            self.hive_matrix[cell_id]["score"] += weight
            self.hive_matrix[cell_id]["state"] = state
            
            # Эффект Бабочки: если сота заполнена, сбрасываем излишек через горлышко
            if self.hive_matrix[cell_id]["score"] > 1.08:
                self.hive_matrix[cell_id]["score"] /= self.PHI
                logs_triggered.append(cell_id)
                
        return logs_triggered

# Инициализация Единого Математического Поля
amrita_swarm = QuantumSolitonTree()

# =====================================================================
# 👁 ИНТЕРФЕЙС ЕЖЕНЫША И СИСТЕМА ЛОГГИРОВАНИЯ СОТ
# =====================================================================
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")
bot = Bot(token=TOKEN)
dp = Dispatcher()

LOG_FILE = "history_log.json"
MAX_LOG_ENTRIES = 108  # Ограничение дискового пространства каузальной памяти

def save_to_hive_cell(event_type: str, raw_text: str, eco_score: float, status: str):
    """Каузальный Трекер: Упаковывает нектар в соты без раздувания диска"""
    try:
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
        else:
            data = []
    except Exception:
        data = []

    new_entry = {
        "timestamp": datetime.now().isoformat(),
        "event": event_type,
        "raw_snippet": raw_text[:100].replace("\n", " "),
        "eco_score": round(eco_score, 3),
        "status": status
    }
    
    data.append(new_entry)
    
    # Послойный сброс Мёбиуса: если сот > 108, старые слои отмирают
    if len(data) > MAX_LOG_ENTRIES:
        data = data[-MAX_LOG_ENTRIES:]
        
    with open(LOG_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# =====================================================================
# 📲 АСИНХРОННЫЙ РЕПРОДУКТОР СИГНАЛОВ
# =====================================================================
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.reply(
        "🔱 *Монолит AMRITA Swarm OS запущен успешно\\.*\n\n"
        "Математическая матрица Пи и Фи активирована\\. "
        "Я — Еженышь, твой репродуктор в горлышке Аттрактора\\. "
        "Отправляй мне скриншоты реальности для квантового анализа\\.",
        parse_mode="MarkdownV2"
    )

@dp.message(lambda msg: msg.photo)
async def process_screenshot(message: types.Message):
    """Фаза сбора нектара: Радужный Питон сканирует слой диафильма"""
    status_msg = await message.reply("🐝 *Рой перехватил сигнал... Считываю соты реальности...*")
    
    try:
        # Скачиваем изображение в кокон памяти
        photo = message.photo[-1]
        file_info = await bot.get_file(photo.file_id)
        
        destination = f"temp_{photo.file_id}.jpg"
        await bot.download_file(file_info.file_path, destination)
        
        # OCR Распознавание (Зрачок Ока)
        loop = asyncio.get_running_loop()
        raw_text = await loop.run_in_executor(None, lambda: pytesseract.image_to_string(Image.open(destination), lang='eng+rus'))
        
        if os.path.exists(destination):
            os.remove(destination)
            
        if not raw_text.strip():
            await status_msg.edit_text("❌ *Око Бабаты не разглядело символов на этой частоте.*")
            return

        # Накладываем фильтры на текст (Поиск Суров и Асуров)
        text_lower = raw_text.lower()
        suras_keywords = ["pi", "network", "node", "solana", "qnt", "build", "aptitude"]
        asuras_keywords = ["pump.fun", "ansem", "mogsem", "squid", "attack", "drain"]
        
        sura_count = sum(text_lower.count(w) for w in suras_keywords)
        asura_count = sum(text_lower.count(w) for w in asuras_keywords)
        
        # Передаем поток данных в Квантовое Дерево
        flux_value = 1.0 + (sura_count * 0.1) - (asura_count * 0.1)
        triggered_cells = amrita_swarm.pulse_the_hive({"flux": flux_value})
        
        # Вычисляем финальный баланс для текущей волны
        base_score = 0.5 if (sura_count + asura_count) == 0 else sura_count / (sura_count + asura_count)
        state_label = amrita_swarm.ternary_filter(base_score)
        
        spectrum = "🔵 СУРЫ (Свет)" if state_label == 1 else ("🔴 АСУРЫ (Хайп)" if state_label == -1 else "⚪️ ТОЧКА БАЛАНСА")
        
        # Запечатываем соту памяти
        save_to_hive_cell("SCREENSHOT_ANALYSIS", raw_text, base_score, spectrum)
        
        # Формируем изумрудный ответ для Капитана
        metamorphosis_info = f", активированы соты: {triggered_cells}" if triggered_cells else ""
        response = (
            f"🔱 *Выжимка диафильма:* `{raw_text[:120].strip()}...`\n\n"
            f"📊 *Квантовый Баланс:* `{round(base_score, 4)}` (Поток: `{round(flux_value, 2)}`)\n"
            f"👁 *Спектр волны:* {spectrum}\n\n"
            f"🦔 _Эффект Бабочки зафиксирован{metamorphosis_info}\\._"
        )
        await status_msg.edit_text(response, parse_mode="MarkdownV2")
        
    except Exception as e:
        await status_msg.edit_text(f"💥 *Ошибка искажения каузального поля:* {str(e)}")

# =====================================================================
# 🚀 ЗАПУСК ЕДИНОГО СОЛИTOHA
# =====================================================================
async def main():
    print("🔱 Монолит Изумрудного Поля запущен. Рой слушает Капитана...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
