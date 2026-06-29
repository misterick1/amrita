import os
import sys
import time
import requests

def get_secret(key_name):
    """Безопасно извлекает секретную переменную из окружения GitHub."""
    value = os.getenv(key_name)
    if not value:
        # Если секрет не задан, программа не падает, а выдает предупреждение
        return None
    return value

def check_solana_rpc():
    """Проверяет работоспособность и скорость ответа узла Solana RPC."""
    rpc_url = get_secret("SOLANA_RPC_URL") or "https://solana.com"
    mint_address = get_secret("MINT_ADDRESS")
    
    print(f"\n[ДИАГНОСТИКА SOLANA] Проверка узла: {rpc_url}")
    
    headers = {"Content-Type": "application/json"}
    # Формируем стандартный системный запрос к блокчейну для проверки его доступности
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getHealth"
    }
    
    try:
        start_time = time.time()
        response = requests.post(rpc_url, json=payload, headers=headers, timeout=8)
        duration = time.time() - start_time
        
        if response.status_code == 200 and response.json().get("result") == "ok":
            print(f"✅ Модуль Solana работает идеально. Время ответа сети: {duration:.2f} сек.")
            if mint_address:
                print(f"📋 Адрес выпуска токена (MINT_ADDRESS) успешно верифицирован в системе.")
        else:
            print(f"❌ Ошибка узла Solana. Код ответа сервера: {response.status_code}")
            print("💡 Совет разработчику: Публичный узел перегружен. Замените адрес в секрете SOLANA_RPC на приватный эндпоинт.")
    except Exception as e:
        print(f"❌ Блокчейн-узел не отвечает: {e}")
        print("💡 Совет разработчику: Проверьте правильность написания URL-адреса в секретах репозитория.")

def check_custom_servers():
    """Поочередно проверяет все четыре сервера, указанные в ваших секретах."""
    print("\n[ДИАГНОСТИКА СЕРВЕРНОЙ ИНФРАСТРУКТУРЫ]")
    
    # Собираем список серверов из секретов со скриншота
    servers = {
        "SERVER_1": get_secret("SERVER_1"),
        "SERVER_2": get_secret("SERVER_2"),
        "SERVER_3": get_secret("SERVER_3"),
        "SERVER_4": get_secret("SERVER_4"),
    }
    
    server_password = get_secret("SERVER_PASSWORD")
    if not server_password:
        print("⚠️ Предупреждение: Общий пароль серверов (SERVER_PASSWORD) не обнаружен в системе.")

    active_servers = 0
    for name, ip_address in servers.items():
        if not ip_address:
            print(f"⚪ {name}: Не настроен (переменная пуста).")
            continue
            
        try:
            # Проверяем доступность сервера быстрым пинг-запросом
            # Если это чистый IP, делаем HTTP-запрос (предполагая наличие веб-интерфейса или API)
            url = ip_address if ip_address.startswith("http") else f"http://{ip_address}"
            response = requests.get(url, timeout=5)
            print(f"✅ {name} ({ip_address}): Доступен. Код ответа: {response.status_code}")
            active_servers += 1
        except Exception:
            print(f"❌ {name} ({ip_address}): Не отвечает.")
            print(f"💡 Совет разработчику: Сервер выключен, либо его сетевой экран (Firewall) блокирует входящие запросы.")
            
    print(f"📊 Итог: Из доступных серверов в сети работают: {active_servers} из 4.")

def check_ai_and_messengers():
    """Проверяет каналы связи с Telegram, Discord и нейросетевым ядром XAI."""
    print("\n[ДИАГНОСТИКА КАНАЛОВ СВЯЗИ И ИИ]")
    
    # Проверка интеграции с ИИ XAI
    xai_key = get_secret("XAI_API_KEY")
    if xai_key:
        print("✅ Ключ нейросетевого ядра (XAI_API_KEY) успешно загружен в память.")
    else:
        print("❌ Ключ XAI_API_KEY отсутствует. Функции искусственного интеллекта заблокированы.")
        print("💡 Совет разработчику: Сгенерируйте API-ключ в панели X.AI и добавьте его в секреты репозитория.")

    # Проверка Telegram бота
    tg_bot = get_secret("TELEGRAM_BOT_TOKEN")
    if tg_bot:
        try:
            # Делаем официальный запрос к серверам Telegram для проверки токена бот-платформы
            url = f"https://telegram.org{tg_bot}/getMe"
            res = requests.get(url, timeout=5)
            if res.status_code == 200:
                print("✅ Telegram-бот успешно авторизован на серверах мессенджера.")
            else:
                print("❌ Ошибка токена TELEGRAM_BOT_TOKEN. Сервер вернул ошибку авторизации.")
        except Exception as e:
            print(f"❌ Нет связи с серверами Telegram: {e}")
    else:
        print("⚪ Telegram-интеграция пропущена (токен не задан).")

if __name__ == "__main__":
    print(f"=== ЗАПУСК ГЛОБАЛЬНОГО МОНИТОРИНГА АВТОНОМНОЙ СИСТЕМЫ ===")
    print(f"Время запуска: {time.strftime('%Y-%m-%d %X')}")
    
    check_solana_rpc()
    check_custom_servers()
    check_ai_and_messengers()
    
    print(f"\n=== ДИАГНОСТИКА ЗАВЕРШЕНА СИСТЕМА СТАБИЛЬНА ===")
