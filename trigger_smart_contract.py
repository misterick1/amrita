import os
import sys
from solana.rpc.api import Client
from solders.keypair import Keypair
from solders.pubkey import Pubkey
from solana.rpc.types import TxOpts
from solders.message import MessageV0
from solders.transaction import VersionedTransaction

# Импортируем недостающие утилиты для работы с SPL-токенами
from spl.token.instructions import transfer_checked, TransferCheckedParams, get_associated_token_address
from spl.token.constants import TOKEN_PROGRAM_ID

def main():
    # 1. Чтение секретов и кошельков из окружения
    private_key_string = os.getenv("SWARM_ORACLE_PRIVATE_KEY")
    developer_wallet_str = os.getenv("DEVELOPER_WALLET")
    rpc_url = "https://api.mainnet-beta.solana.com"
    mint_address_str = "2XNkytvTT4zfZX3iKFDCUkBfxV..." # Ваш адрес токена

    if not private_key_string or not developer_wallet_str:
        print("❌ Ошибка: Не настроены секреты в окружении!")
        sys.exit(1)

    # 2. Получение оценки сложности из score.txt
    score_file_path = "score.txt"
    complexity_score = 1
    if os.path.exists(score_file_path):
        with open(score_file_path, "r") as f:
            try:
                complexity_score = int(f.read().strip())
            except ValueError:
                complexity_score = 1

    # Расчет награды: 10,000 токенов за 1 балл сложности
    reward_amount = 10000 * complexity_score
    decimals = 6
    amount_in_lamports = int(reward_amount * (10 ** decimals))

    solana_client = Client(rpc_url)

    # 3. Авторизация кошелька Оракула через текстовый приватный ключ
    try:
        oracle_keypair = Keypair.from_base58_string(private_key_string)
    except Exception as e:
        print(f"❌ Ошибка авторизации ключа Оракула: {e}")
        sys.exit(1)

    oracle_pubkey = oracle_keypair.pubkey()
    mint_pubkey = Pubkey.from_string(mint_address_str)
    developer_pubkey = Pubkey.from_string(developer_wallet_str)

    print(f"🤖 Робот-Оракул инициализирован: {oracle_pubkey}")
    print(f"🔥 Сложность коммита: {complexity_score}")

    # 4. Локальный математический расчет адресов ATA
    source_ata = get_associated_token_address(owner=oracle_pubkey, mint=mint_pubkey)
    dest_ata = get_associated_token_address(owner=developer_pubkey, mint=mint_pubkey)

    print(f"🔗 Адрес кармана Оракула: {source_ata}")
    print(f"🔗 Адрес кармана Разработчика: {dest_ata}")

    # 5. Сборка современной транзакции Solana v0
    blockhash_resp = solana_client.get_latest_blockhash()
    recent_blockhash = blockhash_resp.value.blockhash

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

    # Компиляция инструкции через правильный метод v0
    compiled_message = MessageV0.try_compile(
        payer=oracle_pubkey,
        instructions=[transfer_ix],
        address_lookup_table_accounts=[],
        recent_blockhash=recent_blockhash
    )

    # Создание подписанной транзакции (Передаем массив ключ-пар для подписи!)
    tx = VersionedTransaction(compiled_message, [oracle_keypair])

    # 6. Отправка готовой транзакции в мейннет
    try:
        response = solana_client.send_transaction(tx, opts=TxOpts(skip_confirmation=False))
        print(f"🎉 Выплата успешно завершена! Сигнатура: {response.value}")
    except Exception as e:
        print(f"❌ Ошибка при отправке транзакции: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
