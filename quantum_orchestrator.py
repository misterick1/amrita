import os
import asyncio
import httpx
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from solana.rpc.async_api import AsyncClient
from solders.keypair import Keypair # type: ignore
from solders.pubkey import Pubkey # type: ignore
from fastapi import FastAPI, Request

# Инициализация веб-сервера для Pi Network и бота Telegram
app = FastAPI()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "DUMMY_TOKEN")
XAI_API_KEY = os.getenv("XAI_API_KEY")
SOLANA_RPC_URL = os.getenv("SOLANA_RPC_URL", "https://solana.com")
PI_API_KEY = os.getenv("PI_API_KEY", "DUMMY_PI_KEY")

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()

# --- БЛОК PI NETWORK (Для фиолетового 10-го шага) ---
@app.post("/payment/complete")
async def pi_payment_webhook(request: Request):
    try:
        payload = await request.json()
        payment_id = payload.get("paymentId")
        txid = payload.get("txid")
        
        headers = {"Authorization": f"Key {PI_API_KEY}"}
        async with httpx.AsyncClient() as client:
            # 1. Сервер одобряет транзакцию в блокчейне Pi
            await client.post(f"https://minepi.com{payment_id}/approve", headers=headers)
            # 2. Сервер подтверждает закрытие платежа
            response = await client.post(f"https://minepi.com{payment_id}/complete", json={"txid": txid}, headers=headers)
            
        return {"status": "verified", "pi_status": response.status_code}
    except Exception as e:
        return {"status": "error", "message": str(e)}

# --- БЛОК TELEGRAM & SOLANA ---
async def ask_xai_grok(prompt: str) -> str:
    if not XAI_API_KEY: return "Симуляция ИИ: Солитон активен."
    async with httpx.AsyncClient() as client:
        headers = {"Authorization": f"Bearer {XAI_API_KEY}", "Content-Type": "application/json"}
        payload = {"model": "grok-beta", "messages": [{"role": "user", "content": prompt}]}
        res = await client.post("https://xai.com", json=payload, headers=headers)
        return res.json()["choices"][0]["message"]["content"]

@dp.message(Command("spawn"))
async def spawn_agent(message: types.Message):
    args = message.text.split(maxsplit=3)
    if len(args) < 4:
        await message.answer("❌ Формат: /spawn [Имя] [Тикер] [Идея]")
        return
    
    await message.answer("🔮 Связь с ядром xAI и генерация контракта...")
    desc = await ask_xai_grok(args[3])
    mint = Keypair()
    
    await message.answer(
        f"🧬 **КриптоСолитон Создан!**\n\n"
        f"💎 **Токен:** {args[1]} ({args[2]})\n"
        f"📜 **Концепт:** {desc}\n"
        f"🌐 **Solana Mint:** `{mint.pubkey()}`"
    )

# Функция запуска
async def start_bot():
    await dp.start_polling(bot)

if __name__ == "__main__":
    # Локальный запуск или запуск на VPS
    import uvicorn
    loop = asyncio.get_event_loop()
    loop.create_task(start_bot())
    uvicorn.run(app, host="0.0.0.0", port=8000)
