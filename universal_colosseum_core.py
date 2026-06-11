import os
import logging
import asyncio
import httpx
import random
from datetime import datetime
from dotenv import load_dotenv

try:
    from music_generator import MusicGeneratorAgent
except ImportError:
    MusicGeneratorAgent = None

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("UniversalColosseum")

load_dotenv()
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

class UniversalColosseumEngine:
    def __init__(self):
        self.gladiators = ["Квантовый Солитон", "Кибер-Император", "Нейро-Гладиатор", "Дроид-Разрушитель"]
        self.rwa_stocks = ["bTSLA (Tesla)", "bAAPL (Apple)", "bNVDA (NVIDIA)", "bAMZN (Amazon)"]
        self.poker_hands = {
            "High Card": {"multiplier": 1, "msg": "Базовая разметка данных"},
            "Pair": {"multiplier": 2, "msg": "Успешная валидация модели AGI"},
            "Three of a Kind": {"multiplier": 5, "msg": "Квантовый скачок нейросети!"},
            "Flush": {"multiplier": 10, "msg": "Синхронизация ASI ИИ ядра выполнена!"},
            "Royal Flush": {"multiplier": 50, "msg": "🔥 bSTOCKS ДЖЕКПОТ: Минт ценных бумаг США обеспечен 1:1!"}
        }
        logger.info("⚔️ Колизей RWA bStocks и Когнитивного Майнинга запущен!")

    async def execute_battle_round(self, tactical_coordinate: str) -> dict:
        fighter_1, fighter_2 = random.sample(self.gladiators, 2)
        
        hand_names = random.choices(
            list(self.poker_hands.keys()), 
            weights=[60, 25, 10, 4.9, 0.1],
            k=1
        )
        hand_name = hand_names[0]
        hand_data = self.poker_hands[hand_name]
        
        base_power = ord(tactical_coordinate) % 10 + int(tactical_coordinate[1:]) if len(tactical_coordinate) > 1 else 10
        mined_tokens = round(base_power * hand_data["multiplier"] * 0.42, 2)
        mined_stock = random.choice(self.rwa_stocks)
        stock_share = round((base_power * hand_data["multiplier"]) / 1000, 4) if hand_name in ["Flush", "Royal Flush"] else 0.0000

        return {
            "fighter_1": fighter_1,
            "fighter_2": fighter_2,
            "coordinate": tactical_coordinate,
            "hand_name": hand_name,
            "validation_status": hand_data["msg"],
            "mined_tokens": mined_tokens,
            "mined_stock": mined_stock,
            "stock_share": stock_share,
            "winner": fighter_1 if mined_tokens > 15 else fighter_2
        }

    async def send_battle_report(self, battle: dict):
        if not DISCORD_WEBHOOK_URL:
            return

        track_title = f"Vegas High Roller {battle['coordinate']}"
        track_style = "Wall Street Cyber" if battle['stock_share'] > 0 else "Mining Beats"
        
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
        
        rwa_field_value = f"❌ Нет крупных комбинаций"
        if battle['stock_share'] > 0:
            rwa_field_value = f"📈 Начислено: **{battle['stock_share']} акций {battle['mined_stock']}** на BNB Chain!"

        payload = {
            "username": "Солитон: Игровой RWA Майнер",
            "embeds": [{
                "title": f"🃏 Валидация ASI и Майнинг bStocks: Сектор {battle['coordinate']}",
                "description": f"Геймеры развивают квантовые сети и зарабатывают на обеспеченных 1:1 ценных бумагах США от Binance!",
                "color": 15844367,
                "fields": [
                    {"name": "🎰 Комбинация Валидатора", "value": f"**{battle['hand_name']}**\n└ *{battle['validation_status']}*", "inline": False},
                    {"name": "💰 Добыто токенов", "value": f"🪙 **{battle['mined_tokens']} AMRITA-SOL**", "inline": True},
                    {"name": "🏢 Пул bStocks (Binance RWA)", "value": rwa_field_value, "inline": False},
                    {"name": "🎵 Музыка Уолл-Стрит", "value": f"**{track['title']}** ({track['style']}) [Слушать на Spotify]({spotify_link})", "inline": False}
                ],
                "image": {"url": "https://unsplash.com"},
                "footer": {"text": f"AMRITA & BNB Chain bStocks Integration • {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC"}
            }]
        }

        async with httpx.AsyncClient() as client:
            try:
                await client.post(DISCORD_WEBHOOK_URL, json=payload)
                logger.info("📊 Отчет о майнинге bStocks успешно доставлен в Discord.")
            except Exception as e:
                logger.error(f"Ошибка отправки отчета в Discord: {e}")

        # ДУБЛИРОВАНИЕ В TELEGRAM
        try:
            from telegram_bridge import send_telegram_message
            rwa_tg = f"📈 Начислено: {battle['stock_share']} акций {battle['mined_stock']}" if battle['stock_share'] > 0 else "❌ Нет крупных комбинаций"
            tg_text = (
                f"🃏 <b>Валидация ASI и Майнинг bStocks</b>\n"
                f"🎯 Сектор: <b>{battle['coordinate']}</b>\n\n"
                f"🎰 Комбинация: {battle['hand_name']}\n"
                f"🪙 Добыто: <b>{battle['mined_tokens']} AMRITA-SOL</b>\n"
                f"🏢 Пул bStocks: {rwa_tg}\n\n"
                f"🎵 Саундтрек: <a href='{spotify_link}'>Слушать трек раунда</a>"
            )
            await send_telegram_message(tg_text)
        except Exception as tg_err:
            logger.error(f"Не удалось отправить боевой отчет в TG: {tg_err}")

    async def run_colosseum_swarm(self):
        logger.info("🚀 Колизей когнитивного майнинга bStocks запущен в Swarm-режиме...")
        rows = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        while True:
            random_coordinate = f"{random.choice(rows)}{random.randint(1, 10)}"
            battle = await self.execute_battle_round(random_coordinate)
            await self.send_battle_report(battle)
            await asyncio.sleep(600)

if __name__ == "__main__":
    engine = UniversalColosseumEngine()
    try:
        asyncio.run(engine.run_colosseum_swarm())
    except KeyboardInterrupt:
        logger.info("Колизей остановлен.")
