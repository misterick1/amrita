import os
import json
import requests
from google.oauth2 import id_token
from google.auth.transport import requests as google_requests
from cryptography.fernet import Fernet

LOG_FILE = "history_log.json"
WALLETS_FILE = "secure_wallets_footprint.json"

class WalletCausalTracker:
    def __init__(self):
        self.master_key = os.getenv("AMRITA_MASTER_KEY")
        if not self.master_key:
            # Генерация временного ключа, если основной не задан в секретах GitHub
            self.master_key = Fernet.generate_key().decode()
        self.cipher = Fernet(self.master_key.encode())

    def verify_google_identity(self, google_id_token):
        """Полная идентификация хозяина через цифровой слепок Google OAuth2"""
        try:
            # Проверка токена через сервера Google для подтверждения личности
            client_id = os.getenv("GOOGLE_CLIENT_ID")
            id_info = id_token.verify_oauth2_token(google_id_token, google_requests.Request(), client_id)
            
            # Возвращаем уникальный цифровой слепок хозяина (sub — уникальный ID Google)
            return {
                "owner_id": id_info['sub'],
                "email": id_info['email'],
                "verified": True
            }
        except Exception as e:
            print(f"❌ Сбой каузальной идентификации: {e}")
            return {"verified": False}

    def fetch_solana_balance(self, wallet_address):
        """Мониторинг кошелька: запрашиваем баланс из Solana RPC, чтоб ни копейки не забылось"""
        rpc_url = os.getenv("SOLANA_RPC_URL", "https://solana.com")
        headers = {"Content-Type": "application/json"}
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "getBalance",
            "params": [wallet_address]
        }
        try:
            response = requests.post(rpc_url, json=payload, headers=headers)
            result = response.json()
            lamports = result['result']['value']
            return lamports / 10**9 # Переводим в SOL
        except Exception:
            return 0.0

    def secure_save_wallet(self, google_token, wallet_data):
        """Шифрование, реанимация и вечный лог кошельков под слепком хозяина"""
        identity = self.verify_google_identity(google_token)
        if not identity["verified"]:
            print("🛑 Доступ заблокирован: Личность хозяина не верифицирована!")
            return False

        # Структура слепка, чтобы найти можно было всё
        encrypted_seed_path = self.cipher.encrypt(wallet_data.get("derivation_path", "m/44'/501'/0'/0'").encode()).decode()
        encrypted_private_hint = self.cipher.encrypt(wallet_data.get("hint", "No hint").encode()).decode()

        current_balance = self.fetch_solana_balance(wallet_data["address"])

        new_wallet_entry = {
            "address": wallet_data["address"],
            "network": wallet_data.get("network", "Solana"),
            "alias": wallet_data.get("alias", "Основной хайп-узл"),
            "current_balance": current_balance,
            "secure_meta": {
                "encrypted_seed_path": encrypted_seed_path,
                "encrypted_private_hint": encrypted_private_hint
            }
        }

        # Читаем старую базу слепков
        db = {}
        if os.path.exists(WALLETS_FILE):
            with open(WALLETS_FILE, "r", encoding="utf-8") as f:
                db = json.load(f)

        user_space = db.get(identity["owner_id"], {"email": identity["email"], "wallets": []})
        
        # Обновляем или добавляем кошелек, предотвращая дубликаты
        existing = [w for w in user_space["wallets"] if w["address"] == wallet_data["address"]]
        if existing:
            existing[0]["current_balance"] = current_balance
            existing[0]["secure_meta"] = new_wallet_entry["secure_meta"]
        else:
            user_space["wallets"].append(new_wallet_entry)

        db[identity["owner_id"]] = user_space

        with open(WALLETS_FILE, "w", encoding="utf-8") as f:
            json.dump(db, f, ensure_ascii=False, indent=4)
        
        # Синхронизация с глобальным history_log.json
        self._sync_with_history_log(wallet_data["address"], current_balance)
        print(f"🔱 Слепок кошелька {wallet_data['address']} запечатан. Баланс: {current_balance} SOL.")
        return True

    def _sync_with_history_log(self, address, balance):
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, "r", encoding="utf-8") as f:
                log_data = json.load(f)
        else:
            log_data = {"logs": []}

        log_data["logs"].append({
            "event": "WALLET_MONITOR_SYNC",
            "address": address,
            "detected_balance": balance
        })

        with open(LOG_FILE, "w", encoding="utf-8") as f:
            json.dump(log_data, f, ensure_ascii=False, indent=4)

    def recover_all_wallets(self, google_id_token):
        """Реанимация и восстановление: отдает хозяину полный список его активов"""
        identity = self.verify_google_identity(google_id_token)
        if not identity["verified"]:
            return "🛑 Ошибка идентификации"

        if not os.path.exists(WALLETS_FILE):
            return "🕳 Слепки не найдены. Матрица пуста."

        with open(WALLETS_FILE, "r", encoding="utf-8") as f:
            db = json.load(f)

        user_data = db.get(identity["owner_id"])
        if not user_data:
            return "🔎 Под данным Google-аккаунтом кошельков не обнаружено."

        recovery_report = f"🔱 Хроники Реанимации для {user_data['email']}:\n"
        for w in user_data["wallets"]:
            decrypted_path = self.cipher.decrypt(w["secure_meta"]["encrypted_seed_path"].encode()).decode()
            fresh_balance = self.fetch_solana_balance(w["address"])
            recovery_report += f"\n▪️ [{w['network']}] {w['alias']}\n Адрес: {w['address']}\n Баланс: {fresh_balance} SOL\n Путь восстановления: {decrypted_path}\n"
        
        return recovery_report
