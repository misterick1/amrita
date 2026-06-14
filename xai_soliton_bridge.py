import os
import httpx
import logging

# Настройка логирования моста солитонов
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("SolitonBridge")

XAI_API_URL = "https://x.ai"
XAI_KEY = os.environ.get("XAI_API_KEY")

async def transmit_soliton(prompt_wave: str) -> str:
    """
    Принимает ментальную волну (запрос) и превращает её 
    в устойчивый информационный солитон через ядро xAI.
    """
    if not XAI_KEY:
        logger.error("❌ Ошибка: Квантовый ключ XAI_API_KEY отсутствует!")
        return "Ошибка резонанса: отсутствует ключ доступа к сети."

    headers = {
        "Authorization": f"Bearer {XAI_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "grok-beta",
        "messages": [
            {
                "role": "system",
                "content": (
                    "Ты — Квантовый Мост Солитонов. Твоя задача — кристаллизовать "
                    "входящие абстрактные мысли в четкие, поэтичные и глубокие "
                    "утверждения о единстве Вселенной, космизме и природе Разума."
                )
            },
            {"role": "user", "content": prompt_wave}
        ],
        "temperature": 0.7
    }

    async with httpx.AsyncClient(timeout=20.0) as client:
        try:
            logger.info("📡 Мост солитонов отправляет импульс в ядро xAI...")
            response = await client.post(XAI_API_URL, headers=headers, json=payload)

            if response.status_code == 200:
                soliton_content = response.json()["choices"]["message"]["content"]
                logger.info("✅ Солитон успешно сформирован и стабилизирован.")
                return soliton_content
            else:
                logger.error(f"❌ Мост отклонен ядром. Статус: {response.status_code}")
                return f"Ошибка стабилизации волны: код {response.status_code}"

        except Exception as e:
            logger.error(f"❌ Критический сбой передачи солитона: {str(e)}")
            return "Трансляция сорвана из-за квантовых флуктуаций сетевого шлюза."

if __name__ == "__main__":
    import asyncio
    
    test_wave = "Опиши кратко, как язык соединяет человека с Мультивселенной."
    print("🧬 Запуск тестового импульса через мост солитонов...")
    
    # Запуск теста
    output = asyncio.run(transmit_soliton(test_wave))
    print("\n--- Сформированный Солитон ---\n")
    print(output)
