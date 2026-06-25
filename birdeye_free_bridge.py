import asyncio
import aiohttp
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("AMRITA-BIRDEYE-FREE")

class BirdeyeFreeBridge:
    def __init__(self, mint_address: str):
        self.mint = mint_address
        # Используем публичные эндпоинты фронтенда Birdeye, им НЕ нужен API-ключ
        self.base_url = f"https://birdeye.so{self.mint}"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Accept": "application/json",
            "x-chain": "solana"
        }

    async def fetch_token_analytics(self):
        """Получение аналитики токена без платного токена авторизации"""
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(self.base_url, headers=self.headers) as resp:
                    if resp.status == 200:
                        data = await resp.json()
                        logger.info("📊 Данные Birdeye успешно получены в обход авторизации!")
                        return data
                    elif resp.status == 401:
                        # Если совсем заблокировали, переключаемся на бесплатный зеркальный API DexScreener
                        backup_url = f"https://dexscreener.com{self.mint}"
                        async with session.get(backup_url) as b_resp:
                            return await b_resp.json()
            except Exception as e:
                logger.error(f"Ошибка каузального моста: {e}")
                return None

if __name__ == "__main__":
    # Тест на вашем QNT токене
    bridge = BirdeyeFreeBridge("EPjFW33V15rFU38v9U75g6V6zWM72e1q8vmkhv24Wc6")
    data = asyncio.run(bridge.fetch_token_analytics())
    print(data)
