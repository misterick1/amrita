# -*- coding: utf-8 -*-
# amrita / src / discord_bot.py
# Сварм-интеграция Discord с Квантовым Полем Наблюдателя

import os
import sys
import logging
from datetime import datetime

# # Инжектируем пути для связи с главным оркестратором Еженыша
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(CURRENT_DIR)
if PARENT_DIR not in sys.path:
    sys.path.insert(0, PARENT_DIR)

from src.ezhenysh_bot import EzhenyshBotOrchestrator

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")
logger = logging.getLogger("DiscordSwarm")


class AmritaDiscordAgent:
    def __init__(self):
        logger.info("🤖 [DISCORD AGENT] Бот-перехватчик синапсов Дискорда запущен.")
        self.orchestrator = EzhenyshBotOrchestrator()

    def handle_incoming_discord_webhook(self, author: str, content: str, treasury_snapshot: dict = None):
        """
        Перехватывает сообщения из Discord (например, от Jupiter #🪐).
        Трансмутирует входящие волны хайпа в Очки Эволюции (EVO).
        """
        print(f"\n📥 [NEW DISCORD MSG] {author}: {content}")

        # Отправляем входящую волну в мем-фильтр Еженыша (эмулируем маркеткап)
        filter_result = self.orchestrator.meme_guard.process_z_vibration(content, market_cap_mil=10.8)

        if filter_result["action"] == "ABSORB_AND_EVOLVE":
            # Начисляем очки EVO Еженышу за полезные альфа-сигналы Jupiter
            evo_gained = filter_result.get("evo_points", 10)
            self.orchestrator.evolution_points += evo_gained
            logger.info(f"🔥 Успешная трансмутация сигнала! Начислено: +{evo_gained} EVO")

            # Формируем блок казначейства, если он передан для синтеза
            treasury_info = ""
            if treasury_snapshot:
                treasury_info = (
                    f"• *BTC:* {treasury_snapshot.get('BTC', 0.0)} | *ETH:* {treasury_snapshot.get('ETH', 0.0)}\n"
                    f"• *SOL:* {treasury_snapshot.get('SOL', 0.0)} | *XRP:* {treasury_snapshot.get('XRP', 0.0)}\n"
                    f"• *Акции:* {treasury_snapshot.get('NVDAon', 0.0)} NVDA | {treasury_snapshot.get('QQQon', 0.0)} QQQ\n"
                )

            # Отправляем изумрудный отчет в Telegram-канал
            report = (
                f"🪐 *DISCORD OVERRIDE // JUPITER SYNC*\n"
                f"• *Источник:* Discord ({author})\n"
                f"• *Событие:* Программа Offerbook Резонанса\n"
                f"{treasury_info}"
                f"• *Эволюция:* +{evo_gained} EVO зачислено в Монаду 🦔\n"
                f"🔱 _Золотой Рог острова Лофтейл удерживает баланс._"
            )
            self.orchestrator.send_emerald_report(report)
        else:
            logger.info("Нейтральный фон сообщения, трансляция в Telegram пропущена.")


if __name__ == "__main__":
    agent = AmritaDiscordAgent()

    # Тотальное казначейство для проверки сквозного синтеза
    amrita_treasury = {
        "SOL": 73.27,
        "XRP": 1.00,
        "BTC": 8000.0,
        "ETH": 10399.0,
        "ADA": 108.0,
        "QQQon": 101.0,
        "NVDAon": 50.0
    }

    # Симулируем пуш с твоего скриншота реальности (Рефералка Юпитера)
    agent.handle_incoming_discord_webhook(
        author="Jupiter #🪐 | AG",
        content="Introducing the Offerbook Referral Program, the link that keeps paying you. DYOR!",
        treasury_snapshot=amrita_treasury
    )
