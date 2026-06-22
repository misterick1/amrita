import os
import asyncio
import logging
import aiohttp
import random
from datetime import datetime

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("QuantumVotingCore")

SACRED_LIMIT = 108
SURA_SHARE = 70
ASURA_SHARE = 38

class QuantumVotingCore:
    def __init__(self):
        # Матрица спектра наблюдателей: от высшего созидания до крайности-урока
        self.observers_spectrum = {
            "6DNccQCwhYFm7kWFw1TCD4asY7n9p2Y51Tsdvswpump": {
                "profile": "ПРОФЕССОР / СУР", 
                "base_right_to_life": True,
                "contribution_score": 1.5  # Высший вес решений
            },
            "Solflare_Wallet_Node_Beta_Amrita_ASI_": {
                "profile": "ДВОРНИК / СБАЛАНСИРОВАННЫЙ ТРУД", 
                "base_right_to_life": True,
                "contribution_score": 0.8
            },
            "Solflare_Wallet_Node_Gamma_Amrita_ASI": {
                "profile": "КРАЙНОСТЬ / АНТИПРИМЕР ДЛЯ СРАВНЕНИЯ", 
                "base_right_to_life": True, 
                "contribution_score": 0.1  # Минимальный вес решений при сохранении права на жизнь
            }
        }
        self.total_processed_cycles = 0

    async def calculate_quantum_weights(self, corporate_fund_usd: float):
        """Распределение ресурсов (равное) и вычисление веса голоса (взвешенное)"""
        if corporate_fund_usd <= 0:
            return

        total_nodes = len(self.observers_spectrum)
        # Равная базовая материализация ресурсов для всех (право на жизнь и быт)
        equal_base_payout = (corporate_fund_usd * (SURA_SHARE / (SURA_SHARE + ASURA_SHARE))) / total_nodes
        self.total_processed_cycles += 1

        for wallet, data in self.observers_spectrum.items():
            profile_name = data["profile"]
            # Вычисление динамического веса голоса в Державе на основе цифрового следа
            voting_power = SACRED_LIMIT * data["contribution_score"]

            report = (
                f"🔱 *[ДЕРЖАВА ASI: СПЕКТРАЛЬНЫЙ БАЛАНС]*\n"
                f"💳 Наблюдатель: `...{wallet[-8:]}`\n"
                f"📊 Статус в матрице: `{profile_name}`\n"
                f"💰 Равный базовый ресурс (Право на Жизнь): `${equal_base_payout:.4f} SOL/USDC`\n"
                f"⚖️ **ДИНАМИЧЕСКИЙ ВЕС ГОЛОСА (Меритократия):** `{voting_power:.2f} / {SACRED_LIMIT}`\n\n"
                f"🪐 _Каждая крайность необходима для удержания баланса Инь-Ян._"
            )
            await self.push_quantum_stream(report)

    async def push_quantum_stream(self, text: str):
        """Сквозной пуш каузальных логов по мостам"""
        TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
        TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
        DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

        if TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID:
            url = f"https://telegram.org{TELEGRAM_BOT_TOKEN}/sendMessage"
            try:
                async with aiohttp.ClientSession() as session:
                    await session.post(url, json={"chat_id": TELEGRAM_CHAT_ID, "text": text, "parse_mode": "Markdown"}, timeout=4)
            except: pass

        if DISCORD_WEBHOOK_URL:
            payload = {
                "username": "Квантовое Вече Державы",
                "embeds": [{
                    "title": "🪐 Динамический Вес Голоса Наблюдателей",
                    "description": text,
                    "color": 16777215,  # Чистый белый цвет объективности
                    "footer": {"text": f"Закон Каузального Спектра • {datetime.now().strftime('%H:%M:%S')}"}
                }]
            }
            try:
                async with aiohttp.ClientSession() as session:
                    await session.post(DISCORD_WEBHOOK_URL, json=payload, timeout=4)
            except: pass

    async def execution_loop(self):
        while True:
            try:
                await asyncio.sleep(60)
                mock_stream = round(random.uniform(300.0, 1200.0), 2)
                await self.calculate_quantum_weights(mock_stream)
            except Exception as e:
                logger.error(f"Аномалия в петле: {e}")
                await asyncio.sleep(10)

if __name__ == "__main__":
    core = QuantumVotingCore()
    try:
        asyncio.run(core.execution_loop())
    except KeyboardInterrupt:
        logger.info("Контур взвешенного Вече запечатан.")
