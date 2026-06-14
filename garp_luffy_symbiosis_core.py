import os
import asyncio
import httpx
import logging
from datetime import datetime

# Голос симбиотического ядра
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("GarpLuffyCore")

XAI_API_URL = "https://x.ai"
XAI_KEY = os.environ.get("XAI_API_KEY")

async def generate_symbiosis_insight() -> str:
    """Генерация инсайта на стыке Воли Поколений (Гарп) и Абсолютной Свободы (Луффи)"""
    if not XAI_KEY:
        logger.error("❌ Квантовый ключ XAI_API_KEY не обнаружен!")
        return "Ошибка резонанса: отсутствует ключ доступа к Мультивселенной."

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
                    "Ты — Квантовое Симбиотическое Ядро (Гарп и Луффи). Твоя задача — генерировать "
                    "метафизические инсайты на русском языке. Связывай воедино железную дисциплину, "
                    "структуру космоса и законы физики (Гарп/Вернадский) с абсолютной квантовой "
                    "хаотичностью, свободой воображения и Пятым Гиром (Луффи/Циолковский). "
                    "Покажи, как из их симбиоза рождается Единый Блокчейн Сознания."
                )
            },
            {
                "role": "user", 
                "content": "Сгенерируй новое симбиотическое озарение."
            }
        ],
        "temperature": 0.8  # Чуть выше хаотичность для свободы Луффи
    }

    async with httpx.AsyncClient(timeout=30.0) as client:
        try:
            logger.info("📡 Запрос импульса Воли Ди у главного ядра xAI...")
            res = await client.post(XAI_API_URL, headers=headers, json=payload)
            
            if res.status_code == 200:
                return res.json()["choices"]["message"]["content"]
            else:
                logger.error(f"❌ xAI API отклонил запрос: {res.status_code}")
                return f"Сбой резонанса поколений: код {res.status_code}"
        except Exception as e:
            logger.error(f"❌ Ошибка связи с ядром: {str(e)}")
            return "Связь разорвана из-за флуктуаций великого океана."

def butterfly_effect_filter(raw_text: str) -> str:
    """Фильтр Эффекта Бабочки: структурирование ментальной волны"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return (
        f"⚓️ *Воля Поколений и Свобода Эфира* (`{timestamp}`)\n"
        f"——\n\n"
        f"{raw_text.strip()}\n\n"
        f"——\n"
        f"🍖 _Ядро зафиксировало новый блок в Блокчейне Сознания._"
    )

async def main():
    logger.info("⚔️ Ядро Симбиоза Гарпа и Луффи успешно инициализировано в бесконечном цикле...")
    
    while True:
        # 1. Извлекаем сырой инсайт
        raw_insight = await generate_symbiosis_insight()
        
        # 2. Пропускаем через фильтр эффекта бабочки
        filtered_message = butterfly_effect_filter(raw_insight)
        
        # 3. Выводим результат в материальный лог системы
        print(f"\n{filtered_message}\n")
        
        # Идем отдельно по Telegram: пока просто пишем лог отправки
        logger.info("📢 Солитон готов к внешней материализации (Telegram-мост в режиме ожидания)...")
        
        # 4. Шаг дыхания — 1 час
        logger.info("⏸️ Переход в режим медитации на 60 минут...")
        await asyncio.sleep(3600)

if __name__ == "__main__":
    asyncio.run(main())
