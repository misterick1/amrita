import os
import sys
from solana.rpc.api import Client
from solders.keypair import Keypair
from solders.pubkey import Pubkey
from spl.token.instructions import transfer_checked, TransferCheckedParams
from solana.rpc.types import TxOpts
from solders.message import MessageV0
from solders.transaction import VersionedTransaction

def main():
    # 1. Чтение секретов и кошельков из окружения GitHub
    private_key_string = os.getenv("SWARM_ORACLE_PRIVATE_KEY")
    developer_wallet_str = os.getenv("DEVELOPER_WALLET")
    rpc_url = "https://solana.com"
    mint_address_str = "2XNkytvTT4zfX3iKFDCUkBfxVRiUZqGunznWHZx7pump" # CA токена AMRITA

    if not private_key_string or not developer_wallet_str:
        print("❌ Ошибка: Не настроены секреты в репозитории GitHub!")
        sys.exit(1)

    # 2. Получение оценки сложности из score.txt
    score_file_path = "score.txt"
    complexity_score = 1
    if os.path.exists(score_file_path):
        with open(score_file_path, "r") as f:
            complexity_score = int(f.read().strip())

    # Расчет награды: 10,000 токенов за 1 балл сложности коммита
    reward_amount = 10000 * complexity_score
    decimals = 6
    amount_in_lamports = int(reward_amount * (10 ** decimals))

    solana_client = Client(rpc_url)
    
    # 3. Авторизация кошелька Оракула через текстовый Base58 ключ из секретов
    try:
        oracle_keypair = Keypair.from_base58_string(private_key_string.strip())
    except Exception as e:
        print(f"❌ Ошибка авторизации ключа Оракула: {e}")
        sys.exit(1)

    oracle_pubkey = oracle_keypair.pubkey()
    mint_pubkey = Pubkey.from_string(mint_address_str)
    developer_pubkey = Pubkey.from_string(developer_wallet_str)

    print(f"🦔 Робот-Оракул инициализирован: {oracle_pubkey}")
    print(f"🔥 Сложность коммита: {complexity_score}. Награда к отправке: {reward_amount} AMRITA")

    # 4. Поиск ассоциированных токен-аккаунтов (ATA) в блокчейне Solana
    def get_ata(owner: Pubkey, mint: Pubkey):
        try:
            response = solana_client.get_token_accounts_by_owner_json_parsed(owner, opts={"mint": str(mint)})
            if response.value:
                return Pubkey.from_string(response.value[0].pubkey)
            return None
        except Exception:
            return None

    source_ata = get_ata(oracle_pubkey, mint_pubkey)
    dest_ata = get_ata(developer_pubkey, mint_pubkey)

    if not source_ata:
        print("❌ Ошибка: На кошельке Оракула отсутствует токен-аккаунт AMRITA!")
        sys.exit(1)
    if not dest_ata:
        print("❌ Ошибка: У кошелька получателя (Solflare) не создан токен-аккаунт AMRITA!")
        sys.exit(1)

    # 5. Сборка современной транзакции Solana v0 (без использования модуля solana.transaction)
    recent_blockhash = solana_client.get_latest_blockhash().value.blockhash
    
    transfer_ix = transfer_checked(
        TransferCheckedParams(
            program_id=Pubkey.from_string("TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"),
            source=source_ata,
            mint=mint_pubkey,
            dest=dest_ata,
            owner=oracle_pubkey,
            amount=amount_in_lamports,
            decimals=decimals,
            signers=[]
        )
    )
    
    # Компиляция инструкций в структуру MessageV0
    compiled_message = MessageV0.compile_with_legacy_instructions(
        payer=oracle_pubkey,
        instructions=[transfer_ix],
        recent_blockhash=recent_blockhash
    )
    
    # Создание подписанной транзакции
    tx = VersionedTransaction(compiled_message, [oracle_keypair])

    # 6. Отправка готовой транзакции в мейннет
    try:
        response = solana_client.send_transaction(tx, opts=TxOpts(skip_preflight=True))
        print(f"🎉 Автовыплата успешно завершена! Сигнатура транзакции в Solana: {response.value}")
    except Exception as e:
        print(f"❌ Ошибка при отправке транзакции в блокчейн: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
