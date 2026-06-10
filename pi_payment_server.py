import os
import logging
from fastapi import FastAPI, HTTPException, Request, status
from pydantic import BaseModel, Field
import httpx
from dotenv import load_dotenv

# Настройка логирования под "Единый Квантовый Оркестратор"
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - [%(filename)s] - %(message)s")
logger = logging.getLogger("PiPaymentServer")

# Загружаем переменные окружения из .env
load_dotenv()

PI_API_KEY = os.getenv("PI_API_KEY")
PI_NETWORK_APP_ID = os.getenv("PI_NETWORK_APP_ID")

# Жесткая проверка конфигурации при запуске сервера
if not PI_API_KEY or not PI_NETWORK_APP_ID:
    logger.critical("КРИТИЧЕСКАЯ ОШИБКА: PI_API_KEY или PI_NETWORK_APP_ID не найдены в файле .env!")
    raise RuntimeError("Missing critical configuration environment variables.")

app = FastAPI(title="Pi Network Payment Gateway", version="1.0.0")

# --- МОДЕЛИ ДАННЫХ (PYDANTIC) ---

class PiPaymentCallback(BaseModel):
    action: str  # "complete" или "cancelled"
    paymentId: str
    txid: str | None = None

class CreatePaymentRequest(BaseModel):
    amount: float = Field(..., gt=0, description="Сумма платежа в PI")
    memo: str = Field(..., max_length=100, description="Описание платежа")
    uid: str = Field(..., description="Уникальный ID пользователя в системе")

# --- ЭНДПОИНТЫ ---

@app.get("/health")
async def health_check():
    """Проверка работоспособности шлюза"""
    return {"status": "alive", "pi_api_configured": bool(PI_API_KEY)}

@app.post("/v1/pi/create-payment", status_code=status.HTTP_201_CREATED)
async def create_pi_payment(payload: CreatePaymentRequest):
    """Шаг 1: Создание (инициализация) платежа в системе Pi Network"""
    logger.info(f"Создание платежа для {payload.uid} на {payload.amount} PI")
    
    url = "https://minepi.com"
    headers = {
        "Authorization": f"Key {PI_API_KEY}",
        "Content-Type": "application/json"
    }
    
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
                pi_response = response.json()
                logger.info(f"Платеж зарегистрирован. ID: {pi_response.get('identifier')}")
                return pi_response
            else:
                logger.error(f"Ошибка Pi API [Создание]: {response.status_code} - {response.text}")
                raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY, detail=f"Pi API Error: {response.text}")
        except httpx.RequestError as exc:
            logger.error(f"Сетевой сбой Pi API: {exc}")
            raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="Pi API unavailable")

@app.post("/v1/pi/callback", status_code=status.HTTP_200_OK)
async def pi_payment_callback(payload: PiPaymentCallback):
    """Шаг 2: Прием вебхука от Pi Network после оплаты пользователем"""
    logger.info(f"Получен вебхук. Действие: {payload.action}, ID платежа: {payload.paymentId}")
    
    if payload.action != "complete":
        logger.warning(f"Пропуск обработки. Статус платежа: {payload.action}")
        return {"status": "ignored", "reason": payload.action}
    
    # Верификация транзакции напрямую через Pi API
    is_valid = await verify_pi_payment(payload.paymentId)
    if not is_valid:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Транзакция не валидна")
    
    logger.info(f"УСПЕХ: Платеж {payload.paymentId} верифицирован и проведен.")
    return {"status": "success", "payment_id": payload.paymentId}

# --- ВНУТРЕННИЕ ФУНКЦИИ ---

async def verify_pi_payment(payment_id: str) -> bool:
    """Проверка статуса платежа с тройным повтором при сетевых ошибках"""
    url = f"https://minepi.com/{payment_id}"
    headers = {"Authorization": f"Key {PI_API_KEY}"}
    
    async with httpx.AsyncClient() as client:
        for attempt in range(3):
            try:
                response = await client.get(url, headers=headers, timeout=10.0)
                if response.status_code == 200:
                    data = response.json()
                    if data.get("status", {}).get("completed") is True:
                        return True
                    logger.error(f"Платеж не завершен: {data}")
                    return False
                elif response.status_code in:
                    logger.warning(f"Сбой сервера Pi ({response.status_code}). Попытка {attempt + 1}...")
                    continue
                else:
                    logger.error(f"Ошибка Pi API [Верификация]: {response.status_code}")
                    return False
            except httpx.RequestError as exc:
                logger.error(f"Ошибка сети на попытке {attempt + 1}: {exc}")
    return False
