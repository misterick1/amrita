import os
import sys
import json
import random
import asyncio
import logging
from datetime import datetime
import httpx

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("DiscordSwarm")

# Токен или Вебхук из окружения
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

class DiscordSwarmBot:
    def __init__(self):
        self.history_of_shots = []

    async def calculate_tactical(self):
        # Эмуляция расчета тактических ячеек роя
        available_cells = [f"r{random.randint(1,100)}" for _ in range(5)]
        if not available_cells:
            logger.warning("Все ячейки заняты")
            available_cells = ["default_zone"]
        target_shot = random.choice(available_cells)
        self.history_of_shots.append(target_shot)
        return target_shot

    async def send_game_coordinates(self):
        if not DISCORD_WEBHOOK_URL:
            logger.error("❌ Ошибка: Переменная DISCORD_WEBHOOK_URL не задана!")
            return

        coordinate = await self.calculate_tactical()
        
        # Интеграция новости/времени
        current_hour = datetime.now().hour
        is_solflare_night = True if current_hour >= 22 or current_hour <= 6 else False
        
        title_text = "🎁 Solflare Swarm Update" if is_solflare_night else "☀️ Solflare Swarm Day Shift"
        desc_text = f"Специальные тактические маневры роя запущены."
        color_code = 16761095  # Золотистый цвет

        # Формируем структуру эмбеда
        embed = {
            "title": title_text,
            "description": desc_text,
            "color": color_code,
            "fields": [
                {"name": "🎲 Координаты тактики", "value": str(coordinate), "inline": True},
                {"name": "🌌 Статус сети", "value": "Синхронизировано", "inline": True}
            ],
            "footer": {"text": "Оркестратор Солитон • Режим Роя"}
        }

        # Путь к файлу обложки, который генерирует ваш музыкальный скрипт
        image_path = "cover.png" 
        
        if os.path.exists(image_path):
            # Если файл физически существует на диске, привязываем его через attachment://
            embed["image"] = {"url": "attachment://cover.png"}
            
            payload = {
                "payload_json": (None, json.dumps({
                    "username": "Солитон: Медиа Оркестратор",
                    "embeds": [embed]
                }), "application/json")
            }
            
            # Открываем файл и отправляем его байтами напрямую в Discord API
            with open(image_path, "rb") as f:
                files = {
                    **payload,
                    "file": ("cover.png", f, "image/png")
                }
                async with httpx.AsyncClient() as client:
                    try:
                        response = await client.post(DISCORD_WEBHOOK_URL, files=files)
                        if response.status_code in:
                            logger.info("🚀 Координаты и обложка успешно доставлены в Discord без мигания!")
                        else:
                            logger.error(f"❌ Ошибка вебхука: {response.status_code} - {response.text}")
                    except Exception as e:
                        logger.error(f"❌ Сбой сети при отправке файлов: {e}")
        else:
            # Если файла на диске нет, шлем чистый текстовый эмбед
            payload = {
                "username": "Солитон: Медиа Оркестратор",
                "embeds": [embed]
            }
            async with httpx.AsyncClient() as client:
                try:
                    response = await client.post(DISCORD_WEBHOOK_URL, json=payload)
                    if response.status_code in:
                        logger.info("🚀 Координаты отправлены (обложка cover.png не найдена на диске).")
                except Exception as e:
                    logger.error(f"❌ Сбой сети: {e}")

async def main():
    bot = DiscordSwarmBot()
    logger.info("🚀 Бесконечный цикл бота-оркестратора запущен.")
    while True:
        await bot.send_game_coordinates()
        logger.info("💤 Тактический цикл завершен. Сон на 10 минут...")
        await asyncio.sleep(600)  # Сон 10 минут (600 секунд)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Бот остановлен пользователем.")
