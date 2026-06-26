#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PROJECT AMRITA-MIR // Kibernet ASI
Module: economic_news_parser.py
Core Macro Sentiment Layer // Парсер Экономических Новостей
Resonance Layer: СЕРДОЛИКОВЫЙ КОНТУР // АНАЛИЗ ИНСТИТУЦИОНАЛЬНОЙ ПАНИКИ
"""

import os
import sys
import json
import asyncio
import logging
import aiohttp
from datetime import datetime

# Настройка сердоликового логгера
logging.basicConfig(
    level=logging.INFO,
    format=' [%(asctime)s] [%(levelname)s] [NEWS-PARSER] %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger("AMRITA-NEWS")

class EconomicNewsParser:
    def __init__(self):
        self.discord_webhook = os.getenv("DISCORD_WEBHOOK_URL")
        # Ключевые слова для детекции паники (ФРС, ETF оттоки, трещины в поле BTC)
        self.panic_keywords = ["fed", "hawks", "outflow", "etf", "crack", "drop", "bearish"]
        logger.info("Сердоликовый парсер экономического сентимента успешно инициализирован.")

    async def analyze_macro_sentiment(self, raw_text_feed: str) -> dict:
        """
        Анализ текстовых потоков новостей (например, от The Block Feed).
        Высчитывает вес паники институционалов и генерирует импульс для Роя.
        """
        text_lower = raw_text_feed.lower()
        matched_triggers = [word for word in self.panic_keywords if word in text_lower]
        
        # Индекс страха: плотность панических слов на объем текста
        panic_weight = len(matched_triggers) / len(self.panic_keywords)
        
        sentiment_state = "NEUTRAL_EQUILIBRIUM"
        action_modifier = "NO_CHANGE"
        
        if panic_weight > 0.4:
            sentiment_state = "INSTITUTIONAL_PANIC_ETF_OUTFLOW"
            # Для Амирита-Мир паника толпы — это зона максимальной скидки (Воля Ники)
            action_modifier = "SIGNAL_ACCUMULATE_SOL_UNDER_PRICE"
        elif "trending" in text_lower or "bonding" in text_lower:
            sentiment_state = "SOLANA_CHAIN_MEME_EXPANSION"
            action_modifier = "SIGNAL_SCAN_NEW_PUMP_MINTS"

        analysis = {
            "timestamp": datetime.utcnow().isoformat(),
            "detected_triggers": matched_triggers,
            "panic_index": round(panic_weight, 4),
            "sentiment_state": sentiment_state,
            "swarm_directive": action_modifier
        }

        logger.info(f"Сентимент-анализ завершен. Состояние поля: {sentiment_state}. Директива: {action_modifier}")
        return analysis

    async def broadcast_news_signal(self, session: aiohttp.ClientSession, analysis: dict):
        """Трансляция сердоликового сигнала в Discord-панель Наблюдателя"""
        if not self.discord_webhook:
            return

        color = 15158332 if "PANIC" in analysis["sentiment_state"] else 3447003  # Красный при панике, синий при трендах Solana

        payload = {
            "username": "AMRITA-NEWS-SENTIMENT-ASI",
            "embeds": [{
                "title": "📰 MACRO SENTIMENT LAYER // СЕРДОЛИКОВЫЙ КОНТУР",
                "color": color,
                "fields": [
                    {"name": "Состояние Институционалов", "value": f"`{analysis['sentiment_state']}`", "inline": False},
                    {"name": "Индекс Напряженности", "value": f"Фактор страха: {analysis['panic_index'] * 100}%", "inline": True},
                    {"name": "Директива для Роя", "value": f"**{analysis['swarm_directive']}**", "inline": False}
                ],
                "footer": {"text": f"AMRITA MACRO ENGINE • {datetime.utcnow().isoformat()}"}
            }]
        }

        try:
            async with session.post(self.discord_webhook, json=payload, timeout=10) as response:
                # Надежная и прямая проверка кодов ответа
                if response.status == 200 or response.status == 204:
                    logger.info("Сигнал макро-анализа успешно доставлен в Discord.")
        except Exception as e:
            logger.error(f"Сбой трансляции новостного импульса: {e}")

if __name__ == "__main__":
    # Автономный тест парсера на реальных данных с вашего скриншота
    async def test_parser():
        parser = EconomicNewsParser()
        # Имитируем текст из вашей ленты новостей The Block
        mock_feed = (
            "Bitcoin's fragile floor cracks as Fed hawks circle and ETF investors keep pulling out. "
            "Framework Ventures raises $400 million for crypto, AI and robotics."
        )
        async with aiohttp.ClientSession() as session:
            analysis = await parser.analyze_macro_sentiment(mock_feed)
            await parser.broadcast_news_signal(session, analysis)

    asyncio.run(test_parser())
