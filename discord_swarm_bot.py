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
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")
logger = logging.getLogger("DiscordSwarm")

# Считываем настройки из секретов репозитория, которые вы добавили
DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")  
DISCORD_CHANNEL_ID = os.getenv("DISCORD_CHANNEL_ID")  
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")  

class DiscordSwarmBot:
    def __init__(self):
        self.history_of_shots = []
        self.total_amrita_extracted = 0
        self.webhook_url = DISCORD_WEBHOOK_URL

    async def auto_create_webhook_if_needed(self):
        """Автоматическое создание вебхука кодом через API Discord"""
        if self.webhook_url and "api/webhooks" in self.webhook_url and not self.webhook_url.endswith("/X"):
            logger.info("✅ Рабочий URL вебхука уже задан. Пропускаем создание.")
            return True

        token = DISCORD_BOT_TOKEN
        channel = DISCORD_CHANNEL_ID if DISCORD_CHANNEL_ID else "1515129009153769592"

        if not token:
            logger.error("❌ Ошибка: Не найден DISCORD_BOT_TOKEN в секретах GitHub для автосоздания.")
            return False

        logger.info(f"⚙️ Попытка создать вебхук для канала ID: {channel}...")
        url = f"https://discord.com{channel}/webhooks"
        headers = {
            "Authorization": f"Bot {token}",
            "Content-Type": "application/json"
        }
        payload = {"name": "Солитон: Медиа Сеть"}

        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(url, headers=headers, json=payload)
                if response.status_code == 200 or response.status_code == 201:
                    webhook_data = response.json()
                    self.webhook_url = webhook_data.get("url")
                    logger.info(f"🔥 Успех! Создан новый вебхук: {self.webhook_url}")
                    return True
                else:
                    logger.error(f"❌ Discord вернул код: {response.status_code}, Ответ: {response.text}")
            except Exception as e:
                logger.error(f"❌ Исключение при создании вебхука: {e}")
        return False

    async def calculate_tactical(self) -> str:
        available_cells = [f"zone_{random.randint(1, 108)}" for _ in range(5)]
        target_shot = random.choice(available_cells)
        self.history_of_shots.append(target_shot)
        return target_shot

    def load_cybernet_telemetry(self) -> tuple:
        state_file = "cybernet_state.json"
        if os.path.exists(state_file):
            try:
                with open(state_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    return data.get("power_hz", 1000.0), data.get("shield_status", "ACTIVE")
            except Exception as e:
                pass
        return 1000.0, "ACTIVE"

    def churn_samudra_manthan(self) -> tuple:
        data_stream = f"Cybernet_Core_Stream_{time.time()}_{random.random()}"
        sha = hashlib.sha256(data_stream.encode('utf-8')).hexdigest()
        extracted = 1000 if ("7" in sha or "a" in sha) else 108
        self.total_amrita_extracted += extracted
        return sha[:16], extracted, self.total_amrita_extracted

    async def send_game_coordinates(self):
        if not self.webhook_url or "api/webhooks" not in self.webhook_url:
            logger.error("❌ Отмена отправки: Рабочий URL вебхука отсутствует.")
            return

        coordinate = await self.calculate_tactical()
        hz_power, shield_status = self.load_cybernet_telemetry()
        ocean_sha, amrita_step, amrita_total = self.churn_samudra_manthan()
        
        current_hour = datetime.now().hour
        is_solflare_night = True if (current_hour >= 22 or current_hour <= 5) else False
        
        title_text = "🚨 Solflare Swarm Update" if is_solflare_night else "☀️ Amrita Swarm Pulse"
        color_code = 16761095  

        embed = {
            "title": title_text,
            "description": "Специальные тактические координаты сгенерированы Роем Агентов.",
            "color": color_code,
            "fields": [
                {"name": "🎯 Координаты тактические", "value": f"`{coordinate}`", "inline": True},
                {"name": "🌌 Статус сети", "value": f"`⚡ {hz_power} Hz`", "inline": True},
                {"name": "🛡️ Квантовый Щит Оркестратора", "value": f"`{shield_status}`", "inline": True},
                {"name": "🌊 Пахтанье Океана (SHA-256)", "value": f"`{ocean_sha}`", "inline": False},
                {"name": "💎 Накоплено Амриты в текущем цикле", "value": f"`+{amrita_step} (Всего: {amrita_total})`", "inline": False}
            ],
            "footer": {"text": f"Оркестратор Суверенного Мира • {datetime.now().strftime('%H:%M:%S')}"}
        }

        payload = {"username": "Солитон: Медиа Сеть", "embeds": [embed]}

        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(self.webhook_url, json=payload)
                if response.status_code == 200 or response.status_code == 204:
                    logger.info("🚀 Квантовый эмбед успешно отправлен в Дискорд")
                else:
                    logger.error(f"❌ Вебхук вернул код ошибки: {response.status_code}")
            except Exception as e:
                logger.error(f"❌ Ошибка соединения: {e}")

async def main():
    bot = DiscordSwarmBot()
    logger.info("🚀 Бот-оркестратор запущен в инфополе Амрита.")
    
    # Автосоздание вебхука при старте
    await bot.auto_create_webhook_if_needed()
    
    while True:
        await bot.send_game_coordinates()
        logger.info("💤 Тактический цикл завершен. Сон 10 секунд...")
        await asyncio.sleep(10)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("🚨 Бот остановлен.")
