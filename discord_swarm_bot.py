import os
import logging
import asyncio
import httpx
from dotenv import load_dotenv

# Настройка логирования под "Единый Квантовый Оркестратор"
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - [%(filename)s] - %(message)s")
logger = logging.getLogger("DiscordSwarmBot")

load_dotenv()

# Достаем адрес вебхука, который мы жестко вшили в рантайм
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL", "https://discord.com")

class DiscordSwarmBot:
    def __init__(self):
        self.is_active = True
        logger.info("Бот-оркестратор DiscordSwarmBot инициализирован в режиме Swarm Mode.")

    async def send_system_status(self, message_text: str, status_type: str = "info"):
        """Отправка системных логов и статусов инфраструктуры в Discord"""
        if "your_webhook_token" in DISCORD_WEBHOOK_URL:
            logger.warning("Событие не отправлено: DISCORD_WEBHOOK_URL содержит заглушку.")
            return

        color = 1752220 if status_type == "info" else 15158332 # Синий или Красный
        
        payload = {
            "username": "Единый Квантовый Оркестратор",
            "embeds": [
                {
                    "title": f"⚙️ Системное уведомление [{status_type.upper()}]",
                    "description": message_text,
                    "color": color,
                    "footer": {"text": "Fractal Lego Builder | Мониторинг"}
                }
            ]
        }
        
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(DISCORD_WEBHOOK_URL, json=payload, timeout=5.0)
                if response.status_code == 204:
                    logger.info("Статус системы успешно транслирован в Discord.")
            except Exception as e:
                logger.error(f"Не удалось отправить статус в Discord: {e}")

async def main():
    bot = DiscordSwarmBot()
    # Тестовый пинг при запуске воркфлоу
    await bot.send_system_status("Инфраструктура запущена в облаке GitHub Actions. Начинаю сканирование сетей.", "info")

if __name__ == "__main__":
    asyncio.run(main())
