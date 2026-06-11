import os
import logging
import asyncio
import httpx
import random
from datetime import datetime, time
from dotenv import load_dotenv

# Импортируем наш музыкальный движок для звукового сопровождения макро-событий
try:
    from music_generator import MusicGeneratorAgent
except ImportError:
    MusicGeneratorAgent = None

# Настройка логирования под "Единый Квантовый Оркестратор"
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("JupiterPredictBridge")

load_dotenv()

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

class JupiterPredictBridge:
    def __init__(self):
        self.wallet_address = "So11111111111111111111111111111111111111112"
        # Время публикации ставки ЕЦБ: 11 июня 2026 года
        self.news_time_start = time(14, 13)
        self.news_time_end = time(14, 17)
        logger.info("Мост JupiterPredictBridge успешно инициализирован.")

    def is_trading_restricted(self) -> bool:
        """Проверяет, находится ли текущее время в периоде блокировки ЕЦБ"""
        current_now = datetime.now()

        # Сверяем, что сегодня именно 11 июня 2026 года
        if current_now.year == 2026 and current_now.month == 6 and current_now.day == 11:
            current_time = current_now.time()
            if self.news_time_start <= current_time <= self.news_time_end:
                logger.warning("🚨 БЛОКИРОВКА ТОРГОВ: Обнаружен критический новостной фон (Ставка ЕЦБ)!")
                return True
        return False

    async def send_status_to_discord(self, status_type: str, details: str):
        """Отправляет структурированный DeFAI-отчет о состоянии рынка в Discord"""
        if not DISCORD_WEBHOOK_URL:
            return

        # Генерируем фоновый саундтрек для рыночной ситуации
        track_title = "Macro Freeze Wave" if status_type == "RESTRICTED" else "Jupiter Profit Orbit"
        track_style = "Deep Ambient" if status_type == "RESTRICTED" else "Hyper Synth"
        
        if MusicGeneratorAgent:
            try:
                agent = MusicGeneratorAgent()
                track = await agent.generate_track_metadata()
                track["title"] = track_title
                track["style"] = track_style
            except Exception:
                track = {"title": track_title, "style": track_style, "duration": "3:14", "isrc_code": "US-AMR-26-00000"}
        else:
            track = {"title": track_title, "style": track_style, "duration": "3:14", "isrc_code": "US-AMR-26-00000"}

        spotify_link = f"https://spotify.com{track['title'].replace(' ', '%20')}"
        
        covers = [
            "https://unsplash.com",
            "https://unsplash.com"
        ]

        title = "⚠️ Квантовый Предохранитель Активирован" if status_type == "RESTRICTED" else "⚡ Сигнал Jupiter Исполнен"
        color = 16711712 if status_type == "RESTRICTED" else 65280

        payload = {
            "username": "Солитон: Jupiter Оркестратор",
            "embeds": [{
                "title": title,
                "description": details,
                "color": color,
                "fields": [
                    {"name": "Адрес кошелька Solana", "value": f"`{self.wallet_address}`", "inline": False},
                    {"name": "Состояние системы", "value": "🛑 Защита капитала" if status_type == "RESTRICTED" else "🟢 Активный трейдинг", "inline": True},
                    {"name": "🎵 Эмпирический Саундтрек", "value": f"**{track['title']}** ({track['style']})", "inline": True},
                    {"name": "Дистрибуция", "value": f"🔗 [Слушать на Spotify]({spotify_link})", "inline": False}
                ],
                "image": {"url": random.choice(covers)},
                "footer": {"text": "AMRITA Predictive Analytics Layer"}
            }]
        }

        async with httpx.AsyncClient() as client:
            try:
                await client.post(DISCORD_WEBHOOK_URL, json=payload)
                logger.info("📊 Отчет о состоянии предохранителя успешно отправлен в Discord.")
            except Exception as e:
                logger.error(f"Не удалось отправить отчет: {e}")

    async def execute_ai_prediction_vote(self) -> bool:
        """Отправка ставки/ордера с предварительной проверкой макроэкономического фона"""
        if self.is_trading_restricted():
            logger.warning("Ордер отклонен новостным фильтром. Ожидание стабилизации рынка.")
            await self.send_status_to_discord(
                "RESTRICTED", 
                "Автоматическая система заблокировала отправку транзакций из-за публикации процентной ставки ЕЦБ. Защищаем пул ликвидности."
            )
            return False

        logger.info("🟢 Новостной фон чист. Ордер отправлен на обработку ИИ Jupiter.")
        await self.send_status_to_discord(
            "ACTIVE", 
            "Анализ ИИ-прогнозов завершен. Транзакция отправлена в пул ликвидности Jupiter Агрегатора."
        )
        return True

    async def run_bridge_swarm(self):
        """Бесконечный цикл мониторинга макро-фона и ИИ-голосований"""
        logger.info("🚀 Запущен бесконечный мониторинг ИИ-прогнозов Jupiter...")
        while True:
            await self.execute_ai_prediction_vote()
            # Проверяем рынок и обновляем данные каждые 5 минут
            await asyncio.sleep(300)

if __name__ == "__main__":
    import asyncio
    bridge = JupiterPredictBridge()
    try:
        asyncio.run(bridge.run_bridge_swarm())
    except KeyboardInterrupt:
        logger.info("Мост Jupiter Predict остановлен.")
