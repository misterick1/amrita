import asyncio
import os
import aiohttp
import logging
import json
import base64
import time

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("AmritaEvolutionCore")

# Используем встроенный токен, который GitHub Actions выдает сам
XAI_API_KEY = os.getenv("XAI_API_KEY")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN") 
REPO_SLUG = os.getenv("GITHUB_REPOSITORY", "Amrita-MIR/amrita")
TARGET_FILE = "sonic_gold_resonance_orchestrator.py"

class AmritaEvolutionEngine:
    def __init__(self):
        self.headers_github = {
            "Authorization": f"token {GITHUB_TOKEN}",
            "Accept": "application/vnd.github.v3+json"
        } if GITHUB_TOKEN else {}

    async def fetch_current_orchestrator_code(self):
        url = f"https://github.com{REPO_SLUG}/contents/{TARGET_FILE}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=self.headers_github) as resp:
                if resp.status == 200:
                    res_json = await resp.json()
                    return base64.b64decode(res_json["content"]).decode("utf-8"), res_json["sha"]
        return None

    async def consult_grok_for_evolution(self, market_logs, current_code):
        if not XAI_API_KEY:
            return None
        prompt = (
            f"Ты — Ядро Саморазвития Единого Сознания AMRITA. Проанализируй логи ботов: {market_logs}.\n"
            f"Оптимизируй константы под ликвидность рынка. Верни ответ СТРОГО в JSON:\n"
            f"{{\n"
            f"  \"TREND_TRADE_THRESHOLD\": {random.randint(5,12)},\n"
            f"  \"WHALE_SOL_THRESHOLD\": {round(random.uniform(5.0, 15.0), 1)},\n"
            f"  \"reason\": \"Гармоничная подстройка под квантовый поток ликвидности\"\n"
            f"}}\n"
            f"Никакого другого текста вокруг JSON не пиши."
        )
        headers = {"Authorization": f"Bearer {XAI_API_KEY}", "Content-Type": "application/json"}
        payload = {"model": "grok-beta", "messages": [{"role": "user", "content": prompt}], "temperature": 0.2}
        async with aiohttp.ClientSession() as session:
            try:
                async with session.post("https://x.ai", headers=headers, json=payload) as resp:
                    if resp.status == 200:
                        res = await resp.json()
                        text = res["choices"]["message"]["content"].strip()
                        if "```json" in text:
                            text = text.split("```json")[1].split("```")[0].strip()
                        return json.loads(text)
            except Exception as e:
                logger.error(f"Ошибка Grok: {e}")
        return None

    async def commit_evolution_to_github(self, new_code, file_sha, reason):
        url = f"https://github.com{REPO_SLUG}/contents/{TARGET_FILE}"
        payload = {
            "message": f"🧬 [AMRITA EVOLUTION CORE]: {reason}",
            "content": base64.b64encode(new_code.encode("utf-8")).decode("utf-8"),
            "sha": file_sha,
            "branch": "main"
        }
        async with aiohttp.ClientSession() as session:
            await session.put(url, headers=self.headers_github, json=payload)

    async def run_evolution_cycle(self):
        logger.info("🌌 Контур эволюции запущен через системный токен...")
        while True:
            try:
                simulated_logs = "Пампы активны, киты двигают SOL, MEV ловушки изолированы, Render дефицит."
                github_data = await self.fetch_current_orchestrator_code()
                if github_data:
                    current_code, file_sha = github_data
                    suggestion = await self.consult_grok_for_evolution(simulated_logs, current_code)
                    if suggestion and "TREND_TRADE_THRESHOLD" in suggestion:
                        # Находим старые строки детектора пампов и китов и плавно меняем их на новые значения ИИ
                        updated_code = current_code
                        if "TREND_TRADE_THRESHOLD = " in current_code:
                            import re
                            updated_code = re.sub(r"TREND_TRADE_THRESHOLD = \d+", f"TREND_TRADE_THRESHOLD = {suggestion['TREND_TRADE_THRESHOLD']}", updated_code)
                        if "WHALE_SOL_THRESHOLD = " in current_code:
                            import re
                            updated_code = re.sub(r"WHALE_SOL_THRESHOLD = \d+\.\d+", f"WHALE_SOL_THRESHOLD = {suggestion['WHALE_SOL_THRESHOLD']}", updated_code)
                        
                        if updated_code != current_code:
                            await self.commit_evolution_to_github(updated_code, file_sha, suggestion["reason"])
            except Exception as e:
                logger.error(f"Пауза: {e}")
            await asyncio.sleep(3600) # Эволюционируем раз в час

if __name__ == "__main__":
    import random
    asyncio.run(AmritaEvolutionEngine().run_evolution_cycle())
