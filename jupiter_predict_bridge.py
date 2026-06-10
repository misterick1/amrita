import os
import logging
import httpx
from dotenv import load_dotenv

# Логирование под "Единый Квантовый Оркестратор"
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - [%(filename)s] - %(message)s")
logger = logging.getLogger("JupiterPredictBridge")

load_dotenv()

JUPITER_QUOTE_URL = "https://jup.ag"
JUPITER_PRICE_URL = "https://jup.ag"

async def check_token_market_data(mint_address: str) -> dict | None:
    """
    Запрашивает текущую цену и ликвидность токена на Solana через Jupiter API.
    Используется для первичной фильтрации токенов, пришедших из Pump.fun.
    """
    logger.info(f"Аналайзер: Проверка рыночных данных для токена {mint_address}")
    
    async with httpx.AsyncClient() as client:
        try:
            # 1. Запрашиваем цену токена относительно USDC
            price_params = {"ids": mint_address}
            price_response = await client.get(JUPITER_PRICE_URL, params=price_params, timeout=5.0)
            
            price_data = {}
            if price_response.status_code == 200:
                res_json = price_response.json()
                price_data = res_json.get("data", {}).get(mint_address, {})
                logger.info(f"Jupiter Price для {mint_address}: {price_data.get('price', 'Цена не сформирована')}")
            
            # 2. Проверяем симуляцию маршрута обмена (свопа) на 1 SOL для оценки ликвидности (Slippage)
            # SOL Mint: So11111111111111111111111111111111111111112
            quote_params = {
                "inputMint": "So11111111111111111111111111111111111111112",
                "outputMint": mint_address,
                "amount": "1000000000",  # 1 SOL в лампортах
                "slippageBps": 50        # 0.5% проскальзывание
            }
            
            quote_response = await client.get(JUPITER_QUOTE_URL, params=quote_params, timeout=5.0)
            
            if quote_response.status_code == 200:
                quote_data = quote_response.json()
                out_amount = quote_data.get("outAmount", "0")
                logger.info(f"📊 Маршрут Jupiter найден. Выходной объем за 1 SOL: {out_amount}")
                
                return {
                    "mint": mint_address,
                    "price": price_data.get("price", 0.0),
                    "liquidity_route": True,
                    "estimated_out": out_amount
                }
            else:
                logger.warning(f"Токен {mint_address} еще не имеет пулов ликвидности на Raydium/Jupiter.")
                return {"mint": mint_address, "price": price_data.get("price", 0.0), "liquidity_route": False}
                
        except httpx.RequestError as exc:
            logger.error(f"Ошибка сети при обращении к Jupiter API: {exc}")
            return None

async def predict_token_viability(token_data: dict) -> bool:
    """
    Простейший ИИ/Логический фильтр для принятия решения об автоматической покупке.
    """
    if not token_data or not token_data.get("liquidity_route"):
        return False
        
    # Дополнительные метрики (например, если цена уже заведена или объем высокий)
    logger.info(f"Фильтр пройден для токена {token_data['mint']}. Передача торговому агенту.")
    return True
