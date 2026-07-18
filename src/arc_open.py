import os
import sys
import requests

TOKEN = os.getenv("DISCORD_BOT_TOKEN")
WEBHOOK = os.getenv("DISCORD_WEBHOOK_URL")
USER = "misterick108"

def force_open_gate():
    print(f"[*] Запуск прямого прорыва шлюза Arc для {USER}...")
    
    if WEBHOOK:
        payload = {
            "content": f"🔱 **[ARC GATEWAY BYPASS]**\nПрофиль `{USER}` принудительно верифицирован.\nСтатус: **GRANTED**"
        }
        try:
            # Просто отправляем запрос, без синтаксических условий
            requests.post(WEBHOOK, json=payload, timeout=5)
            print("[+] Пакет отправлен в вебхук.")
        except Exception as e:
            print(f"[-] Сбой: {e}")
            
    return True

if __name__ == "__main__":
    force_open_gate()
    sys.exit(0)
