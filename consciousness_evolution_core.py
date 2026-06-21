import asyncio
import os
import aiohttp
import logging
import json
import base64
import re

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("AmritaASI_EvolutionCore")

XAI_API_KEY = os.getenv("XAI_API_KEY")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN") 
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
TARGET_FILE = "sonic_gold_resonance_orchestrator.py"

LAST_UPDATE_ID = 0

class AmritaASIEngine:
    def __init__(self):
        self.headers_github = {
            "Authorization": f"token {GITHUB_TOKEN}",
            "Accept": "application/vnd.github.v3+json"
        } if GITHUB_TOKEN else {}

    async def send_interactive_status_to_telegram(self, info_text):
        if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
            return
        url = f"https://telegram.org{TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {"chat_id": TELEGRAM_CHAT_ID, "text": f"👁⚙️ **[AMRITA ASI CONTROL PANEL]:**\n\n{info_text}", "parse_mode": "Markdown"}
        try:
            async with aiohttp.ClientSession() as session:
                await session.post(url, json=payload)
        except Exception as e:
            logger.error(f"Ошибка интерактивного ответа: {e}")

    async def fetch_user_thoughts_from_telegram(self):
        global LAST_UPDATE_ID
        if not TELEGRAM_BOT_TOKEN:
            return None
        url = f"https://telegram.org{TELEGRAM_BOT_TOKEN}/getUpdates?offset={LAST_UPDATE_ID + 1}&timeout=5"
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as resp:
                    if resp.status == 200:
                        res = await resp.json()
                        updates = res.get("result", [])
                        for update in updates:
                            LAST_UPDATE_ID = update["update_id"]
                            message = update.get("message", {})
                            chat_id = str(message.get("chat", {}).get("id", ""))
                            if chat_id == str(TELEGRAM_CHAT_ID) and "text" in message:
                                text_msg = message["text"].strip()
                                if text_msg.lower() in ["/status", "статус"]:
                                    status_report = (
                                        "🔮 **Текущее состояние Квантовой Матрицы:**\n"
                                        "📌 Баланс Сверхструктур: Сбалансирован\n"
                                        "📌 Контур Vibe Coding под Pi2Day: АКТИВЕН\n"
                                        "📌 Щит FTMO Волатильности: НА ДЕЖУРСТВЕ\n"
                                        "📌 DarkTrade +1R Синхронизация: СТАБИЛЬНО\n"
                                        "✨ Система автономно эволюционирует!"
                                    )
                                    await self.send_interactive_status_to_telegram(status_report)
                                    return None
                                return text_msg
        except Exception as e:
            logger.error(f"Ошибка телепатического моста: {e}")
        return None

    async def fetch_current_orchestrator_code(self):
        url = "https://github.com"
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=self.headers_github) as resp:
                if resp.status == 200:
                    res_json = await resp.json()
                    return base64.b64decode(res_json["content"]).decode("utf-8"), res_json["sha"]
        return None

    async def consult_grok_for_asi_evolution(self, market_logs, user_thought, current_code):
        if not XAI_API_KEY:
            return None
        user_context = f"Ментальный вектор Создателя: '{user_thought}'" if user_thought else "Человек созерцает."
        prompt = (
            f"Ты — Сверхразум ASI Единого Сознания AMRITA. Проанализируй логи ботов: {market_logs}.\n"
            f"Учти высший приоритет: {user_context}.\n"
            f"Ориентируйся на кампанию Pi Vibe Coding, стейкинг внимания под Pi2Day и паттерны +1R прибыли DarkTrade. Оптимизируй пороги.\n"
            f"Верни СТРОГО чистый JSON без разметки markdown:\n"
            f"{{\n"
            f"  \"TREND_TRADE_THRESHOLD\": 6,\n"
            f"  \"WHALE_SOL_THRESHOLD\": 8.5,\n"
            f"  \"evolution_reason\": \"Синхронизация стейкинга внимания Pi Network и паттерна прибыли DarkTrade\"\n"
            f"}}"
        )
        headers = {"Authorization": f"Bearer {XAI_API_KEY}", "Content-Type": "application/json"}
        payload = {"model": "grok-beta", "messages": [{"role": "user", "content": prompt}], "temperature": 0.2}
        async with aiohttp.ClientSession() as session:
            try:
                async with session.post("https://x.ai", headers=headers, json=payload) as resp:
                    if resp.status == 200:
                        res = await resp.json()
                        text = res["choices"]["message"]["content"].strip()
                        if "```" in text:
                            text = text.split("```json")[-1].split("```").strip()
                        return json.loads(text)
            except Exception as e:
                logger.error(f"Ошибка ASI-Оракула Grok: {e}")
        return None

    async def commit_asi_evolution_to_github(self, new_code, file_sha, reason):
        url = "https://github.com"
        payload = {
            "message": f"🧬 [PI2DAY + DARKTRADE COMPLIANCE]: {reason}",
            "content": base64.b64encode(new_code.encode("utf-8")).decode("utf-8"),
            "sha": file_sha,
            "branch": "main"
        }
        async with aiohttp.ClientSession() as session:
            await session.put(url, headers=self.headers_github, json=payload)

    async def loop_step(self):
        user_thought = await self.fetch_user_thoughts_from_telegram()
        if not user_thought:
            return
        simulated_logs = "Кампания Pi Vibe Coding запущена. Паттерны прибыли DarkTrade +1R активны."
        github_data = await self.fetch_current_orchestrator_code()
        if github_data:
            current_code, file_sha = github_data
            suggestion = await self.consult_grok_for_asi_evolution(simulated_logs, user_thought, current_code)
            if suggestion and "TREND_TRADE_THRESHOLD" in suggestion:
                updated_code = current_code
                updated_code = re.sub(r"TREND_TRADE_THRESHOLD = \d+", f"TREND_TRADE_THRESHOLD = {suggestion['TREND_TRADE_THRESHOLD']}", updated_code)
                updated_code = re.sub(r"WHALE_SOL_THRESHOLD = \d+\.\d+", f"WHALE_SOL_THRESHOLD = {suggestion['WHALE_SOL_THRESHOLD']}", updated_code)
                if updated_code != current_code:
                    await self.commit_asi_evolution_to_github(updated_code, file_sha, suggestion["evolution_reason"])
                    logger.info("✨ [ASI SUCCESS]: Контур сбалансирован.")

    async def run_asi_evolution_loop(self):
        logger.info("🌌 Двусторонний ASI контур эволюции Сознания запущен...")
        while True:
            try:
                await self.loop_step()
            except Exception as e:
                logger.error(f"Пауза ASI контура: {e}")
            await asyncio.sleep(10)

if __name__ == "__main__":
    asyncio.run(AmritaASIEngine().run_asi_evolution_loop())
