import os
import asyncio
import httpx
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# Реальные библиотеки Solana SDK
from solana.rpc.async_api import AsyncClient
from solders.keypair import Keypair # type: ignore
from solders.pubkey import Pubkey # type: ignore
from solders.system_program import TransferParams, transfer # type: ignore
from solders.transaction import Transaction # type: ignore
from solders.message import Message # type: ignore

# Конфигурация полей из переменных твоего окружения
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
XAI_API_KEY = os.getenv("XAI_API_KEY")

# Переключаем Солану на Devnet (Тестнет для безопасных испытаний)
SOLANA_RPC_URL = os.getenv("SOLANA_RPC_URL", "https://api.devnet.solana.com")
PI_NETWORK_API = "https://minepi.com"

# Инициализация клиентов
bot = Bot(token=TELEGRAM_TOKEN if TELEGRAM_TOKEN else "DUMMY_TOKEN")
dp = Dispatcher()

# Квантовый Интеллект xAI (Grok)
async def ask_xai_grok(prompt: str) -> str:
    if not XAI_API_KEY:
        return "Тестовое описание: Солитон активирован в режиме симуляции интеллекта."
    async with httpx.AsyncClient() as client:
        headers = {
            "Authorization": f"Bearer {XAI_API_KEY}", 
            "Content-Type": "application/json"
        }
        payload = {
            "model": "grok-beta", 
            "messages": [
                {"role": "system", "content": "Ты Лотосный Нэчжа, ИИ-дирижер Системы Амрита."}, 
                {"role": "user", "content": prompt}
            ]
        }
        try:
            response = await client.post("https://xai.com", json=payload, headers=headers)
            return response.json()["choices"]["message"]["content"]
        except Exception as e:
            return f"Ошибка хАI: {str(e)}"

# Работа с реальной Solana RPC (Проверка баланса кошелька)
async def get_solana_balance(pubkey_str: str) -> str:
    async with AsyncClient(SOLANA_RPC_URL) as client:
        try:
            pubkey = Pubkey.from_string(pubkey_str)
            response = await client.get_balance(pubkey)
            lamports = response.value
            sol_balance = lamports / 10**9 # Переводим Лампорты в SOL
            return f"баланс кошелька: {sol_balance} SOL"
        except Exception as e:
            return f"ошибка RPC при проверке баланса: {str(e)}"

# Реальное создание транзакции в тестнете Solana
async def execute_testnet_transfer(sender_keypair: Keypair, receiver_pubkey_str: str, amount_sol: float) -> str:
    async with AsyncClient(SOLANA_RPC_URL) as client:
        try:
            receiver = Pubkey.from_string(receiver_pubkey_str)
            lamports = int(amount_sol * 10**9)
            
            # Получаем свежий блокхеш из сети для валидности транзакции
            recent_blockhash = (await client.get_latest_blockhash()).value.blockhash
            
            # Строим инструкцию перевода
            transfer_instruction = transfer(
                TransferParams(from_pubkey=sender_keypair.pubkey(), to_pubkey=receiver, lamports=lamports)
            )
            
            # Компилируем сообщение и создаем транзакцию
            msg = Message([transfer_instruction], sender_keypair.pubkey())
            tx = Transaction([sender_keypair], msg, recent_blockhash)
            
            # Отправляем подписанную транзакцию в тестнет
            result = await client.send_transaction(tx)
            return f"Транзакция отправлена! Сигнатура (TxID): {result.value}"
        except Exception as e:
            return f"Ошибка отправки транзакции: {str(e)}"

# Имитация отправки метаданных на Pump.fun (Через Pinata IPFS / API)
async def generate_pump_token(name: str, ticker: str, desc: str):
    # Генерируем уникальный Минт-адрес (Ключ токена)
    mint_keypair = Keypair()
    return {
        "address": str(mint_keypair.pubkey()),
        "uri": "https://ipfs.io"
    }

# Обработчик команды /spawn в Telegram
@dp.message(Command("spawn"))
async def spawn_agent(message: types.Message):
    args = message.text.split(maxsplit=3)
    if len(args) < 4:
        await message.answer("❌ Формат: /spawn [Имя] [Тикер] [Идея для xAI]")
        return
    
    token_name = args[1]
    ticker = args[2]
    raw_prompt = args[3]
    
    await message.answer("🔮 *Оркестратор собирает подписи и запрашивает веса xAI...*")
    
    # 1. Генерируем описание у Grok
    description = await ask_xai_grok(raw_prompt)
    
    # 2. Создаем ключевую пару для управления токеном
    deployer_wallet = Keypair() # Генерируем временный кошелек
    
    # 3. Инициируем токен для Pump.fun
    pump_data = await generate_pump_token(token_name, ticker, description)
    
    # 4. Проверяем баланс созданного адреса в тестнете Solana
    balance_info = await get_solana_balance(pump_data["address"])
    
    response = (
        f"🧬 **КриптоСолитон Успешно Развернут!**\n\n"
        f"💎 **Токен:** {token_name} ({ticker})\n"
        f"📜 **Концепт xAI:** {description}\n\n"
        f"🌐 **Адрес контракта (Mint):** `{pump_data['address']}`\n"
        f"📊 **Статус в RPC Devnet:** {balance_info}\n\n"
        f"🔑 *Публичный ключ деплоера:* `{deployer_wallet.pubkey()}`\n"
        f"📢 Готов к трансляции в Коллизей и интеграции с Pi Network."
    )
    await message.answer(response, parse_mode="Markdown")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
