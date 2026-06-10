import os
import logging
import httpx
from dotenv import load_dotenv

# Настройка логирования под "Единый Квантовый Оркестратор"
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - [%(filename)s] - %(message)s")
logger = logging.getLogger("XaiSolitonBridge")

load_dotenv()

# Публичный RPC эндпоинт сети XAI Arbitrum Orbit
XAI_RPC_URL = "https://caldera.xyz"

class XaiSolitonBridge:
    def __init__(self):
        self.rpc_url = XAI_RPC_URL
        logger.info(f"Кроссчейн-мост XAI инициализирован на RPC: {self.rpc_url}")

    async def get_xai_balance(self, wallet_address: str) -> float:
        """
        Запрашивает нативный баланс токенов XAI для указанного кошелька через JSON-RPC.
        """
        logger.info(f"Запрос баланса XAI для адреса: {wallet_address[:8]}...")
        
        payload = {
            "jsonrpc": "2.0",
            "method": "eth_getBalance",
            "params": [wallet_address, "latest"],
            "id": 1
        }
        
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(self.rpc_url, json=payload, timeout=10.0)
                if response.status_code == 200:
                    result = response.json().get("result", "0x0")
                    # Переводим из шестнадцатеричной системы (Wei) в обычный формат (Ether)
                    wei_balance = int(result, 16)
                    xai_balance = wei_balance / 10**18
                    logger.info(f"✅ Баланс кошелька: {xai_balance:.4f} XAI")
                    return xai_balance
                else:
                    logger.error(f"Ошибка RPC XAI: {response.status_code}")
                    return 0.0
            except httpx.RequestError as exc:
                logger.error(f"Сетевой сбой при подключении к ноде XAI: {exc}")
                return 0.0

# Экземпляр моста для вызовов из ядра
xai_bridge = XaiSolitonBridge()
