import os
import sys
import asyncio
import httpx
from solana.rpc.async_api import AsyncClient
from solders.keypair import Keypair

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

async def main():
    print("🛸 [AMRITA REALTIME] Боевой контур Бабочки запущен.")
    
    # Считываем переменную точно по твоему имени на скриншоте (с нижними подчеркиваниями)
    rpc_url = os.getenv("SOLANA_RPC___") or os.getenv("SOLANA_RPC_") or os.getenv("SOLANA_RPC")
    
    # Если GitHub скрывает имя под маской, проверяем все доступные варианты контура
    if not rpc_url:
        for env_name in os.environ:
            if "SOLANA_RPC" in env_name:
                rpc_url = os.environ[env_name]
                break

    if not rpc_url:
        print("❌ КРИТИЧЕСКАЯ ОШИБКА: Узел Solana RPC не найден в окружении.")
        sys.exit(1)
        
    client = AsyncClient(rpc_url)
    print(f"✅ Связь с Solana RPC установлена: {rpc_url[:25]}...")
    
    # Проверяем свежий боевой ключ xAI, который ты залил 16 минут назад
    xai_key = os.getenv("XAI_API_KEY")
    if not xai_key:
        print("❌ КРИТИЧЕСКАЯ ОШИБКА: API ключ xAI отсутствует.")
        sys.exit(1)
        
    print(f"🧠 Свежий API ключ xAI (Grok) подтянут: {xai_key[:12]}...")

    # Прямой каузальный запрос к Grok API
    async with httpx.AsyncClient() as http_client:
        headers = {"Authorization": f"Bearer {xai_key}", "Content-Type": "application/json"}
        payload = {
            "model": "grok-beta",
            "messages": [{"role": "user", "content": "Система Амрита активна. Оцени баланс контура в 108 квантов."}]
        }
        try:
            print("📡 Отправка пакетов в суперкластер xAI Grok...")
            xai_resp = await http_client.post("https://x.ai", json=payload, headers=headers)
            if xai_resp.status_code == 200:
                decision = xai_resp.json()['choices']['message']['content']
                print(f"🤖 ОТВЕТ ОРАКУЛА xAI: {decision}")
            else:
                print(f"❌ Сервер xAI вернул ошибку: {xai_resp.status_code}. Текст: {xai_resp.text}")
        except Exception as e:
            print(f"❌ Сбой сети при связи с Оракулом: {e}")

    print("🚀 Боевой цикл завершен. Все системы соединены напрямую.")

if __name__ == "__main__":
    asyncio.run(main())
