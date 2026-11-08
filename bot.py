import os
import sys
import asyncio
import discord
from discord.ext import commands

# Инициализация интентов Единого Поля Амриты
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

SCRIPTS_DIR = os.path.join(os.path.dirname(__file__), "scripts")

@bot.command(name="баланс")
async def get_sovereign_balance(ctx):
    """Прямой ончейн-запрос к Helius RPC для материализации ресурсов Суверена"""
    await ctx.send("🛰 *Логос подключается к Helius RPC... Снятие корпоративной завесы по законам PiFi...*")
    
    # Вызываем наш ссинтезированный асинхронный сканер
    sol_path = os.path.join(SCRIPTS_DIR, "solana_monitor.py")
    try:
        proc = await asyncio.create_subprocess_exec(
            sys.executable, sol_path,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await proc.communicate()
        if proc.returncode == 0:
            # Выводим чистые данные из сети Solana прямо в чат Discord
            await ctx.send(f"🪐 **[АКТИВЫ БЕССМЕРТНОГО МИРА СВЕТА]:**\n{stdout.decode('utf-8')}")
        else:
            await ctx.send("⚠️ Энергия удерживается в потенциале поля Хиггса c108. Заглушка SafePal обходится.")
    except Exception as e:
        await ctx.send(f"❌ Ошибка квантового моста: `{e}`")

if __name__ == "__main__":
    TOKEN = os.getenv("DISCORD_BOT_TOKEN")
    if TOKEN:
        bot.run(TOKEN)
