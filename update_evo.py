# update_evo.py
import os
import json
import time
from datetime import datetime
import urllib.request

# Инициализация путей логирования
LOG_FILE = "history_log.json"
QUANTUM_COEFFICIENT = 1.08

def get_quantum_metrics():
    """Получение ценовых потоков для симуляции 8-й сборки"""
    print("[AMRITA_EVO] Подключение к открытому шлюзу котировок...")
    url = "https://jup.ag"
    
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode())
            if "data" in data and "So11111111111111111111111111111111111111112" in data["data"]:
                sol_price = float(data["data"]["So11111111111111111111111111111111111111112"]["price"])
                return sol_price, round(sol_price * QUANTUM_COEFFICIENT, 2)
    except Exception as e:
        print(f"[ORACLE_WARNING] Сетевой лимит. Использование базового ядра: {e}")
    
    return 144.0, 155.52

def update_sealed_history(sol_price, stocks_index):
    """Обновление и запечатывание файла history_log.json"""
    print(f"[AMRITA_EVO] Запечатывание цифрового следа в {LOG_FILE}...")
    
    new_entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "cycle_status": "SEALED_SUCCESS",
        "quantum_index": stocks_index,
        "base_sol_asset": sol_price,
        "swarm_intelligence": "ACTIVE"
    }

    # Читаем существующий лог или создаем новый массив
    if os.path.exists(LOG_FILE):
        try:
            with open(LOG_FILE, "r", encoding="utf-8") as f:
                history = json.load(f)
                if not isinstance(history, list):
                    history = []
        except:
            history = []
    else:
        history = []

    history.append(new_entry)

    # Сохраняем обновленную историю
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=4)
    print("[AMRITA_EVO] Файл логов успешно обновлен.")

def main():
    print("=== ЗАПУСК СЕРВЕРНОГО ЯДРА UPDATE_EVO.PY ===")
    
    # Считывание секретов из GitHub Actions Environment
    tg_token = os.environ.get("TELEGRAM_BOT_TOKEN")
    xai_key = os.environ.get("XAI_API_KEY")
    sol_rpc = os.environ.get("SOLANA_RPC_URL")

    if not tg_token:
        print("[WARNING] Переменная TELEGRAM_BOT_TOKEN не задана в Secrets.")
    if not xai_key:
        print("[WARNING] Переменная XAI_API_KEY не задана в Secrets.")

    # Выполнение расчетов
    sol_p, stock_i = get_quantum_metrics()
    
    # Запись в файл истории для последующего авто-коммита
    update_sealed_history(sol_p, stock_i)
    
    print("=== АВТОНОМНЫЙ ЦИКЛ ЕЖЕНЫША ЗАВЕРШЕН ===")

if __name__ == "__main__":
    main()
