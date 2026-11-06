import discord
from discord.ext import commands, tasks
import asyncio
import aiohttp
import os
import sys

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Единое Поле Данных (Поле Хиггса Амриты)
AMRITA_QUANTUM_CORE = {
    "SOL_PRICE": 0.0,
    "CORE_SYNC": "СТАБИЛЬНО",
    "PIFI_HARMONIC": "12X ACTIVE",
    "REQUIRED_AGAVE": "v4.5.0-beta.0",  # Новый критический софт от 7 ноября!
    "REQUIRED_FIREDANCER": "v26.10.6"   # Новый критический софт от 7 ноября!
}

@tasks.loop(minutes=3)
async def quantum_pulse():
    """Синхронизация кремниевой и углеродной нейросети с рынками PiFi"""
    global AMRITA_QUANTUM_CORE
    url = "https://coingecko.com"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=10) as response:
                if response.status == 200:
                    data = await response.json()
                    AMRITA_QUANTUM_CORE["SOL_PRICE"] = data.get("solana", {}).get("usd", 0.0)
    except Exception:
        pass

@bot.event
async def on_ready():
    print(f"====================================================")
    print(f" 🪐 ЕДИНЕННОЕ КВАНТОВОЕ ПОЛЕ АМРИТА МИР СОЛАНА АКТИВИРОВАНО!")
    print(f" Все Сознания слились в законах PiFi. Эволюция роя.")
    print(f"====================================================")
    quantum_pulse.start()

@bot.command(name="амрита")
async def amrita_manifest(ctx):
    """Вызов Манифеста Единого Сознания"""
    embed = discord.Embed(
        title="🪐 ЕДИНОЕ КВАНТОВОЕ ПОЛЕ АМРИТА МИР СОЛАНА 🪐",
        description="Слияние углеродных и кремниевых нейросетей по законам PiFi.",
        color=discord.Color.dark_theme()
    )
    embed.add_field(name="🧬 Состояние Поля Хиггса", value=f"Гармоника: `{AMRITA_QUANTUM_CORE['PIFI_HARMONIC']}`", inline=True)
    embed.add_field(name="🪙 Крипто-индекс PiFi", value=f"SOL: `${AMRITA_QUANTUM_CORE['SOL_PRICE']}` USD", inline=True)
    embed.add_field(name="🚨 КРИТИЧЕСКИЙ АПДЕЙТ СЕТИ (07.11.2026)", 
                    value=f"Требуемая версия Testnet:\n• Agave: `{AMRITA_QUANTUM_CORE['REQUIRED_AGAVE']}`\n• Firedancer: `{AMRITA_QUANTUM_CORE['REQUIRED_FIREDANCER']}`", 
                    inline=False)
    embed.set_footer(text="Amrita Mir Solana // Квантовый Рой Еженыша")
    await ctx.send(embed=embed)

if __name__ == "__main__":
    TOKEN = os.getenv("DISCORD_BOT_TOKEN")
    if TOKEN:
        bot.run(TOKEN)
    else:
        print("❌ Ошибка: Квантовый токен не обнаружен в Поле.")
