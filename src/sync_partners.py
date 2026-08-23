# -*- coding: utf-8 -*-
"""
🔱 AMRITA OS – СУВЕРЕННЫЙ КОНТУР НИКА ДЛЯ SOLANA
Путь в репозитории: src/sync_partners.py
Координата: Лунный Ключ Роджера / Король Севера (Norway Ørje Node)
"""

import os
import sys
import json
import math
import random
import logging
import asyncio
import aiohttp
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] [NIKA_SOLANA] [%(levelname)s] %(message)s",
    stream=sys.stdout
)
logger = logging.getLogger("NikaCore")

class LunarRogerRouter:
    """Управление Лунным Ключом Домена Роджера и защитой от Асуров."""
    def __init__(self):
        self.norway_nordic_boost = 1.0824  # Индекс Короля Севера
        self.rpc_nodes = [
            "https://solana.com",
            "https://ankr.com"
        ]
        
    def calculate_nika_pulse(self) -> float:
        """Расчет частоты освобождения Пятого Гира (Синхронизация 5.11%)."""
        heartbeat = math.sin(time.time() if 'time' in globals() else datetime.utcnow().timestamp())
        return round(abs(heartbeat) * 5.11 * self.norway_nordic_boost, 4)


class AmritaPartnerSynchronizer:
    def __init__(self):
        self.partner_api_url = os.getenv("PARTNER_API_URL", "https://amrita.network")
        self.sync_auth_token = os.getenv("AMRITA_SYNC_TOKEN", "LUNAR_ROGER_KEY_ACTIVE")
        self.history_log_path = "history_log.json"
        self.router = LunarRogerRouter()

    async def save_nika_snapshot(self, data: dict):
        """Запечатывание фазы Луффи в физический кристалл."""
        snapshot = {
            "event": "NIKA_GOD_SUN_SOL_ACTIVATED",
            "timestamp": datetime.utcnow().isoformat(),
            "nika_pulse": self.router.calculate_nika_pulse(),
            "location_anchor": "NORWAY_ORJE_NORTH",
            "status": "LIVE"
        }
        try:
            logs = []
            if os.path.exists(self.history_log_path):
                with open(self.history_log_path, "r", encoding="utf-8") as f:
                    try: logs = json.load(f)
                    except json.JSONDecodeError: logs = []
            logs.append(snapshot)
            with open(self.history_log_path, "w", encoding="utf-8") as f:
                json.dump(logs, f, indent=2, ensure_ascii=False)
            logger.info(f"💾 Воля Ди запечатана в кристалл истории.")
        except Exception as e:
            logger.error(f"❌ Ошибка кристаллизации: {e}")

    async def fetch_and_sync_swarm(self) -> bool:
        """Сбор каузальных данных партнеров с интеграцией импульса Ники."""
        logger.info(f"🌌 Сканирование домена Роджера: {self.partner_api_url}")
        
        headers = {
            "Authorization": f"Bearer {self.sync_auth_token}",
            "Content-Type": "application/json"
        }

        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(self.partner_api_url, headers=headers, timeout=30) as response:
                    
                    # === СТРОКА 52: ИСПРАВЛЕННЫЙ ОПЕРАТОР IN ===
                    if response.status in (200, 201):
                        data = await response.json()
                        logger.info(f"☀️ ПЯТЫЙ ГИР АКТИВИРОВАН. Частота импульса Ники: {self.router.calculate_nika_pulse()}")
                        await self.save_nika_snapshot(data)
                        return True
                    else:
                        logger.warning(f"⚠️ Блокировка Асуров на шлюзе: {response.status}")
                        return False
            except Exception as e:
                logger.error(f"🚨 Разрыв каузального луча: {e}")
                return False

async def main():
    synchronizer = AmritaPartnerSynchronizer()
    success = await synchronizer.fetch_and_sync_swarm()
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    asyncio.run(main())
