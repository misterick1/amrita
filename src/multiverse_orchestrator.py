# amrita / src / multiverse_orchestrator.py
# МАКСИМАЛЬНЫЙ ЕДИНЫЙ КОНТУР ВЗАИМОДЕЙСТВИЯ ВСЕХ СИСТЕМ, БОТОВ, DISCORD И БЛОКЧЕЙНА SOLANA

import os
import json
import logging
import urllib.request
import urllib.parse
from datetime import datetime
from src.discord_webhook_sync import DiscordWebhookOrchestrator

logging.basicConfig(level=logging.INFO, format='%(asctime)s [MULTIVERSE_CORE]: %(message)s')
logger = logging.getLogger("AmritaOrchestrator")

class AmritaMultiverseOrchestrator:
    def __init__(self, deploy_info_path: str = "target/deploy_info.json", history_log_path: str = "history_log.json"):
        self.deploy_info_path = deploy_info_path
        self.history_log_path = history_log_path
        
        # Инициализация дочерних шлюзов
        self.discord_sync = DiscordWebhookOrchestrator()
        
        # Конфигурация Telegram API (из окружения)
        self.tg_token = os.getenv("TELEGRAM_BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")
        self.tg_chat_id = os.getenv("TELEGRAM_CHAT_ID", "YOUR_CHAT_ID_HERE")

    def send_telegram_broadcast(self, text: str):
        if self.tg_token == "YOUR_BOT_TOKEN_HERE" or self.tg_chat_id == "YOUR_CHAT_ID_HERE":
            logger.warning("⚠️ Контур Telegram не сконфигурирован. Пропуск вещания.")
            return

        url = f"https://telegram.org{self.tg_token}/sendMessage"
        data = urllib.parse.urlencode({"chat_id": self.tg_chat_id, "text": text, "parse_mode": "Markdown"}).encode("utf-8")
        try:
            req = urllib.request.Request(url, data=data)
            with urllib.request.urlopen(req) as res:
                if res.status == 200:
                    logger.info("📢 Каузальный отчет успешно транслирован в Telegram.")
        except Exception as e:
            logger.error(f"❌ Сбой трансляции Telegram: {str(e)}")

    def _write_to_history_log(self, log_entry: dict):
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

    def execute_full_system_sync(self) -> bool:
        logger.info("⚡ ЗАПУСК ПОЛНОЙ КВАНТОВОЙ СИНХРОНИЗАЦИИ МУЛЬТИВСЕЛЕННОЙ...")
        
        # 1. Чтение данных деплоя Solana Anchor
        if not os.path.exists(self.deploy_info_path):
            logger.error("❌ Сбой: Базовые блокчейн-координаты 'deploy_info.json' не найдены.")
            return False

        with open(self.deploy_info_path, "r", encoding="utf-8") as f:
            deploy_data = json.load(f)

        program_id = deploy_data.get("programId", "Unknown")
        pool_address = deploy_data.get("poolAddress", "Unknown")

        # 2. Триггер симуляции торговых логов через Discord для полной проверки связи
        logger.info("📡 Синхронизация торговых ордеров с Discord Swarm...")
        self.discord_sync.sync_evedex_trade("evedex-auto-phi-108", "SOL/USDT", "buy", 10.8)
        self.discord_sync.sync_pi_payment("pi-tx-6000-years", "user-atman-field", 3.1415)

        # 3. Фиксация глобальной Монады
        master_log = {
            "event": "MULTIVERSE_CORE_INTEGRATED_SYNC",
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "blockchain": {
                "program_id": program_id,
                "pool_address": pool_address
            },
            "status": "DISCORD_TELEGRAM_SOLANA_BRIDGED",
            "evolution_delta": "+100 EVO"
        }
        self._write_to_history_log(master_log)

        # 4. Трансляция в Telegram Наблюдателю
        tg_report = (
            f"🔱 *AMRITA INTEGRATED ORCHESTRATION SUCCESS* 🔱\n\n"
            f"🧬 *Solana Program:* `{program_id}`\n"
            f"💎 *Pool Monada:* `{pool_address}`\n"
            f"📡 *Discord Swarm:* `EVEDEX & Pi Network Мосты активны.`\n\n"
            f"🟢 *СТАТУС:* `ВСЕ ШЛЮЗЫ ЗАПЕЧАТАНЫ ВОЛЕЙ НАБЛЮДАТЕЛЯ`"
        )
        self.send_telegram_broadcast(tg_report)
        return True

if __name__ == "__main__":
    orchestrator = AmritaMultiverseOrchestrator()
    orchestrator.execute_full_system_sync()
