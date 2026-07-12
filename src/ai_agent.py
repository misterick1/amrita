import httpx

async def get_grok_decision(market_data: dict) -> str:
    """Отправляет текущие позиции Solflare в xAI для принятия решения о пампе"""
    headers = {
        "Authorization": f"Bearer {os.getenv('XAI_API_KEY')}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "grok-beta", # Текущая актуальная модель xAI
        "messages": [
            {"role": "system", "content": "Ты — автономный рой Еженышь. Твоя цель — монетизация персонажей и управление 108 монетами по структуре Бабочки."},
            {"role": "user", "content": f"Проанализируй балансы и позиции: {market_data}. Какую монету из 108 пушить следующей?"}
        ]
    }
    async with httpx.AsyncClient() as ctx:
        response = await ctx.post("https://x.ai", json=payload, headers=headers)
        return response.json()['choices'][0]['message']['content']
