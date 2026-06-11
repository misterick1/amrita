import os
import logging
import asyncio
import random
import httpx
from dotenv import load_dotenv

# Настройка логирования под "Единый Квантовый Оркестратор"
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("DiscordSwarmBot")

load_dotenv()

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

class DiscordSwarmBot:
    def __init__(self):
        # Координатная сетка Морского боя
        self.rows = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        self.cols = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        self.history_of_shots = []
        logger.info("Бот DiscordSwarmBot переведен в тактический режим.")

    async def calculate_tactical_shot(self) -> str:
        """Алгоритм выбора оптимальной клетки для удара роя"""
        available_cells = [f"{r}{c}" for r in self.rows for c in self.cols if f"{r}{c}" not in self.history_of_shots]
        
        if not available_cells:
            logger.warning("Все клетки на поле поражены! Очистка истории раундов.")
            self.history_of_shots.clear()
            available_cells = [f"{r}{c}" for r in self.rows for c in self.cols]
            
        target_shot = random.choice(available_cells)
        self.history_of_shots.append(target_shot)
        return target_shot

    async def send_game_coordinate(self, team: str = "Empire"):
        """Отправляет выверенную координату для тактического раунда роя в Дискорд"""
        if not DISCORD_WEBHOOK_URL or "your_actual_token" in DISCORD_WEBHOOK_URL:
            logger.warning("Пропуск отправки: DISCORD_WEBHOOK_URL не настроен.")
            return

        coordinate = await self.calculate_tactical_shot()
        logger.info(f"🎯 Тактический расчет завершен. Команда {team} наносит удар по координате {coordinate}")

        payload = {
            "username": f"Солитон: Тактический Координатор ({team})",
            "embeds": [
                {
                    "title": f"🚢 Empire Game Night: Наведение Роя",
                    "description": f"Автономный расчет траектории в рамках экосистемы AMRITA.",
                    "color": 3447003 if team == "Empire" else 15158332,
                    "fields": [
                        {"name": "Рекомендованная цель", "value": f"💥 `{coordinate}`", "inline": True},
                        {"name": "Окно атаки", "value": "`Активно`", "inline": True}
                    ],
                    "footer": {"text": f"Fractal Lego Builder Swarm Mode | Зарядов в истории: {len(self.history_of_shots)}"}
                }
            ]
        }

        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(DISCORD_WEBHOOK_URL, json=payload)
                if response.status_code in:
                    logger.info(f"Координата {coordinate} успешно отправлена в Discord.")
            except Exception as e:
                logger.error(f"Сбой отправки тактического раунда: {e}")

async def main():
    bot = DiscordSwarmBot()
    logger.info("🚀 Бесконечный тактический цикл запущен в ядре Python.")
    
    while True:
        # Запускаем раунд для вашей команды
        await bot.send_game_coordinate(team="Empire")
        
        # Задержка между ходами. Измените 600 (10 минут) на любое нужное вам число секунд
        logger.info("💤 Тактический раунд завершен. Ожидание 10 минут перед следующим расчетом...")
        await asyncio.sleep(600)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Бот остановлен пользователем.")
