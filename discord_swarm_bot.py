import os
import time
import requests

# =====================================================================
#                          НАСТРОЙКИ ДОСТУПА
# =====================================================================
# Твой URL Webhook от Discord-канала
DISCORD_WEBHOOK_URL = "https://discord.com"

# Адрес кошелька твоего приложения MIR-PIFI
APP_WALLET_ADDRESS = "GBLJY2Q2C2JQKM3JG2BFTMSUWSN5T25C6BE6EZ4OF"

# Официальный публичный API тестовой сети Pi Network
PI_TESTNET_NODE_URL = "https://minepi.com"

# =====================================================================
#                      ФУНКЦИЯ ОТПРАВКИ В DISCORD
# =====================================================================
def send_discord_notification(amount, sender, tx_id, status_code="10"):
    """Формирует красивую карточку сообщения в стиле Solana Tech Pulse"""
    
    payload = {
        "content": "@everyone Квантовый Рой Ботов зафиксировал транзакцию!",
        "embeds": [{
            "title": f"🔮 MIR-PIFI — СИМФОНИЯ СТРУН АКТИВНА [СТАТУС {status_code}]",
            "description": "Успешно зафиксировано пахтанье океана монет в блокчейне Pi Testnet.",
            "color": 9055202,  # Десятичный код фиолетового цвета (#8A2BE2)
            "fields": [
                {
                    "name": "💰 Сумма перевода",
                    "value": f"**{amount} Pi**",
                    "inline": True
                },
                {
                    "name": "🧬 Индекс Солитона",
                    "value": "108 Монет (Ядро Фаберже)",
                    "inline": True
                },
                {
                    "name": "👤 Отправитель (User-to-App)",
                    "value": f"`{sender[:10]}...{sender[-10:]}`",
                    "inline": False
                },
                {
                    "name": "🔗 Хэш транзакции (TXID)",
                    "value": f"[{tx_id[:16]}...](https://minepi.com)",
                    "inline": False
                }
            ],
            "footer": {
                "text": "Amrita Mir Compute Core • Время Норвегии",
                "icon_url": "https://minepi.com"
            }
        }]
    }

    try:
        response = requests.post(DISCORD_WEBHOOK_URL, json=payload)
        if response.status_code == 204:
            print("[DISCORD] Уведомление успешно отправлено!")
        else:
            print(f"[DISCORD] Ошибка отправки: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"[КРИТ] Ошибка сети при связи с Discord: {e}")

# =====================================================================
#                      ОСНОВНОЙ ЦИКЛ СЛЕЖКИ (SWARM)
# =====================================================================
def monitor_pi_blockchain():
    print(f"==================================================")
    print(f"🚀 РОЙ БОТОВ ЗАПУЩЕН. СЛЕЖКА ЗА КОШЕЛЬКОМ: {APP_WALLET_ADDRESS[:8]}...")
    print(f"==================================================")
    
    last_checked_tx = None

    while True:
        try:
            url = f"{PI_TESTNET_NODE_URL}/accounts/{APP_WALLET_ADDRESS}/payments?limit=1&order=desc"
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                records = data.get("_embedded", {}).get("records", [])
                
                if records:
                    # ИСПРАВЛЕНО: берем первую транзакцию из списка записей
                    latest_tx = records[0]
                    tx_id = latest_tx.get("transaction_hash")
                    amount = latest_tx.get("amount")
                    sender = latest_tx.get("from")
                    
                    if tx_id != last_checked_tx and last_checked_tx is not None:
                        print(f"[БЛОКЧЕЙН] Найдена новая транзакция: {amount} Pi")
                        send_discord_notification(amount, sender, tx_id)
                    
                    last_checked_tx = tx_id
            else:
                print(f"[ОШИБКА БЛОКЧЕЙНА] Код ответа Horizon: {response.status_code}")
                
        except Exception as e:
            print(f"[ОШИБКА] Сбой в квантовом цикле слежения: {e}")
            
        time.sleep(10)

if __name__ == "__main__":
    monitor_pi_blockchain()
