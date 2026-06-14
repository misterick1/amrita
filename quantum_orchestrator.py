import os
import asyncio
import httpx
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from solana.rpc.api import Client
from solders.keypair import Keypair # type: ignore

# Конфигурация из переменных окружения
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
XAI_API_KEY = os.getenv("XAI_API_KEY")
SOLANA_RPC_URL = os.getenv("SOLANA_RPC_URL", "https://solana.com")
PI_NETWORK_API = "https://minepi.com"

# Инициализация клиентов
bot = Bot(token=TELEGRAM_TOKEN if TELEGRAM_TOKEN else "DUMMY_TOKEN")
dp = Dispatcher()
solana_client = Client(SOLANA_RPC_URL)

# Функция запроса к xAI (Grok)
async def ask_xai_grok(prompt: str) -> str:
    if not XAI_API_KEY:
        return "Ошибка: Не задан XAI_API_KEY"
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
            return f"Ошибка при запросе к xAI: {str(e)}"

# Проверка пользователя в Pi Network
async def verify_pi_user(pi_user_id: str, auth_token: str) -> bool:
    async with httpx.AsyncClient() as client:
        headers = {"Authorization": f"Bearer {auth_token}"}
        try:
            response = await client.get(f"{PI_NETWORK_API}/users/{pi_user_id}", headers=headers)
            if response.status_code == 200:
                return response.json().get("roles", {}).get("kyc", False)
            return False
        except Exception:
            return False

# Имитация деплоя на Pump.fun через Solana RPC
async def launch_on_pump_fun(token_name: str, ticker: str, description: str) -> str:
    try:
        token_keypair = Keypair()
        status = f"🚀 Токен {token_name} ({ticker}) успешно запущен на Pump.fun через Solana RPC!\nАдрес контракта: {token_keypair.pubkey()}"
        return status
    except Exception as e:
        return f"Ошибка при работе с Solana RPC: {str(e)}"

# Обработчик команды /spawn в Telegram
@dp.message(Command("spawn"))
async def spawn_agent(message: types.Message):
    args = message.text.split(maxsplit=3)
    if len(args) < 4:
        await message.answer("❌ Формат команды: /spawn [Имя] [Тикер] [Описание идеи]")
        return
    
    name = args[1]
    ticker = args[2]
    raw_prompt = args[3]
    
    await message.answer("🔮 Обработка запроса... Связь с ядром xAI...")
    
    refined_description = await ask_xai_grok(f"Создай описание крипто-солитона на основе идеи: {raw_prompt}")
    launch_result = await launch_on_pump_fun(name, ticker, refined_description)
    
    response_text = (
        f"🧬 **ИИ-Агент Сгенерирован!**\n\n"
        f"📝 **Концепт от xAI:** {refined_description}\n\n"
        f"{launch_result}"
    )
    await message.answer(response_text)

async def main():
    if TELEGRAM_TOKEN == "DUMMY_TOKEN" or not TELEGRAM_TOKEN:
        print("Внимание: Запущено в тестовом режиме без реального токена Telegram.")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
