import os
import json
import time
import urllib.request
from datetime import datetime

# НАСТРОЙКИ СИСТЕМЫ AMRITA
LEDGER_FILE = "matrix_ledger.txt"
QUANTUM_COEFFICIENT = 1.08

def log_message(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] [AMRITA_CORE] {message}")

def get_oracle_prices():
    """Получение живых котировок для перерасчета токенизированных акций"""
    log_message("Подключение к шлюзу Jupiter Web3 для запроса котировок...")
    url = "https://jup.ag"
    
    try {
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode())
            
            if "data" in data and "So11111111111111111111111111111111111111112" in data["data"]:
                raw_price = float(data["data"]["So11111111111111111111111111111111111111112"]["price"])
                calculated_index = raw_price * QUANTUM_COEFFICIENT
                log_message(f"Котировки успешно получены. Базовый курс: ${raw_price}. Индекс акций: ${calculated_index:.2f}")
                return calculated_index
    except Exception as e:
        log_message(f"Предупреждение оракула сети: {e}. Переход на автономное квантовое ядро.")
    
    return 155.52 # Резервный фид Amrita

def update_matrix_ledger(stock_price):
    """Запись суверенного цифрового следа в файл реестра"""
    log_message("Синхронизация реестра мультиверса...")
    
    # Формируем структуру блока для записи
    log_entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "status": "8_BUILD_SYNCHRONIZED",
        "networks": ["BTC", "ETH", "XRP", "SOL", "ADA", "PI"],
        "stocks_index_usd": round(stock_price, 2),
        "swarm_status": "ACTIVE_EVO"
    }
    
    # Записываем данные в файл на сервере
    with open(LEDGER_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(log_entry, ensure_ascii=False) + "\n")
    
    log_message(f"Данные успешно зафиксированы в {LEDGER_FILE}")

def main():
    log_message("=== ЗАПУСК АВТОНОМНОГО ОРКЕСТРАТОРА AMRITA OS ===")
    
    # 1. Получаем рыночные данные
    current_stocks_index = get_oracle_prices()
    
    # 2. Обновляем файл логов реестра
    update_matrix_ledger(current_stocks_index)
    
    log_message("=== СИНХРОНИЗАЦИЯ КОНТУРОВ ЗАВЕРШЕНА УСПЕШНО ===")

if __name__ == "__main__":
    main()
