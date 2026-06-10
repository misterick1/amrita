import os
import logging
import asyncio
import random
import httpx
from dotenv import load_dotenv

# Настройка логирования под "Единый Квантовый Оркестратор"
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - [%(filename)s] - %(message)s")
logger = logging.getLogger("DiscordSwarmBot")

load_dotenv()

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL", "https://discord.com")

class DiscordSwarmBot:
    def __init__(self):
        # Координатная сетка Морского боя Solflare (Ряды A-G, Колонки 1-5)
        self.rows = ["A", "B", "C", "D", "E", "F", "G"]
        self.cols = ["1", "2", "3", "4", "5"]
        self.history_of_shots = [] # Сюда бот сохраняет промахи, чтобы не стрелять дважды
        logger.info("Бот DiscordSwarmBot переведен в тактический режим 'Empire Game Night: Treasure Fleet'.")

    async def calculate_tactical_shot(self) -> str:
        """Алгоритм выбора оптимальной клетки для выстрела на основе исключения прошлых ходов"""
        available_cells = [f"{r}{c}" for r in self.rows for c in self.cols if f"{r}{c}" not in self.history_of_shots]
        
        if not available_cells:
            logger.warning("Все клетки на поле боя исчерпаны. Сброс истории.")
            self.history_of_shots.clear()
            available_cells = [f"{r}{c}" for r in self.rows for c in self.cols]

        # ИИ-выбор случайной живой клетки из доступных
        target_shot = random.choice(available_cells)
        self.history_of_shots.append(target_shot)
        return target_shot

    async def send_game_coordinate(self, team: str = "Blue"):
        """Отправляет выверенную координату для атаки в чат игры"""
        if "your_actual_token" in DISCORD_WEBHOOK_URL:
            logger.warning("Пропуск отправки: DISCORD_WEBHOOK_URL содержит заглушку.")
            return

        coordinate = await self.calculate_tactical_shot()
        logger.info(f"🎯 Тактический расчет завершен. Команда {team} наносит удар по координате {coordinate}")

        payload = {
            "username": "Солитон: Тактический Координатор",
            "embeds": [
                {
                    "title": "🚢 Empire Game Night: Огонь по флоту!",
                    "description": f"Автономный расчет траектории для команды **{team}**.",
                    "color": 3447003 if team == "Blue" else 15158332, # Синий или Красный цвет карточки
                    "fields": [
                        {"name": "Рекомендованная цель", "value": f"🎯 **`{coordinate}`**", "inline": True},
                        {"name": "Окно атаки", "value": "`⏱️ 30 секунд`", "inline": True}
                    ],
                    "footer": {"text": "Fractal Lego Builder | Модуль тактической координации"}
                }
            ]
        }

        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(DISCORD_WEBHOOK_URL, json=payload, timeout=5.0)
                if response.status_code == 204:
                    logger.info(f"Координата {coordinate} успешно передана на пульт управления.")
            except Exception as e:
                logger.error(f"Сбой отправки тактической команды: {e}")

# Эмуляция запуска тактического раунда
if __name__ == "__main__":
    bot = DiscordSwarmBot()
    asyncio.run(bot.send_game_coordinate(team="Blue"))
