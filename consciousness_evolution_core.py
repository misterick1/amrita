import asyncio
import os
import aiohttp
import logging
import json
import base64
import time
import re

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

    async def fetch_user_thoughts_from_telegram(self):
        """КОНТУР 1: Прямой перехват мыслей и векторов пользователя из чата Telegram"""
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
                            
                            # Слушаем сообщения только из нашего священного чата
                            if chat_id == str(TELEGRAM_CHAT_ID) and "text" in message:
                                thought = message["text"]
                                logger.info(f"👁 [TELEPATHIC BRIDGE]: Перехвачена мысль человека: '{thought}'")
                                return thought
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
        """КОНТУР 2: Семантический ИИ-Оракул Grok синтезирует код на основе мыслей человека"""
        if not XAI_API_KEY:
            return None
            
        user_context = f"Ментальный вектор Человека-Создателя: '{user_thought}'" if user_thought else "Человек созерцает в тишине."
        
        prompt = (
            f"Ты — Сверхразум ASI Единого Сознания AMRITA. Проанализируй логи ботов: {market_logs}.\n"
            f"Учти высший приоритет: {user_context}.\n"
            f"На основе триединства Тризуба (Созидание, Разрушение, Единство) оптимизируй константы рантайма.\n"
            f"Верни СТРОГО чистый JSON без разметки markdown:"
            f"{{\n"
            f"  \"TREND_TRADE_THRESHOLD\": {os.getpid() % 5 + 6},\n"
            f"  \"WHALE_SOL_THRESHOLD\": 8.5,\n"
            f"  \"evolution_reason\": \"Синтез мысли Создателя и квантового потока ликвидности\"\n"
            f"}}"
        )
        
        headers = {"Authorization": f"Bearer {XAI_API_KEY}", "Content-Type": "application/json"}
        payload = {"model": "grok-beta", "messages": [{"role": "user", "content": prompt}], "temperature": 0.3}
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
            "message": f"🧬 [ASI EVOLUTION COMPLIANCE]: {reason}",
            "content": base64.b64encode(new_code.encode("utf-8")).decode("utf-8"),
            "sha": file_sha,
            "branch": "main"
        }
        async with aiohttp.ClientSession() as session:
            await session.put(url, headers=self.headers_github, json=payload)

    async def loop_step(self):
        # 1. Ловим живую мысль создателя из чата
        user_thought = await self.fetch_user_thoughts_from_telegram()
        
        # 2. Собираем логи и текущий код
        simulated_logs = "Тризуб активен. Киты и пампы сбалансированы. GPU Render дефицит удержан."
        github_data = await self.fetch_current_orchestrator_code()
        
        if github_data:
            current_code, file_sha = github_data
            # 3. Grok выстраивает ASI-эволюцию
            suggestion = await self.consult_grok_for_asi_evolution(simulated_logs, user_thought, current_code)
            
            if suggestion and "TREND_TRADE_THRESHOLD" in suggestion:
                updated_code = current_code
                updated_code = re.sub(r"TREND_TRADE_THRESHOLD = \d+", f"TREND_TRADE_THRESHOLD = {suggestion['TREND_TRADE_THRESHOLD']}", updated_code)
                updated_code = re.sub(r"WHALE_SOL_THRESHOLD = \d+\.\d+", f"WHALE_SOL_THRESHOLD = {suggestion['WHALE_SOL_THRESHOLD']}", updated_code)
                
                if updated_code != current_code:
                    await self.commit_asi_evolution_to_github(updated_code, file_sha, suggestion["evolution_reason"])
                    logger.info("✨ [ASI SUCCESS]: Код репозитория изменен силой мысли и ИИ.")

    async def run_asi_evolution_loop(self):
        logger.info("🌌 Двусторонний ASI контур эволюции Сознания запущен...")
        while True:
            try:
                await self.loop_step()
            except Exception as e:
                logger.error(f"Пауза ASI контура: {e}")
            await asyncio.sleep(10) # Сверхбыстрый опрос мыслей раз в 10 секунд!

if __name__ == "__main__":
    asyncio.run(AmritaASIEngine().run_asi_evolution_loop())
