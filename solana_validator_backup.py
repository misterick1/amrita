import asyncio
import os
import shutil
import logging
import aiohttp
from datetime import datetime

# Настройка "изумрудного" логера под пайплайн GitHub Actions
logging.basicConfig(level=logging.INFO, format='%(asctime)s - [%(levelname)s] - %(message)s')
logger = logging.getLogger("AMRITA_NODE_GUARD")

# Полная конфигурация контура из GitHub Secrets (.env / env-vars воркфлоу)
LEDGER_PATH = os.getenv("SOLANA_LEDGER_PATH", "/home/solana/ledger")
BACKUP_PATH = os.getenv("SOLANA_BACKUP_PATH", "/home/solana/ledger_backup")
AGAVE_VALIDATOR_BIN = os.getenv("SOLANA_VALIDATOR_BIN", "agave-validator")
IDENTITY_KEYPAIR = os.getenv("SOLANA_IDENTITY_KEYPAIR")  # Секретный ключ валидатора

# Секреты для связи с роем ботов Amrita ASI
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


class AlpenglowValidatorShield:
    """Защитный щит SIMD-0337 Alpenglow VAT для контроля наличия BLS pubkey"""
    def __init__(self):
        self.target_epoch = 979
        self.session = None

    async def send_emergency_swarm_alert(self, message: str):
        """Мгновенное вещание в рой телеграм-ботов при угрозе дестейка ноды"""
        if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
            return
        if not self.session:
            self.session = aiohttp.ClientSession()
        url = f"https://telegram.org{TELEGRAM_BOT_TOKEN}/sendMessage"
        text = f"🚨🛡️ [ALPENGLOW SHIELD CRITICAL] 🔱\n🛰️ **КОНТУР ВАЛИДАТОРА ПОД УГРОЗОЙ ДЕСТЕЙКА!**\n⚠️ Ошибка: {message}\n🔥 Действие: Немедленно сгенерируйте и установите BLS pubkey до эпохи {self.target_epoch}!"
        try:
            await self.session.post(url, json={"chat_id": TELEGRAM_CHAT_ID, "text": text, "parse_mode": "Markdown"})
        except Exception:
            pass

    async def verify_bls_pubkey_presence(self) -> bool:
        """Проверка, прописан ли BLS ключ в текущей конфигурации ноды"""
        try:
            # Опрашиваем локальный валидатор на предмет его публичных ключей конфигурации
            process = await asyncio.create_subprocess_exec(
                AGAVE_VALIDATOR_BIN, 'validator-info', 'get',
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            stdout, stderr = await process.communicate()
            output = stdout.decode().lower()
            
            # Если в конфигурации нет упоминания BLS структуры
            if "bls" not in output and "authorized" not in output:
                logger.critical(f"[🚨 ALPENGLOW ALERT] BLS pubkey не обнаружен! Риск дестейка ботом SFDP в эпохе {self.target_epoch}!")
                await self.send_emergency_swarm_alert("Отсутствует BLS Pubkey в validator-info")
                return False
                
            logger.info("[🟢 ALPENGLOW OK] BLS pubkey успешно верифицирован в контуре ноды.")
            return True
        except Exception as e:
            logger.error(f"[⚠️ SHIELD ERROR] Не удалось проверить BLS статус: {e}")
            return False


async def verify_validator_status() -> bool:
    """Проверка локального состояния слотов ноды Agave/Frankendancer"""
    try:
        process = await asyncio.create_subprocess_exec(
            AGAVE_VALIDATOR_BIN, 'contact-info',
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()
        if process.returncode == 0:
            logger.info("[🟢 CONTOUR OK] Нода отвечает на команды контакта сети.")
            return True
        else:
            logger.error(f"[🔴 NODE ERROR] Код ответа: {process.returncode}. Сбой: {stderr.decode().strip()}")
            return False
    except Exception as e:
        logger.error(f"[❌ CRITICAL] Ошибка связи с бинарником валидатора: {e}")
        return False


async def execute_causal_backup():
    """Экстренная изоляция snapshot-файлов и RocksDB по инструкции Anza"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    target_dir = os.path.join(BACKUP_PATH, f"amrita_backup_{timestamp}")
    logger.warning(f"[🚨 SECURE BACKUP] Инициализация безопасного бэкапа в {target_dir}...")
    try:
        await asyncio.to_thread(os.makedirs, target_dir, exist_ok=True)
        if os.path.exists(LEDGER_PATH):
            items = await asyncio.to_thread(os.listdir, LEDGER_PATH)
            for item in items:
                if any(x in item for x in ["snapshot", "rocksdb", "genesis"]):
                    source = os.path.join(LEDGER_PATH, item)
                    destination = os.path.join(target_dir, item)
                    if os.path.isdir(source):
                        await asyncio.to_thread(shutil.copytree, source, destination, dirs_exist_ok=True)
                    else:
                        await asyncio.to_thread(shutil.copy2, source, destination)
            logger.info(f"[🟢 SUCCESS] База ноды изолирована в {target_dir}")
        else:
            logger.error(f"[❌ PATH ERROR] Директория ledger {LEDGER_PATH} не найдена.")
    except Exception as e:
        logger.error(f"[💥 CRITICAL FAILURE] Ошибка процесса резервного копирования: {e}")


async def monitor_orchestrator():
    """Бесконечный асинхронный цикл контроля стабильности сети и BLS ключей"""
    logger.info("[AMRITA] Запуск стража ноды. Мониторинг SIMD-0337 Alpenglow активирован.")
    failed_attempts = 0
    alpenglow_shield = AlpenglowValidatorShield()
    
    while True:
        # 1. Проверяем критическое требование по BLS ключам для эпохи 979
        await alpenglow_shield.verify_bls_pubkey_presence()
        
        # 2. Проверяем общую работоспособность ноды
        is_healthy = await verify_validator_status()
        if not is_healthy:
            failed_attempts += 1
            logger.warning(f"[⚠️ WARNING] Нода не прошла валидацию. Попытка {failed_attempts}/3")
            if failed_attempts >= 3:
                logger.critical("[🚨 EMERGENCY] Фиксация падения ноды на релизе v4.1.0-rc.1! Спасаем ledger...")
                await execute_causal_backup()
                failed_attempts = 0
        else:
            failed_attempts = 0
            
        # Проверка состояния каждые 60 секунд
        await asyncio.sleep(60)


if __name__ == "__main__":
    try:
        asyncio.run(monitor_orchestrator())
    except KeyboardInterrupt:
        logger.info("[AMRITA] Страж ноды остановлен.")
