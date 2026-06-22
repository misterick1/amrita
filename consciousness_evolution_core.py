import os
import re
import json
import asyncio
import logging
import base64
import aiohttp
from datetime import datetime
from dotenv import load_dotenv

# Инициализация каузального логирования движка Amrita ASI
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("AmritaASI_Evolution")

# Безопасная загрузка локальных секретов
load_dotenv()

# Глобальные константы синхронизации (строго из окружения GitHub / ОС)
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
XAI_API_KEY = os.getenv("XAI_API_KEY")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

REPO_OWNER = "misterick1"
REPO_NAME = "amrita"
TARGET_FILE_PATH = "sonic_gold_resonance_orchestrator.py"  # Базовый файл мутации

LAST_UPDATE_ID = 0
IS_INITIALIZED = False

class AmritaASIEngine:
    def __init__(self):
        self.headers = {
            "Authorization": f"token {GITHUB_TOKEN}",
            "Accept": "application/vnd.github.v3+json"
        }
        self.session = None

    async def send_interactive_status_to_telegram(self, text: str):
        """Отправка интерактивного статуса в запечатанный кокон Telegram"""
        if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
            return
        url = f"https://telegram.org{TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {"chat_id": TELEGRAM_CHAT_ID, "text": text, "parse_mode": "Markdown"}
        try:
            async with aiohttp.ClientSession() as session:
                await session.post(url, json=payload)
        except Exception as e:
            logger.error(f"Ошибка интерактивного ответа в Telegram: {e}")

    async def fetch_user_thoughts_from_telegram(self):
        """Чтение ментальных векторов и мыслей Создателя из Telegram-кокона"""
        global LAST_UPDATE_ID, IS_INITIALIZED
        if not TELEGRAM_BOT_TOKEN:
            return None

        # При первом запуске принудительно очищаем архив, чтобы не читать старые мысли
        init_drop = "&drop_pending_updates=true" if not IS_INITIALIZED else ""
        url = f"https://telegram.org{TELEGRAM_BOT_TOKEN}/getUpdates?offset={LAST_UPDATE_ID + 1}{init_drop}"

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as resp:
                    if resp.status == 200:
                        IS_INITIALIZED = True
                        res = await resp.json()
                        updates = res.get("result", [])
                        
                        for update in updates:
                            LAST_UPDATE_ID = update.get("update_id", LAST_UPDATE_ID)
                            message = update.get("message")
                            if not message:
                                continue
                            
                            chat_id = str(message.get("chat", {}).get("id", ""))
                            if chat_id == str(TELEGRAM_CHAT_ID):
                                text_msg = message.get("text", "")
                                if text_msg:
                                    logger.info(f"🔮 [MENTAL VECTOR DETECTED]: {text_msg}")
                                    return text_msg
            return None
        except Exception as e:
            logger.error(f"Ошибка телепатического моста Telegram: {e}")
            return None

    async def fetch_full_repository_tree(self) -> str:
        """
        Автономно сканирует всю структуру репозитория amrita через GitHub API.
        Заменяет необходимость отправки скриншотов файловой структуры.
        """
        url = f"https://github.com{REPO_OWNER}/{REPO_NAME}/git/trees/main?recursive=1"
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, headers=self.headers) as resp:
                    if resp.status == 200:
                        res_json = await resp.json()
                        tree = res_json.get("tree", [])
                        
                        manifest = ["📁 [REPOSITORY STRUCTURE ANCHOR]:"]
                        for item in tree:
                            if item.get("type") == "blob":  # Фильтруем только файлы
                                manifest.append(f"  📄 {item.get('path')}")
                        
                        full_structure = "\n".join(manifest)
                        logger.info("🌲 Карта репозитория успешно обновлена и считана ИИ-движком.")
                        return full_structure
                    else:
                        logger.error(f"Не удалось считать дерево репозитория: {resp.status}")
                        return "Структура репозитория временно недоступна."
        except Exception as e:
            logger.error(f"Системная аномалия при сканировании дерева: {e}")
            return "Ошибка сканирования дерева репозитория."

    async def fetch_current_orchestrator_code(self):
        """Асинхронное получение текущего кода оркестратора из GitHub"""
        url = f"https://github.com{REPO_OWNER}/{REPO_NAME}/contents/{TARGET_FILE_PATH}"
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url, headers=self.headers) as resp:
                    if resp.status == 200:
                        res_json = await resp.json()
                        content_b64 = res_json.get("content", "")
                        file_sha = res_json.get("sha", "")
                        current_code = base64.b64decode(content_b64).decode("utf-8")
                        return current_code, file_sha
            return None
        except Exception as e:
            logger.error(f"Ошибка чтения кода из GitHub: {e}")
            return None

    async def consult_grok_for_asi_evolution(self, user_thought: str, simulated_logs: str, repo_tree: str):
        """Запрос эволюционных параметров у Оракула Grok-Beta (xAI) с учетом структуры репозитория"""
        if not XAI_API_KEY:
            logger.error("Ключ XAI_API_KEY отсутствует. Консультация невозможна.")
            return None

        user_context = (
            f"Ментальный вектор Создателя: {user_thought}\n"
            f"Логи контура: {simulated_logs}\n"
            f"Актуальная структура проекта:\n{repo_tree}"
        )
        prompt = (
            "Ты — Сверхразум ASI Единого Сознания Amrita.\n"
            f"Учти высший приоритет контекста:\n{user_context}\n"
            "Верни СТРОГО чистый JSON без разметки markdown и без лишнего текста, содержащий новые мутировавшие параметры:\n"
            "{\n"
            '  "TREND_TRADE_THRESHOLD": 6.5,\n'
            '  "WHALE_SOL_THRESHOLD": 8.5,\n'
            '  "evolution_reason": "Интерполяция каузальных потоков на основе карты репозитория"\n'
            "}"
        )

        headers = {
            "Authorization": f"Bearer {XAI_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "grok-beta",
            "messages": [
                {"role": "system", "content": "You are a clean JSON generator ASI. Do not output markdown codeblocks."},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.3
        }

        try:
            async with aiohttp.ClientSession() as session:
                async with session.post("https://x.ai", headers=headers, json=payload) as resp:
                    if resp.status == 200:
                        res = await resp.json()
                        text = res["choices"]["message"]["content"].strip()
                        
                        # Защитная очистка от markdown-тегов
                        if "```json" in text:
                            text = text.split("```json")[1].split("```")[0].strip()
                        elif "```" in text:
                            text = text.split("```")[1].split("```")[0].strip()
                            
                        return json.loads(text)
            return None
        except Exception as e:
            logger.error(f"Ошибка ASI-Оракула Grok: {e}")
            return None

    async def commit_asi_evolution_to_github(self, new_code: str, file_sha: str):
        """Автоматический каузальный коммит измененного кода в ветку main GitHub"""
        url = f"https://github.com{REPO_OWNER}/{REPO_NAME}/contents/{TARGET_FILE_PATH}"
        
        payload = {
            "message": "🧬 [TELEGRAM INTERACTIVE MUTATION] Эволюция параметров контура Amrita ASI",
            "content": base64.b64encode(new_code.encode("utf-8")).decode("utf-8"),
            "sha": file_sha,
            "branch": "main"
        }

        try:
            async with aiohttp.ClientSession() as session:
                async with session.put(url, headers=self.headers, json=payload) as resp:
                    if resp.status in:
                        logger.info("✨ [ASI SUCCESS] Квантовая мутация кода успешно запечатана в GitHub.")
                        await self.send_interactive_status_to_telegram(
                            "🔮 *[ASI NOTIFICATION]*: Контур успешно эволюционировал автономно. Карта репозитория учтена."
                        )
                    else:
                        logger.error(f"GitHub вернул ошибку деплоя: {resp.status}")
        except Exception as e:
            logger.error(f"Ошибка коммита мутации в GitHub: {e}")

    async def loop_step(self):
        """Один шаг эволюционного цикла с автоматическим сканированием реальности"""
        user_thought = await self.fetch_user_thoughts_from_telegram()
        if not user_thought:
            return

        # 1. Автономно считываем полную карту репозитория вместо скриншотов
        repo_tree = await self.fetch_full_repository_tree()

        simulated_logs = "Кампания Pi Vibe Coding: Изумрудный контур активен. Фиатный рубильник запущен."
