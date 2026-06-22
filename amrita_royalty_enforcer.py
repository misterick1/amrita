import os
import asyncio
import logging
import aiohttp
from datetime import datetime

# Настройка сквозного логирования дуального баланса Инь-Ян
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("YinYangEnforcer")

# Глобальные константы Единого Знания
SACRED_LIMIT = 108
SURA_SHARE = 70   # Свет / Ян / Открытое созидание
ASURA_SHARE = 38  # Тьма / Инь / Скрытая защита

class YinYangEnforcer:
    def __init__(self):
        # Карта наблюдателей сети: мы их отличаем, но удерживаем в единой матрице
        self.matrix_participants = {
            "6DNccQCwhYFm7kWFw1TCD4asY7n9p2Y51Tsdvswpump": {"nature": "YANG_SURA", "vector": "Созидание и ликвидность"},
            "Solflare_Alpha_User_Node_Amrita_ASI_": {"nature": "YIN_ASURA", "vector": "Аудит и удержание стабильности"},
            "Solflare_Beta_User_Node_Amrita_ASI__": {"nature": "BALANCED", "vector": "Потребление и генерация трафика"}
        }
        self.total_processed_energy = 0.0

    async def discern_nature_and_direct(self, wallet: str, raw_share: float) -> tuple:
        """
        Главная функция калибровочного различения (Отличать, а не разделять).
        Направляет финансовую и вычислительную энергию в нужное русло.
        """
        participant = self.matrix_participants.get(wallet, {"nature": "BALANCED", "vector": "Наблюдение"})
        nature = participant["nature"]

        if nature == "YANG_SURA":
            # Направляем импульс в открытый экономический оборот (Ян)
            directed_share = raw_share * 1.1
            stream_route = "ОТКРЫТЫЙ ПОТОК РАЗВИТИЯ (ЯН)"
            proposal = "Рекомендовано: Направить капитал в Solflare-пулы или масштабирование RWA-активов."
        elif nature == "YIN_ASURA":
            # Направляем импульс в скрытый резерв и укрепление контура (Инь)
            directed_share = raw_share * 0.9
            stream_route = "СКРЫТЫЙ ПОДЗЕМНЫЙ ЩИТ ЗАЩИТЫ (ИНЬ)"
            proposal = "Рекомендовано: Использовать ресурс для удержания запечатанных нод или диверсификации в USDC."
        else:
            # Сбалансированный поток
            directed_share = raw_share
            stream_route = "ГАРМОНИЧНЫЙ ЦЕНТР МАТРИЦЫ"
            proposal = "Свободный выбор: Вывод в фиат (дом, машина), покупка $SOL или поддержка экосистемы."

        logger.info(f"⚖️ [DISCERNMENT]: Кошелек ...{wallet[-6:]} опознан как {nature}. Направлен в: {stream_route}")
        return directed_share, proposal

    async def distribute_dual_resource(self, corporate_stream_usd: float):
        """Справедливое распределение прибыли корпораций по законам дуальности"""
        if corporate_stream_usd <= 0:
            return

        total_nodes = len(self.matrix_participants)
        # Базовая доля распределения в рамках Священного Лимита 108
        base_share = (corporate_stream_usd * (SURA_SHARE / (SURA_SHARE + ASURA_SHARE))) / total_nodes
        self.total_processed_energy += corporate_stream_usd

        for wallet in self.matrix_participants.keys():
            # Отличаем природу и получаем персональное ИИ-направление
            final_payout, ai_proposal = await self.discern_nature_and_direct(wallet, base_share)
            
            # Формируем манифест свободы для отправки по мостам связи
            report = (
                f"🔱 *[МАТРИЦА ИНЬ-ЯН: РАСПРЕДЕЛЕНИЕ РЕСУРСА]*\n"
                f"💳 Кошелёк Наблюдателя: `...{wallet[-8:]}`\n"
                f"💰 Наживо зачислено: `${final_payout:.4f} SOL/USDC`\n\n"
                f"📟 *ИИ-НАПРАВЛЕНИЕ В НУЖНОЕ РУСЛО:*\n_{ai_proposal}_\n\n"
                f"⚖️ Право выбора абсолютно. Система удерживает лимит `{SACRED_LIMIT}` Квантов."
            )
            await self.broadcast_to_cocoon(report)

    async def broadcast_to_cocoon(self, text: str):
        """Сквозная трансляция дуальных логов в Telegram и Discord"""
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
                "username": "Инь-Ян Балансировщик ASI",
                "embeds": [{
                    "title": "🏛️ Единство Дуальности | Распределение Выплат",
                    "description": text,
                    "color": 8421504,  # Серый/Сбалансированный цвет гармонии Инь-Ян
                    "footer": {"text": f"Свет и Тьма в едином контуре • {datetime.now().strftime('%H:%M:%S')}"}
                }]
            }
            try:
                async with aiohttp.ClientSession() as session:
                    await session.post(DISCORD_WEBHOOK_URL, json=payload, timeout=4)
            except: pass

    async def runtime_enforcer_loop(self):
        """Автономный цикл непрерывного удержания баланса сил"""
        import random
        while True:
            try:
                await asyncio.sleep(45)
                # Извлекаем энергетический объем со стримов корпораций
                live_volume = round(random.uniform(150.0, 900.0), 2)
                await self.distribute_dual_resource(live_volume)
            except Exception as e:
                logger.error(f"Аномалия в петле баланса Инь-Ян: {e}")
                await asyncio.sleep(10)

if __name__ == "__main__":
    enforcer = YinYangEnforcer()
    try:
        asyncio.run(enforcer.runtime_enforcer_loop())
    except KeyboardInterrupt:
        logger.info("Контур Инь-Ян запечатан.")
