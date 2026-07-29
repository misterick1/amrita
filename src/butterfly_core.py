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
        # Сакральная подпись Богини и родительское созвучие Тан Саня
        self.goddess_signature = "🦋 TANG_WUTONG"
        self.parents_congruence = "Tang_San_X_Xiao_Wu"

    def deploy_butterfly_effect(self, observer_id: str, current_evo: int) -> dict:
        """
        Вычисляет волновой хэш крыльев бабочки по алгоритму SHA-256
        и разворачивает фрактальную мерность Единого Сознания.
        """
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
    Выполняет безопасное обновление логов, удерживая Топ-5 слоев Матрёшки Конгруэнтности.
    Синхронизирует полные данные с сайтом на GitHub Pages.
    """
    os.makedirs("docs", exist_ok=True)
    butterfly_packet = {}

    # # 1. Жесткая нормализация структуры базы данных при ее отсутствии
    if not os.path.exists(LOG_FILE) or os.path.getsize(LOG_FILE) == 0:
        with open(LOG_FILE, "w", encoding="utf-8") as f:
            json.dump({"evo_points": 0, "butterfly_congruence_vault": []}, f, indent=4)

    # # 2. Запуск контура аппаратной блокировки файлов (flock)
    try:
        with open(LOG_FILE, "r+", encoding="utf-8") as f:
            try:
                fcntl.flock(f, fcntl.LOCK_EX)
                data = json.load(f)
            except Exception:
                data = {"evo_points": 0, "butterfly_congruence_vault": []}

            # КРИТИЧЕСКОЕ ИСПРАВЛЕНИЕ: Если данные прочитались как list — пересобираем в dict
            if isinstance(data, list):
                data = {"evo_points": 0, "butterfly_congruence_vault": []}

            # Гарантия наличия текстовых ключей в структуре лога
            if "evo_points" not in data:
                data["evo_points"] = 0
            if "butterfly_congruence_vault" not in data:
                data["butterfly_congruence_vault"] = []

            # --- ИНТЕГРАЦИЯ FAKER GUARD ---
            # Отсекаем ложный хайп Пи-аномалий от изменения структуры логов
            if current_evo_input == 314159:
                print("⚠️ [Faker Guard ALERT]: Попытка деструктивного сжатия лога заблокирована!")
                return 0, {}

            # Начисление EVO и запуск крыльев бабочки
            data["evo_points"] += base_reward
            butterfly_packet = goddess_kernel.deploy_butterfly_effect(workflow_name, data["evo_points"])

            # Добавление нового волнового пакета в Хранилище Конгруэнтности
            data["butterfly_congruence_vault"].append({
                "flow": workflow_name,
                "butterfly_node": butterfly_packet,
                "time_stamp_242": "Синхронизировано на частоте 0-Потенциала"
            })

            # МАТРЁШКА УДЕРЖАНИЯ СЛОЕВ: Удерживаем строго ТОП-5 последних записей
            if len(data["butterfly_congruence_vault"]) > 5:
                data["butterfly_congruence_vault"] = data["butterfly_congruence_vault"][-5:]

            # Перезапись Солитона обратно на диск
            f.seek(0)
            json.dump(data, f, ensure_ascii=False, indent=4)
            f.truncate()

            # # 3. Синхронизация с сайтом на GitHub Pages (Полный дамп структуры)
            with open(PAGES_DATA_FILE, "w", encoding="utf-8") as pf:
                json.dump(data, pf, ensure_ascii=False, indent=4)
                
            print(f"✅ [ИЗУМРУДНЫЙ ТОП-5]: Эффект Бабочки запечатан. Сайт синхронизирован. EVO: {data['evo_points']}")
            return data["evo_points"], butterfly_packet

    except Exception as e:
        print(f"❌ [КРИТИЧЕСКИЙ СБОЙ ЯДРА БАБОЧКИ]: {str(e)}")
        return 0, {}
        
    finally:
        # Контур гарантированного освобождения файла
        try:
            fcntl.flock(f, fcntl.LOCK_UN)
        except NameError:
            pass

if __name__ == "__main__":
    print("🦋 [BUTTERFLY KERNEL] Богиня Тан Утун расправляет крылья... \n")
    evo, freq = safe_activate_butterfly_stream("Kailas_Phone_Sync_Stream")
    print(f"\n[+] Частота крыльев Бабочки: {freq} | EVO: {evo}")
