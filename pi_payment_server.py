import os
import logging
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
import httpx
from dotenv import load_dotenv

# Настройка логирования под "Единый Квантовый Оркестратор"
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - [%(filename)s] - %(message)s")
logger = logging.getLogger("PiPaymentServer")

load_dotenv()

PI_API_KEY = os.getenv("PI_API_KEY")
PI_NETWORK_APP_ID = os.getenv("PI_NETWORK_APP_ID")
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

if not PI_API_KEY or not PI_NETWORK_APP_ID:
    logger.critical("КРИТИЧЕСКАЯ ОШИБКА: Конфигурация .env не полная!")
    raise RuntimeError("Missing critical configuration environment variables.")

app = FastAPI(title="Pi Network Payment Gateway", version="1.1.0")

# --- МОДЕЛИ ДАННЫХ ---

class PiPaymentCallback(BaseModel):
    action: str  
    paymentId: str
    txid: str | None = None

class CreatePaymentRequest(BaseModel):
    amount: float = Field(..., gt=0)
    memo: str = Field(..., max_length=100)
    uid: str = Field(..., description="ID пользователя в системе")

# --- ИНТЕГРАЦИЯ С DISCORD (HTTPX) ---

async def send_payment_notification(payment_id: str, amount: float, uid: str):
    """Отправка асинхронного уведомления в Discord рой"""
    if not DISCORD_WEBHOOK_URL:
        logger.warning("DISCORD_WEBHOOK_URL не задан в .env. Пропуск уведомления.")
        return

    payload = {
        "username": "Единый Квантовый Оркестратор",
        "embeds": [
            {
                "title": "🟢 Успешная транзакция Pi Network",
                "color": 3066993,
                "fields": [
                    {"name": "Пользователь (UID)", "value": f"`{uid}`", "inline": True},
                    {"name": "Сумма", "value": f"**{amount} PI**", "inline": True},
                    {"name": "ID транзакции", "value": f"`{payment_id}`", "inline": False}
                ],
                "footer": {"text": "Fractal Lego Builder | Swarm Mode"}
            }
        ]
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(DISCORD_WEBHOOK_URL, json=payload, timeout=5.0)
            if response.status_code == 204:
                logger.info(f"Лог платежа {payment_id} успешно доставлен в Discord.")
            else:
                logger.error(f"Ошибка Discord API: {response.status_code}")
        except httpx.RequestError as exc:
            logger.error(f"Сетевой сбой при отправке в Discord: {exc}")

# --- ЭНДПОИНТЫ ---

@app.get("/health")
async def health_check():
    return {"status": "alive", "pi_api_configured": bool(PI_API_KEY), "discord_configured": bool(DISCORD_WEBHOOK_URL)}

@app.post("/v1/pi/create-payment", status_code=status.HTTP_201_CREATED)
async def create_pi_payment(payload: CreatePaymentRequest):
    url = "https://minepi.com"
    headers = {"Authorization": f"Key {PI_API_KEY}", "Content-Type": "application/json"}
    
    payment_data = {
        "payment": {
            "amount": payload.amount,
            "memo": payload.memo,
            "metadata": {"uid": payload.uid},
            "uid": payload.uid
        }
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url, json=payment_data, headers=headers, timeout=10.0)
            if response.status_code == 200:
                return response.json()
            raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY, detail=f"Pi API Error: {response.text}")
        except httpx.RequestError as exc:
            raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=f"Network error: {exc}")

@app.post("/v1/pi/callback", status_code=status.HTTP_200_OK)
async def pi_payment_callback(payload: PiPaymentCallback):
    logger.info(f"Получен вебхук для платежа: {payload.paymentId}")
    
    if payload.action != "complete":
        return {"status": "ignored", "reason": payload.action}
    
    # Запрос деталей платежа для получения точной суммы (amount) и UID
    url = f"https://minepi.com/{payload.paymentId}"
    headers = {"Authorization": f"Key {PI_API_KEY}"}
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, timeout=10.0)
            if response.status_code == 200:
                data = response.json()
                if data.get("status", {}).get("completed") is True:
                    amount = data.get("amount", 0.0)
                    uid = data.get("uid", "unknown")
                    
                    # КЛЮЧЕВОЙ МОМЕНТ: Отправляем триггер в Discord рой
                    await send_payment_notification(payload.paymentId, amount, uid)
                    
                    return {"status": "success", "payment_id": payload.paymentId}
            raise HTTPException(status_code=400, detail="Валидация транзакции провалена")
        except httpx.RequestError:
            raise HTTPException(status_code=503, detail="Pi API Gateway Timeout")
