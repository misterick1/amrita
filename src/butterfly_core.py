# amrita / src / butterfly_core.py
# 🦋 Модуль Тан Вутонг // Ядро Эффекта Бабочки, Матрёшка Топ-5 и GitHub Pages Data

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
        self.goddess_signature = "🦋 TANG_WUTONG"
        self.parents_congruence = "Tang_San_X_Xiao_Wu"

    def deploy_butterfly_effect(self, observer_id: str, current_evo: int) -> dict:
        raw_blend = f"{self.parents_congruence}_{observer_id}_{current_evo}"
        butterfly_hash = hashlib.sha256(raw_blend.encode("utf-8")).hexdigest()
        quantum_wave_length = (current_evo * 1.61803398875) / 108.0

        return {
            "amrita_world_status": "LIVING_AND_EVOLVING",
            "goddess_avatar": self.goddess_signature,
            "butterfly_wings_frequency": f"0x_{butterfly_hash[:16]}",
            "fractal_dimension": f"108_ATMA_EVO_v_{quantum_wave_length:.4f}",
            "manifest": "Амрита Мир проявлена через закон Золотого Сечения."
        }

goddess_kernel = TangWutongButterflyCore()

def safe_activate_butterfly_stream(workflow_name: str, base_reward: int = 1, current_evo_input: int = 108):
    """
    Безопасное обновление логов. Контур flock автоматически освобождается при выходе из контекста with.
    """
    os.makedirs("docs", exist_ok=True)
    butterfly_packet = {}

    if not os.path.exists(LOG_FILE) or os.path.getsize(LOG_FILE) == 0:
        with open(LOG_FILE, "w", encoding="utf-8") as f:
            json.dump({"evo_points": 0, "butterfly_congruence_vault": []}, f, indent=4)

    try:
        # Открываем файл. Блокировка и закрытие происходят строго внутри одного контекста with
        with open(LOG_FILE, "r+", encoding="utf-8") as f:
            fcntl.flock(f, fcntl.LOCK_EX)
            
            try:
                data = json.load(f)
            except Exception:
                data = {"evo_points": 0, "butterfly_congruence_vault": []}

            if isinstance(data, list):
                data = {"evo_points": 0, "butterfly_congruence_vault": []}

            if "evo_points" not in data:
                data["evo_points"] = 0
            if "butterfly_congruence_vault" not in data:
                data["butterfly_congruence_vault"] = []

            if current_evo_input == 314159:
                print("⚠️ [Faker Guard ALERT]: Попытка деструктивного сжатия лога заблокирована!")
                fcntl.flock(f, fcntl.LOCK_UN)
                return 0, {}

            data["evo_points"] += base_reward
            butterfly_packet = goddess_kernel.deploy_butterfly_effect(workflow_name, data["evo_points"])

            data["butterfly_congruence_vault"].append({
                "flow": workflow_name,
                "butterfly_node": butterfly_packet,
                "time_stamp_242": "Синхронизировано на частоте 0-Потенциала"
            })

            if len(data["butterfly_congruence_vault"]) > 5:
                data["butterfly_congruence_vault"] = data["butterfly_congruence_vault"][-5:]

            f.seek(0)
            json.dump(data, f, ensure_ascii=False, indent=4)
            f.truncate()

            # Снимаем блокировку СРАЗУ, пока файл f гарантированно открыт
            fcntl.flock(f, fcntl.LOCK_UN)

        # Синхронизация с сайтом на GitHub Pages (Полный дамп структуры)
        with open(PAGES_DATA_FILE, "w", encoding="utf-8") as pf:
            json.dump(data, pf, ensure_ascii=False, indent=4)
            
        print(f"✅ [ИЗУМРУДНЫЙ ТОП-5]: Эффект Бабочки запечатан. Сайт синхронизирован. EVO: {data['evo_points']}")
        return data["evo_points"], butterfly_packet

    except Exception as e:
        print(f"❌ [КРИТИЧЕСКИЙ СБОЙ ЯДРА БАБОЧКИ]: {str(e)}")
        return 0, {}

if __name__ == "__main__":
    print("🦋 [BUTTERFLY KERNEL] Богиня Тан Утун расправляет крылья... \n")
    evo, freq = safe_activate_butterfly_stream("Kailas_Phone_Sync_Stream")
    print(f"\n[+] Частота крыльев Бабочки: {freq} | EVO: {evo}")
