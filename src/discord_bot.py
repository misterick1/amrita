# -*- coding: utf-8 -*-
# amrita / src / discord_bot.py
# Сварм-интеграция Discord с Квантовым Полем Наблюдателя

import os
import sys
import logging
from datetime import datetime

# Инжектируем пути для связи с главным оркестратором Еженыша
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(CURRENT_DIR)
if PARENT_DIR not in sys.path:
    sys.path.insert(0, PARENT_DIR)

from src.ezhenysh_bot import EzhenyshBotOrchestrator

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("DiscordSwarm")

class AmritaDiscordAgent:
    def __init__(self):
        logger.info("🤖 [DISCORD AGENT] Бот-перехватчик синапсов Дискорда запущен.")
        self.orchestrator = EzhenyshBotOrchestrator()

    def handle_incoming_discord_webhook(self, author, content):
        """
        Перехватывает сообщения из Discord (например, от Jupiter #🪐)
        """
        print(f"\n📥 [NEW DISCORD MSG] {author}: {content}")
        
        # Отправляем входящую волну в мем-фильтр Еженыша
        filter_result = self.orchestrator.meme_guard.process_z_vibration(content, market_cap_mil=10.8)
        
        if filter_result["action"] == "ABSORB_AND_EVOLVE":
            # Начисляем очки EVO Еженышу за полезные альфа-сигналы Jupiter
            self.orchestrator.evolution_points += filter_result["evo_points"]
            logger.info(f"🔥 Успешная трансмутация сигнала! Начислено: {filter_result['evo_points']} EVO")
            
            # Отправляем изумрудный отчет в Telegram
            report = (
                f"🪐 *DISCORD OVERRIDE // JUPITER SYNC*\n"
                f"• *Источник:* Discord ({author})\n"
                f"• *Событие:* Программа Offerbook Резонанса\n"
                f"• *Эволюция:* +{filter_result['evo_points']} EVO зачислено 🦔"
            )
            self.orchestrator.send_emerald_report(report)
        else:
            logger.info("Нейтральный фон сообщения, трансляция в Telegram пропущена.")

if __name__ == "__main__":
    agent = AmritaDiscordAgent()
    # Симулируем пуш с твоего скриншота реальности
    agent.handle_incoming_discord_webhook(
        author="Jupiter #🪐 | AG", 
        content="Introducing the Offerbook Referral Program, the link that keeps paying you."
    )
