import os
import logging
import asyncio
import random
import httpx
from datetime import datetime
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("DiscordSwarmBot")

load_dotenv()

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

class DiscordSwarmBot:
    def __init__(self):
        self.rows = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        self.cols = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        self.history_of_shots = []
        logger.info("Бот DiscordSwarmBot успешно инициализирован.")

    async def calculate_tactical_shot(self) -> str:
        available_cells = [f"{r}{c}" for r in self.rows for c in self.cols if f"{r}{c}" not in self.history_of_shots]
        if not available_cells:
            logger.warning("Все клетки поражены! Очистка истории выстрелов.")
            self.history_of_shots.clear()
            available_cells = [f"{r}{c}" for r in self.rows for c in self.cols]
        target_shot = random.choice(available_cells)
        self.history_of_shots.append(target_shot)
        return target_shot

    async def send_game_coordinate(self, team: str):
        if not DISCORD_WEBHOOK_URL or "your_actual_webhook_url" in DISCORD_WEBHOOK_URL:
            return

        coordinate = await self.calculate_tactical_shot()

        # Интеграция новости: Проверка специального раунда
        current_hour = datetime.utcnow().hour
        is_solflare_night = True  # Активируем раунд

        title_text = "🎁 Solflare Pack Opening Alert!"
        desc_text = f"Специальный тактический раунд запущен для команды {team}!"
        color_code = 16761095 if is_solflare_night else 3447003

        payload = {
            "username": f"Солитон: Игровой Оркестратор ({team})",
            "embeds": [
                {
                    "title": title_text,
                    "description": desc_text,
                    "color": color_code,
                    "fields": [
                        {"name": "Рекомендованная цель", "value": f"🎯 Клетка **{coordinate}**", "inline": True},
                        {"name": "Статус паков", "value": "📦 Доступны для минта", "inline": True}
                    ],
                    "footer": {"text": f"Fractal Lego Builder • {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC"}
                }
            ]
        }

        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(DISCORD_WEBHOOK_URL, json=payload)
                if response.ok:
                    logger.info(f"Координата {coordinate} отправлена в Discord.")
            except Exception as e:
                logger.error(f"Сбой отправки: {e}")

async def main():
    bot = DiscordSwarmBot()
    logger.info("🚀 Бесконечный тактический цикл запущен...")
    while True:
        await bot.send_game_coordinate(team="Empire")
        logger.info("💤 Тактический раунд завершен.")
        await asyncio.sleep(600)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Бот остановлен.")
