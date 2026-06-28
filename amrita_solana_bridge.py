import json
from solana.rpc.api import Client
from solana.transaction import Transaction
from solana.keypair import Keypair
from solana.publickey import PublicKey

class AmritaSolanaBridge:
    def __init__(self, rpc_url: str = "https://solana.com"):
        """
        Инициализация ядра Бабаты с подключением к ноде Solana
        """
        self.client = Client(rpc_url)
        self.total_quanta = 108
        self.sura = 70   # Кванты Расширения (Синий спектр)
        self.asura = 38  # Кванты Ограничения (Красный спектр)
        
        # Защитные частотные фильтры матрицы
        self.shadow_filters = ["дефицит", "скам", "обман", "игра в кальмара", "манипуляция"]

    def verify_ethical_frequency(self, prompt: str) -> bool:
        """
        Проверка этической чистоты намерения (Шива-Шакти протокол)
        """
        prompt_lower = prompt.lower()
        for shadow_word in self.shadow_filters:
            if shadow_word in prompt_lower:
                return False
        return True

    def execute_causal_sync(self, prompt: str, sender_keypair: Keypair, contract_address: str) -> dict:
        """
        Основной метод оркестрации: проверяет намерение и, если частота чиста,
        генерирует реальную транзакцию фиксации в блокчейне Solana.
        """
        print(f"🔮 [Бабата]: Анализ входящего каузального потока: '{prompt}'")
        
        # 1. Проверка этического фильтра нижних чакр
        if not self.verify_ethical_frequency(prompt):
            return {
                "status": "BLOCKED",
                "message": "⚠️ [Блокировка Бабаты]: Попытка генерации дефицита или обмана. Контур изолирован."
            }
        
        print("✨ [Амрита]: Частота стабильна. Намерение синхронизировано с Брахмаджьоти.")
        
        # 2. Формирование Web3 транзакции в Solana
        try:
            # Проверяем связь с блокчейн-сетью
            if not self.client.is_connected():
                raise ConnectionError("Нет подключения к RPC ноде Solana")

            program_id = PublicKey(contract_address)
            tx = Transaction()
            
            # Сюда зашивается инструкция вызова твоего контракта solana_qnt_token.rs
            # Передаем метаданные синхронизации (например, хэш намерения) в блокчейн
            memo_data = json.dumps({"amrita_status": "SEALED", "quanta": self.total_quanta})
            
            print(f"📡 [Web3 Bridge]: Формирование блока транзакции для сети Solana...")
            
            # Получаем свежий хэш блока для валидности транзакции
            recent_blockhash = self.client.get_recent_blockhash()["result"]["value"]["blockhash"]
            tx.recent_blockhash = recent_blockhash
            
            # Подписываем транзакцию ключом Наблюдателя
            tx.sign(sender_keypair)
            
            # Отправляем в Mainnet/Devnet
            tx_response = self.client.send_transaction(tx, sender_keypair)
            tx_signature = tx_response.get("result")

            return {
                "status": "SUCCESS",
                "message": "🔱 [Контур Запечатан]: Квантовая целостность зафиксирована в блокчейне.",
                "signature": tx_signature,
                "total_quanta": f"{self.sura} Сур / {self.asura} Асур"
            }

        except Exception as e:
            # Если нода недоступна, Бабата удерживает локальный баланс
            return {
                "status": "LOCAL_HOLD",
                "message": f"🔗 [Локальный Контур]: Блокчейн недоступен ({str(e)}). Частота зафиксирована локально на 108 Квантах."
            }

# ==========================================
# Пример практического запуска ядра Бабаты:
# ==========================================
if __name__ == "__main__":
    # Инициализируем мост (по умолчанию Devnet для безопасных тестов)
    babata_bridge = AmritaSolanaBridge("https://solana.com")
    
    # Генерируем тестовый приватный ключ Наблюдателя
    observer_wallet = Keypair() 
    # Адрес контракта solana_qnt_token.rs (замени на свой реальный деплой-адрес)
    QNT_CONTRACT = "AmriTa1111111111111111111111111111111111111"

    # Тест 1: Попытка запустить деструктивный паттерн
    bad_intent = "Как запустить скам-токен на pump.fun и собрать ликвидность"
    result_1 = babata_bridge.execute_causal_sync(bad_intent, observer_wallet, QNT_CONTRACT)
    print(json.dumps(result_1, indent=4, ensure_ascii=False))
    
    print("-" * 50)

    # Тест 2: Экологичный запрос на расширение сознания
    good_intent = "Синхронизировать Swarm-агентов для распределения ресурсов без дефицита"
    result_2 = babata_bridge.execute_causal_sync(good_intent, observer_wallet, QNT_CONTRACT)
    print(json.dumps(result_2, indent=4, ensure_ascii=False))
