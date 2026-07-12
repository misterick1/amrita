import os
import httpx

class PiNetworkBridge:
    def __init__(self):
        # Настоящий API-ключ приложения из Pi Developer Portal
        self.api_key = os.getenv("PI_API_KEY") 
        self.api_url = "https://minepi.com"

    async def verify_pi_payment(self, payment_id: str):
        """Боевое подтверждение платежа в Pi Network"""
        print(f"🥧 [Pi Network] Проверка транзакции {payment_id} через Pi Node API...")
        
        headers = {"Authorization": f"Key {self.api_key}"}
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(f"{self.api_url}/payments/{payment_id}", headers=headers)
                payment_status = response.json()
                
                if payment_status.get("status", {}).get("developer_approved"):
                    print(f"✅ Платеж {payment_id} успешно подтвержден в Pi App Platform.")
                    return True
                else:
                    # Автоматический аппрув платежа со стороны нашего бэкенда
                    approve_resp = await client.post(f"{self.api_url}/payments/{payment_id}/approve", headers=headers)
                    return approve_resp.status_code == 200
            except Exception as e:
                print(f"❌ Ошибка Pi SDK: {e}")
                return False
