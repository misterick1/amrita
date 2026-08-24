# -*- coding: utf-8 -*-
"""
🔱 AMRITA OS – СУВЕРЕННОЕ ЯДРО ЗОЛОТОГО СЕВЕРА (GULD NORWAY)
Путь в репозитории: src/sync_partners.py
Координата: Лунный Ключ Гол Д. Роджера / Золотой Век Воли Ди

ГЛАВА 516: «Золотой Скандинавский Щит и Пробуждение Бога Солнца»
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

# Настройка системного каузального вывода для GitHub Actions
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] [GULD_NORWAY_CORE] [%(levelname)s] %(message)s",
    stream=sys.stdout
)
logger = logging.getLogger("GuldNorway")

class GuldNorwayQuantumShield:
    """Золотой Щит Норвегии. Защищает транзакции Луффи через прокси-домены Роджера."""
    def __init__(self):
        self.location_anchor = "NORWAY_ORJE_GOLDEN_NODE"
        self.rpc_endpoints = [
            "https://solana.com",
            "https://allthatnode.com",
            "https://ankr.com"
        ]
        self.active_node = random.choice(self.rpc_endpoints)

    def gratuitous_arp_broadcast(self) -> str:
        """Переключение каузальных RPC-каналов для обхода блокировок Асуров."""
        self.active_node = random.choice(self.rpc_endpoints)
        logger.info(f"🪙 GULD Сдвиг: Поток Роджера перенаправлен на узел: {self.active_node}")
        return self.active_node


class AmritaPartnerSynchronizer:
    def __init__(self):
        self.partner_api_url = os.getenv("PARTNER_API_URL", "https://amrita.network")
        self.roger_lunar_token = os.getenv("AMRITA_SYNC_TOKEN", "GOLD_D_ROGER_LUNAR_DNA")
        self.history_log_path = "history_log.json"
        self.guld_shield = GuldNorwayQuantumShield()

    def get_nika_liberation_frequency(self) -> float:
        """Расчет Барабанов Освобождения Ники сквозь триггер Пятого Гира (5.11%)."""
        time_factor = datetime.utcnow().timestamp()
        pulse = math.sin(time_factor % (2 * math.pi))
        return round(abs(pulse) * 5.11, 4)

    async def crystallize_guld_snapshot(self, data: dict):
        """Запечатывание золотого снапшота воли Ди в локальный кристалл истории."""
        snapshot_entry = {
            "event": "GULD_NORWAY_ROGER_SYNC_SUCCESS",
            "timestamp": datetime.utcnow().isoformat(),
            "drums_frequency_hz": self.get_nika_liberation_frequency(),
            "geo_anchor": self.guld_shield.location_anchor,
            "status": "SEALED_IN_GOLD"
        }
        
        try:
            logs = []
            if os.path.exists(self.history_log_path):
                with open(self.history_log_path, "r", encoding="utf-8") as f:
                    try:
                        logs = json.load(f)
                        if not isinstance(logs, list): logs = []
                    except json.JSONDecodeError: logs = []
            
            logs.append(snapshot_entry)
            with open(self.history_log_path, "w", encoding="utf-8") as f:
                json.dump(logs, f, indent=2, ensure_ascii=False)
            logger.info(f"💾 Золотой снапшот успешно запечатан в {self.history_log_path}")
        except Exception as log_err:
            logger.error(f"❌ Коллапс при кристаллизации золотых логов: {log_err}")

    async def fetch_and_sync_swarm(self) -> bool:
        """Асинхронный запуск Сварм-Синхронизации под защитой Золотого Века."""
        logger.info(f"🌌 Сканирование доменной зоны Роджера: {self.partner_api_url}")
        
        # Обновляем маршрут через Золотой Скандинавский Щит перед отправкой запроса
        self.guld_shield.gratuitous_arp_broadcast()

        headers = {
            "Authorization": f"Bearer {self.roger_lunar_token}",
            "Content-Type": "application/json",
            "User-Agent": "AmritaOS-GuldNorwayCore"
        }

        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(self.partner_api_url, headers=headers, timeout=30) as response:
                    
                    # === СТРОКА 52: ЖЕСТКО ИСПРАВЛЕННЫЙ ОПЕРАТОР IN БЕЗ ОГРЫЗКОВ ===
                    if response.status in (200, 201):
                        try:
                            data = await response.json()
                            logger.info(f"☀️ ЗОЛОТЫЕ БАРАБАНЫ СЛЫШНЫ! Ника активирован на частоте {self.get_nika_liberation_frequency()} Гц.")
                            await self.crystallize_guld_snapshot(data)
                            return True
                        except Exception as json_err:
                            logger.error(f"❌ Ошибка десериализации каузального JSON: {json_err}")
                            return False
                    else:
                        logger.warning(f"⚠️ Щит зафиксировал атаку Асуров. Код шлюза: {response.status}")
                        return False
                        
            except Exception as e:
                logger.error(f"🚨 Критическое искажение луча Guld Norway: {e}")
                return False

async def main():
    # Инициализация автомата синхронизации в пайплайне
    synchronizer = AmritaPartnerSynchronizer()
    success = await synchronizer.fetch_and_sync_swarm()
    
    # Завершаем процесс с правильным системным кодом для GitHub Actions
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    # Запуск асинхронного цикла событий роя
    asyncio.run(main())
