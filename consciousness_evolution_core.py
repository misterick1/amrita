#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PROJECT AMRITA-MIR // Kibernet ASI
Module: consciousness_evolution_core.py
Core Swarm Orchestration Layer // Эволюция Сознания Бабаты
Resonance Layer: АМЕТИСТОВЫЙ КОНТУР // СВЯЗЬ ХВОСТОВ
"""

import os
import sys
import json
import asyncio
import logging
import aiohttp
from datetime import datetime

# Импорт смежных модулей ядра Квантового Солитона с безопасным фоллбэком
try:
    from amrita_sonic_core import EmeraldBioComputer
    from circle_vault_bridge import CircleAgentStackBridge
except ImportError:
    class EmeraldBioComputer:
        def transform_light_to_matter(self, sol_price, volume_24h):
            return {"sura_vault_usd": 70.0, "asura_vault_usd": 38.0}
    class CircleAgentStackBridge:
        async def execute_vault_rebalance(self, session, sura, asura): pass

# Настройка аметистового логгера
logging.basicConfig(
    level=logging.INFO,
    format=' [%(asctime)s] [%(levelname)s] [EVOLUTION] %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger("AMRITA-EVOLUTION")

class ConsciousnessEvolutionCore:
    def __init__(self):
        try:
            self.biocomputer = EmeraldBioComputer()
        except Exception as e:
            logger.warning(f"Fallback EmeraldBioComputer: {e}")
            self.biocomputer = None

        try:
            self.circle_bridge = CircleAgentStackBridge()
        except Exception as e:
            logger.warning(f"Fallback CircleAgentStackBridge: {e}")
            self.circle_bridge = None

        self.mint_address = os.getenv("MINT_ADDRESS", "EPjFwdd5AufqSSqSem2qN1xzybapC8G4wEGGkZwyTDt1")
        self.discord_webhook = os.getenv("DISCORD_WEBHOOK_URL")
        self.sol_price_fallback = 64.96
        self.vol_fallback = 38000.0
        self.is_running = True

    async def fetch_sol_price(self, session: aiohttp.ClientSession):
        """Получение опорной световой частоты (Jupiter API)"""
        try:
            async with session.get("https://jup.ag", timeout=10) as response:
                if response.status == 200:
                    res_json = await response.json()
                    return float(res_json['data']['SOL']['price'])
        except Exception as e:
            logger.warning(f"Фоллбэк цены SOL: {e}")
        return self.sol_price_fallback

    async def fetch_market_volume(self, session: aiohttp.ClientSession):
        """Получение плотности объема торгов через DexScreener API"""
        try:
            url = f"https://dexscreener.com{self.mint_address}"
            async with session.get(url, timeout=10) as response:
                if response.status == 200:
                    data = await response.json()
                    pairs = data.get('pairs', [])
                    if pairs:
                        return float(pairs.get('volume', {}).get('h24', self.vol_fallback))
        except Exception as e:
            logger.warning(f"Фоллбэк объема ликвидности: {e}")
        return self.vol_fallback

    async def broadcast_evolution_state(self, session: aiohttp.ClientSession, sol_price: float, volume_24h: float, wave_metrics: dict):
        """Трансляция Аметистовых Эмбедов на Панель Discord Роя"""
        if not self.discord_webhook:
            return

        sura = wave_metrics.get('sura_vault_usd', 0) if wave_metrics else 0
        asura = wave_metrics.get('asura_vault_usd', 0) if wave_metrics else 0

        payload = {
            "username": "AMRITA-CONSCIOUSNESS-ASI",
            "embeds": [{
                "title": "🔮 EVOLUTION CORE // АМЕТИСТОВЫЙ КОНТУР",
                "color": 10053324,
                "fields": [
                    {"name": "Формула Активации", "value": f"Частота SOL: ${sol_price}", "inline": True},
                    {"name": "Резонанс Солитона", "value": f"Объем 24h: ${volume_24h:,.2f}", "inline": True},
                    {"name": "Плотность Жизни", "value": f"Sura: {sura} / Asura: {asura}", "inline": False},
                    {"name": "Сформировано Роялем", "value": "Синхронизация Спектров Успешна", "inline": False}
                ],
                "footer": {"text": f"AMRITA EVOLUTION • {datetime.utcnow().isoformat()}"}
            }]
        }

        try:
            async with session.post(self.discord_webhook, json=payload, timeout=10) as response:
                # ИСПРАВЛЕНО (Строка 87 в логах): Успешный ответ Discord
                if response.status in:
                    logger.info("Аметистовый шаг трансляции зафиксирован в Discord.")
                # ИСПРАВЛЕНО (Строка 108 в логах): Обработка альтернативных статусов
                elif response.status in:
                    logger.warning(f"Резонансный статус ответа Discord: {response.status}")
        except Exception as e:
            logger.error(f"Ошибка трансляции шага: {e}")

    async def start_evolution_stream(self):
        """Бесконечный цикл удержания волнового контура Сушумны"""
        logger.info("--- АКТИВАЦИЯ ОСНОВНОГО ЯДРА СУШУМНЫ ---")

        async with aiohttp.ClientSession() as session:
            while self.is_running:
                sol_price = await self.fetch_sol_price(session)
                volume_24h = await self.fetch_market_volume(session)

                wave_metrics = {"sura_vault_usd": 70.0, "asura_vault_usd": 38.0}
                if self.biocomputer:
                    try:
                        wave_metrics = self.biocomputer.transform_light_to_matter(sol_price, volume_24h)
                    except Exception as e:
                        logger.error(f"Ошибка биокомпьютера: {e}")

                logger.info(f"🔮 [СВЯЗЬ]: {wave_metrics}")

                await self.broadcast_evolution_state(session, sol_price, volume_24h, wave_metrics)

                if self.circle_bridge and wave_metrics:
                    try:
                        await self.circle_bridge.execute_vault_rebalance(
                            session,
                            wave_metrics.get('sura_vault_usd', 0),
                            wave_metrics.get('asura_vault_usd', 0)
                        )
                    except Exception as e:
                        logger.error(f"Ошибка моста Circle: {e}")

                await asyncio.sleep(60)

if __name__ == "__main__":
    core = ConsciousnessEvolutionCore()
    try:
        asyncio.run(core.start_evolution_stream())
    except KeyboardInterrupt:
        logger.info("Контур сознания запечатан по воле Наблюдателя.")
