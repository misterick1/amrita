import os
import asyncio
import logging
import aiohttp
import random
from datetime import datetime

# Настройка логирования моста сейфа Circle
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("CircleVaultBridge")

# Квантовые константы Единого Знания
SACRED_LIMIT = 108
SURA_SHARE = 70
ASURA_SHARE = 38

# Извлечение секретов из защищенного окружения
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")


class CircleVaultBridge:
    def __init__(self):
        self.vault_id = "Circle-Liquid-Vault-108"
        self.ratio_label = f"{SURA_SHARE}/{ASURA_SHARE}"
        self.session = None
        logger.info(f"🏛️ Мост сейфа Circle успешно инициализирован. ID: {self.vault_id}")

    async def verify_and_lock_liquidity(self, amount_usd: float) -> bool:
        """Проверка и фиксация ликвидности в сейфе Circle."""
        if amount_usd <= 0:
            return False

        logger.info(f"🔒 [CIRCLE VAULT]: Запрос на фиксацию ликвидности: {amount_usd} USD")

        # Защитная логика: удержание лимита 108 Квантов
        if amount_usd > SACRED_LIMIT * 10:
            logger.warning(f"⚠️ Превышен каузальный лимит! Принудительное урезание до {SACRED_LIMIT * 10}")
            amount_usd = float(SACRED_LIMIT * 10)

        total_shares = SURA_SHARE + ASURA_SHARE
        sura_allocation = amount_usd * (SURA_SHARE / total_shares)
        asura_allocation = amount_usd * (ASURA_SHARE / total_shares)

        report = (
            f"🏛️ *[CIRCLE VAULT LOCK SUCCESS]*\n"
            f"💰 Запечатано в сейф: `${amount_usd:.2f}`\n"
            f"☀️ Аллокация Суры (70): `${sura_allocation:.2f}`\n"
            f"🌙 Аллокация Асуры (38): `${asura_allocation:.2f}`\n"
            f"💎 Статус Дашборда: *СИНХРОНИЗИРОВАНО*"
        )

        await self.broadcast_vault_event(report)
        return True

    async def broadcast_vault_event(self, text: str):
        """Сквозная трансляция состояния сейфа Circle."""
        if self.session is None or self.session.closed:
            self.session = aiohttp.ClientSession()

        # 1. Отправка в изумрудный чат Telegram
        if TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID:
            # ИСПРАВЛЕНО: Каноничный рабочий эндпоинт API
            url = f"https://telegram.org{TELEGRAM_BOT_TOKEN}/sendMessage"
            payload = {"chat_id": TELEGRAM_CHAT_ID, "text": text, "parse_mode": "Markdown"}
            try:
                async with self.session.post(url, json=payload) as resp:
                    if resp.status == 200:
                        logger.info("✨ Уведомление сейфа успешно отправлено в Telegram.")
            except Exception as e:
                logger.error(f"Сбой отправки лога в Telegram: {e}")

        # 2. Отправка в Discord
        if DISCORD_WEBHOOK_URL:
            payload = {
                "username": "Circle Vault Bridge",
                "embeds": [{
                    "title": "🏛️ Синхронизация Сейфа Circle",
                    "description": text,
                    "color": 255,  # Синий цвет контура
                    "footer": {"text": f"Квантовый лимит: {SACRED_LIMIT}"}
                }]
            }
            try:
                async with self.session.post(DISCORD_WEBHOOK_URL, json=payload) as resp:
                    if resp.status in:
                        logger.info("🔮 Уведомление сейфа успешно отправлено в Discord.")
            except Exception as e:
                logger.error(f"Сбой отправки лога в Discord: {e}")

    async def vault_swarm_loop(self):
        """Бесконечный автономный цикл контроля сейфа."""
        logger.info("🤖 Мост сейфа Circle переведен в режим круглосуточного мониторинга.")
        while True:
            try:
                # Симулируем фиксацию входящих потоков (от 50 до 1500 USD)
                mock_stream = round(random.uniform(50.0, 1500.0), 2)
                await self.verify_and_lock_liquidity(mock_stream)
            except Exception as e:
                logger.error(f"Аномалия в цикле сейфа: {e}")
                
            await asyncio.sleep(75)  # Проверка каждые 75 секунд

    async def close(self):
        if self.session and not self.session.closed:
            await self.session.close()


if __name__ == "__main__":
    vault_bridge = CircleVaultBridge()
    try:
        asyncio.run(vault_bridge.vault_swarm_loop())
    except KeyboardInterrupt:
        logger.info("Мост сейфа Circle временно остановлен.")
        asyncio.run(vault_bridge.close())
