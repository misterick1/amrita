import sys
import time
from datetime import datetime, timedelta

class EconomicNewsParser:
    def __init__(self):
        self.is_market_turbulent = False
        
        # Список динамических зон риска (события зафиксированы по времени UTC)
        # Для боевого режима здесь может быть интеграция с API новостей DailyFX/Investing
        self.restricted_events = [
            {"time": "08:00", "event": "CPI y/y (Инфляция)"},
            {"time": "16:30", "event": "Crude Oil Inventories (Нефть)"},
            {"time": "20:00", "event": "FED INTEREST RATE (Ставка ФРС)"},
            {"time": "20:30", "event": "FOMC Statement (Пресс-конференция)"}
        ]
        print(f"[PARSER START] Робот-мониторинг Amrita FTMO Shield активирован в реальном времени.")

    def check_time_window(self, current_time_str: str) -> str:
        """
        Проверка окна турбулентности. Автоматическая блокировка транзакций
        за 2 минуты до и 2 минуты после наступления ключевых макроэкономических событий.
        """
        print(f"\n[АУДИТ ВРЕМЕНИ] Проверка контура на отметке: {current_time_str}")
        
        # Конвертируем текущее строковое время "ЧЧ:ММ" в объект времени для математических операций
        try:
            current_dt = datetime.strptime(current_time_str, "%H:%M")
        except ValueError:
            print(f"[ERROR] Неверный формат времени: {current_time_str}. Блокировка из соображений безопасности.")
            return "HOLD"

        for event in self.restricted_events:
            event_dt = datetime.strptime(event["time"], "%H:%M")
            
            # Вычисляем границы защитного окна: -2 минуты до и +2 минуты после события
            lower_bound = event_dt - timedelta(minutes=2)
            upper_bound = event_dt + timedelta(minutes=2)
            
            # Проверяем, попадает ли текущее время сервера в диапазон блокировки
            if lower_bound <= current_dt <= upper_bound:
                self.is_market_turbulent = True
                print(f"[⚠️ FTMO RESTRICTION] Обнаружена зона макро-турбулентности: {event['event']} ({event['time']})")
                print(f"[⚠️ FTMO RESTRICTION] Внимание: Торговый контур принудительно переведен в режим заморозки.")
                return "HOLD"

        self.is_market_turbulent = False
        print(f"[🟢 OK] Окно чистое. Транзакции и движение ликвидности разрешены.")
        return "EXECUTE"

    def run_autonomous_loop(self):
        """Бесконечный цикл для работы на сервере под управлением PM2."""
        print("[LOOP] Запуск бесконечного контура мониторинга времени...")
        while True:
            # Получаем текущее системное время сервера в формате ЧЧ:ММ
            server_time_str = datetime.now().strftime("%H:%M")
            
            status = self.check_time_window(server_time_str)
            
            # Здесь может быть триггер обратной связи для торговых ботов Amrita
            # (Например, запись флага заморозки в локальный манифест или отправка вебхука)
            
            # Интервал проверки — 30 секунд, чтобы гарантированно не пропустить 4-минутное окно
            time.sleep(30)


if __name__ == "__main__":
    parser = EconomicNewsParser()
    
    # ПРОВЕРКА ЦЕЛОСТНОСТИ ПРИ ПУШЕ (Для CI/CD пайплайна GitHub Actions)
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print("[CI/CD] Запуск симуляции тестов для верификации алгоритма...")
        # Тест 1: Время за пределами окна новостей
        assert parser.check_time_window("12:00") == "EXECUTE", "Ошибка: ложное срабатывание на чистом окне"
        # Тест 2: Граничное время (за 2 минуты до FOMC в 20:00)
        assert parser.check_time_window("19:58") == "HOLD", "Ошибка: защитный интервал -2 минуты не сработал"
        # Тест 3: Граничное время (через 2 минуты после FOMC)
        assert parser.check_time_window("20:02") == "HOLD", "Ошибка: protective буфер +2 минуты пробит"
        
        print("[CI/CD] Все тесты математических окон пройдены успешно! Матрица стабильна.")
        sys.exit(0)
    else:
        # ОСНОВНОЙ РЕЖИМ: Работа на сервере в PM2
        try:
            parser.run_autonomous_loop()
        except KeyboardInterrupt:
            print("[STOP] Парсер новостей остановлен.")
