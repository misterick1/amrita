import os
import sys
import time
import requests

# Конфигурация серверов и каналов связи для проверки
SERVERS = {
    "Solana Mainnet RPC": "https://api.mainnet-beta.solana.com",
    "Telegram Gateway": "https://telegram.org",
    "Pi Network Developer Portal": "https://minepi.com"
}

# Ссылка на ваш чистый исходный код для самообновления (вставьте ссылку на raw-файл)
GITHUB_RAW_URL = "https://githubusercontent.com"

def check_connections():
    """Проверяет доступность узлов и дает понятные подсказки для саморазвития."""
    print(f"\n--- [ЗАПУСК ДИАГНОСТИКИ СВЯЗИ: {time.strftime('%X')}] ---")
    
    for name, url in SERVERS.items():
        try:
            # Отправляем быстрый тестовый запрос с ограничением ожидания в 5 секунд
            response = requests.get(url, timeout=5)
            
            if response.status_code == 200:
                print(f"[УСПЕШНО] {name} работает исправно. (Код 200: Сервер ответил корректно).")
            else:
                print(f"[ВНИМАНИЕ] {name} вернул статус-код {response.status_code}.")
                give_learning_tip(name, response.status_code)
                
        except requests.exceptions.Timeout:
            print(f"[ОШИБКА] {name} не ответил вовремя (Таймаут).")
            print("👉 Подсказка: Сервер перегружен или блокирует ваш IP-адрес за частые запросы.")
            print("💡 Что изучить: Изучите тему 'Прокси-серверы и ротация IP-адресов', чтобы обходить защиту.")
            
        except requests.exceptions.ConnectionError:
            print(f"[ОШИБКА] Нет физического доступа к серверу {name}.")
            print("👉 Подсказка: Либо у вас отключился интернет, либо адрес сервера заблокирован провайдером.")
            print("💡 Что изучить: Проверьте утилиту трассировки маршрута `traceroute` (или `tracert` в Windows).")

def give_learning_tip(server_name, status_code):
    """Выдает образовательные рекомендации на основе кодов ошибок."""
    if status_code == 401 or status_code == 403:
        print("👉 Причина: Отказано в доступе. Сбросились или устарели ключи авторизации.")
        print("💡 Что изучить: Почитайте про 'OAuth 2.0' и 'Безопасное хранение токенов в файлах .env'.")
    elif status_code == 429:
        print("👉 Причина: Слишком много запросов. Сервер временно заблокировал вас за спам.")
        print("💡 Что изучить: Изучите алгоритм 'Rate Limiting' (ограничение частоты) и задержки `time.sleep()`.")

def auto_update():
    """Проверяет обновления на GitHub, скачивает новую версию и перезапускает скрипт."""
    print("[ОБНОВЛЕНИЕ] Проверка наличия новой версии кода на GitHub...")
    try:
        response = requests.get(GITHUB_RAW_URL, timeout=5)
        if response.status_code == 200:
            current_script_path = os.path.abspath(sys.argv[0])
            
            with open(current_script_path, 'r', encoding='utf-8') as f:
                local_code = f.read()
            
            # Если код на удаленном сервере отличается от локального — обновляем
            if response.text != local_code:
                print("[ОБНОВЛЕНИЕ] Обнаружена новая архитектура кода! Скачивание обновлений...")
                with open(current_script_path, 'w', encoding='utf-8') as f:
                    f.write(response.text)
                print("[ОБНОВЛЕНИЕ] Код успешно перезаписан. Перезапуск программы...")
                
                # Команда на самоперезапуск текущего процесса
                os.execv(sys.executable, [sys.executable] + sys.argv)
            else:
                print("[СТАТУС] У вас установлена самая актуальная версия системы.")
    except Exception as e:
        print(f"[ОШИБКА ОБНОВЛЕНИЯ] Не удалось связаться с репозиторием: {e}")

if __name__ == "__main__":
    # Сначала проверяем и подтягиваем обновления
    auto_update()
    
    # Запускаем бесконечный цикл мониторинга
    while True:
        check_connections()
        print("\nСледующая проверка через 60 секунд. Для выхода нажмите Ctrl+C...")
        time.sleep(60)
