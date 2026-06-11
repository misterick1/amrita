import os
import logging
import httpx
from dotenv import load_dotenv

# Настройка логирования под общую стилистику квантового ядра AMRITA
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("HyperliquidClient")

load_dotenv()

HYPERLIQUID_API_URL = "https://hyperliquid.xyz"

async def get_hyperliquid_market_data():
    """
    Получение актуальных рыночных данных с Hyperliquid (Объемы, Открытый интерес).
    Интеграция миллиардных потоков ликвидности в ядро DeFAI.
    """
    logger.info("📊 Запрос аналитических данных с серверов Hyperliquid...")
    
    # Payload для получения общей статистики мета-данных рынка
    payload = {"type": "metaAndAssetCtxs"}
    headers = {"Content-Type": "application/json"}
    
    async with httpx.AsyncClient() as client:
        try:
            resp = await client.post(HYPERLIQUID_API_URL, json=payload, headers=headers)
            if resp.status_code == 200:
                data = resp.json()
                logger.info("📈 Данные о ликвидности Hyperliquid успешно получены.")
                # Возвращаем сырые данные для дальнейшего ИИ-анализа через Grok
                return str(data)[:1000] # Ограничиваем срез для контекста ИИ
            logger.warning(f"Не удалось получить данные Hyperliquid (Статус: {resp.status_code})")
            return "Данные Hyperliquid временно недоступны."
        except Exception as e:
            logger.error(f"Ошибка подключения к API Hyperliquid: {e}")
            return "Сбой сети при опросе Hyperliquid."

if __name__ == "__main__":
    import asyncio
    # Локальный тест модуля
    res = asyncio.run(get_hyperliquid_market_data())
    print("Срез данных:", res)
