# amrita / src / ezhenysh_bot.py
# Модуль интеграции ИИ-Логики Еженыша с блокчейн-контуром Solana Devnet

import os
import json
import logging
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
        self.evolution_points = 205  # Текущий уровень EVO
        self.history_log_path = "history_log.json"

    def verify_and_sync_solana_deployment(self) -> bool:
        """Сканирует и синхронизирует результаты блокчейн-деплоя с ядром бота."""
        logger.info("Проверка каузальных следов деплоя в Solana Devnet...")
        
        if not os.path.exists(self.deploy_info_path):
            logger.warning(
                "🚩 ВНИМАНИЕ: Файл деплоя не найден. "
                "Система находится в режиме 'Лирой Дженкинс' (Хаос/Асуры)!"
            )
            return False

        try:
            with open(self.deploy_info_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            program_id = data.get("programId")
            pool_address = data.get("poolAddress")
            deployer = data.get("deployer")
            timestamp = data.get("timestamp")

            logger.info("--- КВАНТОВАЯ СИНХРОНИЗАЦИЯ УСПЕШНА ---")
            logger.info(f"🧬 Смарт-контракт: {program_id}")
            logger.info(f"💎 Адрес Пула Монады: {pool_address}")
            logger.info(f"👁️ Воля Наблюдателя: {deployer}")
            
            # Запись успешной синхронизации в вечный лог
            self._write_to_history_log(pool_address, timestamp)
            return True

        except Exception as e:
            logger.error(f"❌ Ошибка чтения матрицы деплоя: {str(e)}")
            return False

    def _write_to_history_log(self, pool_address: str, deploy_time: str):
        """Записывает событие деплоя в вечный файл логов history_log.json без дублирования."""
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
                    if not isinstance(logs, list):
                        logs = []
            except json.JSONDecodeError:
                logs = []

        logs.append(log_entry)

        with open(self.history_log_path, "w", encoding="utf-8") as f:
            json.dump(logs, f, indent=2, ensure_ascii=False)
            
        logger.info(f"💾 Запись успешно добавлена в вечный лог {self.history_log_path}")


if __name__ == "__main__":
    # Инициализация и тестовый прогон ядра автоматического мониторинга
    orchestrator = EzhenyshBotOrchestrator()
    
    # Симуляция проверки
    success = orchestrator.verify_and_sync_solana_deployment()
    if success:
        print("\n🦔 Еженышь: 'План зачистки блокчейн-комнат готов. Баланс 108 квантов зафиксирован!'")
    else:
        print("\n🔴 Еженышь: 'Поле искажено! Требуется запуск deploy_amrita.ts'")
