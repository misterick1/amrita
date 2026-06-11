import os
import sys
from solana.rpc.api import Client
from solders.keypair import Keypair
from solders.pubkey import Pubkey
from spl.token.instructions import transfer_checked, TransferCheckedParams, get_associated_token_address
from solana.rpc.types import TxOpts
from solders.message import MessageV0
from solders.transaction import VersionedTransaction

def main():
    private_key_string = os.getenv("SWARM_ORACLE_PRIVATE_KEY")
    developer_wallet_str = os.getenv("DEVELOPER_WALLET")
    
    # Меняем публичный RPC на стабильный и быстрый узел
    rpc_url = "https://api.mainnet-beta.solana.com" 
    mint_address_str = "2XNkytvTT4zfX3iKFDCUkBfxVRiUZqGunznWHZx7pump"

    if not private_key_string or not developer_wallet_str:
        print("❌ Ошибка: Не настроены секреты!")
        sys.exit(1)

    score_file_path = "score.txt"
    complexity_score = 1
    if os.path.exists(score_file_path):
        with open(score_file_path, "r") as f:
            complexity_score = int(f.read().strip())

    reward_amount = 10000 * complexity_score
    decimals = 6
    amount_in_lamports = int(reward_amount * (10 ** decimals))

    solana_client = Client(rpc_url)
    
    try:
        oracle_keypair = Keypair.from_base58_string(private_key_string.strip())
    except Exception as e:
        print(f"❌ Ошибка ключа: {e}")
        sys.exit(1)

    oracle_pubkey = oracle_keypair.pubkey()
    mint_pubkey = Pubkey.from_string(mint_address_str)
    developer_pubkey = Pubkey.from_string(developer_wallet_str)

    print(f"🦔 Оракул: {oracle_pubkey}")
    print(f"🔥 Сложность: {complexity_score}. Выплата: {reward_amount} AMRITA")

    # 🛠️ ЖЕЛЕЗНЫЙ РАСЧЕТ: Вычисляем ATA адреса локально по формуле Solana, обходя лаги RPC
    source_ata = get_associated_token_address(oracle_pubkey, mint_pubkey)
    dest_ata = get_associated_token_address(developer_pubkey, mint_pubkey)

    print(f"🔗 Адрес кармана Оракула: {source_ata}")
    print(f"🔗 Адрес кармана Разработчика: {dest_ata}")

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
    
    compiled_message = MessageV0.compile_with_legacy_instructions(
        payer=oracle_pubkey,
        instructions=[transfer_ix],
        recent_blockhash=recent_blockhash
    )
    
    tx = VersionedTransaction(compiled_message, [oracle_keypair])

    try:
        response = solana_client.send_transaction(tx, opts=TxOpts(skip_preflight=True))
        print(f"🎉 Выплата успешно отправлена в мейннет! Tx Hash: {response.value}")
    except Exception as e:
        print(f"❌ Ошибка отправки транзакции: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
