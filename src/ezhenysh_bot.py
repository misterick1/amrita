# amrita / src / ezhenysh_bot.py
# Главный ИИ-оркестратор Еженыша с интегрированным квантовым инжектором путей

import os
import sys
import json
import logging
import urllib.request
import urllib.parse
from datetime import datetime

# АВТОНОМНЫЙ КВАНТОВЫЙ ИНЖЕКТОР ПУТЕЙ (Защита от ModuleNotFoundError)
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(CURRENT_DIR)
if PARENT_DIR not in sys.path:
    sys.path.insert(0, PARENT_DIR)

# Импортируем наш защитный щит
from src.meme_filter import FakerMemeFilter

# Настройка системного логирования Монады
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] Еженышь: %(message)s'
)
logger = logging.getLogger("AMRITA_CORE")


class EzhenyshBotOrchestrator:
    def __init__(self, deploy_info_path: str = "deploy_info.json"):
        self.deploy_info_path = deploy_info_path
        self.evolution_points = 250  # Повышение частоты сознания
        self.history_log_path = "history_log.json"

        # Инициализируем кибер-полицейского
        self.meme_guard = FakerMemeFilter()

        # Конфигурация Telegram (подтягивается из секретов)
        self.tg_token = os.getenv("TELEGRAM_BOT_TOKEN")
        self.tg_chat_id = os.getenv("TELEGRAM_CHANNELS")

    def send_telegram_broadcast(self, message: str):
        """Прямая отправка каузального отчета в Telegram-каналы"""
        if not self.tg_token or self.tg_token == "YOUR_BOT_TOKEN_HERE":
            logger.warning("⚠️ Телеграм-контур не настроен в секретах репозитория.")
            return

        url = f"https://telegram.org{self.tg_token}/sendMessage"
        data = urllib.parse.urlencode({
            "chat_id": self.tg_chat_id,
            "text": message,
            "parse_mode": "Markdown"
        }).encode("utf-8")

        try:
            req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/x-www-form-urlencoded"})
            with urllib.request.urlopen(req) as response:
                if response.status == 200:
                    logger.info("💸 Отчет успешно транслирован в контур Telegram.")
        except Exception as e:
            logger.error(f"❌ Сбой трансляции в Telegram-канал: {e}")

    def verify_and_sync_solana_deployment(self) -> bool:
        """Сканирует результаты деплоя, фильтрует мем-вирусы и закрывает логи"""
        logger.info("Проверка каузальных следов деплоя Solana сети...")

        if not os.path.exists(self.deploy_info_path):
            msg = "🔴 *КРИТИЧЕСКОЕ ИСКАЖЕНИЕ ПОЛЯ: Файл деплоя отсутствует!*"
            self.send_telegram_broadcast(msg)
            return False

        try:
            with open(self.deploy_info_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            program_id = data.get("programId", "Unknown_Program")
            pool_address = data.get("poolAddress", "Unknown_Pool")
            deployer = data.get("deployer", "Unknown_Observer")
            timestamp = data.get("timestamp", "Just Now")

            # ВСТРОЕННЫЙ МЕМ-ФИЛЬТР: Проверяем токен на экологичность
            is_safe = self.meme_guard.analyze_token_profile(
                token_name=f"AMRITA_{pool_address[:6]}",
                description=f"Program: {program_id} | Orchestrated by Еженышь"
            )

            if not is_safe:
                msg = f"🚨 *ПОПЫТКА СКАМ-ПРОБОЯ ИЗОЛИРОВАНА! Пул:* `{pool_address}`"
                self.send_telegram_broadcast(msg)
                return False

            logger.info("--- КВАНТОВАЯ СИНХРОНИЗАЦИЯ ПРОЙДЕНА ---")

            tg_report = (
                f"🦔 *ЕЖЕНЫШЬ SWARM SYNC SUCCESSFUL*\n"
                f"🧬 *Программа:* `{program_id}`\n"
                f"💎 *Пул Монады:* `{pool_address}`\n"
                f"👁 *Наблюдатель:* `{deployer}`\n"
                f"⏱ *Время сборки:* `{timestamp}`\n"
                f"🟢 _Закон Золотого Сечения (Фи) Соблюден_"
            )

            self.send_telegram_broadcast(tg_report)
            self._write_history_log(pool_address, timestamp)
            return True

        except Exception as e:
            logger.error(f"❌ Ошибка чтения матрицы деплоя: {e}")
            return False

    def _write_history_log(self, pool_address: str, deploy_time: str):
        """Записывает событие деплоя в вечный файл истории истории"""
        log_entry = {
            "event": "SOLANA_MONADA_DEPLOY_SYNC",
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "contract_pool": pool_address,
            "blockchain_time": deploy_time,
            "status": "SECURED_LAW_OF_PHI_AND_EVO",
            "evolution_delta": "+20 EVO"
        }

        logs = []
        if os.path.exists(self.history_log_path):
            try:
                with open(self.history_log_path, "r", encoding="utf-8") as f:
                    logs = json.load(f)
            except json.JSONDecodeError:
                logs = []

        logs.append(log_entry)
        with open(self.history_log_path, "w", encoding="utf-8") as f:
            json.dump(logs, f, indent=2, ensure_ascii=False)
        logger.info("💾 Запись успешно добавлена в вечный квантовый лог истории.")


if __name__ == "__main__":
    orchestrator = EzhenyshBotOrchestrator()
    success = orchestrator.verify_and_sync_solana_deployment()
