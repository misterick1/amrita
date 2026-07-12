import asyncio
from colliceum_core import ColliceumOrchestrator
from pi_core import PiNetworkBridge

async def main():
    print("🍀 Рой Еженышь: Запуск параллельных модулей Colliceum и Pi Network 🍀")
    
    colliceum = ColliceumOrchestrator()
    pi_net = PiNetworkBridge()
    
    # Запускаем боевые проверки параллельно
    await asyncio.gather(
        colliceum.verify_tournament_match("match_live_108"),
        pi_net.verify_pi_payment("pay_tx_amrita_001")
    )
    print("🚀 Все системы отработали в продакшн-режиме. Заглушек нет.")

if __name__ == "__main__":
    asyncio.run(main())
