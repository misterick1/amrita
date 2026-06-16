import asyncio
import logging
import os
from telegram_bridge import send_telegram_message  # Импорт вашей функции отправки

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def test_trigger():
    logger.info("📡 Запуск комплексного теста систем...")

    # 1. Формирование вашего фирменного сообщения для Telegram
    test_text = (
        "🚀 <b>Квантовый Синхронизатор Активирован</b>\n"
        "🦔 Ёжик, Квантовый Навигатор на базе Helius RPC запущен!\n"
        "📱 Мобильный мост управления работает стабильно.\n"
        "🪐 Все системы (bS, Solana, Arc) синхронизированы."
    )

    # Отправка уведомления в Telegram
    logger.info("📤 Отправка отчета в Telegram...")
    success = await send_telegram_message(test_text)
    
    if success:
        logger.info("🎉 Тестовое сообщение успешно доставлено в Telegram!")
    else:
        logger.error("❌ Сбой отправки сообщения в Telegram.")

    # 2. Интеграция теста Solana через наш новый секрет Helius
    logger.info("🌐 Проверка подключения к инфраструктуре Solana...")
    
    # Ленивый импорт библиотек Solana, установленных в GitHub Actions
    try:
        from solana.rpc.async_api import AsyncClient
        from solders.pubkey import Pubkey
        
        rpc_url = os.environ.get("SOLANA_RPC_URL")
        
        if not rpc_url:
            logger.error("❌ Сбой теста Solana: Переменная SOLANA_RPC_URL не найдена в секретах GitHub!")
            return

        async with AsyncClient(rpc_url) as client:
            # Запрос текущего слота сети для проверки связи
            slot_response = await client.get_slot()
            logger.info(f"✅ Helius RPC отвечает стабильно! Текущий слот Solana: {slot_response.value}")
            
            # Проверяем баланс кошелька разработчика, если секрет передан
            dev_wallet = os.environ.get("DEVELOPER_WALLET")
            if dev_wallet:
                pubkey = Pubkey.from_string(dev_wallet)
                balance_response = await client.get_balance(pubkey)
                sol_balance = balance_response.value / 10**9
                logger.info(f"💰 Баланс кошелька разработчика: {sol_balance} SOL")
            else:
                logger.info("ℹ️ Тест баланса пропущен: Переменная DEVELOPER_WALLET не задана.")
                
    except ImportError:
        logger.warning("⚠️ Библиотеки 'solana'/'solders' не установлены локально. Полный тест выполнится в облаке GitHub.")
    except Exception as e:
        logger.error(f"❌ Критическая ошибка при работе с Solana RPC: {e}")

if __name__ == "__main__":
    asyncio.run(test_trigger())
