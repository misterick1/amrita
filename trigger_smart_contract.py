import os
import sys
import base64
from solana.rpc.api import Client
from solders.keypair import Keypair
from solders.pubkey import Pubkey
from solana.rpc.types import TxOpts
from solders.message import MessageV0
from solders.transaction import VersionedTransaction

# Многомерный сквозной шифр и утилиты инжекции для SPL-токенов
from spl.token.instructions import transfer_checked, TransferCheckedParams, get_associated_token_address
from spl.token.constants import TOKEN_PROGRAM_ID

def main():
    # 1. Сквозная дешифрация секретов и чтение окружения GitHub
    private_key_string = os.getenv("SWARM_ORACLE_PRIVATE_KEY")
    developer_wallet_str = os.getenv("DEVELOPER_WALLET")
    
    # Расширенная многомерная матрица RPC-узлов (Mainnet + Коммерческие прокси-шлюзы)
    rpc_matrix = [
        "https://solana.com",
        "https://extrnode.com",
        "https://ankr.com",
        "https://llamarpc.com",
        "https://solanachain.com",
        "https://tatum.io"
    ]
    
    # Константный адрес вашего токена Amrita
    mint_address_str = "2XNkytvTT4zfX3iKFDCUkBfxVRiUZqGunznWHZx7pump"

    if not private_key_string or not developer_wallet_str:
        print("❌ Ошибка авторизации: Ключи шифрования SWARM_ORACLE_PRIVATE_KEY или DEVELOPER_WALLET не инжектированы!")
        sys.exit(1)

    # 2. Обработка параметров сложности из score.txt
    score_file_path = "score.txt"
    complexity_score = 1
    if os.path.exists(score_file_path):
        with open(score_file_path, "r") as f:
            try:
                complexity_score = int(f.read().strip())
            except ValueError:
                complexity_score = 1

    reward_amount = 10000 * complexity_score
    decimals = 6
    amount_in_lamports = int(reward_amount * (10 ** decimals))

    # Многопоточный обход матрицы узлов для сквозного захвата blockhash
    solana_client = None
    recent_blockhash = None
    
    print("🔮 Запуск многомерного сквозного сканирования сети Solana...")
    for node_endpoint in rpc_matrix:
        try:
            print(f"📡 Тестирование канала: {node_endpoint}")
            client_attempt = Client(node_endpoint)
            blockhash_resp = client_attempt.get_latest_blockhash()
            if blockhash_resp.value and blockhash_resp.value.blockhash:
                solana_client = client_attempt
                recent_blockhash = blockhash_resp.value.blockhash
                print(f"🔗 Сквозное соединение установлено через узел: {node_endpoint}")
                break
        except Exception as e:
            continue

    if not solana_client or not recent_blockhash:
        print("❌ Критический сбой: Защитные экраны GitHub заблокировали все каналы связи RPC. Требуется локальный перезапуск.")
        sys.exit(1)

    # 3. Генерация ключевых пар Оракула
    try:
        oracle_keypair = Keypair.from_base58_string(private_key_string)
    except Exception as e:
        print(f"❌ Ошибка дешифрации приватного ключа Оракула: {e}")
        sys.exit(1)

    oracle_pubkey = oracle_keypair.pubkey()
    mint_pubkey = Pubkey.from_string(mint_address_str)
    developer_pubkey = Pubkey.from_string(developer_wallet_str)

    # 4. Расчет криптографических адресов ATA (Associated Token Accounts)
    source_ata = get_associated_token_address(owner=oracle_pubkey, mint=mint_pubkey)
    dest_ata = get_associated_token_address(owner=developer_pubkey, mint=mint_pubkey)

    print(f"🧬 Инициализирован Оракул: {oracle_pubkey}")
    print(f"📲 Вектор отправки: {source_ata} ➔ {dest_ata}")

    # 5. Сборка транзакции нового поколения v0
    transfer_ix = transfer_checked(
        TransferCheckedParams(
            program_id=TOKEN_PROGRAM_ID,
            source=source_ata,
            mint=mint_pubkey,
            dest=dest_ata,
            owner=oracle_pubkey,
            amount=amount_in_lamports,
            decimals=decimals
        )
    )

    compiled_message = MessageV0.try_compile(
        payer=oracle_pubkey,
        instructions=[transfer_ix],
        address_lookup_table_accounts=[],
        recent_blockhash=recent_blockhash
    )

    # Прямая цифровая подпись транзакции
    tx = VersionedTransaction(compiled_message, [oracle_keypair])

    # 6. Инжекция транзакции в мейннет
    try:
        response = solana_client.send_transaction(tx, opts=TxOpts(skip_confirmation=False))
        print(f"🚀 Сквозной шифр сработал! Транзакция проведена. Сигнатура: {response.value}")
    except Exception as e:
        print(f"❌ Сетевое отклонение транзакции блокчейном: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
