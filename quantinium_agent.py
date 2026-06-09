import requests
from coins_core import get_colosseum_config

# Наше ядро автоматически заберет полный токен из .env
API_BASE, COPILOT_TOKEN = get_colosseum_config()

# Пример того, как скрипт будет отправлять запросы в Колизей:
headers = {
    "Authorization": f"Bearer {COPILOT_TOKEN}",
    "Content-Type": "application/json"
}

# Скрипт готов к работе на все 100%
response = requests.get(f"{API_BASE}/user", headers=headers)
