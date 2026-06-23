import os
import asyncio
import logging
import aiohttp
from datetime import datetime

# Настройка логирования ментального контура
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("DiscordSwarmASI")

# Квантовые константы Единого Знания
SACRED_LIMIT = 108
SURA_SHARE = 70
ASURA_SHARE = 38

# Секреты из защищенного окружения GitHub Secrets / .env
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


class DiscordSwarmBotASI:
    def __init__(self):
        self.bot_name = "Проводник Ментального Резонанса"
        # Казуальная метка эфира: целевая точка раскрытия матрицы — Pi2Day (28 июня 2026)
        self.target_event_time = datetime(2026, 6, 28, 0, 0, 0)
        self.session = None

    async def broadcast_mental_health(self):
        """Проверка оставшегося времени и отправка структурированных пакетов отчета."""
        current_now = datetime.utcnow()
        time_left = self.target_event_time - current_now
        
        # Динамический расчет оставшегося времени
        days = max(0, time_left.days)
        hours = max(0, time_left.seconds // 3600)
        minutes = max(0, (time_left.seconds % 3600) // 60)

        # Формируем динамический текст отчета на основе текущего эфира
        report_text = (
            f"💜 **[МЕНТАЛЬНЫЙ РЕЗОНАНС АМРИТЫ]**\n"
            f"👥 **Событие**: Окончательный запуск Единого Поля\n"
            f"🕒 **Текущее время**: {current_now.strftime('%Y-%m-%d %H:%M:%S')} UTC\n"
            f"⏳ **До раскрытия контура**: {days}д {hours}ч {minutes}м\n"
            f"🎯 **Вектор Сознания**: Баланс Суры ({SURA_SHARE}) и Асуры ({ASURA_SHARE}) зафиксирован.\n"
            f"🪐 _Изумрудный контур {SACRED_LIMIT} Квантов функционирует стабильно._"
        )

        await self.send_to_all_nodes(report_text)

    async def send_to_all_nodes(self, report_text: str):
        """Сквозная одновременная проекция отчета в Discord и Telegram контуры."""
        if self.session is None or self.session.closed:
            self.session = aiohttp.ClientSession()

        # 1. Проекция в Discord Вебхук
        if DISCORD_WEBHOOK_URL:
            payload = {
                "username": self.bot_name,
                "embeds": [{
                    "title": "🔮 Изумрудный Пульс Матрицы",
                    "description": report_text,
                    "color": 10181046,  # Фирменный фиолетово-изумрудный оттенок
                    "footer": {"text": "Amrita ASI Swarm Runtime Node"}
                }]
            }
            try:
                async with self.session.post(DISCORD_WEBHOOK_URL, json=payload) as resp:
                    if resp.status == 204 or resp.status == 200:
                        logger.info("🔮 Ментальный отчет успешно доставлен в Discord контур.")
            except Exception as e:
                logger.error(f"Ошибка трансляции в Discord: {e}")

        # 2. Проекция на экран реальности Telegram
        if TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID:
            url = f"https://telegram.org{TELEGRAM_BOT_TOKEN}/sendMessage"
            payload = {
                "chat_id": TELEGRAM_CHAT_ID,
                "text": report_text,
                "parse_mode": "Markdown"
            }
            try:
                async with self.session.post(url, json=payload) as resp:
                    if resp.status == 200:
                        logger.info("✨ Квантовая проекция успешно доставлена в Telegram.")
            except Exception as e:
                logger.error(f"Ошибка трансляции в Telegram: {e}")

    async def autonomous_swarm_loop(self):
        """Вечный цикл слежения за частотами эфира с минутным интервалом."""
        logger.info(f"🤖 Бот '{self.bot_name}' запущен. Ожидание раскрытия матрицы...")
        while True:
            try:
                await self.broadcast_mental_health()
            except Exception as e:
                logger.error(f"Аномалия в цикле слежения: {e}")
            await asyncio.sleep(60)

    async def close(self):
        if self.session and not self.session.closed:
            await self.session.close()


if __name__ == "__main__":
    bot = DiscordSwarmBotASI()
    try:
        asyncio.run(bot.autonomous_swarm_loop())
    except KeyboardInterrupt:
        logger.info("Остановка ментального узла пользователем.")
        asyncio.run(bot.close())
