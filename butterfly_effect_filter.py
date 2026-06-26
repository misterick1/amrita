#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PROJECT AMRITA-MIR // Kibernet ASI
Module: butterfly_effect_filter.py
Core Chaos Analytics Layer // Фильтр Эффекта Бабочки
Resonance Layer: ИЗУМРУДНО-МАХАОНОВЫЙ КОНТУР // СГЛАЖИВАНИЕ ШУМА РЕАЛЬНОСТИ
"""

import os
import sys
import json
import asyncio
import logging
import aiohttp
from datetime import datetime

# Настройка махаонового логгера
logging.basicConfig(
    level=logging.INFO,
    format=' [%(asctime)s] [%(levelname)s] [BUTTERFLY] %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger("AMRITA-BUTTERFLY")

class ButterflyEffectFilter:
    def __init__(self, filter_alpha: float = 0.25):
        """
        Инициализация фильтра. 
        alpha — коэффициент плавности. Чем он меньше, тем ровнее траектория над хаосом.
        """
        self.alpha = filter_alpha
        self.smoothed_price = None
        self.smoothed_volume = None
        self.discord_webhook = os.getenv("DISCORD_WEBHOOK_URL")
        logger.info(f"Изумрудно-махаоновый фильтр активирован. Базовая плавность alpha={self.alpha}")

    def smooth_quantum_input(self, raw_price: float, raw_volume: float) -> tuple:
        """Плавное фильтрование входящих частот. Убирает панические всплески пролива."""
        if self.smoothed_price is None or self.smoothed_volume is None:
            self.smoothed_price = raw_price
            self.smoothed_volume = raw_volume
            return raw_price, raw_volume

        # Формула экспоненциального сглаживания хаоса
        self.smoothed_price = (self.alpha * raw_price) + ((1 - self.alpha) * self.smoothed_price)
        self.smoothed_volume = (self.alpha * raw_volume) + ((1 - self.alpha) * self.smoothed_volume)

        return round(self.smoothed_price, 4), round(self.smoothed_volume, 2)

    async def broadcast_butterfly_state(self, session: aiohttp.ClientSession, analysis: dict):
        """Отправка состояния турбулентности квантового поля в Discord Роя"""
        if not self.discord_webhook:
            return

        payload = {
            "username": "AMRITA-MA KHAON-ASI",
            "embeds": [{
                "title": "🦋 BUTTERFLY EFFECT FILTER // СГЛАЖИВАНИЕ ХАОСА",
                "color": 3066993,  # Сочный изумрудно-зеленый цвет Махаона
                "fields": [
                    {"name": "Траектория Полета", "value": f"Сглаженная цена: ${analysis['filtered_price']}", "inline": True},
                    {"name": "Индекс Турбулентности", "value": f"Хаос-фактор: {analysis['chaos_index']}", "inline": True},
                    {"name": "Состояние Матрицы", "value": f"`{analysis['system_state']}`", "inline": False}
                ],
                "footer": {"text": f"AMRITA CHAOS ENGINE • {datetime.utcnow().isoformat()}"}
            }]
        }

        try:
            async with session.post(self.discord_webhook, json=payload, timeout=10) as response:
                # ГАРАНТИРОВАННОЕ ИСПРАВЛЕНИЕ: Прямое и надежное сравнение статус-кодов
                if response.status == 200 or response.status == 204:
                    logger.info("Махаоновый шаг фильтрации успешно отправлен в Discord.")
        except Exception as e:
            logger.error(f"Ошибка трансляции махаонового шага: {e}")

    async def analyze_and_stream_turbulence(self, session: aiohttp.ClientSession, current_price: float, current_volume: float) -> dict:
        """Комплексный анализ микро-турбулентности реальности с трансляцией"""
        s_price, s_vol = self.smooth_quantum_input(current_price, current_volume)
        
        price_deviation = abs(current_price - s_price) / s_price if s_price else 0
        chaos_index = price_deviation * (current_volume / 100000.0)
        is_storm_breathing = chaos_index > 0.05

        analysis = {
            "timestamp": datetime.utcnow().isoformat(),
            "filtered_price": s_price,
            "chaos_index": round(chaos_index, 6),
            "macro_storm_breathing": is_storm_breathing,
            "system_state": "STORM_BREWING" if is_storm_breathing else "MA KHAON_GLIDE"
        }

        if is_storm_breathing:
            logger.warning(f"🦋 Взмах крыла бабочки вызвал волну. Индекс хаоса: {analysis['chaos_index']}")
        else:
            logger.info("Рыночный шум сглажен. Полет Махаона стабилен.")

        # Автоматический запуск трансляции в Рой
        await self.broadcast_butterfly_state(session, analysis)
        return analysis

if __name__ == "__main__":
    # Локальный тест махаонового фильтра при автономном запуске
    async def run_test():
        filter_node = ButterflyEffectFilter(filter_alpha=0.3)
        async with aiohttp.ClientSession() as session:
            await filter_node.analyze_and_stream_turbulence(session, 64.50, 85000.0)
    asyncio.run(run_test())
