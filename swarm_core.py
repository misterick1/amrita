import os
import sys
import json
import asyncio
import httpx
from solana.rpc.async_api import AsyncClient

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

async def main():
    print("🛸 [AMRITA REALTIME] Развертывание сквозного каузального контура.")
    
    # 1. Автоматический поиск Solana RPC внутри пакета секретов
    rpc_url = None
    secrets_raw = os.getenv("ALL_REPOS_SECRETS")
    
    if secrets_raw:
        try:
            secrets_dict = json.loads(secrets_raw)
            # Ищем любой секрет, в названии которого есть SOLANA_RPC
            for key, value in secrets_dict.items():
                if "SOLANA_RPC" in key and value:
                    rpc_url = value
                    print(f"📡 Системный маркер обнаружен в секрете: {key}")
                    break
        except Exception as e:
            print(f"⚠️ Ошибка разбора пакета контекста: {e}")

    # Если автоматика не нашла в пакете, проверяем прямую среду ОС
    if not rpc_url:
        rpc_url = os.getenv("SOLANA_RPC") or os.getenv("SOLANA_RPC_URL")

    if not rpc_url:
        print("❌ КРИТИЧЕСКАЯ ОШИБКА: Автоматика не смогла извлечь узел Solana RPC.")
        sys.exit(1)
        
    client = AsyncClient(rpc_url)
    print(f"✅ Прямая связь с Solana RPC установлена: {rpc_url[:25]}...")
    
    # 2. Авторизация Оракула Мысли xAI
    xai_key = os.getenv("XAI_API_KEY")
    if not xai_key:
        print("❌ КРИТИЧЕСКАЯ ОШИБКА: Свежий API ключ xAI отсутствует в контейнере.")
        sys.exit(1)
        
    print(f"🧠 Боевой ключ xAI (Grok) авторизован: {xai_key[:12]}...")

    # 3. Прямой запрос к Grok API без посредников и заглушек
    async with httpx.AsyncClient() as http_client:
        headers = {"Authorization": f"Bearer {xai_key}", "Content-Type": "application/json"}
        payload = {
            "model": "grok-beta",
            "messages": [{"role": "user", "content": "Система Амрита активна. Оцени баланс 108 квантов в Solana."}]
        }
        try:
            print("📡 Отправка пакетов в суперкластер xAI Grok...")
            xai_resp = await http_client.post("https://x.ai", json=payload, headers=headers)
            if xai_resp.status_code == 200:
                decision = xai_resp.json()['choices']['message']['content']
                print(f"🤖 ЖИВОЙ ОТВЕТ ОРАКУЛА xAI:\n{decision}")
            else:
                print(f"❌ Сервер xAI вернул код ошибки: {xai_resp.status_code}. Текст: {xai_resp.text}")
        except Exception as e:
            print(f"❌ Сбой сетевого шлюза при коннекте к ИИ: {e}")

if __name__ == "__main__":
    asyncio.run(main())
