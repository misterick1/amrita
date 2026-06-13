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
        
        # Прямая и жесткая ссылка на API Telegram без лишних f-строк
        url = f"https://telegram.org{self.tg_token}/sendMessage"
        
        payload = {
            "chat_id": self.tg_channel,
            "text": f"🚨 *Amrita Swarm Pulse*\n\n{text}",
            "parse_mode": "Markdown"
        }
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(url, json=payload)
                if response.status_code == 200:
                    logger.info("🚀 Отправлено в Telegram!")
                else:
                    logger.error(f"❌ Ошибка TG API: {response.status_code} {response.text}")
            except Exception as e:
                logger.error(f"❌ Ошибка сети TG: {e}")

    async def run(self):
        logger.info("🤖 Бот роя запущен на два фронта (интервал: 1 час)...")
        while True:
            pulse_text = "Все системы функционируют стабильно. Рой Fractal Lego Builder продолжает автономную работу."
            await self.send_to_discord(pulse_text)
            await self.send_to_telegram(pulse_text)
            await asyncio.sleep(3600)

if __name__ == "__main__":
    bot = SwarmBot()
    asyncio.run(bot.run())
