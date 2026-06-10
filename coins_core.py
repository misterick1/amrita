import logging
from typing import Dict, Any

# Логирование под "Единый Квантовый Оркестратор"
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - [%(filename)s] - %(message)s")
logger = logging.getLogger("CoinsCore")

class CoinsCore:
    def __init__(self):
        # Конфигурация нативных сетей без посредников (Исключен MetaMask Snap для SOL)
        self.supported_ecosystems: Dict[str, Dict[str, Any]] = {
            "solana": {
                "ticker": "SOL",
                "decimals": 9,
                "contract": "So11111111111111111111111111111111111111112",
                "enabled": True,
                "provider": "Native_Solflare_RPC_Only"  # Строго нативное подключение
            },
            "pi_network": {
                "ticker": "PI",
                "decimals": 7,
                "contract": "native",
                "enabled": True,
                "provider": "Pi_Mainnet_Node"
            },
            "hyperliquid": {
                "ticker": "HYPE",
                "decimals": 6,
                "contract": "l1_native",
                "enabled": True,
                "provider": "Hyperliquid_L1"
            },
            "xai": {
                "ticker": "XAI",
                "decimals": 18,
                "contract": "0x4Cb9a741553AC6D311F35549012cd6c3422492f5",
                "enabled": True,
                "provider": "Arbitrum_Orbit_EVM"
            }
        }
        logger.info("CoinsCore: Нативная конфигурация провайдеров успешно обновлена.")

    def get_ecosystem_details(self, name: str) -> Dict[str, Any] | None:
        ecosystem = self.supported_ecosystems.get(name.lower())
        if not ecosystem:
            logger.warning(f"Запрошена неподдерживаемая экосистема: {name}")
            return None
        return ecosystem

    async def calculate_cross_rate(self, amount: float, from_coin: str, to_coin: str, prices: dict) -> float:
        from_ticker = from_coin.upper()
        to_ticker = to_coin.upper()
        
        if from_ticker == to_ticker:
            return amount
            
        price_from = prices.get(from_ticker)
        price_to = prices.get(to_ticker)
        
        if not price_from or not price_to:
            logger.error(f"Невозможно рассчитать курс для {from_ticker} или {to_ticker}")
            raise ValueError("Missing asset price")
            
        value_in_usd = amount * price_from
        return value_in_usd / price_to

core = CoinsCore()
