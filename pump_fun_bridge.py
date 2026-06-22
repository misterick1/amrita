import asyncio
import aiohttp
import logging
from typing import Dict, Any, List

logger = logging.getLogger("AmritaPumpBridge")

class BirdeyeInsiderDetector:
    """Модуль каузального анализа инсайдеров через Birdeye v2 API"""
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://birdeye.so"
        
    async def analyze_token_insiders(self, session: aiohttp.ClientSession, token_address: str) -> List[Dict[str, Any]]:
        url = f"{self.base_url}/defi/v2/tokens/{token_address}/top_traders"
        headers = {
            "X-API-KEY": self.api_key,
            "x-chain": "solana"
        }
        params = {
            "time_frame": "30d",
            "sort_by": "pnl",
            "limit": "15"
        }
        try:
            async with session.get(url, headers=headers, params=params) as resp:
                if resp.status == 200:
                    payload = await resp.json()
                    traders = payload.get("data", {}).get("items", [])
                    return self._filter_target_tags(traders)
                logger.error(f"[Birdeye] Ошибка запроса: {resp.status}")
                return []
        except Exception as e:
            logger.error(f"[Birdeye] Исключение при парсинге: {e}")
            return []

    def _filter_target_tags(self, traders: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        detected = []
        target_tags = {"insider", "sniper", "dev", "bundler"}
        for t in traders:
            tags = set(t.get("tags", []))
            # Проверяем пересечение тегов или совпадение с ключевыми кошельками
            if tags.intersection(target_tags) or t.get("realized_pnl", 0) > 500:
                detected.append(t)
        return detected
