import os, random, asyncio, logging, hashlib, time, httpx
from datetime import datetime

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s]: %(message)s")
logger = logging.getLogger("DiscordSwarm")

DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")  
DISCORD_CHANNEL_ID = os.getenv("DISCORD_CHANNEL_ID") or "1515129009153769592"
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")  

class DiscordSwarmBot:
    def __init__(self):
        self.webhook_url = DISCORD_WEBHOOK_URL

    async def auto_create_webhook(self):
        if self.webhook_url and "api/webhooks" in self.webhook_url:
            return True
        if not DISCORD_BOT_TOKEN:
            logger.error("❌ Нет токена бота в секретах GitHub.")
            return False
        
        url = f"https://discord.com{DISCORD_CHANNEL_ID}/webhooks"
        headers = {"Authorization": f"Bot {DISCORD_BOT_TOKEN}", "Content-Type": "application/json"}
        
        async with httpx.AsyncClient() as client:
            try:
                res = await client.post(url, headers=headers, json={"name": "Солитон: Медиа Сеть"})
                if res.status_code == 200 or res.status_code == 201:
                    self.webhook_url = res.json().get("url")
                    logger.info(f"🔥 Вебхук создан автоматически: {self.webhook_url}")
                    return True
                logger.error(f"❌ Discord отказал: {res.status_code}")
            except Exception as e:
                logger.error(f"❌ Ошибка API: {e}")
        return False

    async def send_pulse(self):
        if not self.webhook_url:
            return
        
        sha = hashlib.sha256(f"{time.time()}".encode()).hexdigest()[:16]
        embed = {
            "title": "🚨 Amrita Swarm Pulse",
            "description": "Тактические координаты сгенерированы Роем Агентов.",
            "color": 16761095,
            "fields": [
                {"name": "🎯 Координаты", "value": f"`zone_{random.randint(1, 108)}`", "inline": True},
                {"name": "🌊 Пахтанье Океана", "value": f"`{sha}`", "inline": False}
            ],
            "footer": {"text": f"Амрита Мир • {datetime.now().strftime('%H:%M:%S')}"}
        }

        async with httpx.AsyncClient() as client:
            try:
                res = await client.post(self.webhook_url, json={"username": "Солитон", "embeds": [embed]})
                if res.status_code == 200 or res.status_code == 204:
                    logger.info("🚀 Карточка успешно отправлена в Дискорд!")
            except Exception as e:
                logger.error(f"❌ Сбой сети: {e}")

async def main():
    bot = DiscordSwarmBot()
    logger.info("🚀 Бот-оркестратор запущен.")
    await bot.auto_create_webhook()
    while True:
        await bot.send_pulse()
        await asyncio.sleep(10)

if __name__ == "__main__":
    asyncio.run(main())
