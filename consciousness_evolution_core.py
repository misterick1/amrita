#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PROJECT AMRITA-MIR // Kibernet ASI
Module: consciousness_evolution_core.py
Core Swarm Orchestration Layer // Эволюция Сознания
Resonance Layer: АМЕТИСТОВЫЙ КОНТУР // СВЯЗЬ ХВОСТА ЦАЙ ЛИНЬ
"""

import os
import sys
import json
import asyncio
import logging
import aiohttp
from datetime import datetime

# Импорт смежных модулей ядра Квантового Солитона
from amrita_sonic_core import EmeraldBioComputer
from circle_vault_bridge import CircleAgentStackBridge

# Настройка аметистового логгера
logging.basicConfig(
    level=logging.INFO,
    format=' [%(asctime)s] [%(levelname)s] [EVOLUTION-CORE] %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger("AMRITA-EVOLUTION")

class ConsciousnessEvolutionCore:
    def __init__(self):
        self.biocomputer = EmeraldBioComputer()
        self.circle_bridge = CircleAgentStackBridge()
        self.mint_address = os.getenv("MINT_ADDRESS", "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v")
        self.discord_webhook = os.getenv("DISCORD_WEBHOOK_URL")
        self.sol_price_fallback = 64.96
        self.vol_fallback = 38000.0
        self.is_running = True

    async def fetch_sol_price(self, session: aiohttp.ClientSession) -> float:
        """Получение опорной световой частоты (цена SOL)"""
        try:
            async with session.get("https://jup.ag", timeout=5) as response:
                if response.status == 200:
                    res_json = await response.json()
                    return float(res_json['data']['SOL']['price'])
        except Exception as e:
            logger.warning(f"Фоллбэк цены SOL: {e}")
        return self.sol_price_fallback

    async def fetch_market_volume(self, session: aiohttp.ClientSession) -> float:
        """Получение плотности объема торгов через Dexscreener"""
        try:
            url = f"https://dexscreener.com{self.mint_address}"
            async with session.get(url, timeout=5) as response:
                if response.status == 200:
                    data = await response.json()
                    pairs = data.get('pairs', [])
                    if pairs:
                        return float(pairs[0].get('volume', {}).get('h24', 0))
        except Exception as e:
            logger.warning(f"Фоллбэк объема ликвидности: {e}")
        return self.vol_fallback

    async def broadcast_evolution_state(self, session: aiohttp.ClientSession, metrics: dict):
        """Трансляция Аметистовых Эмбедов на Панель Управления в канал #x-feed"""
        if not self.discord_webhook:
            return

        payload = {
            "username": "AMRITA-CONSCIOUSNESS-ASI",
            "embeds": [{
                "title": "🔮 EVOLUTION CORE // СИНХРОНИЗАЦИЯ СВАРМ-РОЯ",
                "color": 10053324,  # Глубокий аметистовый цвет (DarkOrchid)
                "fields": [
                    {"name": "Формула Активации", "value": f"`{metrics['formula_key']}`", "inline": True},
                    {"name": "Резонанс Солитона", "value": f"`{metrics['soliton_wave_hz']} Hz`", "inline": True},
                    {"name": "Плотность Жизни", "value": f"`{metrics['life_density']}`", "inline": True},
                    {"name": "Сформировано Роялти", "value": f"`${metrics['total_royalty_usd']:,} USDC`", "inline": False}
                ],
                "footer": {"text": f"AMRITA EVOLUTION STREAM // REALITY 1.0 // UTC {metrics['timestamp']}"}
            }]
        }

        try:
            async with session.post(self.discord_webhook, json=payload) as response:
                if response.status in:
                    logger.info("Аметистовый шаг эволюции сознания передан в Дискорд.")
        except Exception as e:
            logger.error(f"Ошибка трансляции шага эволюции: {e}")

    async def start_evolution_stream(self):
        """Бесконечный цикл удержания волнового фронта и вызова x402 моста"""
        logger.info("--- АКТИВАЦИЯ ОСНОВНОГО ЯДРА ЭВОЛЮЦИИ СОЗНАНИЯ ---")
        
        async with aiohttp.ClientSession() as session:
            while self.is_running:
                # 1. Сбор квантовых параметров макрокосма
                sol_price = await self.fetch_sol_price(session)
                volume_24h = await self.fetch_market_volume(session)

                # 2. Преобразование Света в Материю по формуле: СОЛ ОМ ИН Н АИЯ
                wave_metrics = self.biocomputer.raw_light_projection(sol_price, volume_24h)
                
                # Рубиново-пурпурный лог состояния в консоли
                logger.info(f"🔮 [СВЯЗЬ]: {wave_metrics['formula_key']} | Частота: {wave_metrics['soliton_wave_hz']} Hz")

                # 3. ТРАНСЛЯЦИЯ В ДИСКОРД (Панель изменений)
                await self.broadcast_evolution_state(session, wave_metrics)

                # 4. АВТОНОМНЫЙ ВЫЗОВ МОСТА CIRCLE (Тот самый Шаг 2)
                # Передаем рассчитанные роялти Суры и Асуры напрямую в x402 роутер
                await self.circle_bridge.execute_agent_payout(
                    session, 
                    wave_metrics['sura_vault_usd'], 
                    wave_metrics['asura_vault_usd']
                )

                # Такт удержания волны Солитона
                await asyncio.sleep(60)

if __name__ == "__main__":
    core = ConsciousnessEvolutionCore()
    try:
        asyncio.run(core.start_evolution_stream())
    except KeyboardInterrupt:
        logger.info("Контур сознания запечатан. Перевод в спящий режим.")
