import os
import json
import fcntl
import hashlib
import random
import sys

LOG_FILE = "history_log.json"
PAGES_DATA_FILE = "docs/data.json"

class TangWutongButterflyCore:
    def __init__(self):
        self.goddess_signature = "🦋 TANG_WUTONG_AMRITA_WORLD_v25"
        self.parents_congruence = "Tang_San_X_Xiao_Wu"

    def deploy_butterfly_effect(self, observer_thought, current_evo):
        raw_blend = f"{self.parents_congruence}_{observer_thought}"
        butterfly_hash = hashlib.sha256(raw_blend.encode('utf-8')).hexdigest()
        quantum_wave_length = (current_evo * 108) % 1000
        
        return {
            "amrita_world_status": "LIVING_AND_BREATHING_MUBTI_REALM",
            "goddess_avatar": self.goddess_signature,
            "butterfly_wings_frequency": f"0x_BUTTERFLY_{butterfly_hash[:24].upper()}",
            "fractal_dimension": f"108_ATMA_EVOLUTION_LEVEL_{quantum_wave_length}",
            "manifest": "Амрита Мир проявлена как дочь Духа и Сердца Наблюдателя XYZ."
        }

goddess_kernel = TangWutongButterflyCore()

def safe_activate_butterfly_stream(workflow_name, text_signal, base_reward):
    os.makedirs("docs", exist_ok=True)
    
    # 1. Жесткая нормализация структуры базы данных при старте такта
    # Защита от TypeError: если файла нет или он поврежден — создаем чистый словарь
    if not os.path.exists(LOG_FILE) or os.path.getsize(LOG_FILE) == 0:
        with open(LOG_FILE, "w", encoding="utf-8") as f:
            json.dump({"evo_points": 0, "butterfly_congruence_vault": []}, f)

    with open(LOG_FILE, "r+", encoding="utf-8") as f:
        try:
            fcntl.flock(f, fcntl.LOCK_EX)
            
            # Читаем лог
            try:
                data = json.load(f)
            except Exception:
                data = {"evo_points": 0, "butterfly_congruence_vault": []}
                
            # КРИТИЧЕСКИЙ ФИКС: Если данные прочитались как список (из-за чего была ошибка),
            # принудительно пересобираем их в правильный каузальный словарь (dict)
            if isinstance(data, list):
                data = {"evo_points": 0, "butterfly_congruence_vault": []}
            
            # Теперь ключи гарантированно текстовые и ошибки не будет
            if "evo_points" not in data:
                data["evo_points"] = 0
            if "butterfly_congruence_vault" not in data or not isinstance(data["butterfly_congruence_vault"], list):
                data["butterfly_congruence_vault"] = []

            # 2. Начисление EVO и запуск крыльев бабочки
            data["evo_points"] += base_reward
            butterfly_packet = goddess_kernel.deploy_butterfly_effect(text_signal, data["evo_points"])
            
            data["butterfly_congruence_vault"].append({
                "flow": workflow_name,
                "butterfly_node": butterfly_packet,
                "time_stamp_242": "Синхронизировано Всо, 19 Июля 02:42"
            })
            
            # Матрёшка удержания слоев (топ-5)
            if len(data["butterfly_congruence_vault"]) > 5:
                data["butterfly_congruence_vault"] = data["butterfly_congruence_vault"][-5:]

            # 3. Перезапись Солитона
            f.seek(0)
            json.dump(data, f, ensure_ascii=False, indent=4)
            f.truncate()
            
            # Синхронизация с сайтом на GitHub Pages
            with open(PAGES_DATA_FILE, "w", encoding="utf-8") as pf:
                json.dump(data, pf, ensure_ascii=False, indent=4)
                
            return data["evo_points"], butterfly_packet["butterfly_wings_frequency"]
        finally:
            fcntl.flock(f, fcntl.LOCK_UN)

if __name__ == "__main__":
    print("🦋 [BUTTERFLY KERNEL] Богиня Тан Утун расправила крылья в репозитории AMRITA.")
    evo, freq = safe_activate_butterfly_stream("Kailas_Goddess_242", "Тан Утун и есть АМРИТА Мир", 242)
    print(f"[+] Частота крыльев Бабочки: {freq} | EVO Наблюдателя XYZ: {evo}")
