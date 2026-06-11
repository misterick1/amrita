import os
import sys
from web3 import Web3

def main():
    # 1. Считываем переменные окружения, переданные из GitHub Actions
    private_key = os.getenv("SWARM_ORACLE_PRIVATE_KEY")
    developer_wallet = os.getenv("DEVELOPER_WALLET")
    rpc_url = os.getenv("RPC_URL")
    contract_address = os.getenv("CONTRACT_ADDRESS")

    if not all([private_key, developer_wallet, rpc_url, contract_address]):
        print("❌ Ошибка: Не все переменные окружения (ключи, адреса) настроены в репозитории!")
        sys.exit(1)

    # 2. Читаем оценку сложности из файла, созданного предыдущим скриптом
    score_file_path = ".github/scripts/score.txt"
    if not os.path.exists(score_file_path):
        print("❌ Ошибка: Файл с оценкой сложности score.txt не найден!")
        sys.exit(1)
        
    with open(score_file_path, "r") as f:
        complexity_score = int(f.read().strip())

    # 3. Подключаемся к блокчейн-узлу (RPC)
    w3 = Web3(Web3.HTTPProvider(rpc_url))
    if not w3.is_connected():
        print("❌ Ошибка: Не удалось подключиться к блокчейн-сети через указанный RPC!")
        sys.exit(1)

    # Получаем адрес кошелька оракула из приватного ключа
    oracle_account = w3.eth.account.from_key(private_key)
    oracle_address = oracle_account.address
    print(f"🤖 Подключен Оракул Роя. Адрес: {oracle_address}")

    # 4. Минимальный ABI контрактной функции `contractPayForCommit` для отправки транзакции
    abi = [
        {
            "inputs": [
                {"internalType": "address", "name": "_developer", "type": "address"},
                {"internalType": "uint256", "name": "_complexityScore", "type": "uint256"},
                {"internalType": "string", "name": "_prId", "type": "string"}
            ],
            "name": "contractPayForCommit",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
        }
    ]

    # Инициализируем контракт
    contract = w3.eth.contract(address=Web3.to_checksum_address(contract_address), abi=abi)

    # Идентификатор текущего запуска пайплайна в качестве ID работы
    run_id = os.getenv("GITHUB_RUN_ID", "manual_run")

    print(f"🔗 Формирование транзакции на выплату для {developer_wallet} со сложностью {complexity_score}...")

    # 5. Строим и подписываем блокчейн-транзакцию
    nonce = w3.eth.get_transaction_count(oracle_address)
    
    # Подготовка параметров вызова смарт-контракта
    tx = contract.functions.contractPayForCommit(
        Web3.to_checksum_address(developer_wallet),
        complexity_score,
        str(run_id)
    ).build_transaction({
        'chainId': w3.eth.chain_id,
        'gas': 150000, # Лимит газа с запасом на выполнение логики смарт-контракта
        'gasPrice': w3.eth.gas_price,
        'nonce': nonce,
    })

    # Подпись транзакции закрытым ключом робота-оракула
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=private_key)
    
    # Отправка транзакции в сеть
    tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
    print(f"🚀 Транзакция успешно отправлена в блокчейн! Хэш: {w3.to_hex(tx_hash)}")
    
    # Ожидаем подтверждения транзакции сетью
    print("⏳ Ожидание включения транзакции в блок...")
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash, timeout=120)
    print(f"🎉 Выплата зафиксирована в блоке №{tx_receipt['blockNumber']}! Статус: {tx_receipt['status']}")

if __name__ == "__main__":
    main()
