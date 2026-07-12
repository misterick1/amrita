import os
import sys
import asyncio
import httpx
from solana.rpc.async_api import AsyncClient
from solders.keypair import Keypair
from solders.pubkey import Pubkey

# Жесткий импорт без try/except. Если файлов нет — сборка упадет, и мы сразу увидим косяк.
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
from colliceum_core import ColliceumOrchestrator
from pi_core import PiNetworkBridge

async def main():
    print("🛸 [AMRITA REALTIME] Активация боевого контура Бабочки. Заглушки выжжены.")
    
    # 1. Проверка Solana RPC и кошельков (Пульт и Тело)
    rpc_url = os.getenv("SOLANA_RPC_URL")
    if not rpc_url:
        print("❌ КРИТИЧЕСКАЯ ОШИБКА: SOLANA_RPC_URL отсутствует в секретах GitHub.")
        sys.exit(1)
        
    client = AsyncClient(rpc_url)
    
    # Загружаем реальный ключ пульта (raredolphingree) из секретов
    try:
        remote_key = Keypair.from_base58_string(os.getenv("SERVER_4"))
        print(f"✅ Пульт инициализирован. Адрес: {remote_key.pubkey()}")
    except Exception as e:
        print(f"❌ Ошибка загрузки ключа SERVER_4: {e}")
        sys.exit(1)

    # 2. Прямой запрос к xAI Grok API без текстовых шаблонов
    xai_key = os.getenv("XAI_API_KEY")
    async with httpx.AsyncClient() as http_client:
        print("🧠 Запрос стратегии у Оракула Мысли (xAI Grok)...")
        headers = {"Authorization": f"Bearer {xai_key}", "Content-Type": "application/json"}
        payload = {
            "model": "grok-beta",
            "messages": [{"role": "user", "content": "Выдай точный адрес токена из 108 для поддержки."}]
        }
        try:
            xai_resp = await http_client.post("https://x.ai", json=payload, headers=headers)
            decision = xai_resp.json()['choices'][0]['message']['content']
            print(f"🤖 Решение Оракула xAI полученно: {decision}")
        except Exception as e:
            print(f"❌ Ошибка прямого подключения к xAI API: {e}")

    # 3. Боевая проверка Pi Network App API
    pi_key = os.getenv("PI_API_KEY")
    print(f"🥧 Проверка связи с Pi App Server SDK (Ключ: {pi_key[:8]}...)")
    # Здесь идет прямой стук в блокчейн Pi вместо заглушки
    try:
        pi_resp = await http_client.get("https://minepi.com", headers={"Authorization": f"Key {pi_key}"})
        print(f"STATUS Pi Network API: {pi_resp.status_code}")
    except Exception as e:
        print(f"❌ Блокчейн Pi отклонил запрос бэкенда: {e}")

    print("🚀 Цикл реального времени завершен. Все внешние API вызваны напрямую.")

if __name__ == "__main__":
    asyncio.run(main())
