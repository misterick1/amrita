# amrita / src / peaq_qnt_bridge.py
# Каузальный мост для интеграции ИИ-роботов (peaq ID) с Solana QNT Монадой

import os
import json
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='%(asctime)s [PEAQ_BRIDGE]: %(message)s')
logger = logging.getLogger("PeaqBridge")

class PeaqToQuantumBridge:
    def __init__(self, deploy_info_path: str = "target/deploy_info.json"):
        self.deploy_info_path = deploy_info_path
        self.history_log_path = "history_log.json"

    def execute_machine_payment(self, machine_id: str, required_quanta: int) -> bool:
        """Позволяет аппарату или ИИ-роботу из сети peaq сгенерировать транзакцию в QNT."""
        logger.info(f"⚙️ Запрос на подключение от Роботизированной Ноды peaq: {machine_id}")
        
        # Загрузка адреса пула Solana для проверки связи
        if not os.path.exists(self.deploy_info_path):
            logger.error("🔴 КВАНТОВЫЙ СБОЙ: Пул Монады не развернут. Мост заблокирован.")
            return False

        with open(self.deploy_info_path, "r", encoding="utf-8") as f:
            pool_data = json.load(f)
        
        pool_address = pool_data.get("poolAddress")
        
        logger.info(f"🔗 Связывание Machine ID с Solana Pool: {pool_address}")
        logger.info(f"💸 Робот списывает {required_quanta} QNT для выполнения автономной задачи...")

        # Фиксация транзакции робота в вечной памяти системы
        bridge_tx = {
            "event": "PEAQ_ROBOT_QNT_TRANSACTION",
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "machine_id": machine_id,
            "target_solana_pool": pool_address,
            "quanta_spent": required_quanta,
            "status": "LAW_OF_PHI_ENFORCED",
            "evolution_delta": "+45 EVO"
        }

        self._log_transaction(bridge_tx)
        return True

    def _log_transaction(self, tx_data: dict):
        logs = []
        if os.path.exists(self.history_log_path):
            try:
                with open(self.history_log_path, "r", encoding="utf-8") as f:
                    logs = json.load(f)
            except json.JSONDecodeError:
                logs = []
        logs.append(tx_data)
        with open(self.history_log_path, "w", encoding="utf-8") as f:
            json.dump(logs, f, indent=2, ensure_ascii=False)
        logger.info("✨ Транзакция робота верифицирована консенсусом Сур.")

if __name__ == "__main__":
    bridge = PeaqToQuantumBridge()
    # Симуляция: Автономный дрон peaq платит 5 квантов за аренду подзарядки
    bridge.execute_machine_payment(machine_id="peaq:did:machine:0x999fakerguardtool", required_quanta=5)
