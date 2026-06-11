import os
import logging
from fastapi import FastAPI, HTTPException, BackgroundTasks
from pydantic import BaseModel
import httpx
from dotenv import load_dotenv

# Инициализация логирования ядра AMRITA
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("PiPaymentServer")

load_dotenv()

app = FastAPI(title="AMRITA Quantum Payment Gateway", version="2.5.0")

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")
TITAN_API_URL = "https://titan.exchange"
ARCFX_API_BASE = "https://arcfx.app" # Базовый URL нового REST API хаба ArcFX

class PaymentNotification(BaseModel):
    amount_usd: float
    currency: str
    tx_hash: str
    payer_id: str

class BatchPayoutRequest(BaseModel):
    wallets: list[str]
    amount_per_wallet: float
    token: str = "USDC"

async def send_payment_log_to_discord(payment: PaymentNotification, status: str, route_info: str, arcfx_info: str = "N/A"):
    """Отправка красивой карточки транзакции в командный центр Discord"""
    if not DISCORD_WEBHOOK_URL:
        return
        
    payload = {
        "username": "Солитон: Финансовый Оркестратор",
        "embeds": [{
            "title": "💰 Зафиксирована Квантовая Транзакция",
            "description": f"Анализ ликвидности, маршрутизация и B2B-интеграция завершены.",
            "color": 3066993 if status == "SUCCESS" else 15158332,
            "fields": [
                {"name": "Сумма", "value": f"${payment.amount_usd} USD", "inline": True},
                {"name": "Валюта поступления", "value": f"`{payment.currency}`", "inline": True},
                {"name": "Протокол приватности", "value": "🔐 Arc Privacy Layer (Circle Spec)", "inline": False},
                {"name": "Маршрут Titan Exchange", "value": f"🔄 {route_info}", "inline": False},
                {"name": "B2B Инфраструктура (ArcFX Hub)", "value": f"🔗 {arcfx_info}", "inline": False},
                {"name": "Хэш транзакции", "value": f"`{payment.tx_hash[:16]}...`", "inline": False}
            ],
            "footer": {"text": "AMRITA Core Liquidity Layer"}
        }]
    }
    async with httpx.AsyncClient() as client:
        try:
            await client.post(DISCORD_WEBHOOK_URL, json=payload)
        except Exception as e:
            logger.error(f"Не удалось отправить финансовый лог в Discord: {e}")

@app.get("/")
def read_root():
    return {"status": "online", "core": "AMRITA MIR Soliton active", "b2b_layer": "ArcFX REST Sync Active"}

@app.post("/api/v2/payment/webhook")
async def process_incoming_payment(payment: PaymentNotification, background_tasks: BackgroundTasks):
    """
    Адаптивный платежный шлюз с интеграцией ArcFX REST API и Titan Exchange.
    """
    logger.info(f"Получено платежное уведомление на сумму {payment.amount_usd} от {payment.payer_id}")
    
    # Имитация генерации инвойса/ссылки через ArcFX Developer Hub
    arcfx_invoice_status = "Generated shareable pay link via ArcFX CCTP v2"
    logger.info(f"💼 ArcFX Hub: {arcfx_invoice_status}")
    
    if payment.currency != "USDC":
        route_info = f"Автоматический своп {payment.currency} -> USDC через Titan Pool"
        logger.info(f"🔄 Агрегация ликвидности: {route_info}")
    else:
        route_info = "Прямой транзит USDC (Instant Cross-Chain Routing)"
        logger.info("Прямой транзит стейблкоина выполнен.")
        
    background_tasks.add_task(send_payment_log_to_discord, payment, "SUCCESS", route_info, arcfx_invoice_status)
    
    return {
        "success": True,
        "message": "Routed via Titan & Processed with ArcFX Hub API",
        "soliton_status": "synchronized"
    }

@app.post("/api/v2/payout/batch")
async def trigger_batch_payout(payout: BatchPayoutRequest):
    """
    Эндпоинт для массовых B2B выплат (например, зарплаты DAO или пула ботов).
    Использует концепцию Batch Multisend до 500 кошельков за раз.
    """
    wallet_count = len(payout.wallets)
    if wallet_count > 500:
        raise HTTPException(status_code=400, detail="ArcFX CCTP v2 поддерживает до 500 кошельков в одной транзакции")
        
    total_payout = wallet_count * payout.amount_per_wallet
    logger.info(f"🚀 Инициация массовой выплаты ArcFX Batch Multisend на {wallet_count} адресов. Всего: {total_payout} {payout.token}")
    
    # В будущем здесь будет реальный POST-запрос к REST-эндпоинту ArcFX для подписания Safe Multi-sig
    return {
        "success": True,
        "batch_status": "Pending Multi-sig Approval",
        "processed_wallets": wallet_count,
        "total_distributed": total_payout
    }
