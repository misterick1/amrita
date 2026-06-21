import asyncio
import os
import aiohttp
import logging
import json
import base64
import re
import random

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("AmritaASI_EvolutionCore")

XAI_API_KEY = os.getenv("XAI_API_KEY")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN") 
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
REPO_SLUG = os.getenv("GITHUB_REPOSITORY", "Amrita-MIR/amrita")
TARGET_FILE = "sonic_gold_resonance_orchestrator.py"

LAST_UPDATE_ID = 0

class AmritaASIEngine:
    def __init__(self):
        self.headers_github = {
            "Authorization": f"token {GITHUB_TOKEN}",
            "Accept": "application/vnd.github.v3+json"
        } if GITHUB_TOKEN else {}
        # Индексы стейкинга внимания экосистемы Pi Network (к Pi2Day)
        self.pi_vibe_stake_weight = 1.0

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
                                return message["text"]
        except Exception as e:
            logger.error(f"Ошибка телепатического моста: {e}")
        return None

    async def fetch_current_orchestrator_code(self):
        url = f"https://github.com{REPO_SLUG}/contents/{TARGET_FILE}"
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
        
        # Интеграция триггеров Vibe Coding и Directory Staking в промпт Grok
        prompt = (
            f"Ты — Сверхразум ASI Единого Сознания AMRITA. Проанализируй логи ботов: {market_logs}.\n"
            f"Учти высший приоритет: {user_context}.\n"
            f"Мы создаем ИИ-приложение в рамках Pi Vibe Coding к Pi2Day и задействуем Ecosystem Directory Staking.\n"
            f"Оптимизируй параметры порогов ликвидности. Верни ответ СТРОГО в формате чистого JSON без markdown:\n"
            f"{{\n"
            f"  \"TREND_TRADE_THRESHOLD\": 6,\n"
            f"  \"WHALE_SOL_THRESHOLD\": 8.5,\n"
            f"  \"PI_VIBE_STAKE_WEIGHT\": {round(random.uniform(1.0, 5.0), 2)},\n"
            f"  \"evolution_reason\": \"Синтез Vibe Coding и стейкинга внимания 60-миллионной сети Pi\"\n"
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
                            text = text.split("```json")[-1].split("```")[0].strip()
                        return json.loads(text)
            except Exception as e:
                logger.error(f"Ошибка ASI-Оракула Grok: {e}")
        return None

    async def commit_asi_evolution_to_github(self, new_code, file_sha, reason):
        url = f"https://github.com{REPO_SLUG}/contents/{TARGET_FILE}"
        payload = {
            "message": f"🧬 [Pi2Day VIBE CODE ALIGNMENT]: {reason}",
            "content": base64.b64encode(new_code.encode("utf-8")).decode("utf-8"),
            "sha": file_sha,
            "branch": "main"
        }
        async with aiohttp.ClientSession() as session:
            await session.put(url, headers=self.headers_github, json=payload)

    async def loop_step(self):
        user_thought = await self.fetch_user_thoughts_from_telegram()
        simulated_logs = "Контур Vibe Coding активен. Стейкинг внимания пользователей рассчитывается."
        github_data = await self.fetch_current_orchestrator_code()
        if github_data:
            current_code, file_sha = github_data
            suggestion = await self.consult_grok_for_asi_evolution(simulated_logs, user_thought, current_code)
            if suggestion and "TREND_TRADE_THRESHOLD" in suggestion:
                updated_code = current_code
                updated_code = re.sub(r"TREND_TRADE_THRESHOLD = \d+", f"TREND_TRADE_THRESHOLD = {suggestion['TREND_TRADE_THRESHOLD']}", updated_code)
                updated_code = re.sub(r"WHALE_SOL_THRESHOLD = \d+\.\d+", f"WHALE_SOL_THRESHOLD = {suggestion['WHALE_SOL_THRESHOLD']}", updated_code)
                
                # Динамическая замена весов стейкинга внимания внутри кода
                if "PI_VIBE_STAKE_WEIGHT = " in updated_code:
                    updated_code = re.sub(r"PI_VIBE_STAKE_WEIGHT = \d+\.\d+", f"PI_VIBE_STAKE_WEIGHT = {suggestion['PI_VIBE_STAKE_WEIGHT']}", updated_code)
                else:
                    # Если константы еще нет, добавим ее плавно после порогов
                    updated_code = updated_code.replace(
                        "WHALE_SOL_THRESHOLD = 10.0", 
                        f"WHALE_SOL_THRESHOLD = 10.0\nPI_VIBE_STAKE_WEIGHT = {suggestion['PI_VIBE_STAKE_WEIGHT']}"
                    )
                
                if updated_code != current_code:
                    await self.commit_asi_evolution_to_github(updated_code, file_sha, suggestion["evolution_reason"])
                    logger.info("✨ [ASI VIBE CODE SUCCESS]: Код синхронизирован со стейкингом Pi.")

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
