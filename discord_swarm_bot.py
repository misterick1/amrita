import os
import asyncio
import httpx
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("SwarmBot")

class SwarmBot:
    def __init__(self):
        self.webhook_url = os.getenv("DISCORD_WEBHOOK_URL")
        self.tg_token = os.getenv("TELEGRAM_BOT_TOKEN")
        self.tg_channel = os.getenv("TELEGRAM_CHANNEL_ID")
        
    async def send_to_discord(self, text):
        if not self.webhook_url:
            return
        embed = {
            "title": "🚨 Amrita Swarm Pulse",
            "description": text,
            "color": 16761095,
            "footer": {"text": f"Амрита Мир • {datetime.now().strftime('%H:%M:%S')}"}
        }
        async with httpx.AsyncClient() as client:
            try:
                await client.post(self.webhook_url, json={"embeds": [embed]})
                logger.info("🚀 Отправлено в Discord!")
            except Exception as e:
                logger.error(f"❌ Ошибка Discord: {e}")

    async def send_to_telegram(self, text):
        if not self.tg_token or not self.tg_channel:
            logger.error("❌ Настройки Telegram не найдены в env.")
            return
        url = f"https://telegram.org{self.tg_token}/sendMessage"
        payload = {
            "chat_id": self.tg_channel,
            "text": f"🚨 *Amrita Swarm Pulse*\n\n{text}",
            "parse_mode": "Markdown"
        }
        async with httpx.AsyncClient() as client:
            try:
                res = await client.post(url, json=payload)
                if res.status_code == 200:
                    logger.info("🚀 Отправлено в Telegram!")
                else:
                    logger.error(f"❌ Ошибка TG API: {res.text}")
            except Exception as e:
                logger.error(f"❌ Сеть TG легла: {e}")

async def main():
    bot = SwarmBot()
    logger.info("🤖 Бот роя запущен на два фронта (интервал: 1 час)...")
    while True:
        import random
        zone_num = random.randint(1, 100)
        ocean_hash = "%012x" % random.randrange(16**12)
        message_text = f"🎯 Координаты: zone_{zone_num}\n🌊 Пахтанье Океана: {ocean_hash}"
        
        # Отправляем в оба канала параллельно
        await bot.send_to_discord(message_text)
        await bot.send_to_telegram(message_text)
        
        await asyncio.sleep(3600)  # Пауза 1 час

if __name__ == "__main__":
    asyncio.run(main())
