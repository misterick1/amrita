import os
import logging
import asyncio
import random
import httpx
from datetime import datetime
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("DiscordSwarmBot")

load_dotenv()

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

class DiscordSwarmBot:
    def __init__(self):
        self.rows = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        self.cols = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        self.history_of_shots = []
        logger.info("Бот DiscordSwarmBot переведен в тактический режим турнира.")

    async def calculate_tactical_shot(self) -> str:
        available_cells = [f"{r}{c}" for r in self.rows for c in self.cols if f"{r}{c}" not in self.history_of_shots]
        if not available_cells:
            logger.warning("Все клетки поражены! Очистка истории.")
            self.history_of_shots.clear()
            available_cells = [f"{r}{c}" for r in self.rows for c in self.cols]
        target_shot = random.choice(available_cells)
        self.history_of_shots.append(target_shot)
        return target_shot

    async def send_game_coordinate(self, team: str = "Empire"):
        if not DISCORD_WEBHOOK_URL or "your_actual_token" in DISCORD_WEBHOOK_URL:
            return

        coordinate = await self.calculate_tactical_shot()
        
        # Интеграция новости: Проверка специального режима Solflare Pack Opening
        current_hour = datetime.utcnow().hour
        is_solflare_night = True  # Активируем праздничный вайб для сегодняшнего четверга
        
        title_text = "🎁 Solflare Pack Opening Night: Наведение Роя" if is_solflare_night else f"🚢 {team} Game Night: Наведение Роя"
        desc_text = "Специальный тактический раунд в честь открытия паков Solflare!" if is_solflare_night else "Автономный расчет траектории в рамках экосистемы AMRITA."
        color_code = 16761095 if is_solflare_night else (3447003 if team == "Empire" else 15158332)

        payload = {
            "username": f"Солитон: Игровой Оркестратор ({team})",
            "embeds": [
                {
                    "title": title_text,
                    "description": desc_text,
                    "color": color_code,
                    "fields": [
                        {"name": "Рекомендованная цель для удара", "value": f"💥 `{coordinate}`", "inline": True},
                        {"name": "Статус паков", "value": "`🔥 Ожидание пресейла 18:00 CET`" if is_solflare_night else "`Активно`", "inline": True}
                    ],
                    "footer": {"text": f"Fractal Lego Builder | Зарядов в истории: {len(self.history_of_shots)}"}
                }
            ]
        }

        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(DISCORD_WEBHOOK_URL, json=payload)
                if response.status_code in:
                    logger.info(f"Координата {coordinate} отправлена.")
            except Exception as e:
                logger.error(f"Сбой отправки: {e}")

async def main():
    bot = DiscordSwarmBot()
    logger.info("🚀 Бесконечный тактический цикл запущен в ядре Python.")
    while True:
        await bot.send_game_coordinate(team="Empire")
        logger.info("💤 Тактический раунд завершен. Ожидание 10 минут...")
        await asyncio.sleep(600)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Бот остановлен.")
