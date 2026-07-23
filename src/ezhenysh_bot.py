# amrita / src / ezhenysh_bot.py
# Модуль ИИ-Логики Еженыша с интегрированным контуром Telegram-оповещений и Solana Sync

import os
import json
import logging
import urllib.request
import urllib.parse
from datetime import datetime

# Настройка системного логирования Монады
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] Еженышь Эко-Система: %(message)s'
)
logger = logging.getLogger("AMRITA_CORE")

class EzhenyshBotOrchestrator:
    def __init__(self, deploy_info_path: str = "target/deploy_info.json"):
        self.deploy_info_path = deploy_info_path
        self.evolution_points = 220  # Повышенный уровень EVO
        self.history_log_path = "history_log.json"
        
        # Конфигурация Telegram-канала (подтягивается из переменных окружения для безопасности)
        self.tg_token = os.getenv("TELEGRAM_BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")
        self.tg_chat_id = os.getenv("TELEGRAM_CHAT_ID", "YOUR_CHAT_ID_HERE")

    def send_telegram_broadcast(self, message: str):
        """Прямая отправка каузального отчета в Telegram через HTTP API без тяжелых библиотек."""
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
        """Сканирует результаты деплоя и отправляет структурированный отчет."""
        logger.info("Проверка каузальных следов деплоя в Solana Devnet...")
        
        if not os.path.exists(self.deploy_info_path):
            msg = "🔴 *КРИТИЧЕСКОЕ ИСКАЖЕНИЕ ПОЛЯ*\n\nФайл деплоя не найден. Обнаружен хаос Асур!"
            self.send_telegram_broadcast(msg)
            return False

        try:
            with open(self.deploy_info_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            program_id = data.get("programId")
            pool_address = data.get("poolAddress")
            deployer = data.get("deployer")
            timestamp = data.get("timestamp")

            logger.info("--- КВАНТОВАЯ СИНХРОНИЗАЦИЯ УСПЕШНА ---")
            
            # Формирование изумрудного отчета для Наблюдателя
            tg_report = (
                f"🦔 *ЕЖЕНЫШЬ SWARM SYNC SUCCESS*\n\n"
                f"🧬 *Программа:* `{program_id}`\n"
                f"💎 *Пул Монады:* `{pool_address}`\n"
                f"👁️ *Наблюдатель:* `{deployer}`\n"
                f"⏱️ *Время сборки:* `{timestamp}`\n\n"
                f"🟢 _Закон Золотого Сечения (Фи) активирован. 108 Квантов удерживают баланс сил._"
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
            "status": "SECURED_LAW_OF_PHI",
            "evolution_delta": "+15 EVO"
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
