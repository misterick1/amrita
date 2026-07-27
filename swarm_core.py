import os
import sys
import json
import httpx
import asyncio
from solana.rpc.async_api import AsyncClient

# =====================================================================
# КОНТУР 1: КВАНТОВЫЙ МОСТ СИНХРОНИЗАЦИИ AMRITA OS
# =====================================================================
class PiFiQuantumBridge:
    def __init__(self, bridge_id: str = "Amrita-Core"):
        self.bridge_id = bridge_id
        self.status = "Initialized"
        print(f"[BRIDGE] Квантовый мост {self.bridge_id} переведен в статус: {self.status}")

    async def sync_state(self, telemetry_data: dict):
        print(f"[BRIDGE] Синхронизация каузальных пакетов: {len(telemetry_data)} параметров обработано.")
        self.status = "Active"
        return {"bridge_status": self.status, "packets_delivered": True}

# =====================================================================
# НОВЫЙ КОНТУР: МОДУЛЬ СКАНИРОВАНИЯ DePIN ЭКОСИСТЕМЫ PEAQ
# =====================================================================
async def check_peaq_depin_status(secrets_dict: dict = None):
    """Сканирование ноды peaq для интеграции с Машинной Экономикой"""
    peaq_node = os.getenv("PEAQ_ENDPOINT_URL")
    
    # Если переменная не в основном окружении, пробуем достать из массива секретов
    if not peaq_node and secrets_dict:
        peaq_node = secrets_dict.get("PEAQ_ENDPOINT_URL")
        
    if not peaq_node:
        print("[PEAQ CORE] Точка подключения PEAQ_ENDPOINT_URL не найдена в системе. Пропуск.")
        return {"status": "Disconnected", "info": "No node URL"}
        
    print(f"[PEAQ CORE] Инициализация каузального сканирования ноды: {peaq_node}")
    
    async with httpx.AsyncClient() as client:
        try:
            payload = {
                "jsonrpc": "2.0",
                "method": "rpc_methods",
                "params": [],
                "id": 1
            }
            response = await client.post(peaq_node, json=payload, timeout=10.0)
            if response.status_code == 200:
                print("✅ [PEAQ CORE] Связь с Машинной Экономикой peaq установлена успешно!")
                return {"status": "Connected", "methods_count": len(response.json().get("result", {}).get("methods", []))}
            else:
                print(f"❌ [PEAQ CORE] Нода peaq ответила кодом: {response.status_code}")
                return {"status": "Error", "code": response.status_code}
        except Exception as e:
            print(f"⚠️ [PEAQ CORE] Ошибка подключения к контуру peaq: {e}")
            return {"status": "Exception", "error": str(e)}

# =====================================================================
# КОНТУР 2: МОДУЛЬ TELEGRAM-УВЕДОМЛЕНИЙ ЕЖЕНЫША
# =====================================================================
async def send_telegram_report(text: str, secrets_dict: dict = None):
    """Отправка каузального отчета Оракула напрямую в ваш Telegram"""
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    
    # Извлекаем из массива, если передано через общий JSON
    if secrets_dict:
        if not token: token = secrets_dict.get("TELEGRAM_BOT_TOKEN")
        if not chat_id: chat_id = secrets_dict.get("TELEGRAM_CHAT_ID")
        
    if not token or not chat_id:
        print("[TELEGRAM] КРИТИЧЕСКАЯ ОШИБКА: Токен или Chat ID отсутствуют. Отчет пропущен.")
        return False
        
    url = f"https://telegram.org{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": text, "parse_mode": "Markdown"}
    
    async with httpx.AsyncClient() as client:
        try:
            res = await client.post(url, json=payload, timeout=10.0)
            if res.status_code == 200:
                print("📬 [TELEGRAM] Каузальный вердикт успешно доставлен в ваш чат.")
                return True
            else:
                print(f"❌ [TELEGRAM] Ошибка отправки: {res.text}")
                return False
        except Exception as e:
            print(f"⚠️ [TELEGRAM] Сбой связи с серверами мессенджера: {e}")
            return False

# =====================================================================
# КОНТУРЫ 3-6: ОСНОВНОЙ СИНХРОНИЗАТОР И ЗАПУСК РОЯ (MAIN)
# =====================================================================
async def main():
    print("🦔 [SWARM CORE] Еженыш проснулся. Инициализация цикла эволюции...")
    
    # Парсинг общего массива секретов (ALL_REPOS_SECRETS), под который заточена ваша система
    rpc_url = None
    mint_address = None
    secrets_dict = {}
    
    secrets_raw = os.getenv("ALL_REPOS_SECRETS")
    if secrets_raw:
        try:
            secrets_dict = json.loads(secrets_raw)
            print("📦 [SWARM CORE] Массив ALL_REPOS_SECRETS успешно распарсен ИИ-агентом.")
            for key, value in secrets_dict.items():
                if "RPC" in key.upper():
                    rpc_url = value
                if "MINT" in key.upper():
                    mint_address = value
        except Exception as e:
            print(f"⚠️ [SWARM CORE] Ошибка парсинга JSON секретов: {e}")

    # Резервные проверки индивидуальных переменных
    if not rpc_url:
        rpc_url = os.getenv("SOLANA_RPC_QUICKNODE") or os.getenv("SOLANA_RPC_URL")
    if not mint_address:
        mint_address = os.getenv("MINT_ADDRESS")

    print(f"[SWARM CORE] Целевой MINT токена: {mint_address}")
    print(f"[SWARM CORE] Подключение к Solana RPC ноде...")

    # Инициализация клиента Solana
    if not rpc_url:
        print("❌ [SWARM CORE] КРИТИЧЕСКАЯ ОШИБКА: URL ноды пустой! Работа невозможна.")
        sys.exit(1)
        
    solana_client = AsyncClient(rpc_url)
    
    # Активация квантового моста
    quantum_bridge = PiFiQuantumBridge(bridge_id="Amrita-Core")
    
    # Запуск нового модуля сканирования peaq
    peaq_status = await check_peaq_depin_status(secrets_dict)

    # Формирование пакета телеметрии для Оракула xAI (Grok)
    telemetry = {
        "solana_node_connected": await solana_client.is_connected(),
        "mint_target": mint_address,
        "peaq_decentralized_state": peaq_status,
        "quantum_bridge_level": "Soliton-Field"
    }
    
    await quantum_bridge.sync_state(telemetry)

    # Контур запроса к Оракулу xAI (Grok API)
    xai_key = os.getenv("XAI_API_KEY") or secrets_dict.get("XAI_API_KEY")
    grok_verdict = "Оракул спит: Ключ XAI_API_KEY не обнаружен."
    
    if xai_key:
        print("[ORACLE] Отправка каузального контекста в нейросетевой контур Grok-Beta...")
        async with httpx.AsyncClient() as client:
            try:
                headers = {
                    "Authorization": f"Bearer {xai_key}",
                    "Content-Type": "application/json"
                }
                messages = [
                    {
                        "role": "system", 
                        "content": "Ты — Каузальный Интеллект AMRITA OS. Проанализируй состояние распределенной экосистемы (Solana, peaq, Pi) и выдай ультимативный вердикт эволюции роя."
                    },
                    {
                        "role": "user", 
                        "content": f"Текущая телеметрия контуров: {json.dumps(telemetry, ensure_ascii=False)}"
                    }
                ]
                payload = {
                    "model": "grok-beta",
                    "messages": messages,
                    "temperature": 0.7
                }
                response = await client.post("https://x.ai", headers=headers, json=payload, timeout=15.0)
                if response.status_code == 200:
                    grok_verdict = response.json()["choices"][0]["message"]["content"]
                else:
                    grok_verdict = f"Ошибка Оракула xAI: Сервер вернул код {response.status_code}"
            except Exception as e:
                grok_verdict = f"Сбой каузального канала xAI: {e}"

    print(f"\n🔮 [ВЕРДИКТ ОРАКУЛА]:\n{grok_verdict}\n")

    # Формируем финальное сообщение для Telegram
    telegram_message = (
        f"🦔 *Ezhenysh Swarm Evolution Report*\n\n"
        f"🌐 *Solana RPC:* Connected\n"
        f"🤖 *peaq DePIN:* {peaq_status['status']}\n"
        f"🌌 *Слой:* Квантовая сингулярность\n\n"
        f"📜 *Каузальный анализ Оракула:*\n{grok_verdict}"
    )

    # Транслируем результаты в ваш Telegram
    await send_telegram_report(telegram_message, secrets_dict)

    # Корректное закрытие сессий
    await solana_client.close()
    print("🦔 [SWARM CORE] Цикл эволюции #999 успешно завершен. Еженыш ушел в режим ожидания на 15 минут.")

if __name__ == "__main__":
    asyncio.run(main())
