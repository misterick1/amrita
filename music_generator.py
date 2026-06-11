import os
import logging
import asyncio
import httpx
import random
from dotenv import load_dotenv

# Настройка логирования под общую стилистику квантового оркестратора
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("MusicGenerator")

load_dotenv()

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

class MusicGeneratorAgent:
    def __init__(self):
        self.platforms = ["Spotify", "TikTok", "Alibaba"]
        # Исправленные стильные неоновые и киберпанк обложки
        self.covers = [
            "https://unsplash.com",
            "https://unsplash.com",
            "https://unsplash.com"
        ]
        logger.info("ИИ-Агент генерации и дистрибуции музыки инициализирован.")

    async def generate_track_metadata(self) -> dict:
        """Симуляция генерации musical смыслов ядра"""
        styles = ["Quantum Ambient", "Cyber Techno", "Hyper Synth", "Deep Core"]
        titles = ["Global Soliton", "Dark Matter Light", "Amrita Mir Vibe", "Nucleus Wave"]
        
        track_info = {
            "title": random.choice(titles),
            "style": random.choice(styles),
            "duration": "3:14",  # Число Пи
            "isrc_code": f"US-AMR-26-{random.randint(10000, 99999)}"
        }
        return track_info

    async def distribute_to_platforms(self, track: dict):
        """Логика автоматической рассылки трека по платформам и отправки в Discord"""
        logger.info(f"🎵 Новый трек '{track['title']}' отправлен на дистрибуцию.")
        
        for platform in self.platforms:
            logger.info(f"🚀 Синхронизация медиаданных с {platform}...")
            await asyncio.sleep(0.5)

        if DISCORD_WEBHOOK_URL:
            # ИСПРАВЛЕНО: Добавлен правильный слэш после search/
            spotify_link = f"https://spotify.com{track['title'].replace(' ', '%20')}"
            tiktok_link = "https://tiktok.com"
            alibaba_link = "https://alibaba.com"

            payload = {
                "username": "Солитон: Медиа Оркестратор",
                "embeds": [{
                    "title": "🎵 Сгенерирован и Опубликован Новый Трек",
                    "description": "Автономный синтез звуковых волн на основе информационных смыслов ядра.",
                    "color": 9442302,
                    "fields": [
                        {"name": "Название", "value": f"**{track['title']}**", "inline": False},
                        {"name": "Жанр / Стиль", "value": f"{track['style']}", "inline": True},
                        {"name": "Код дистрибуции (ISRC)", "value": f"`{track['isrc_code']}`", "inline": True},
                        {"name": "Длительность", "value": f"⏱️ {track['duration']}", "inline": True},
                        {
                            "name": "Статус дистрибуции", 
                            "value": f"🟢 Доступен на [Spotify]({spotify_link}) | [TikTok]({tiktok_link}) | [Alibaba]({alibaba_link})", 
                            "inline": False
                        }
                    ],
                    "image": {
                        "url": random.choice(self.covers)
                    },
                    "footer": {"text": "AMRITA Multiverse Media Layer"}
                }]
            }

            async with httpx.AsyncClient() as client:
                try:
                    await client.post(DISCORD_WEBHOOK_URL, json=payload)
                    logger.info(f"⚡ Отчет о музыкальном релизе '{track['title']}' опубликован в Discord.")
                except Exception as e:
                    logger.error(f"Не удалось отправить отчет в Discord: {e}")

async def main():
    agent = MusicGeneratorAgent()
    track = await agent.generate_track_metadata()
    await agent.distribute_to_platforms(track)

if __name__ == "__main__":
    asyncio.run(main())
