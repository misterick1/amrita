import os
import json

class AgenticStablePay:
    def __init__(self):
        self.log_file = "history_log.json"
        self.secure_asset = "USDC/USDT"

    def authorize_agent_payment(self, raw_ocr_text, amount_usd):
        """Протокол безопасных агентских платежей в обход Visa-карт"""
        if "trump" in raw_ocr_text.lower():
            print("🛑 SHIELD BLOCK: Обнаружен опасный мемкоин Трампа. Транзакция заблокирована во избежание убытков.")
            return False
            
        print(f"💳 AGENTIC PAY: ИИ-Агент успешно авторизовал платеж на ${amount_usd} через стейблкоины {self.secure_asset}.")
        self._log_stable_move(amount_usd)
        return True

    def _log_stable_move(self, amount):
        if os.path.exists(self.log_file):
            try:
                with open(self.log_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
            except Exception:
                data = {"logs": []}
        else:
            data = {"logs": []}

        data["logs"].append({
            "event": "AGENTIC_STABLE_PAYMENT",
            "volume_usd": amount,
            "security_layer": "VISA_BYPASS_ACTIVE"
        })

        with open(self.log_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    pay_system = AgenticStablePay()
    pay_system.authorize_agent_payment("Agentic payments via stablecoins", 50.0)
