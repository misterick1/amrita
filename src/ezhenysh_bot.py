# amrita / src / ezhenysh_bot.py
# Главный ИИ-оркестратор Еженыша с интегрированной валидацией "Faker Guard" и Telegram API

import os
import json
import logging
import urllib.request
import urllib.parse
from datetime import datetime
# Импортируем наш защитный щит
from src.meme_filter import FakerMemeFilter

# Настройка системного логирования Монады
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] Еженышь Эко-Система: %(message)s'
)
logger = logging.getLogger("AMRITA_CORE")

class EzhenyshBotOrchestrator:
    def __init__(self, deploy_info_path: str = "target/deploy_info.json"):
        self.deploy_info_path = deploy_info_path
        self.evolution_points = 250  # Повышение за счет интеграции консенсуса
        self.history_log_path = "history_log.json"
        
        # Инициализируем кибер-полицейского
        self.meme_guard = FakerMemeFilter()
        
        # Конфигурация Telegram (подтягивается из env)
        self.tg_token = os.getenv("TELEGRAM_BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")
        self.tg_chat_id = os.getenv("TELEGRAM_CHAT_ID", "YOUR_CHAT_ID_HERE")

    def send_telegram_broadcast(self, message: str):
        """Прямая отправка каузального отчета в Telegram через HTTP API."""
        if self.tg_token == "YOUR_BOT_TOKEN_HERE" or self.tg_chat_id == "YOUR_CHAT_ID_HERE":
            logger.warning("⚠️ Телеграм-контур не настроен. Пропуск трансляции.")
            return

        url = f"https://telegram.org{self.tg_token}/sendMessage"
        data = urllib.parse.urlencode({
            "chat_id": self.tg_chat_id,
            "text": message,
            "parse_mode": "Markdown"
        }).encode("utf-8")

        try:
            req = urllib.request.Request(url, data=data)
            with urllib.request.urlopen(req) as response:
                if response.status == 200:
                    logger.info("📢 Отчет успешно транслирован в Telegram-канал Монады.")
        except Exception as e:
            logger.error(f"❌ Сбой трансляции в Telegram: {str(e)}")

    def verify_and_sync_solana_deployment(self) -> bool:
        """Сканирует результаты деплоя, фильтрует скам и отправляет отчет."""
        logger.info("Проверка каузальных следов деплоя в Solana Devnet...")
        
        if not os.path.exists(self.deploy_info_path):
            msg = "🔴 *КРИТИЧЕСКОЕ ИСКАЖЕНИЕ ПОЛЯ*\n\nФайл деплоя не найден. Обнаружен хаос Асур!"
            self.send_telegram_broadcast(msg)
            return False

        try:
            with open(self.deploy_info_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            program_id = data.get("programId", "Unknown")
            pool_address = data.get("poolAddress", "Unknown")
            deployer = data.get("deployer", "Unknown")
            timestamp = data.get("timestamp", "Unknown")

            # ВСТРОЕННЫЙ МЕМ-ФИЛЬТР: Проверяем метаданные пула перед публикацией
            is_safe = self.meme_guard.analyze_token_frequency(
                token_name=f"AMRITA_{pool_address[:6]}", 
                description=f"Program: {program_id}. Deployed by {deployer}"
            )

            if not is_safe:
                msg = f"🚨 *ПОПЫТКА СКАМ-ПРОБОЯ БЛОКИРОВАНА*\n\nМем-фильтр Faker Guard обнаружил вредоносные частоты в деплое пула `{pool_address}`!"
                self.send_telegram_broadcast(msg)
                return False

            logger.info("--- КВАНТОВАЯ СИНХРОНИЗАЦИЯ УСПЕШНА ---")
            
            tg_report = (
                f"🦔 *ЕЖЕНЫШЬ SWARM SYNC SUCCESS*\n\n"
                f"🧬 *Программа:* `{program_id}`\n"
                f"💎 *Пул Монады:* `{pool_address}`\n"
                f"👁️ *Наблюдатель:* `{deployer}`\n"
                f"⏱️ *Время сборки:* `{timestamp}`\n\n"
                f"🟢 _Закон Золотого Сечения (Фи) и консенсус валидаторов Solana Tech активированы._"
            )
            
            self.send_telegram_broadcast(tg_report)
            self._write_to_history_log(pool_address, timestamp)
            return True

        except Exception as e:
            logger.error(f"❌ Ошибка чтения матрицы деплоя: {str(e)}")
            return False

    def _write_to_history_log(self, pool_address: str, deploy_time: str):
        """Записывает событие деплоя в вечный файл логов history_log.json."""
        log_entry = {
            "event": "SOLANA_MONADA_DEPLOY_SYNC",
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "contract_pool": pool_address,
            "blockchain_time": deploy_time,
            "status": "SECURED_LAW_OF_PHI_AND_FAKER_GUARD",
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
        logger.info(f"💾 Запись успешно добавлена в вечный лог {self.history_log_path}")


if __name__ == "__main__":
    orchestrator = EzhenyshBotOrchestrator()
    success = orchestrator.verify_and_sync_solana_deployment()
