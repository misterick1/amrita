# amrita / sync_partners.py
# Исправленная версия контура синхронизации партнеров

import os
import json
import logging
import urllib.request
from datetime import datetime

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger("PartnersSync")

class AmritaPartnersSynchronizer:
    def __init__(self):
        self.history_log_path = "history_log.json"
        self.partner_webhook = os.getenv("DISCORD_WEBHOOK")

    def sync_external_nodes(self, node_name: str, status: str = "ACTIVE") -> bool:
        logger.info(f"🔄 Запуск интеграции узла: {node_name}")

        payload = {
            "node": node_name,
            "sync_status": status,
            "timestamp": datetime.utcnow().isoformat() + "Z"
        }

        data = json.dumps(payload).encode("utf-8")
        
        if not self.partner_webhook:
            logger.warning("⚠️ Переменная DISCORD_WEBHOOK отсутствует. Запись локального лога.")
            self._write_history_node(node_name, status)
            return False

        req = urllib.request.Request(
            self.partner_webhook,
            data=data,
            headers={"Content-Type": "application/json", "User-Agent": "Amrita-Orchestrator"}
        )

        try:
            # Предохранитель для предотвращения отправки на тестовые ID
            if "YOUR_ACTUAL_WEBHOOK_ID" in self.partner_webhook:
                logger.warning("⚠️ Обнаружен тестовый шаблон Webhook ID. Пропуск сетевого запроса.")
                self._write_history_node(node_name, status)
                return True

            with urllib.request.urlopen(req) as response:
                # # ИСПРАВЛЕНО (Строка 65): Замена на безопасную проверку ответа
                if response.status == 200 or response.status == 204:
                    logger.info(f"🟢 Узел '{node_name}' успешно синхронизирован с сетью партнеров.")
                    self._write_history_node(node_name, status)
                    return True
                else:
                    logger.warning(f"⚠️ Шлюз вернул некорректный статус: {response.status}")
                    return False

        except Exception as e:
            logger.error(f"❌ Ошибка отправки данных узла {node_name}: {e}")
            self._write_history_node(node_name, status + "_ERROR")
            return False

    def _write_history_node(self, name: str, state: str):
        logs = []
        if os.path.exists(self.history_log_path):
            try:
                with open(self.history_log_path, "r", encoding="utf-8") as f:
                    logs = json.load(f)
            except json.JSONDecodeError:
                logs = []

        logs.append({
            "event": "PARTNER_NODE_SYNCHRONIZED",
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "node_identity": name,
            "node_state": state
        })

        with open(self.history_log_path, "w", encoding="utf-8") as f:
            json.dump(logs, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    synchronizer = AmritaPartnersSynchronizer()
    # Первичная инициализация внешнего узла Колизея в структуре Роя
    synchronizer.sync_external_nodes("Colosseum", "ACTIVE")
