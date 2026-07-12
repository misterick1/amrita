import os
import sys
import asyncio
import httpx
from solana.rpc.async_api import AsyncClient
from solders.keypair import Keypair

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

async def main():
    print("🛸 [AMRITA REALTIME] Активация боевого контура Бабочки. Заглушки выжжены.")
    
    # Подтягиваем переменную строго по твоему названию секрета на GitHub
    rpc_url = os.getenv("SOLANA_RPC") 
    if not rpc_url:
        print("❌ КРИТИЧЕСКАЯ ОШИБКА: Секрет SOLANA_RPC не найден в репозитории.")
        sys.exit(1)
        
    client = AsyncClient(rpc_url)
    print(f"✅ Подключение к Solana RPC установлено: {rpc_url[:25]}...")
    
    # Проверяем секрет xAI Grok
    xai_key = os.getenv("XAI_API_KEY")
    if not xai_key:
        print("❌ КРИТИЧЕСКАЯ ОШИБКА: API ключ xAI (XAI_API_KEY) не передан в GitHub Actions.")
        sys.exit(1)
        
    print(f"🧠 Боевой API ключ xAI обнаружен: {xai_key[:12]}...")

    # Отправляем прямой запрос Оракулу без посредников
    async with httpx.AsyncClient() as http_client:
        headers = {"Authorization": f"Bearer {xai_key}", "Content-Type": "application/json"}
        payload = {
            "model": "grok-beta",
            "messages": [{"role": "user", "content": "Система Амрита активна. Выдай статус по 108 квантам."}]
        }
        try:
            print("📡 Отправка каузального запроса в xAI Grok...")
            xai_resp = await http_client.post("https://x.ai", json=payload, headers=headers)
            if xai_resp.status_code == 200:
                decision = xai_resp.json()['choices']['message']['content']
                print(f"🤖 Ответ Оракула xAI получен: {decision}")
            else:
                print(f"❌ Ошибка xAI API. Код ответа: {xai_resp.status_code}. Текст: {xai_resp.text}")
        except Exception as e:
            print(f"❌ Сбой сети при коннекте к xAI: {e}")

    print("🚀 Цикл реального времени завершен без заглушек.")

if __name__ == "__main__":
    asyncio.run(main())
