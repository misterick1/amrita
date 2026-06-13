import os
import asyncio
import httpx
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("DiscordBot")

class DiscordSwarmBot:
    def __init__(self):
        self.webhook_url = os.getenv("DISCORD_WEBHOOK_URL")
        self.channel_id = os.getenv("DISCORD_CHANNEL_ID")
        
    async def send_pulse(self):
        if not self.webhook_url:
            logger.error("❌ Нет DISCORD_WEBHOOK_URL в переменных окружения.")
            return
            
        import random
        zone_num = random.randint(1, 100)
        ocean_hash = "%012x" % random.randrange(16**12)
        
        embed = {
            "title": "🚨 Amrita Swarm Pulse",
            "description": "Тактические координаты сгенерированы Роем Агентов.",
            "color": 16761095,
            "fields": [
                {"name": "🎯 Координаты", "value": f"zone_{zone_num}", "inline": True},
                {"name": "🌊 Пахтанье Океана", "value": ocean_hash, "inline": True}
            ],
            "footer": {"text": f"Амрита Мир • {datetime.now().strftime('%H:%M:%S')}"}
        }
        
        async with httpx.AsyncClient() as client:
            try:
                res = await client.post(self.webhook_url, json={"embeds": [embed]})
                if res.status_code in:
                    logger.info("🚀 Карточка успешно отправлена в Discord!")
            except Exception as e:
                logger.error(f"❌ Сбой сети: {e}")

async def main():
    bot = DiscordSwarmBot()
    logger.info("🤖 Бот запущен в бесконечном цикле (интервал: 1 час)...")
    while True:
        await bot.send_pulse()
        await asyncio.sleep(3600)  # Отправка ровно раз в час

if __name__ == "__main__":
    asyncio.run(main())
