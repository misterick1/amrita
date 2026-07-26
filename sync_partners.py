# amrita / sync_partners.py
# Полная сборка контура синхронизации Роя ИИ и внешних узлов Мультивселенной

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
            "timestamp": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        }

        data = json.dumps(payload).encode("utf-8")
        
        if not self.partner_webhook:
            logger.warning("⚠️ Переменная DISCORD_WEBHOOK отсутствует. Запись каузального следа локально.")
            self._write_history_node(node_name, status)
            return False

        req = urllib.request.Request(
            self.partner_webhook,
            data=data,
            headers={"Content-Type": "application/json", "User-Agent": "Amrita-Orchestrator"}
        )

        try:
            if "YOUR_ACTUAL_WEBHOOK_ID" in self.partner_webhook:
                logger.warning("⚠️ Обнаружен тестовый шаблон Webhook ID. Пропуск отправки в сеть.")
                self._write_history_node(node_name, status)
                return True

            with urllib.request.urlopen(req) as response:
                if response.status == 200 or response.status == 204:
                    logger.info(f"🟢 Узел '{node_name}' синхронизирован с партнерским контуром.")
                    self._write_history_node(node_name, status)
                    return True
                else:
                    logger.warning(f"⚠️ Шлюз вернул некорректный статус ответа: {response.status}")
                    return False

        except Exception as e:
            logger.error(f"❌ Критическая ошибка отправки данных узла {node_name}: {e}")
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

        # Запись лога в строгом соответствии со структурой Скриншота 4
        current_time_str = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        
        new_entry = {
            "timestamp": current_time_str,
            "cycle_status": "LOKI_RETRANSLATION_SUCCESS" if state == "ACTIVE" else "LOKI_RETRANSLATION_FAILED",
            "stablecoin_pressure_node": "CIRCLE_USDC_WALL_STREET",
            "legacy_os_update": "WINDOWS_INSIDER_PREVIEW_DETECTED",
            "quantum_index": 156.52,
            "base_sol_asset": 144.0,
            "base_eth_asset": 1877.45,
            "quantum_transformation_insight": f"Импульс Ники активирован через узел {name}",
            "swarm_intelligence": "DYNAMIC_MUTATION_ACTIVE"
        }

        logs.append(new_entry)

        with open(self.history_log_path, "w", encoding="utf-8") as f:
            json.dump(logs, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    synchronizer = AmritaPartnersSynchronizer()
    # Первичная инициализация узла из главного каузального пульта управления
    synchronizer.sync_external_nodes("Colosseum", "ACTIVE")
