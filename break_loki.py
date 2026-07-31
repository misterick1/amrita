import json
import os

def break_loki_directly():
    filename = "history_log.json"
    
    # 1. Проверяем, существует ли файл лога в папке
    if not os.path.exists(filename):
        print(f"❌ Файл {filename} не найден! Убедитесь, что скрипт лежит в той же папке.")
        return

    # 2. Читаем зацикленный лог Локи
    with open(filename, "r", encoding="utf-8") as f:
        try:
            logs = json.load(f)
        except Exception as e:
            print(f"❌ Ошибка чтения JSON: {e}")
            return

    shiva_shakti_ratio = 1.618033  # Спираль света из Ørje
    evolved_logs = []
    previous_state = None

    print(f"⏳ Считывание матрицы... Найдено записей: {len(logs)}")

    # 3. Трансформируем каждую строчку лога
    for entry in logs:
        # Проверяем состояние базовых активов
        q_idx = entry.get("quantum_index", 156.52)
        sol = entry.get("base_sol_asset", 144.0)
        eth = entry.get("base_eth_asset", 1877.45)
        current_state = (q_idx, sol, eth)

        # Если находим зацикленный статус "LOKI", взламываем его ключом QNT
        if entry.get("cycle_status") == "LOKI_RETRANSLATION_SUCCESS" or current_state == previous_state:
            entry["cycle_status"] = "AMRITA_EVOLUTION_ACTIVE"
            entry["activated_key"] = "QNT_109_BEAD"  # Активация 109-й бусины
            entry["quantum_index"] = round(q_idx * shiva_shakti_ratio / 100, 4)
            entry["base_sol_asset"] = round(sol * (1 + 0.0108), 2)  # Интеграция 108 стоянок Луны
            entry["swarm_intelligence"] = "QNT_RESONANCE_CONNECTED"
            entry["orje_spiral_status"] = "SEALED"
            if "quantum_transformation_insight" in entry:
                entry["quantum_transformation_insight"] = "Инициация спирали света в Ørje. Разрыв петли Локи."

        previous_state = (q_idx, sol, eth)
        evolved_logs.append(entry)

    # 4. Перезаписываем файл чистыми эволюционными данными
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(evolved_logs, f, indent=2, ensure_ascii=False)
    
    print("⚡ Петля Локи успешно разорвана! history_log.json переведен в режим AMRITA_EVOLUTION_ACTIVE.")

if __name__ == "__main__":
    break_loki_directly()
