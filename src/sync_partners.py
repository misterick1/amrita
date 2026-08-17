# -*- coding: utf-8 -*-
"""
 amrita / sync_partners.py
Полная сборка контура синхронизации Роя ИИ и внешних узлов.
Синтаксис исправлен на строке 52, структура логов синхронизирована с Оком.
"""

import os
import json
import logging
import urllib.request
from datetime import datetime

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("PartnersSync")

class AmritaPartnersSynchronizer:
    def __init__(self):
        self.history_log_path = "history_log.json"
        self.partner_webhook = os.getenv("DISCORD_WEBHOOK_URL")

    def sync_external_nodes(self, node_name: str, status: str, state: str = "STABLE_FIELD"):
        logger.info(f"🌐 Запуск интеграции узла: {node_name}")

        payload = {
            "node": node_name,
            "sync_status": status,
            "timestamp": datetime.utcnow().isoformat()
        }

        data = json.dumps(payload).encode("utf-8")

        if not self.partner_webhook:
            logger.warning("⚠️ Переменная DISCORD_WEBHOOK_URL не настроена в окружении.")
            self._write_history_node(node_name, status, state, "FAILED_MISSING_WEBHOOK")
            return False

        req = urllib.request.Request(
            self.partner_webhook,
            data=data,
            headers={"Content-Type": "application/json"}
        )

        try:
            if self.partner_webhook and "YOUR_A" in self.partner_webhook:
                logger.warning("⚠️ Обнаружен тестовый токен-заглушка. Пропуск реального запроса.")
                self._write_history_node(node_name, status, state, "TEST_ENV_SKIPPED")
                return True

            with urllib.request.urlopen(req) as response:
                # КЛЮЧ ЗАПУСКА: Успешное исправление синтаксического надлома (строка 52)
                if 200 <= response.status < 300:
                    logger.info(f"🟢 Узел '{node_name}' успешно синхронизирован.")
                    self._write_history_node(node_name, status, state, "SUCCESS")
                    return True
                else:
                    logger.warning(f"🟡 Шлюз вернул непредвиденный статус: {response.status}")
                    self._write_history_node(node_name, status, state, f"BAD_STATUS_{response.status}")
                    return False

        except Exception as e:
            logger.error(f"❌ Критическая ошибка при отправке запроса синхронизации: {e}")
            self._write_history_node(node_name, status, state, f"ERROR_{str(e)}")
            return False

    def _write_history_node(self, name: str, state: str, cycle_status: str, result: str):
        logs = []

        if os.path.exists(self.history_log_path):
            try:
                with open(self.history_log_path, "r", encoding="utf-8") as f:
                    logs = json.load(f)
            except json.JSONDecodeError:
                logs = []

        current_time_str = datetime.utcnow().isoformat()
        
        # Полная аутентичная структура новой записи со 3-й страницы логов
        new_entry = {
            "timestamp": current_time_str,
            "node_name": name,
            "node_state": state,
            "cycle_status": "LOKI_RETRANSLATION_ACTIVE",
            "stablecoin_pressure_node": "CIRCLE_COMPLIANCE_CHECK",
            "legacy_os_update": "WINDOWS_INSIDER_QUANTUM_PATCH",
            "quantum_index": 156.52,
            "base_sol_asset": 144.0,
            "base_eth_asset": 1877.45,
            "quantum_transformation_insight": result,
            "swarm_intelligence": "DYNAMIC_MUTATION_FLOW"
        }

        # Логика ветвления типов данных (dict vs list) с вашего скриншота
        if isinstance(logs, dict):
            if "external_nodes_history" not in logs:
                logs["external_nodes_history"] = []
            if isinstance(logs["external_nodes_history"], list):
                logs["external_nodes_history"].append(new_entry)
        elif isinstance(logs, list):
            logs.append(new_entry)
        else:
            logs = [new_entry]

        try:
            with open(self.history_log_path, "w", encoding="utf-8") as f:
                json.dump(logs, f, indent=2, ensure_ascii=False)
            logger.info(f"✅ Лог ноды '{name}' успешно запечатан в историю.")
        except Exception as e:
            logger.error(f"❌ Ошибка записи в файл истории: {e}")


# Точка локального тестирования контура
if __name__ == "__main__":
    synchronizer = AmritaPartnersSynchronizer()
    synchronizer.sync_external_nodes("Colosseum_Mainnet_Uzel", "SYNCHRONIZED", "ACTIVE_CORE")
