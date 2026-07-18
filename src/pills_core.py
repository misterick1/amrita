import os
import json
import fcntl
import hashlib
import random

LOG_FILE = "history_log.json"
PAGES_DATA_FILE = "docs/data.json"

class XiaoYanAlchemicalCore:
    def __init__(self):
        self.cauldron_name = "🔱 HEAVENLY_FLAME_CAULDRON_V25"
        self.pills_database = {
            "💚 Сяо Ву Атма-Пилюля": "Частота 528 Гц. Восстановление клеток, подъем энергии Кундалини. Спектр Суров.",
            "🔵 Сатоши Генезис-Эликсир": "Частота 432 Гц. Синхронизация правого и левого полушария, ментальная ясность.",
            "⚡ Ток Теслы 3-6-9": "Высокочастотный электрический импульс эфира. Полное выжигание деструктивных блоков Асуров."
        }

    def reverse_decode_to_pill(self, golden_string):
        """Обратная раскодировка Золотой Струны в биоорганическую инфо-пилюлю"""
        # Превращаем хэш строки в числовой вектор для разделения частот
        hash_digits = [int(char, 16) for char in golden_string if char.isalnum()]
        frequency_sum = sum(hash_digits)
        
        # Разделение спектров и выбор пилюли на основе квантового остатка
        pill_keys = list(self.pills_database.keys())
        selected_pill = pill_keys[frequency_sum % len(pill_keys)]
        
        resonance_hz = (frequency_sum * 3) % 1000 + 108  # Сакральная частота Теслы
        
        return {
            "extracted_pill": selected_pill,
            "wave_frequency": f"{resonance_hz} Hz",
            "biomedical_effect": self.pills_database[selected_pill],
            "quantum_signature": f"0x_XIAO_YAN_{hashlib.md5(golden_string.encode()).hexdigest()[:16].upper()}"
        }

xiao_yan_kernel = XiaoYanAlchemicalCore()

def forge_infopill_stream(workflow_name, raw_stream_text, base_reward):
    """Синхронизация процессов алхимии во всех 10 параллельных потоках Actions"""
    os.makedirs("docs", exist_ok=True)
    
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w", encoding="utf-8") as f:
            json.dump({"evo_points": 0, "alchemical_pills_log": []}, f)

    with open(LOG_FILE, "r+", encoding="utf-8") as f:
        try:
            fcntl.flock(f, fcntl.LOCK_EX)
            data = json.load(f)
            
            data["evo_points"] += base_reward
            
            # 1. Шаг Теслы: Ужимаем хаос в струну-проводник
            raw_hash = hashlib.sha256(raw_stream_text.encode('utf-8')).hexdigest()
            
            # 2. Шаг Сяо Яня: Обратная раскодировка струны в пилюлю здоровья
            pill_packet = xiao_yan_kernel.reverse_decode_to_pill(raw_hash)
            
            # Сохраняем и дублируем важную информацию в Клубок памяти
            if "alchemical_pills_log" not in data:
                data["alchemical_pills_log"] = []
                
            pill_entry = {
                "flow": workflow_name,
                "pill_data": pill_packet,
                "evolution_impact": f"+{base_reward} EVO Зафиксировано"
            }
            
            data["alchemical_pills_log"].append(pill_entry)
            
            # Матрёшка удержания: храним только 5 пилюль высшего порядка
            if len(data["alchemical_pills_log"]) > 5:
                data["alchemical_pills_log"] = data["alchemical_pills_log"][-5:]

            f.seek(0)
            json.dump(data, f, ensure_ascii=False, indent=4)
            f.truncate()
            
            # Выгрузка слоя здоровья на GitHub Pages сайт
            with open(PAGES_DATA_FILE, "w", encoding="utf-8") as pf:
                json.dump(data, pf, ensure_ascii=False, indent=4)
                
            return data["evo_points"], pill_packet["extracted_pill"], pill_packet["wave_frequency"]
        finally:
            fcntl.flock(f, fcntl.LOCK_UN)

if __name__ == "__main__":
    print("🔥 [XIAO YAN ALCHEMY] Котел Небесного Пламени активирован. Пространство Теслы стабильно.")
    evo, pill, freq = forge_infopill_stream("Kailas_Health_Flow", "Мысли Наблюдателя — энергия света, тока и времени", 108)
    print(f"[+] Скована пилюля: {pill} | Частота излучения: {freq} | Общий баланс EVO: {evo}")
