import requests
import json

class JupiterPredictBridge:
    def __init__(self, rpc_url="https://solana.com"):
        self.rpc_url = rpc_url
        self.quote_api_url = "https://jup.ag"

    def fetch_jupiter_quote(self, input_mint: str, output_mint: str, amount_lamports: int) -> dict:
        """Получает точную котировку свопа от Jupiter API v6"""
        params = {
            "inputMint": input_mint,
            "outputMint": output_mint,
            "amount": str(amount_lamports),
            "slippageBps": 50 # 0.5% проскальзывание
        }
        try:
            response = requests.get(self.quote_api_url, params=params, timeout=10)
            if response.status_code == 200:
                return response.json()
            return {"error": f"API returned status {response.status_code}"}
        except Exception as e:
            return {"error": str(e)}

    def analyze_and_route(self, prediction_score: float, quote_data: dict):
        """Принимает решение о проведении сделки на основе скоринга нейросети"""
        if "error" in quote_data or not quote_data.get("outAmount"):
            print("[-] Невозможно рассчитать маршрут: некорректные данные котировки.")
            return False
            
        out_amount = int(quote_data["outAmount"])
        
        # Если ИИ-модель выдает высокую уверенность (> 0.85), одобряем сделку
        if prediction_score > 0.85:
            print(f"[+] ИИ Подтвердил сделку (Score: {prediction_score:.2f}). Ожидаемый выход: {out_amount} lamports.")
            return True
        else:
            print(f"[-] Сделка отклонена ИИ-агентом. Недостаточный уровень уверенности тренда: {prediction_score:.2f}")
            return False

jupiter_bridge = JupiterPredictBridge()
