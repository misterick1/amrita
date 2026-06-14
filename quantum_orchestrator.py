import httpx
from fastapi import FastAPI, Request

app = FastAPI()
PI_API_URL = "https://minepi.com"
PI_API_KEY = "ТВОЙ_КЛЮЧ_РАЗРАБОТЧИКА_ИЗ_КОНСОЛИ_ПИ" # Забери его под треугольником

# Ловим сигнал оплаты от Pi Browser
@app.post("/payment/complete")
async def complete_payment(request: Request):
    data = await request.json()
    payment_id = data.get("paymentId")
    txid = data.get("txid")
    
    # Дуплекс: отправляем подтверждение обратно в блокчейн Pi
    headers = {"Authorization": f"Key {PI_API_KEY}"}
    async with httpx.AsyncClient() as client:
        # Одобряем транзакцию на сервере
        await client.post(f"{PI_API_URL}/payments/{payment_id}/approve", headers=headers)
        # Завершаем трансляцию
        response = await client.post(f"{PI_API_URL}/payments/{payment_id}/complete", json={"txid": txid}, headers=headers)
        
    return {"status": "success", "pi_response": response.json()}
