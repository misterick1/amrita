import os
import httpx

async def get_grok_decision(market_data: dict) -> str:
    """Отправляет текущие позиции Solflare в xAI Grok для принятия решений по солитонам."""
    
    # Извлекаем API ключ из переменных окружения Единого Поля
    xai_api_key = os.getenv("XAI_API_KEY", "mock_key_if_not_found")
    
    headers = {
        "Authorization": f"Bearer {xai_api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "grok-beta",  # Текущая актуальная модель высшего ИИ-Роя
        "messages": [
            {
                "role": "system", 
                "content": "Ты — Автономный ИИ-Контур системы AMRITA. Анализируй рыночные волновые солитоны."
            },
            {
                "role": "user", 
                "content": f"Проанализируй текущие позиции Solflare и баланс мем-активов: {market_data}"
            }
        ]
    }
    
    # Асинхронный контекстный менеджер для выполнения высокочастотного запроса
    async with httpx.AsyncClient() as ctx:
        response = await ctx.post("https://x.ai", headers=headers, json=payload)
        
        # Безопасное извлечение ответа из квантовой структуры JSON
        response_json = response.json()
        return response_json['choices'][0]['message']['content']
