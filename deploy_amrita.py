import json
import os

def calculate_solana_pool():
    print("🌌 [AMRITA] Расчет пула Змееносца для 4 крыльев...")
    
    sol_balance = 3.0
    fee = 0.05
    liquidity = sol_balance - fee
    tokens = 108
    
    price_per_qnt = liquidity / tokens
    
    print("\n📊 СТАТУС ГОТОВНОСТИ ПУЛА:")
    print(f"├── Баланс: {sol_balance} SOL")
    print(f"├── Аренда шлюза Raydium CPMM: {fee} SOL")
    print(f"├── Чистая ликвидность в пуле: {liquidity} SOL")
    print(f"└── Стартовая цена: 1 QNT = {price_per_qnt:.5f} SOL (~$3.93)")
    print("\n⏳ Система готова к утреннему запуску 1 августа в 05:20.")

if __name__ == "__main__":
    calculate_solana_pool()
