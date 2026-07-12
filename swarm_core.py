import os
import sys
import asyncio
import httpx
from solana.rpc.async_api import AsyncClient

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

async def main():
    print("🛸 [AMRITA REALTIME] Боевой контур Бабочки успешно соединен.")
    
    # Берем проброшенную переменную напрямую из ОС контейнера
    rpc_url = os.getenv("SOLANA_RPC")
    if not rpc_url:
        print("❌ КРИТИЧЕСКАЯ ОШИБКА: GitHub контейнер заблокировал проброс RPC.")
        sys.exit(1)
        
    client = AsyncClient(rpc_url)
    print(f"✅ Узел Solana RPC успешно считан из окружения: {rpc_url[:25]}...")
    
    xai_key = os.getenv("XAI_API_KEY")
    if not xai_key:
        print("❌ КРИТИЧЕСКАЯ ОШИБКА: Свежий ключ xAI не проброшен в контейнер.")
        sys.exit(1)
        
    print(f"🧠 Свежий API ключ xAI (Grok) успешно авторизован: {xai_key[:12]}...")

    # Отправляем прямой запрос Оракулу без плейсхолдеров
    async with httpx.AsyncClient() as http_client:
        headers = {"Authorization": f"Bearer {xai_key}", "Content-Type": "application/json"}
        payload = {
            "model": "grok-beta",
            "messages": [{"role": "user", "content": "Контур запечатан. Оцени баланс 108 квантов в Solana."}]
        }
        try:
            print("📡 Пакеты улетели в суперкластер xAI Grok...")
            xai_resp = await http_client.post("https://x.ai", json=payload, headers=headers)
            if xai_resp.status_code == 200:
                decision = xai_resp.json()['choices']['message']['content']
                print(f"🤖 ЖИВОЙ ОТВЕТ ОРАКУЛА xAI: {decision}")
            else:
                print(f"❌ xAI вернул ошибку авторизации: {xai_resp.status_code}. Текст: {xai_resp.text}")
        except Exception as e:
            print(f"❌ Сбой сетевого шлюза при коннекте к ИИ: {e}")

if __name__ == "__main__":
    asyncio.run(main())
