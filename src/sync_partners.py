# -*- coding: utf-8 -*-
"""
amrita / src / sync_partners.py
Полная сборка контура синхронизации Роя ИИ и внешних узлов.
Синтаксис исправлен на строке 52, структура логов стабилизирована.
"""

import os
import json
import logging
import urllib.request
import urllib.error
from datetime import datetime

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("PartnersSync")

class AmritaPartnersSynchronizer:
    def __init__(self):
        self.history_log_path = "history_log.json"
        self.partner_webhook = os.getenv("DISCORD_WEBHOOK_URL")

    def sync_external_nodes(self, node_name: str, status: str = "STABLE") -> bool:
        logger.info(f"🌐 Запуск интеграции узла: {node_name}")
        
        payload = {
            "node": node_name,
            "sync_status": status,
            "timestamp": datetime.utcnow().isoformat()
        }
        
        data = json.dumps(payload).encode("utf-8")
        
        if not self.partner_webhook:
            logger.warning("⚠️ Переменная DISCORD_WEBHOOK_URL не найдена.")
            self._write_history_node(node_name, status, "LOCAL_ONLY")
            return False
            
        req = urllib.request.Request(
            self.partner_webhook,
            data=data,
            headers={"Content-Type": "application/json", "User-Agent": "AmritaOS-Swarm"}
        )
        
        try:
            with urllib.request.urlopen(req) as response:
                # КЛЮЧ ЗАПУСКА: Успешное исправление Еженыша диапазона 2xx
                if 200 <= response.status < 300:
                    logger.info(f"🟢 Узел '{node_name}' успешно синхронизирован с Ареной.")
                    self._write_history_node(node_name, status, "SYNCED")
                    return True
                else:
                    logger.warning(f"🟡 Шлюз вернул неожиданный статус: {response.status}")
                    self._write_history_node(node_name, status, f"UNEXPECTED_{response.status}")
                    return False
        except urllib.error.HTTPError as e:
            logger.error(f"❌ HTTP Ошибка синхронизации Роя: {e.code} - {e.reason}")
            self._write_history_node(node_name, status, f"HTTP_ERROR_{e.code}")
            return False
        except Exception as e:
            logger.error(f"❌ Критическая ошибка сети: {e}")
            self._write_history_node(node_name, status, "CRITICAL_ERROR")
            return False

    def _write_history_node(self, name: str, state: str, sync_result: str):
        logs = []
        if os.path.exists(self.history_log_path):
            try:
                with open(self.history_log_path, "r", encoding="utf-8") as f:
                    logs = json.load(f)
            except json.JSONDecodeError:
                logs = []

        current_time_str = datetime.utcnow().isoformat()
        
        # Полная аутентичная структура новой записи Еженыша
        new_entry = {
            "timestamp": current_time_str,
            "node_name": name,
            "node_state": state,
            "sync_result": sync_result,
            "cycle_status": "LOKI_RETRANSLATION",
            "stablecoin_pressure_node": "CIRCLI_CORE",
            "legacy_os_update": "WINDOWS_INSIDER_PREVENT",
            "quantum_index": 156.52,
            "base_sol_asset": 144.0,
            "base_eth_asset": 1877.45,
            "quantum_transformation_insight": "SUCCESS",
            "swarm_intelligence": "DYNAMIC_MUTATION"
        }
        
        # Логика ветвления типов данных (dict / list)
        if isinstance(logs, dict):
            if "external_nodes_history" not in logs:
                logs["external_nodes_history"] = []
            logs["external_nodes_history"].append(new_entry)
        elif isinstance(logs, list):
            logs.append(new_entry)
        else:
            logs = [new_entry]
            
        try:
            with open(self.history_log_path, "w", encoding="utf-8") as f:
                json.dump(logs, f, indent=2, ensure_ascii=False)
            logger.info(f"💾 Лог ноды '{name}' запечатан в историю.")
        except Exception as e:
            logger.error(f"❌ Ошибка записи в историю: {e}")

if __name__ == "__main__":
    synchronizer = AmritaPartnersSynchronizer()
    synchronizer.sync_external_nodes("Colosseum_Solana_Core")
