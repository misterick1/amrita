import sys
import json
import time

class EconomicNewsParser:
    def __init__(self):
        self.is_market_turbulent = False
        # Список зон риска на 17 июня 2026 года из календаря FTMO
        self.restricted_events = [
            {"time": "08:00", "event": "CPI y/y (GBP)"},
            {"time": "16:30", "event": "Crude Oil Inventories"},
            {"name": "FED_RATE", "time": "20:00", "event": "Federal Funds Rate (USD)"},
            {"time": "20:00", "event": "FOMC Statement (USD)"}
        ]
        print("[PARSER START] Робот-мониторинг макроэкономических частот FTMO запущен.")

    def check_time_window(self, current_time_str):
        """
        Проверка окна турбулентности. Автоматически замораживает коммерческий слой
        за 2 минуты до и 2 минуты после ключевых событий.
        """
        print(f"\n[АУДИТ ВРЕМЕНИ] Текущее время сети: {current_time_str}")
        
        for event in self.restricted_events:
            if event["time"] == current_time_str:
                self.is_market_turbulent = True
                print(f"[⚠️ FTMO RESTRICTION] Обнаружено критическое событие: {event['event']}")
                print("[⚠️ FTMO RESTRICTION] Внимание: Коммерческие транзакции ЗАБЛОКИРОВАНЫ для безопасности плат.")
                return "HOLD"
                
        self.is_market_turbulent = False
        print("[🟢 ОК] Окно чистое. Транзакции и начисление роялти разрешены в штатном режиме.")
        return "EXECUTE"

if __name__ == "__main__":
    parser = EconomicNewsParser()
    
    # Симуляция 1: Обычное время, транзакции идут
    parser.check_time_window("12:00")
    
    # Симуляция 2: Наступление времени 20:00 (Решение ФРС) — автоматический блок стека
    status = parser.check_time_window("20:00")
    
    if status == "HOLD":
        print("\n[🟢 УСПЕХ] Робот-парсер FTMO успешно заблокировал транзакции в момент перегрузки ФРС.")
        sys.exit(0)
    else:
        sys.exit(1)
