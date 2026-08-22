# -*- coding: utf-8 -*-
"""
amrita / src / sync_partners.py
Исправленный контур синхронизации Роя ИИ
"""

import os
import json
import logging
import urllib.request
import urllib.error
from datetime import datetime

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger("PartnersSync")

class AmritaPartnersSynchronizer:
    def __init__(self):
        self.history_log_path = "history_log.json"
        self.partner_webhook = os.getenv("DISCORD_WEBHOOK_URL")

    def sync_external_nodes(self, node_name: str, status: str = "active"):
        logger.info(f"🌐 Запуск интеграции узла: {node_name}")

        payload = {
            "node": node_name,
            "sync_status": status,
            "timestamp": datetime.utcnow().isoformat()
        }

        data = json.dumps(payload).encode("utf-8")

        if not self.partner_webhook:
            logger.warning("⚠️ Переменная DISCORD_WEBHOOK_URL не задана в окружении.")
            self._write_history_node(node_name, status, "failed_no_webhook")
            return False

        req = urllib.request.Request(
            self.partner_webhook,
            data=data,
            headers={"Content-Type": "application/json"}
        )

        try:
            with urllib.request.urlopen(req) as response:
                status_code = response.getcode()
                if 200 <= status_code < 300:
                    logger.info(f"🟢 Узел '{node_name}' успешно синхронизирован. Код: {status_code}")
                    self._write_history_node(node_name, status, "success")
                    return True
                else:
                    logger.warning(f"🟡 Шлюз вернул нетипичный статус: {status_code}")
                    self._write_history_node(node_name, status, f"warning_{status_code}")
                    return False
        except urllib.error.HTTPError as e:
            logger.error(f"❌ HTTP Ошибка синхронизации: {e.code}")
            self._write_history_node(node_name, status, f"http_error_{e.code}")
            return False
        except Exception as e:
            logger.error(f"❌ Критическая ошибка контура: {str(e)}")
            self._write_history_node(node_name, status, "critical_error")
            return False

    def _write_history_node(self, name: str, state: str, sync_result: str):
        logs = []
        if os.path.exists(self.history_log_path):
            try:
                with open(self.history_log_path, "r", encoding="utf-8") as f:
                    logs = json.load(f)
            except Exception:
                logs = []

        current_time_str = datetime.utcnow().isoformat()

        new_entry = {
            "timestamp": current_time_str,
            "node_name": name,
            "node_state": state,
            "sync_result": sync_result,
            "cycle_status": "LOKI_RETRANSLATION",
            "stablecoin_pressure_node": "CIRCLI_CORE",
            "quantum_index": 156.52,
            "base_sol_asset": 144.0,
            "base_eth_asset": 1877.45,
            "X_AI_COEFFICIENT": 1.94159456
        }

        if isinstance(logs, list):
            logs.append(new_entry)
        else:
            logs = [new_entry]

        try:
            with open(self.history_log_path, "w", encoding="utf-8") as f:
                json.dump(logs, f, indent=2, ensure_ascii=False)
            logger.info(f"💾 Лог ноды '{name}' записан в историю.")
        except Exception as e:
            logger.error(f"❌ Ошибка записи в историю: {str(e)}")


if __name__ == "__main__":
    synchronizer = AmritaPartnersSynchronizer()
    synchronizer.sync_external_nodes("Colosseum_Solana")
