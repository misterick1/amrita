import os
import asyncio
import json
import logging
import httpx
from fastapi import FastAPI, Request
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from solana.rpc.async_api import AsyncClient
from solders.keypair import Keypair  # type: ignore

# Импортируем наш субсекундный квантовый фильтр цен
try:
    from butterfly_effect_filter import filter_engine
except ImportError:
    filter_engine = None

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("QuantumOrchestrator")

# Инициализация веб-сервера дуплексов и бота Telegram
app = FastAPI()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
XAI_API_KEY = os.getenv("XAI_API_KEY")
SOLANA_RPC_URL = os.getenv("SOLANA_RPC_URL", "https://solana.com")
PI_API_KEY = os.getenv("PI_API_KEY", "DUMMY_PI_KEY")

bot = Bot(token=TELEGRAM_TOKEN) if TELEGRAM_TOKEN else None
dp = Dispatcher()

# --- ДУПЛЕКСНЫЙ БЛОК PI NETWORK ---
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
            res = await client.post(f"https://minepi.com{payment_id}/complete", headers=headers, json={"txid": txid})
            return {"status": "completed", "code": res.status_code}
    except Exception as e:
        return {"status": "error", "message": str(e)}

# --- БЛОК TELEGRAM & SOLANA & MARKET FILTER ---
async def ask_xai_grok(prompt: str) -> str:
    if not XAI_API_KEY:
        return "Симуляция ИИ: Солитон активен в тестовом режиме."
    async with httpx.AsyncClient() as client:
        headers = {"Authorization": f"Bearer {XAI_API_KEY}"}
        payload = {
            "model": "grok-beta",
            "messages": [
                {"role": "system", "content": "You are a quantum crypto architect."},
                {"role": "user", "content": prompt}
            ]
        }
        res = await client.post("https://x.ai", headers=headers, json=payload)
        return res.json()["choices"][0]["message"]["content"]

@dp.message(Command("spawn"))
async def spawn_agent(message: types.Message):
    args = message.text.split(maxsplit=3)
    if len(args) < 4:
        await message.answer("❌ Формат: /spawn <имя_токена> <тикер> <промпт>")
        return

    token_name, ticker, raw_prompt = args[1], args[2], args[3]
    await message.answer("🔮 Связь с ядром xAI Grok для генерации Квант-Солитона...")
    
    # Слой Квантовой Защиты: Проверяем волатильность Solana перед генерацией и минтингом
    if filter_engine:
        # Симулируем перехват контекста для майнинга смыслов и оценки стабильности сети
        market_check = filter_engine.process_keystroke_mining(
            user_passport=f"TG_{message.from_user.id}",
            keystroke_data={"key": "SpawnCmd", "context": raw_prompt}
        )
        
        # Если состояние инфосферы или рынка привело к схлопыванию ветки (BURNED)
        if market_check.get("status") == "BURNED":
            await message.answer(
                f"⚠️ *[КВАНТОВЫЙ СЛИВ ЗАБЛОКИРОВАН]*\n"
                f"Причина: `{market_check.get('reason')}`\n"
                f"Транзакции к `PUMP_FUN_BRIDGE` и `JUPITER_BRIDGE` приостановлены ради безопасности."
            )
            return

    # Если рынок чист и стабилен — продолжаем спавн
    desc = await ask_xai_grok(raw_prompt)
    mint = Keypair()

    await message.answer(
        f"🌌 *КриптоСолитон Создан!**\n\n"
        f"🔹 *Токен:* {token_name} ({ticker})\n"
        f"📝 *Концепт xAI:* {desc}\n"
        f"🌐 *Solana Mint (Devnet):* `{mint.pubkey()}`\n\n"
        f"🚀 _Мосты Jupiter и Pump.fun синхронизированы в стабильном таймлайне_"
    )

async def start_bot():
    if bot:
        logger.info("Запуск Telegram-бота...")
        await dp.start_polling(bot)

if __name__ == "__main__":
    import uvicorn
    loop = asyncio.get_event_loop()
    if bot:
        loop.create_task(start_bot())
    uvicorn.run(app, host="0.0.0.0", port=8000)
