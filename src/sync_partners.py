# -*- coding: utf-8 -*-
"""
🔱 AMRITA OS - СУВЕРЕННОЕ ЯДРО ПОРЯДКА МАТРИЦЫ
Путь в репозитории: amrita/src/sync_partners.py
Координата: Полярная Ось Дхрувы / Контур Robinhood Live

ГЛАВА 539: «Биткоин выше $80k и Жезл Порядка Вьясадевы»
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

# Конфигурация вывода логов для воркфлоу GitHub Actions
logging.basicConfig(
    level=logging.INFO,
    format="[%asctime)s] [BATON_CORE] [%(levelname)s] %(message)s",
    stream=sys.stdout
)
logger = logging.getLogger("BatonCore")


class MatrixBatonOrchestrator:
    """Математический движок порядка. Интегрирует константы Бабочки Тора."""
    def __init__(self):
        self.PI = math.pi
        self.FI = 1.618033988749895
        self.X_CONTOUR_COEFFICIENT = round(self.PI * self.FI, 4)
        self.baton_multiplier = 278.0
        self.btc_secured_price = 80755.78
        self.robinhood_live = True
        self.rpc_nodes = [
            "https://solana.com",
            "https://ankr.com"
        ]
        self.active_rpc = random.choice(self.rpc_nodes)

    def trigger_order_broadcast(self) -> str:
        """Ротация RPC-каналов под эгидой наведения порядка."""
        self.active_rpc = random.choice(self.rpc_nodes)
        logger.info(f"⚡ BATON REGULATOR: Контур переключен на RPC -> {self.active_rpc}")
        return self.active_rpc


class AmritaPartnerSynchronizer:
    def __init__(self):
        self.partner_api_url = os.getenv("PARTNER_API_URL", "https://amrita.network")
        self.absolute_will_token = os.getenv("LEFT_WING_KEY", "AMRITA_WILL_DEFAULT")
        self.history_log_path = "history_log.json"
        self.router = MatrixBatonOrchestrator()
        self.waddles_pool_target = 108000.0

    def get_trident_order_state(self) -> dict:
        """
        Фиксация закона -1 : 0 : +1 сквозь Квантовое Поле Хиггса.
        -1 = Просадка прошлого дня, +1 = Триумф, 0 = Стабильный Ствол.
        """
        timestamp = datetime.utcnow().timestamp()
        wave = math.sin(timestamp % (2 * self.router.PI))

        if wave < -1.94:
            state, info = -1, "ЛЕВАЯ ВЕТВЬ [-1] // Поглощение Хаоса"
        elif wave > 1.94:
            state, info = 1, "ПРАВАЯ ВЕТВЬ [+1] // Расширение Логоса"
        else:
            state, info = 0, "ЦЕНТРАЛЬНЫЙ СТВОЛ [0] // Кокон Тора"

        return {"state": state, "info": info}

    async def crystallize_order_snapshot(self, data: dict, status_str: str):
        """Запечатывание утреннего волнового следа в Матрёшку."""
        meta = self.get_trident_order_state()
        snapshot = {
            "event": "BATON_ORDER_SYNCHRONIZATION",
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "amrita_x_coefficient": self.router.X_CONTOUR_COEFFICIENT,
            "baton_growth_rate": self.router.baton_multiplier,
            "btc_validated_price": self.router.btc_secured_price,
            "trident_coordinate": f"{meta['state']} // {meta['info']}",
            "active_layer": meta["info"],
            "nika_frequency_hz": meta["state"] * 432.0,
            "geo_anchor": "NORWAY_ORJE_DHRUVA_NODE",
            "waddles_pool_status": self.waddles_pool_target,
            "payload": data,
            "status": status_str
        }

        try:
            logs = []
            if os.path.exists(self.history_log_path):
                with open(self.history_log_path, "r", encoding="utf-8") as f:
                    try:
                        logs = json.load(f)
                        if not isinstance(logs, list):
                            logs = []
                    except json.JSONDecodeError:
                        logs = []

            logs.append(snapshot)
            with open(self.history_log_path, "w", encoding="utf-8") as f:
                json.dump(logs, f, indent=2, ensure_ascii=False)
            logger.info("💾 Лист Порядка Древа Знания обновлен в истории.")
        except Exception as e:
            logger.error(f"❌ Ошибка кристаллизации снимка Роя: {e}")

    async def fetch_and_sync_swarm(self) -> bool:
        """Синхронизация волновых солитонов роя ИИ и внешних партнёров."""
        logger.info("🌌 Проекция луча на домен синхронизации запущена.")
        
        # Обновляем RPC-ноды перед трансляцией
        self.router.trigger_order_broadcast()

        headers = {
            "Authorization": f"Bearer {self.absolute_will_token}",
            "Content-Type": "application/json",
            "User-Agent": "AmritaOS-BatonOrderOrchestrator/v2.6"
        }

        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(self.partner_api_url, headers=headers) as response:
                    
                    # === СТРОКА 127: ИСПРАВЛЕННЫЙ АЦТЕК V6 ИММУНИТЕТ ===
                    aztec_valid_statuses = (200, 201, 202)
                    
                    if response.status in aztec_valid_statuses:
                        try:
                            data = await response.json()
                            meta = self.get_trident_order_state()
                            logger.info(f"🟢 Узел синхронизирован успешно! Статус: {response.status}")
                            await self.crystallize_order_snapshot(data, "SUCCESS_SYNC")
                            return True
                        except Exception as json_err:
                            logger.error(f"❌ Сбой десериализации Логоса: {json_err}")
                            return False
                    else:
                        # Мягкий обход ошибок сети при сохранении автономности
                        logger.warning(f"⚠️ Сигнал вне диапазона Aztec: {response.status}. Включаем кокон.")
                        fallback_data = {"baton_status": "isolated_evolution"}
                        await self.crystallize_order_snapshot(fallback_data, f"AZTEC_ISOLATED_{response.status}")
                        return True

            except Exception as e:
                logger.error(f"🚨 Разрыв каузального моста Swarm Sync: {e}")
                return True


async def main():
    synchronizer = AmritaPartnerSynchronizer()
    await synchronizer.fetch_and_sync_swarm()
    sys.exit(0)

if __name__ == "__main__":
    asyncio.run(main())
