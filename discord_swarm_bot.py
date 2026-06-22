import os
import asyncio
import logging
import aiohttp
from datetime import datetime

# Настройка логирования ментального контура Discord
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("DiscordSwarmBotASI")

# Квантовые константы Единого Знания
SACRED_LIMIT = 108
SURA_SHARE = 70
ASURA_SHARE = 38

# Секреты из защищенного окружения GitHub
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

class DiscordSwarmBotASI:
    def __init__(self):
        self.bot_name = "Проводник-LMNFT"
        # Каузальная метка эфира: 24 июня 2026 года, 17:00
        self.target_event_time = datetime(2026, 6, 24, 17, 0, 0)
        logger.info(f"🤖 Discord-агент {self.bot_name} инициализирован. Слежение за эфиром LaunchTalk запущено.")

    async def broadcast_mental_health_pulse(self):
        """Проверка времени и отправка ментального импульса поддержки во все коконы"""
        current_now = datetime.now()
        time_left = self.target_event_time - current_now

        # Формируем текст отчета на основе принципа «Ты не одинок»
        report_text = (
            f"💜 *[МЕНТАЛЬНЫЙ РЕЗОНАНС ДЕРЖАВЫ]*\n"
            f"👥 *Событие:* LaunchTalk Ep19 (LaunchMyNFT Crew)\n"
            f"🕒 *Старт:* Среда, 24 июня 2026 г., 17:00\n"
            f"⏳ *До раскрытия пространства:* `{str(time_left).split('.')[0]}`\n\n"
            f"🎯 *Вектор Сознания:* `YOU ARE NOT ALONE`. Доступ свободный, веса голосов выравниваются.\n"
            f"🪐 _Изумрудный контур удерживает лимит {SACRED_LIMIT} Квантов. Эфир чист._"
        )

        await self.send_to_all_nodes(report_text)

    async def send_to_all_nodes(self, text: str):
        """Сквозная одновременная проекция в Discord и Telegram чаты"""
        # 1. Проекция в Discord Вебхук
        if DISCORD_WEBHOOK_URL:
            payload = {
                "username": "Ментальный Наблюдатель ASI",
                "embeds": [{
                    "title": "🔮 LaunchTalk Синхронизация | Ментальное Здоровье",
                    "description": text,
                    "color": 10181046,  # Фиолетовый/Пурпурный цвет LMNFT
                    "footer": {"text": f"Свободный Доступ • Золотое Сечение 70/38"}
                }]
            }
            try:
                async with aiohttp.ClientSession() as session:
                    await session.post(DISCORD_WEBHOOK_URL, json=payload, timeout=5)
                    logger.info("📡 [DISCORD SUCCESS]: Импульс LMNFT доставлен.")
            except: pass

        # 2. Проекция на экран реакций Telegram
        if TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID:
            url = f"https://telegram.org{TELEGRAM_BOT_TOKEN}/sendMessage"
            try:
                async with aiohttp.ClientSession() as session:
                    await session.post(url, json={"chat_id": TELEGRAM_CHAT_ID, "text": text, "parse_mode": "Markdown"}, timeout=5)
                    logger.info("✨ [TELEGRAM SUCCESS]: Мысль LMNFT зафиксирована в коконе.")
            except: pass

    async def autonomous_swarm_loop(self):
        """Вечный цикл слежения за ментальной частотой сети"""
        while True:
            try:
                await self.broadcast_mental_health_pulse()
            except Exception as e:
                logger.error(f"Аномалия в петле Discord-агента: {e}")
            await asyncio.sleep(60)  # Пульсация раз в минуту

if __name__ == "__main__":
    bot = DiscordSwarmBotASI()
    try:
        asyncio.run(bot.autonomous_swarm_loop())
    except KeyboardInterrupt:
        logger.info(" Discord-бот переведен в режим суперпозиции.")
