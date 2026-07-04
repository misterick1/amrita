import os
import json
import requests

class MultiAssetScanner:
    def __init__(self):
        self.rpc_solana = os.getenv("SOLANA_RPC_URL", "https://solana.com")
        self.log_file = "history_log.json"

    def scan_custom_token(self, wallet_address, token_mint_address):
        """Сканирование SPL-токенов хозяина (будь то elchef, bStocks или ликвидность DeFi)"""
        headers = {"Content-Type": "application/json"}
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "getTokenAccountsByOwner",
            "params": [
                wallet_address,
                {"mint": token_mint_address},
                {"encoding": "jsonParsed"}
            ]
        }
        try:
            response = requests.post(self.rpc_solana, json=payload, headers=headers)
            res_data = response.json()
            accounts = res_data.get('result', {}).get('value', [])
            if accounts:
                amount = accounts[0]['account']['data']['parsed']['info']['tokenAmount']['uiAmount']
                return float(amount)
            return 0.0
        except Exception as e:
            print(f"⚠️ Ошибка сканирования токена {token_mint_address}: {e}")
            return 0.0

    def log_defi_pulse(self, market_name, deposit_volume):
        """Фиксация глобальных DeFi аномалий (типа $100M на Monad/Aave) для ИИ-анализа"""
        print(f"📊 DeFi Трекер: Рыночный импульс [{market_name}] достиг ${deposit_volume}M")
        if os.path.exists(self.log_file):
            with open(self.log_file, "r", encoding="utf-8") as f:
                log = json.load(f)
            log["logs"].append({"event": "DEFI_MACRO_PULSE", "market": market_name, "volume": f"${deposit_volume}M"})
            with open(self.log_file, "w", encoding="utf-8") as f:
                json.dump(log, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    scanner = MultiAssetScanner()
    # Фиксируем взрывной рост Monad из уведомления на скриншоте
    scanner.log_defi_pulse("Aave Monad Market", 100)
