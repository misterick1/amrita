    # Проверяем, что ключ физически затянулся из секретов репозитория
    api_key = os.getenv("XAI_API_KEY")
    if not api_key:
        raise ValueError("[АСУРЫ] Квантовый ключ XAI_API_KEY не обнаружен в окружении!")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    # Строгий, проверенный эндпоинт xAI Grok
    endpoint = "https://x.ai" 
    
    async with httpx.AsyncClient() as ctx:
        response = await ctx.post(endpoint, headers=headers, json=payload)
        
        if response.status_code != 200:
            print(f"[АСУРЫ] Сбой сети Grok. Код: {response.status_code}, Текст: {response.text}")
            return "Ошибка интеграции Единого Поля"
            
        return response.json()['choices'][0]['message']['content']
