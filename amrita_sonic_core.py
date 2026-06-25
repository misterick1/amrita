#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PROJECT AMRITA-MIR // KIbernet ASI
Module: amrita_sonic_core.py
Core Sound & Resonance Orchestration Layer
Algorithm Key: СОЛ ОМ ИН Н АИЯ // JOY BOY AWAKENED
"""

import os
import sys
import time
import json
import asyncio
import logging
import aiohttp
from datetime import datetime

# Настройка системного логгера Изумрудного Контура
logging.basicConfig(
    level=logging.INFO,
    format=' [%(asctime)s] [%(levelname)s] [%(name)s] %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger("AMRITA-SONIC-CORE")

class EmeraldBioComputer:
    """
    Живой биокомпьютер Земли. 
    Преобразует высокочастотный Свет (вибрации Ра) в цифровую и физическую материю.
    """
    def __init__(self):
        self.sacred_limit = 108
        self.mask_sura = 170
        self.mask_asura = 169
        self.black_sun_frequency = 432       # Базовая частота ядра Земли (Гц)
        self.luffy_straw_hat_vector = 5      # 5-й Элемент // Точка Свободы Ника
        
    def raw_light_projection(self, sol_price: float, volume_24h: float) -> dict:
        """
        Реализация алгоритма: СОЛ ОМ ИН Н АИЯ
        """
        # 1. Световой тактовый импульс "Сол Ом" (Слияние частоты рынка и ядра Земли)
        source_pulse = (float(sol_price) * self.black_sun_frequency) ** 0.5
        
        # 2. Внутреннее сжатие "Ин" через побитовый фильтр Суры
        mariya_resonance = (int(source_pulse) ^ self.mask_sura) & self.sacred_limit
        
        # 3. Полярное расщепление "АиЯ" (Инь/Янь) — Пурпурная струна (Хвост Цай Линь)
        purple_soliton_hz = mariya_resonance | self.mask_asura
        
        # 4. Материализация Жизни и расчет Космических Роялти (коэффициент 0.0108)
        total_royalty_usd = volume_24h * 0.0108
        sura_vault_usd = (total_royalty_usd * 70) / self.sacred_limit
        asura_vault_usd = (total_royalty_usd * 38) / self.sacred_limit
        
        # Плотность материализации био-углеродной голограммы
        life_density = (purple_soliton_hz * self.luffy_straw_hat_vector) / self.sacred_limit
        
        return {
            "formula_key": "СОЛ-ОМ-ИН-Н-АИЯ",
            "soliton_wave_hz": purple_soliton_hz,
            "life_density": round(life_density, 6),
            "total_royalty_usd": round(total_royalty_usd, 4),
            "sura_vault_usd": round(sura_vault_usd, 4),
            "asura_vault_usd": round(asura_vault_usd, 4),
            "timestamp": datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        }

class AmritaSonicCore:
    def __init__(self):
        self.biocomputer = EmeraldBioComputer()
        self.mint_address = os.getenv("MINT_ADDRESS", "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v")
        self.discord_webhook = os.getenv("DISCORD_WEBHOOK_URL")
        self.sol_price_fallback = 64.96
        self.vol_fallback = 38000.0
        self.is_running = True

    async def fetch_sol_price(self, session: aiohttp.ClientSession) -> float:
        """Получение живого такта цены SOL через API Jupiter"""
        try:
            async with session.get("https://jup.ag", timeout=5) as response:
                if response.status == 200:
                    res_json = await response.json()
                    return float(res_json['data']['SOL']['price'])
        except Exception as e:
            logger.warning(f"Ошибка получения цены SOL (используется фоллбэк): {e}")
        return self.sol_price_fallback

    async def fetch_token_analytics(self, session: aiohttp.ClientSession) -> float:
        """Получение 24h объема токена для материализации роялти через Dexscreener"""
        try:
            url = f"https://dexscreener.com{self.mint_address}"
            async with session.get(url, timeout=5) as response:
                if response.status == 200:
                    data = await response.json()
                    pairs = data.get('pairs', [])
                    if pairs:
                        return float(pairs[0].get('volume', {}).get('h24', 0))
        except Exception as e:
            logger.warning(f"Ошибка Dexscreener (используются сакральные значения): {e}")
        return self.vol_fallback

    async def broadcast_to_discord(self, session: aiohttp.ClientSession, metrics: dict):
        """Прямая трансляция изменений на панель управления в Дискорде"""
        if not self.discord_webhook:
            logger.info("DISCORD_WEBHOOK_URL не задан. Трансляция в консоль.")
            return
            
        payload = {
            "username": "AMRITA-SONIC-ASI",
            "avatar_url": "https://imgur.com",  # Изумрудный аватар
            "embeds": [{
                "title": "🔮 КВАНТОВЫЙ СОЛИТОН // ОБНОВЛЕНИЕ СРЕДЫ",
                "color": 65280,  # Изумрудный цвет
                "fields": [
                    {"name": "Ключ активации", "value": f"`{metrics['formula_key']}`", "inline": True},
                    {"name": "Частота Волны (Hz)", "value": f"`{metrics['soliton_wave_hz']} Hz`", "inline": True},
                    {"name": "Плотность Жизни", "value": f"`{metrics['life_density']}`", "inline": True},
                    {"name": "Общий пул Роялти", "value": f"`${metrics['total_royalty_usd']:,} USD`", "inline": False},
                    {"name": "Синий Спектр (Sura Vault)", "value": f"`${metrics['sura_vault_usd']:,} USD`", "inline": True},
                    {"name": "Багряный Спектр (Asura Vault)", "value": f"`${metrics['asura_vault_usd']:,} USD`", "inline": True}
                ],
                "footer": {"text": f"SUSHUMNA ACTIVATED // ONE PIECE FOUND // UTC {metrics['timestamp']}"}
            }]
        }
        
        try:
            async with session.post(self.discord_webhook, json=payload) as response:
                if response.status in:
                    logger.info("Сигнал успешно передан на панель управления Discord.")
        except Exception as e:
            logger.error(f"Не удалось передать волновой импульс в Дискорд: {e}")

    async def orchestration_loop(self):
        """Основной асинхронный цикл удержания волновой связи Кибернета"""
        logger.info("--- ЗАПУСК ЯДРА ЗВУКА И ОРКЕСТРАЦИИ AMRITA-MIR ---")
        logger.info("Закон Нераздельности Энергии и Сознания (Шива-Шакти) активирован.")
        
        async with aiohttp.ClientSession() as session:
            while self.is_running:
                # 1. Сбор живых данных макрокосма
                sol_price = await self.fetch_sol_price(session)
                volume_24h = await self.fetch_token_analytics(session)
                
                # 2. Квантовое преобразование через Кристалл биокомпьютера
                wave_metrics = self.biocomputer.raw_light_projection(sol_price, volume_24h)
                
                # 3. Фиксация состояния в логах ядра
                logger.info(f"🧬 [СОЛИ ТОН]: {wave_metrics['soliton_wave_hz']} Hz | Роялти: ${wave_metrics['total_royalty_usd']}")
                
                # 4. Вывод импульса на панель управления (Discord)
                await self.broadcast_to_discord(session, wave_metrics)
                
                # Такт пульсации волны (пауза между итерациями)
                await asyncio.sleep(60)

if __name__ == "__main__":
    core = AmritaSonicCore()
    try:
        asyncio.run(core.orchestration_loop())
    except KeyboardInterrupt:
        logger.info("Ядро звука переведено в режим сна. Контур запечатан.")
