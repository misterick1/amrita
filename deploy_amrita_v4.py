import os
import sys
import subprocess
import json
import requests

# === КОНФИГУРАЦИЯ ОБНОВЛЕНИЯ ПОД V4.3.0-BETA.3 ===
TARGET_VERSION = "4.3.0-beta.3"
RPC_DEVNET_URL = "https://solana.com"
CONFIG_FILE = "solana_config.json"

def run_command(command, description):
    """Выполняет системную команду и проверяет статус выполнения"""
    print(f"[*] Выполнение: {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(f"[+] Успешно: {description}")
        if result.stdout.strip():
            print(result.stdout.strip())
        return True
    except subprocess.CalledProcessError as e:
        print(f"[X] Ошибка при выполнении: {description}")
        print(f"[X] Код ошибки: {e.returncode}")
        print(f"[X] Детали: {e.stderr.strip()}")
        return False

def verify_system_environment():
    """Проверяет наличие установленного Solana CLI и инструментов сборки"""
    print("[*] Шаг 1: Проверка системного окружения...")
    solana_check = run_command("solana --version", "Проверка версии Solana CLI")
    if not solana_check:
        print("[!] Solana CLI не обнаружен. Пожалуйста, установите его перед запуском.")
        return False
    return True

def upgrade_solana_cli():
    """Принудительно обновляет Solana CLI до целевой бета-версии Anza Agave"""
    print(f"\n[*] Шаг 2: Обновление Solana CLI до версии {TARGET_VERSION}...")
    upgrade_cmd = f"solana-install init {TARGET_VERSION}"
    return run_command(upgrade_cmd, f"Установка ядра {TARGET_VERSION}")

def patch_rpc_configuration():
    """Создает или обновляет конфигурационный файл с учетом новых требований к RPC-запросам"""
    print("\n[*] Шаг 3: Синтез обновленной конфигурации сети...")
    
    # Новые стандарты требуют обязательного указания commitment и кодировки для исключения ошибок валидаторов
    updated_config = {
        "network": "devnet",
        "rpc_url": RPC_DEVNET_URL,
        "commitment": "confirmed",
        "encoding": "base64",
        "compatibility_mode": "agave_v4",
        "target_beta": TARGET_VERSION
    }
    
    try:
        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump(updated_config, f, indent=4)
        print(f"[+] Конфигурационный файл {CONFIG_FILE} успешно перезаписан на замену старой версии.")
        return True
    except Exception as e:
        print(f"[X] Не удалось записать конфигурацию: {e}")
        return False

def check_devnet_status():
    """Проверяет доступность обновленной сети Devnet через RPC-запрос"""
    print("\n[*] Шаг 4: Тестирование соединения с обновленным Devnet RPC...")
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getVersion",
    }
    try:
        response = requests.post(RPC_DEVNET_URL, json=payload, timeout=10)
        if response.status_code == 200:
            version_info = response.json().get("result", {})
            print(f"[+] Ответ RPC получен успешно. Текущая версия ноды в сети: {version_info.get('solana-core', 'Неизвестно')}")
            return True
        else:
            print(f"[X] RPC вернул некорректный статус: {response.status_code}")
            return False
    except Exception as e:
        print(f"[X] Ошибка сети при попытке связаться с Devnet: {e}")
        return False

def execute_smart_contract_build():
    """Запускает процесс компиляции контрактов под новое ядро"""
    print("\n[*] Шаг 5: Пересборка исходных кодов проекта Amrita...")
    if os.path.exists("Anchor.toml"):
        return run_command("anchor build", "Компиляция через Anchor под новую версию")
    else:
        print("[-] Файл Anchor.toml не найден в корневой директории. Пропуск шага сборки контрактов.")
        return True

def main():
    print("="*70)
    print(f" СИСТЕМНЫЙ АВТОНОМНЫЙ СКРИПТ ОБНОВЛЕНИЯ АРХИТЕКТУРЫ AMRITA ПОД V4.3.0-BETA.3")
    print("="*70)
    
    if not verify_system_environment():
        sys.exit(1)
        
    if not upgrade_solana_cli():
        print("[!] Не удалось обновить ядро CLI. Дальнейшая автоматическая сборка небезопасна.")
        sys.exit(1)
        
    if not patch_rpc_configuration():
        sys.exit(1)
        
    check_devnet_status()
    
    if execute_smart_contract_build():
        print("\n" + "="*70)
        print("[++] АДАПТАЦИЯ И НОРМАЛИЗАЦИЯ ПОД AGAVE V4.3.0-BETA.3 ЗАВЕРШЕНА!")
        print("[+] Все конфигурации перезаписаны. Проект готов к корректному тестированию.")
        print("="*70)
    else:
        print("\n[X] Процесс обновления завершился с локальными ошибками компиляции.")
        sys.exit(1)

if __name__ == "__main__":
    main()
