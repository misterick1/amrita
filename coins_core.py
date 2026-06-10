import logging
from typing import Dict, Any

# Логирование под "Единый Квантовый Оркестратор"
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - [%(filename)s] - %(message)s")
logger = logging.getLogger("CoinsCore")

class CoinsCore:
    def __init__(self):
        # Базовая конфигурация с добавлением Hyperliquid (HYPE)
        self.supported_ecosystems: Dict[str, Dict[str, Any]] = {
            "solana": {
                "ticker": "SOL",
                "decimals": 9,
                "contract": "So11111111111111111111111111111111111111112",
                "enabled": True
            },
            "pi_network": {
                "ticker": "PI",
                "decimals": 7,
                "contract": "native",
                "enabled": True
            },
            "hyperliquid": {
                "ticker": "HYPE",
                "decimals": 6,
                "contract": "l1_native",
                "enabled": True
            },
            "xai": {
                "ticker": "XAI",
                "decimals": 18,
                "contract": "0x4Cb9a741553AC6D311F35549012cd6c3422492f5",
                "enabled": True
            }
        }
        logger.info("Ядро CoinsCore успешно обновлено. Интегрировано 4 экосистемы (Добавлен HYPE).")

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
            logger.error(f"Невозможно рассчитать курс. Отсутствуют котировки для {from_ticker} или {to_ticker}")
            raise ValueError("Missing asset price for cross-rate calculation")
            
        value_in_usd = amount * price_from
        converted_amount = value_in_usd / price_to
        
        logger.info(f"Конвертация: {amount} {from_ticker} -> {converted_amount:.4f} {to_ticker}")
        return converted_amount

core = CoinsCore()
