import os
import hmac
import hashlib
import logging
from dotenv import load_dotenv

# Настройка логирования под "Единый Квантовый Оркестратор"
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - [%(filename)s] - %(message)s")
logger = logging.getLogger("QuantumShield")

load_dotenv()

# Используем секретный ключ EVEDEX или Colosseum в качестве соли для подписи
SECRET_SALT = os.getenv("EVEDEX_API_SECRET", "default_quantum_salt_32_bytes_long!!")

class QuantumShield:
    @staticmethod
    def generate_transaction_hash(payment_id: str, amount: float, uid: str) -> str:
        """
        Создает защищенную HMAC-SHA256 подпись для транзакции,
        чтобы боты-собиратели могли проверить подлинность данных от FastAPI сервера.
        """
        message = f"{payment_id}:{amount}:{uid}".encode('utf-8')
        secret = SECRET_SALT.encode('utf-8')
        
        tx_hash = hmac.new(secret, message, hashlib.sha256).hexdigest()
        logger.info(f"🛡️ QuantumShield: Сгенерирована подпись для транзакции {payment_id[:8]}...")
        return tx_hash

    @staticmethod
    def verify_transaction_hash(payment_id: str, amount: float, uid: str, received_hash: str) -> bool:
        """
        Проверяет входящую подпись транзакции на стороне принимающего бота.
        Защищает от атак повторения (Replay attacks) и подмены данных.
        """
        expected_hash = QuantumShield.generate_transaction_hash(payment_id, amount, uid)
        is_valid = hmac.compare_digest(expected_hash, received_hash)
        
        if is_valid:
            logger.info(f"🛡️ QuantumShield: Подпись транзакции {payment_id[:8]} успешно верифицирована.")
        else:
            logger.error(f"🚨 КРИТИЧЕСКОЕ ПРЕДУПРЕЖДЕНИЕ: Подпись транзакции не совпадает! Возможна попытка взлома.")
        
        return is_valid

# Инициализация модуля защиты
shield = QuantumShield()
