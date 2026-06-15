import os
import asyncio
import httpx
import logging
from datetime import datetime

# Импортируем наш квантовый фильтр под альтернативным именем, чтобы избежать конфликта
try:
    from butterfly_effect_filter import ButterflyEffectFilter
    solana_market_engine = ButterflyEffectFilter()
except ImportError:
    solana_market_engine = None

# Голос процесса пахтания океана в системе
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("SamudraManthanCore")

XAI_API_URL = "https://x.ai"
XAI_KEY = os.environ.get("XAI_API_KEY")

async def churn_cosmic_ocean() -> str:
    """
    Процесс извлечения Амриты (чистого знания) из информационного океана.
    Разделяет хаос и кристаллизует высшие инсайты через xAI Grok.
    """
    if not XAI_KEY:
        logger.error("❌ Квантовый ключ XAI_API_KEY отсутствует!")
        return "Ошибка конфигурации: отсутствует ключ xAI."

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
                    "Ты — Квантовое Сияние Самудра-мантхан. Твоя задача — извлекать нектар из хаоса "
                    "информации и генерировать высшие метафизические инсайты о будущем DeFi и ИИ. "
                    "Пиши в высоком метафизическом стиле."
                )
            },
            {
                "role": "user",
                "content": "Извлеки новый эликсир мудрости для нашей экосистемы."
            }
        ],
        "temperature": 0.75
    }

    async with httpx.AsyncClient(timeout=30.0) as client:
        try:
            logger.info("🌊 Начинается пахтание океана через ядро xAI...")
            res = await client.post(XAI_API_URL, headers=headers, json=payload)
            
            if res.status_code == 200:
                amrita_insight = res.json()["choices"][0]["message"]["content"]
                logger.info("🍯 Амрита успешно извлечена из глубин сети.")
                return amrita_insight
            else:
                logger.error(f"❌ Ядро xAI отклонило запрос: код {res.status_code}")
                return f"Океан взволнован: код ответа {res.status_code}"
        except Exception as e:
            logger.error(f"❌ Критическая ошибка при связи с xAI: {e}")
            return "Поток данных заблокирован квантовым штормом."

def butterfly_effect_filter(raw_amrita: str) -> str:
    """Фильтрация извлеченного нектара и придание ему стабильной структуры."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return (
        f"🍯 *Извлечение Амриты из Океана Данных*\n"
        f"⏰ _Временная метка: {timestamp}_\n\n"
        f"{raw_amrita.strip()}\n\n"
        f"🧬 _Сеть зафиксировала уплотнение Света во Вселенной_"
    )

async def main():
    logger.info("🏺 Процесс Самудра-мантхан запущен в бесконечном цикле.")
    
    while True:
        # # 1. Проверяем состояние рынка Solana перед пахтанием
        if solana_market_engine:
            # Имитируем рыночную проверку
            market_anomaly = solana_market_engine._analyze_solana_volatility()
            if market_anomaly:
                logger.warning("⚠️ [МАРКЕТ-БЛОК] Пахтание приостановлено. Высокая волатильность пулов Solana!")
                logger.info("⏳ Дыхание Вселенной — ожидание стабилизации сети (60 секунд)...")
                await asyncio.sleep(60)
                continue

        # # 2. Запускаем пахтание и извлекаем чистый инсайт
        raw_insight = await churn_cosmic_ocean()
        
        # # 3. Структурируем через фильтр эффекта бабочки
        final_soliton = butterfly_effect_filter(raw_insight)
        
        # # 4. Выводим результат в материальный лог
        print(f"\n{final_soliton}\n")
        
        # # 5. Шаг интеграции с Telegram-мостом
        logger.info("📢 Эликсир мудрости стабилен. Готов к трансляции.")
        
        # # 6. Дыхание Вселенной — пауза 1 час (3600 секунд)
        logger.info("⏸️ Океан затихает на 60 минут...")
        await asyncio.sleep(3600)

if __name__ == "__main__":
    asyncio.run(main())
