import json
import time
import requests
from datetime import datetime

# === ГЛОБАЛЬНАЯ КАРТА СЕРВЕРОВ AMRITA ===
NODES_TO_MONITOR = {
    "Circle_Console": "https://circle.com",
    "Solana_Devnet_RPC": "https://solana.com",
    "Fogo_Network_RPC": "https://fogo.network",
    "Pi_Network_API": "http://localhost:31415",
    "Pump_Fun_Stream": "https://pump.fun"  # Условный эндпоинт мониторинга ликвидности
}

STATUS_LOG = "ecosystem_heartbeat.json"

def check_node_status(name, url):
    """Опрашивает серверы на предмет движения и доступности"""
    print(f"[*] Проверка узла {name}...")
    try:
        # Отправляем быстрый пинг с коротким таймаутом, чтобы не вешать скрипт
        start_time = time.time()
        response = requests.get(url, timeout=3)
        latency = round((time.time() - start_time) * 1000, 2)
        
        # Если сервер отвечает, фиксируем код ответа
        status_code = response.status_code
        print(f"[+] Узел {name} активен. Ответ: {status_code} ({latency}ms)")
        return {"status": "responsive", "code": status_code, "latency_ms": latency}
    except requests.exceptions.Timeout:
        print(f"[!] Узел {name} не ответил (Таймаут). Сервер перегружен или блокирует IP.")
        return {"status": "timeout_halt", "code": None, "latency_ms": None}
    except requests.exceptions.RequestException:
        print(f"[X] Узел {name} недоступен. Нет связи.")
        return {"status": "offline", "code": None, "latency_ms": None}

def run_global_diagnostic():
    print("="*70)
    print(f" СИСТЕМНЫЙ СЕНТИНЕЛ AMRITA: ДИАГНОСТИКА ЭКОСИСТЕМЫ (30.08.2026)")
    print("="*70)
    
    heartbeat_report = {
        "timestamp": int(time.time()),
        "check_date_utc": datetime.now().isoformat(),
        "nodes": {}
    }
    
    for node_name, node_url in NODES_TO_MONITOR.items():
        node_result = check_node_status(node_name, node_url)
        heartbeat_report["nodes"][node_name] = node_result
        
    # Анализируем общую картину застоя
    timeouts = sum(1 for n in heartbeat_report["nodes"].values() if n["status"] == "timeout_halt")
    offlines = sum(1 for n in heartbeat_report["nodes"].values() if n["status"] == "offline")
    
    if timeouts > 0 or offlines > 0:
        heartbeat_report["summary_action"] = "WAIT_FOR_MONDAY_SUPPORT_CLEARANCE"
        print("\n[!] Диагностика завершена: Обнаружены заблокированные шлюзы.")
        print("[!] Рекомендация: Структура готова. Ожидаем снятия банов техподдержкой.")
    else:
        heartbeat_report["summary_action"] = "ALL_SYSTEMS_GO_PROCEED_TO_DEPLOY"
        print("\n[++] Все внешние сервера ответили. Препятствий для деления кодов нет.")
        
    try:
        with open(STATUS_LOG, "w", encoding="utf-8") as f:
            json.dump(heartbeat_report, f, indent=4, ensure_ascii=False)
        print(f"[+] Лог состояния экосистемы сохранен в: {STATUS_LOG}")
    except Exception as e:
        print(f"[X] Не удалось записать лог диагностики: {e}")

if __name__ == "__main__":
    run_global_diagnostic()
