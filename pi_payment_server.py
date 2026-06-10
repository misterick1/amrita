import os
import logging
from fastapi import FastAPI, HTTPException, Request, status
from pydantic import BaseModel
import httpx
from dotenv import load_dotenv

# 1. Настройка логирования под "Единый Квантовый Оркестратор"
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - [%(filename)s] - %(message)s")
logger = logging.getLogger("PiPaymentServer")

# Загружаем переменные окружения
load_dotenv()

PI_API_KEY = os.getenv("PI_API_KEY")
PI_NETWORK_APP_ID = os.getenv("PI_NETWORK_APP_ID")

# Жесткая проверка конфигурации при запуске (Защита от пустых ключей)
if not PI_API_KEY or not PI_NETWORK_APP_ID:
    logger.critical("КРИТИЧЕСКАЯ ОШИБКА: PI_API_KEY или PI_NETWORK_APP_ID не найдены в файле .env!")
    raise RuntimeError("Missing critical configuration environment variables.")

app = FastAPI(title="Pi Network Payment Gateway", version="1.0.0")

# Модель данных для входящего вебхука от Pi API
class PiPaymentCallback(BaseModel):
    action: str  # например, "complete" или "cancelled"
    paymentId: str
    txid: str | None = None

# 2. Эндпоинт для приема вебхуков (Callback URL)
@app.post("/v1/pi/callback", status_code=status.HTTP_200_OK)
async def pi_payment_callback(payload: PiPaymentCallback):
    logger.info(f"Получен вебхук от Pi Network. Действие: {payload.action}, ID платежа: {payload.paymentId}")
    
    if payload.action != "complete":
        logger.warning(f"Платеж {payload.paymentId} имеет статус: {payload.action}. Пропускаем обработку.")
        return {"status": "ignored", "reason": payload.action}
    
    # Запускаем верификацию транзакции на серверах Pi
    is_valid = await verify_pi_payment(payload.paymentId)
    
    if not is_valid:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Транзакция не прошла валидацию на стороне Pi API"
        )
    
    # ТУТ БУДЕТ ИНТЕГРАЦИЯ С DISCORD SWARM BOT
    logger.info(f"УСПЕХ: Платеж {payload.paymentId} подтвержден. Отправляем триггер в систему...")
    return {"status": "success", "payment_id": payload.paymentId}

# 3. Функция верификации платежа через официальное Pi API с экспоненциальными повторами
async def verify_pi_payment(payment_id: str) -> bool:
    url = f"https://minepi.com{payment_id}"
    headers = {"Authorization": f"Key {PI_API_KEY}"}
    
    # Механизм повторов (Retry) в случае сетевых сбоев
    async with httpx.AsyncClient() as client:
        for attempt in range(3):
            try:
                response = await client.get(url, headers=headers, timeout=10.0)
                
                if response.status_code == 200:
                    data = response.json()
                    # Проверяем финальный статус внутри Pi Network
                    if data.get("status", {}).get("completed") is True:
                        logger.info(f"Сервер Pi подтвердил транзакцию {payment_id}")
                        return True
                    else:
                        logger.error(f"Сервер Pi вернул транзакцию, но статус не 'completed': {data}")
                        return False
                
                elif response.status_code in:
                    logger.warning(f"Ошибка сервера Pi ({response.status_code}). Попытка {attempt + 1}...")
                    continue
                else:
                    logger.error(f"Ошибка Pi API: {response.status_code} - {response.text}")
                    return False
                    
            except httpx.RequestError as exc:
                logger.error(f"Сетевая ошибка при запросе к Pi API: {exc}. Попытка {attempt + 1}...")
    
    return False

# Тестовый эндпоинт проверки работоспособности (Healthcheck)
@app.get("/health")
async def health_check():
    return {"status": "alive", "pi_api_configured": bool(PI_API_KEY)}
