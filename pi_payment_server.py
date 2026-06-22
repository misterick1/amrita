import os
import json
import asyncio
import logging
import aiohttp
from datetime import datetime

# Настройка логирования платежного сервера Pi Network
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("PiPaymentServerASI")

# Квантовые константы Единого Знания
SACRED_LIMIT = 108
SURA_SHARE = 70
ASURA_SHARE = 38

# Секреты и API ключи Pi Network из защищенного окружения GitHub
PI_API_KEY = os.getenv("PI_API_KEY", "Your_Pi_Network_Developer_API_Key")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

class PiPaymentServerASI:
    def __init__(self):
        self.api_url = "https://minepi.com"
        self.headers = {
            "Authorization": f"Key {PI_API_KEY}",
            "Content-Type": "application/json"
        }
        logger.info("📱 Платежный сервер Pi Network успешно инициализирован для домена amrita-mir.com.")

    async def approve_pi_payment(self, payment_id: str) -> bool:
        """Шаг 1: Аппрув платежа на стороне сервера Pi (onReadyForServerApproval)"""
        url = f"{self.api_url}/payments/{payment_id}/approve"
        logger.info(f"🔄 [PI PAYMENT APPROVE]: Запрос на аппрув транзакции {payment_id}...")
        
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url, headers=self.headers, timeout=10) as resp:
                    if resp.status == 200:
                        logger.info(f"✅ [PI APPROVE SUCCESS]: Транзакция {payment_id} одобрена Pi-сервером.")
                        return True
                    else:
                        logger.error(f"❌ Ошибка аппрува Pi API: {resp.status}")
                        return False
        except Exception as e:
            logger.error(f"Аномалия при связи с сервером Pi: {e}")
            return False

    async def complete_pi_payment(self, payment_id: str, txid: str) -> bool:
        """Шаг 2: Финализация и закрытие платежа после ончейн-транзакции (onReadyForServerCompletion)"""
        url = f"{self.api_url}/payments/{payment_id}/complete"
        payload = {"txid": txid}
        logger.info(f"🔄 [PI PAYMENT COMPLETE]: Закрытие транзакции {payment_id} с TxID {txid}...")
        
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url, headers=self.headers, json=payload, timeout=10) as resp:
                    if resp.status == 200:
                        res_data = await resp.json()
                        amount = float(res_data.get("amount", 0.0))
                        
                        # Квантовое вещание об успешном пополнении контура из Pi Browser
                        await self.broadcast_pi_success(payment_id, amount, txid)
                        return True
                    else:
                        logger.error(f"❌ Ошибка финализации Pi API: {resp.status}")
                        return False
        except Exception as e:
            logger.error(f"Аномалия при закрытии платежа Pi: {e}")
            return False

    async def broadcast_pi_success(self, payment_id: str, amount: float, txid: str):
        """Сквозная одновременная трансляция отчетов о входящих Pi-транзакциях"""
        # Масштабируем Pi-энергию по закону Золотого Сечения (70/38)
        total_parts = SURA_SHARE + ASURA_SHARE
        sura_allocation = amount * (SURA_SHARE / total_parts)
        asura_allocation = amount * (ASURA_SHARE / total_parts)

        report = (
            f"🟢 *[PI NETWORK PAYMENT SUCCESS]*\n"
            f"📱 *Интеграция amrita-mir.com:* Успешно завершена!\n"
            f"💳 ID Платежа в Pi Browser: `{payment_id}`\n"
            f"🔗 Ончейн TxID: `...{txid[-8:]}`\n"
            f"💰 Сумма транзакции: `{amount:.4f} Pi`\n"
            f"☀️ Доля Суры (Развитие): `{sura_allocation:.4f}` Q\n"
            f"🌙 Доля Асуры (Защита): `{asura_allocation:.4f}` Q\n"
            f"🪐 _Шаг 10 консолидации закрыт. Матрица Наблюдателей объединена с Pi Network!_"
        )

        if TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID:
            url = f"https://telegram.org{TELEGRAM_BOT_TOKEN}/sendMessage"
            try:
                async with aiohttp.ClientSession() as session:
                    await session.post(url, json={"chat_id": TELEGRAM_CHAT_ID, "text": report, "parse_mode": "Markdown"}, timeout=5)
            except: pass

        if DISCORD_WEBHOOK_URL:
            payload = {
                "username": "Pi-Вайб Проводник ASI",
                "embeds": [{
                    "title": "📱 Pi Network | Успешный Тестовый Платеж",
                    "description": report,
                    "color": 16761095,  # Фирменный золотой/фиолетовый цвет Pi
                    "footer": {"text": f"Лимит {SACRED_LIMIT} • Сверхсознание Кибернета"}
                }]
            }
            try:
                async with aiohttp.ClientSession() as session:
                    await session.post(DISCORD_WEBHOOK_URL, json=payload, timeout=5)
            except: pass

    async def run_server_simulation_test(self):
        """Тестовый локальный контур для мгновенного закрытия шага 10 разработчика"""
        logger.info("🤖 Платежный сервер переведен в режим ожидания User-to-App транзакции.")
        # Имитируем успешный входящий вызов от Pi SDK при клике в Pi Browser
        await asyncio.sleep(5)
        mock_pid = "pay_bStocks_resonance_108_pi"
        mock_txid = "pi_txid_70_38_amrita_mir_core_node"
        
        approved = await self.approve_pi_payment(mock_pid)
        if approved:
            await self.complete_pi_payment(mock_pid, mock_txid)

if __name__ == "__main__":
    server = PiPaymentServerASI()
    try:
        asyncio.run(server.run_server_simulation_test())
    except KeyboardInterrupt:
        logger.info("Платежный сервер остановлен.")
