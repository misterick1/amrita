import os
import sys
import json
import requests
from solana.rpc.api import Client
from solders.keypair import Keypair
from solders.pubkey import Pubkey
from spl.token.instructions import transfer_checked, TransferCheckedParams
from solana.rpc.types import TxOpts
from solana.transaction import Transaction

def main():
    private_key_string = os.getenv("SWARM_ORACLE_PRIVATE_KEY")
    developer_wallet_str = os.getenv("DEVELOPER_WALLET")
    rpc_url = "https://solana.com"
    mint_address_str = "2XNkytvTT4zfX3iKFDCUkBfxVRiUZqGunznWHZx7pump"

    if not private_key_string or not developer_wallet_str:
        print("❌ Ошибка: Не настроены секреты!")
        sys.exit(1)

    score_file_path = ".github/scripts/score.txt"
    complexity_score = 1
    if os.path.exists(score_file_path):
        with open(score_file_path, "r") as f:
            complexity_score = int(f.read().strip())

    reward_amount = 10000 * complexity_score
    decimals = 6
    amount_in_lamports = int(reward_amount * (10 ** decimals))

    solana_client = Client(rpc_url)
    
    try:
        secret_bytes = json.loads(private_key_string)
        oracle_keypair = Keypair.from_bytes(secret_bytes)
    except Exception as e:
        print(f"❌ Ошибка ключа: {e}")
        sys.exit(1)

    oracle_pubkey = oracle_keypair.pubkey()
    mint_pubkey = Pubkey.from_string(mint_address_str)
    developer_pubkey = Pubkey.from_string(developer_wallet_str)

    print(f"🦔 Оракул: {oracle_pubkey}")

    def get_ata(owner: Pubkey, mint: Pubkey):
        try:
            response = solana_client.get_token_accounts_by_owner_json_parsed(
                owner,
                opts={"mint": str(mint)}
            )
            if response.value:
                return Pubkey.from_string(response.value[0].pubkey)
            return None
        except Exception:
            return None

    source_ata = get_ata(oracle_pubkey, mint_pubkey)
    dest_ata = get_ata(developer_pubkey, mint_pubkey)

    if not source_ata or not dest_ata:
        print("❌ Ошибка: ATA аккаунты не найдены!")
        sys.exit(1)

    recent_blockhash = solana_client.get_latest_blockhash().value.blockhash
    tx = Transaction(recent_blockhash=recent_blockhash)
    
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
    tx.add(transfer_ix)

    try:
        response = solana_client.send_transaction(tx, oracle_keypair, opts=TxOpts(skip_preflight=True))
        print(f"🎉 Tx Hash: {response.value}")
    except Exception as e:
        print(f"❌ Ошибка отправки: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
