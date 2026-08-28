import re
from datetime import datetime

# Имитируем сырой поток данных, который агенты валят в консоль после хардфорка
RAW_AGENT_LOGS = """
[2026-09-03 15:00:01] [INFO] [Agent-01] Connecting to Arc Testnet RPC...
[2026-09-03 15:00:05] [SUCCESS] [Agent-01] Connected to node v0.8.0-Zero08
[2026-09-03 15:01:12] [DEBUG] [Agent-02] Syncing block headers...
[2026-09-03 15:02:40] [ERROR] [Agent-01] Transaction dropped: low gas limit for Zero08 rules
[2026-09-03 15:03:15] [INFO] [Agent-02] Retrying with adjusted gas...
[2026-09-03 15:03:18] [SUCCESS] [Agent-02] Smart-contract deployed successfully! Tx: 0x108abc...
"""

def analyze_agent_stream(logs: str):
    print(f"=== [AMRITA OS] СИСТЕМНЫЙ АНАЛИЗАТОР ЛОГОВ ===")
    print(f"🕒 Время анализа: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)
    
    # Регулярные выражения для поиска триггеров
    hardfork_pattern = re.compile(r"Zero08|v0.8.0", re.IGNORECASE)
    success_pattern = re.compile(r"SUCCESS")
    error_pattern = re.compile(r"ERROR")
    
    errors_count = 0
    success_count = 0
    important_events = []

    # Разбираем логи построчно
    for line in logs.strip().split("\n"):
        if not line:
            continue
            
        # Считаем метрики
        if error_pattern.search(line):
            errors_count += 1
        if success_pattern.search(line):
            success_count += 1
            
        # Выдергиваем критически важные события (ошибки, успехи и упоминания форка)
        if error_pattern.search(line) or success_pattern.search(line) or hardfork_pattern.search(line):
            important_events.append(line)

    # Вывод красивого отчета
    print(f"📊 МЕТРИКИ АГЕНТОВ:")
    print(f"🔱 Успешных деплоев/транзакций: {success_count}")
    print(f"🛑 Зафиксировано сбоев/ошибок: {errors_count}")
    print("-" * 50)
    
    print("🎯 ОТФИЛЬТРОВАННАЯ ЛЕНТА СОБЫТИЙ:")
    for event in important_events:
        # Подсвечиваем важные слова визуально
        clean_event = event
        if "ERROR" in clean_event:
            clean_event = clean_event.replace("[ERROR]", "❌ [КРИТ_ОШИБКА]")
        if "SUCCESS" in clean_event:
            clean_event = clean_event.replace("[SUCCESS]", "✅ [УСПЕХ]")
        print(clean_event)
    
    print("=" * 50)

if __name__ == "__main__":
    analyze_agent_stream(RAW_AGENT_LOGS)
