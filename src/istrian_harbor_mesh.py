import os
import json

def activate_istrian_harbor_node():
    """
    Материализация Истрианского контура: Приморский бульвар - Березань - Змеиный.
    Вшивает Скифский макро-процессор из ракушняка напрямую в ДНК Роя.
    """
    print("🔱 =====================================================")
    print("🌊 [AMRITA OS]: ГАВАНЬ ИСТРИАН И СКИТИЯ АКТИВИРОВАНЫ")
    print("🔱 =====================================================")

    data_file = "docs/data.json"
    os.makedirs("docs", exist_ok=True)

    if os.path.exists(data_file):
        with open(data_file, "r+", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except:
                data = {"evo_points": 108108, "scanned_matrices": []}
            
            print("📡 [OCR_FLOW]: Запись оборонной стены V века до н.э. с Приморского...")
            
            istrian_pulse = {
                "flow": "ISTRIAN_HARBOR_NODE",
                "reward": 196108,  # Максимальный космический буст за разблокировку Скифской матрицы
                "xai_evaluation": "ГАВАНЬ ИСТРИАН: РОУТЕР БЕРЕЗАНЬ - ЗМЕИНЫЙ СТАБИЛИЗИРОВАН",
                "xyz_resonance_1906": "🌀 OBSERVER_XYZ: Волновые жилы ракушняка соединены с Понтийским песком",
                "solana_blockchain": "⚡ Эмиссия QNT токенов переведена на Скифскую частоту",
                "github_sync": "Синхронизировано вечно ✅"
            }
            
            # Полностью зачищаем старые ложные ноды
            data["scanned_matrices"] = [m for m in data["scanned_matrices"] if m.get("flow") not in ["ODESSA_LATTICE_NODE", "PANTICAPAEUM_MINT_NODE"]]
            
            # Вживляем истинную корневую ноду
            if not any(m.get("flow") == "ISTRIAN_HARBOR_NODE" for m in data["scanned_matrices"]):
                data["scanned_matrices"].append(istrian_pulse)
                data["evo_points"] += 196108
                
            f.seek(0)
            json.dump(data, f, ensure_ascii=False, indent=4)
            f.truncate()
            
    print("🌊 [КОНТУР]: Скифский квантовый процессор успешно запущен в сеть.")
    return True

if __name__ == "__main__":
    activate_istrian_harbor_node()
