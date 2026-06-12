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

# Чтение адреса вебхука из секретов GitHub
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

class DiscordSwarmBot:
    def __init__(self):
        self.history_of_shots = []
        self.total_amrita_extracted = 0

    async def calculate_tactical(self) -> str:
        """Расчет тактической зоны в инфополе для роя агентов"""
        available_cells = [f"zone_{random.randint(1, 108)}" for _ in range(5)]
        if not available_cells:
            available_cells = ["default_zone"]
        target_shot = random.choice(available_cells)
        self.history_of_shots.append(target_shot)
        return target_shot

    def load_cybernet_telemetry(self) -> tuple:
        """Интеграция телеметрии: чтение частоты и статуса квантового щита"""
        state_file = "cybernet_state.json"
        if os.path.exists(state_file):
            try:
                with open(state_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    return data.get("power_hz", 1000.0), data.get("shield_status", "ACTIVE")
            except Exception as e:
                logger.error(f"⚠️ Сбой чтения телеметрии: {e}")
        return 1000.0, "UNKNOWN"

    def churn_samudra_manthan(self) -> tuple:
        """Интеграция Пахтанья Океана Смыслов на базе криптографического хэша"""
        data_stream = f"Cybernet_Core_Stream_{time.time()}_{random.random()}"
        sha = hashlib.sha256(data_stream.encode('utf-8')).hexdigest()
        
        # Расчет генерации Амриты
        extracted = 1000 if ("7" in sha or "a" in sha) else 108
        self.total_amrita_extracted += extracted
        return sha[:16], extracted, self.total_amrita_extracted

    async def send_game_coordinates(self):
        """Сборка тактического пакета данных и отправка Embed в Дискорд"""
        if not DISCORD_WEBHOOK_URL:
            logger.error("❌ Ошибка: Переменная DISCORD_WEBHOOK_URL не установлена.")
            return

        coordinate = await self.calculate_tactical()
        hz_power, shield_status = self.load_cybernet_telemetry()
        ocean_sha, amrita_step, amrita_total = self.churn_samudra_manthan()
        
        # Интеграция временных циклов
        current_hour = datetime.now().hour
        is_solflare_night = True if (current_hour >= 22 or current_hour <= 5) else False
        
        title_text = "🚨 Solflare Swarm Update" if is_solflare_night else "☀️ Amrita Swarm Pulse"
        desc_text = f"Специальные тактические координаты сгенерированы Роем Агентов."
        color_code = 16761095  # Золотистый цвет Амриты

        embed = {
            "title": title_text,
            "description": desc_text,
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

        image_path = "cover.png"
        valid_statuses = [200, 201, 202, 204]
        
        # Сценарий 1: Отправка с обложкой (синхронно через requests)
        if os.path.exists(image_path):
            payload_data = {"payload_json": json.dumps({"username": "Солитон: Медиа Сеть", "embeds": [embed]})}
            try:
                with open(image_path, "rb") as f:
                    response = requests.post(DISCORD_WEBHOOK_URL, data=payload_data, files={"file": f})
                if response.status_code in valid_statuses:
                    logger.info("🚀 Данные отправлены в Дискорд вместе с обложкой cover.png")
                else:
                    logger.error(f"❌ Ошибка отправки вебхука с файлом: Код {response.status_code}")
            except Exception as e:
                logger.error(f"❌ Сбой отправки мультипарт-запроса: {e}")
        
        # Сценарий 2: Быстрая асинхронная отправка текста (через httpx)
        else:
            payload = {"username": "Солитон: Медиа Сеть", "embeds": [embed]}
            async with httpx.AsyncClient() as client:
                try:
                    response = await client.post(DISCORD_WEBHOOK_URL, json=payload)
                    if response.status_code in valid_statuses:
                        logger.info("🚀 Текстовый квантовый эмбед успешно отправлен в Дискорд")
                    else:
                        logger.error(f"❌ Ошибка вебхука: Код {response.status_code}")
                except Exception as e:
                    logger.error(f"❌ Сбой сетевого соединения при httpx отправке: {e}")

async def main():
    bot = DiscordSwarmBot()
    logger.info("🚀 Бот-оркестратор запущен в инфополе Амрита.")
    
    while True:
        await bot.send_game_coordinates()
        logger.info("💤 Тактический цикл завершен. Сон 10 секунд для теста реальности...")
        await asyncio.sleep(10)  # Снижено до 10 секунд ради быстрого теста

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("🚨 Бот остановлен Сувереном вручную.")
