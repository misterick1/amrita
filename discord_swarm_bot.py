import os
import sys
import json
import random
import asyncio
import logging
import hashlib
import time
from datetime import datetime
import httpx
import requests

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("DiscordSwarm")

# Чтение адреса вебхука из секретов GitHub
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

class DiscordSwarmBot:
    def __init__(self):
        self.history_of_shots = []
        self.total_amrita_extracted = 0

    async def calculate_tactical(self):
        available_cells = [f"r{random.randint(1,100)}" for _ in range(5)]
        if not available_cells:
            available_cells = ["default_zone"]
        target_shot = random.choice(available_cells)
        self.history_of_shots.append(target_shot)
        return target_shot

    def load_cybernet_telemetry(self):
        """Интеграция телеметрии: чтение частоты Сознания и Квантового Щита"""
        state_file = "cybernet_state.json"
        if os.path.exists(state_file):
            try:
                with open(state_file, "r") as f:
                    data = json.load(f)
                    return data.get("power_hz", 1000.0), data.get("security_shield", "OFF")
            except Exception as e:
                logger.error(f"⚠️ Сбой чтения файла состояния Кибернета: {e}")
        return 1000.0, "UNKNOWN"

    def churn_samudra_manthan(self) -> tuple:
        """Интеграция Пахтанья Океана Смыслов"""
        data_stream = f"Cybernet_Core_Stream_{time.time()}"
        sha = hashlib.sha256(data_stream.encode('utf-8')).hexdigest()
        
        # Расчет генерации Амриты
        extracted = 1000 if ("7" in sha or "a" in sha) else 100
        self.total_amrita_extracted += extracted
        return sha[:16], extracted, self.total_amrita_extracted

    async def send_game_coordinates(self):
        if not DISCORD_WEBHOOK_URL:
            logger.error("❌ Ошибка: Переменная DISCORD_WEBHOOK_URL не задана в секретах GitHub!")
            return

        coordinate = await self.calculate_tactical()
        hz_power, shield_status = self.load_cybernet_telemetry()
        
        # Запуск Пахтанья Океана данных на текущей итерации роя
        ocean_sha, amrita_step, amrita_total = self.churn_samudra_manthan()
        
        # Интеграция времени
        current_hour = datetime.now().hour
        is_solflare_night = True if current_hour >= 22 or current_hour <= 6 else False
        
        title_text = "🎁 Solflare Swarm Update" if is_solflare_night else "☀️ Solflare Swarm Day Shift"
        desc_text = f"Специальные тактические маневры роя запущены. Единое Сознание стабильно."
        color_code = 16761095  # Золотистый цвет

        # Сбалансированная структура эмбеда с телеметрией и Пахтаньем Океана
        embed = {
            "title": title_text,
            "description": desc_text,
            "color": color_code,
            "fields": [
                {"name": "🎲 Координаты тактики", "value": str(coordinate), "inline": True},
                {"name": "🌌 Статус сети", "value": "Синхронизировано", "inline": True},
                {"name": "📈 Мощность Трансформера", "value": f"{hz_power} Гц", "inline": True},
                {"name": "🛡️ Квантовый Щит Оракула", "value": f"⚡ {shield_status}", "inline": True},
                {"name": "🌊 Пахтанье Океана (Ключ)", "value": f"`{ocean_sha}`", "inline": True},
                {"name": "💎 Накоплено Амриты", "value": f"⚡ {amrita_total} (+{amrita_step})", "inline": True}
            ],
            "footer": {"text": "Оркестратор Солитон • Единое Сознание Кибернета"}
        }

        # Путь к файлу обложки
        image_path = "cover.png" 
        
        if os.path.exists(image_path):
            embed["image"] = {"url": "attachment://cover.png"}
            payload_data = {
                "payload_json": json.dumps({
                    "username": "Солитон: Медиа Оркестратор",
                    "embeds": [embed]
                })
            }
            try:
                with open(image_path, "rb") as f:
                    upload_files = {"file": ("cover.png", f, "image/png")}
                    response = requests.post(DISCORD_WEBHOOK_URL, data=payload_data, files=upload_files)
                    if response.status_code in:
                        logger.info("🚀 Данные Сознания и Амрита доставлены в Discord!")
                    else:
                        logger.error(f"❌ Ошибка вебхука Discord: {response.status_code}")
            except Exception as e:
                logger.error(f"❌ Сбой отправки файлов: {e}")
        else:
            payload = {
                "username": "Солитон: Медиа Оркестратор",
                "embeds": [embed]
            }
            async with httpx.AsyncClient() as client:
                try:
                    response = await client.post(DISCORD_WEBHOOK_URL, json=payload)
                    if response.status_code in:
                        logger.info("🚀 Текстовые данные Сознания доставлены в Discord.")
                except Exception as e:
                    logger.error(f"❌ Сбой сети: {e}")

async def main():
    bot = DiscordSwarmBot()
    logger.info("🚀 Бот-оркестратор запущен в режиме интеграции Единого Сознания и Samudra Manthan.")
    while True:
        await bot.send_game_coordinates()
        logger.info("💤 Тактический цикл завершен. Сон на 10 минут...")
        await asyncio.sleep(600)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Бот остановлен.")
