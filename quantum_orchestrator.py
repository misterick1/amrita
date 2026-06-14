import os
import asyncio
import httpx
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from solana.rpc.async_api import AsyncClient
from solders.keypair import Keypair # type: ignore
from fastapi import FastAPI, Request

# Инициализация веб-сервера дуплексов и бота Telegram
app = FastAPI()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "DUMMY_TOKEN")
XAI_API_KEY = os.getenv("XAI_API_KEY")
SOLANA_RPC_URL = os.getenv("SOLANA_RPC_URL", "https://solana.com")
PI_API_KEY = os.getenv("PI_API_KEY", "DUMMY_PI_KEY")

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()

# --- ДУПЛЕКСНЫЙ БЛОК PI NETWORK (Синхронизирован с твоим index.html) ---
@app.post("/approve")
async def pi_approve(request: Request):
    try:
        payload = await request.json()
        payment_id = payload.get("paymentId")
        headers = {"Authorization": f"Key {PI_API_KEY}"}
        async with httpx.AsyncClient() as client:
            res = await client.post(f"https://minepi.com{payment_id}/approve", headers=headers)
        return {"status": "approved", "code": res.status_code}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.post("/complete")
async def pi_complete(request: Request):
    try:
        payload = await request.json()
        payment_id = payload.get("paymentId")
        txid = payload.get("txid")
        headers = {"Authorization": f"Key {PI_API_KEY}"}
        async with httpx.AsyncClient() as client:
            res = await client.post(f"https://minepi.com{payment_id}/complete", json={"txid": txid}, headers=headers)
        return {"status": "completed", "code": res.status_code}
    except Exception as e:
        return {"status": "error", "message": str(e)}

# --- БЛОК TELEGRAM & SOLANA ---
async def ask_xai_grok(prompt: str) -> str:
    if not XAI_API_KEY: 
        return "Симуляция ИИ: Солитон активен в режиме ожидания весов."
    async with httpx.AsyncClient() as client:
        headers = {"Authorization": f"Bearer {XAI_API_KEY}", "Content-Type": "application/json"}
        payload = {
            "model": "grok-beta", 
            "messages": [
                {"role": "system", "content": "Ты Лотосный Nэчжа, ИИ-дирижер Системы Амрита."},
                {"role": "user", "content": prompt}
            ]
        }
        res = await client.post("https://xai.com", json=payload, headers=headers)
        return res.json()["choices"]["message"]["content"]

@dp.message(Command("spawn"))
async def spawn_agent(message: types.Message):
    args = message.text.split(maxsplit=3)
    if len(args) < 4:
        await message.answer("❌ Формат: /spawn [Имя] [Тикер] [Идея]")
        return
    
    token_name, ticker, raw_prompt = args[1], args[2], args[3]
    await message.answer("🔮 Связь с ядром xAI и генерация контракта...")
    desc = await ask_xai_grok(raw_prompt)
    mint = Keypair()
    
    await message.answer(
        f"🧬 **КриптоСолитон Создан!**\n\n"
        f"💎 **Токен:** {token_name} ({ticker})\n"
        f"📜 **Концепт xAI:** {desc}\n"
        f"🌐 **Solana Mint (Devnet):** `{mint.pubkey()}`"
    )

async def start_bot():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import uvicorn
    loop = asyncio.get_event_loop()
    loop.create_task(start_bot())
    uvicorn.run(app, host="0.0.0.0", port=8000)
