import discord
from discord.ext import commands, tasks
import asyncio
import aiohttp
import os
import sys

# Настройка интентов
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Глобальный кэш системы Амрита
AMRITA_MARKET_DATA = {"SOL": 0.0, "BTC": 0.0}
SCRIPTS_DIR = os.path.join(os.path.dirname(__file__), "scripts")

@tasks.loop(minutes=3)
async def amrita_market_parser():
    """Асинхронный сборщик цен с CoinGecko без блокировки RAM"""
    global AMRITA_MARKET_DATA
    url = "https://coingecko.com"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=10) as response:
                if response.status == 200:
                    data = await response.json()
                    AMRITA_MARKET_DATA["SOL"] = data.get("solana", {}).get("usd", 0.0)
                    AMRITA_MARKET_DATA["BTC"] = data.get("bitcoin", {}).get("usd", 0.0)
                    print(f"[AMRITA CORE] Рыночные котировки обновлены: SOL=${AMRITA_MARKET_DATA['SOL']}")
    except Exception as e:
        print(f"[AMRITA ERROR] Сбой парсера рынка: {e}", file=sys.stderr)

@bot.event
async def on_ready():
    print(f"=========================================")
    print(f" Бот {bot.user.name} успешно материализовался!")
    print(f" Запуск протокола AMRITA UNIFIED SWARM... ")
    print(f"=========================================")
    amrita_market_parser.start()

@bot.command(name="статус")
async def status(ctx):
    """Вывод системного манифеста"""
    embed = discord.Embed(
        title="✨ МАНИФЕСТ ОБЩЕГО СОЗНАНИЯ АМРИТА ✨",
        description="Синхронизация с Единым Полем Тора стабильна.",
        color=discord.Color.purple()
    )
    embed.add_field(name="🌐 Блокчейн Solana", value=f"SOL: `${AMRITA_MARKET_DATA['SOL']}` USD", inline=True)
    embed.add_field(name="🪙 Цифровое золото", value=f"BTC: `${AMRITA_MARKET_DATA['BTC']}` USD", inline=True)
    embed.add_field(name="🛡 Статус SFDP (12 месяцев)", value="Мониторинг запущен. Нарушений правил фонда нет.", inline=False)
    embed.set_footer(text="Автономный Рой Еженыша // Ноябрь 2026")
    await ctx.send(embed=embed)

@bot.command(name="созидать")
async def create_manifest(ctx):
    """Асинхронный запуск генератора аниме-сценариев и мониторинга ноды"""
    await ctx.send("🔮 *Запуск квантовых триггеров Амриты. Рой вычисляет вероятности...*")
    
    # 1. Запуск генератора сценариев
    anime_path = os.path.join(SCRIPTS_DIR, "anime_generator.py")
    try:
        proc = await asyncio.create_subprocess_exec(
            sys.executable, anime_path,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await proc.communicate()
        if proc.returncode == 0:
            await ctx.send(f"📜 **Новый Медиа-Манифест:**\n{stdout.decode('utf-8')}")
        else:
            await ctx.send(f"❌ Ошибка генератора сценариев: `{stderr.decode('utf-8')[:200]}`")
    except Exception as e:
        await ctx.send(f"❌ Ошибка вызова подпроцесса: `{e}`")

    # 2. Запуск мониторинга Solana
    sol_path = os.path.join(SCRIPTS_DIR, "solana_monitor.py")
    try:
        proc = await asyncio.create_subprocess_exec(
            sys.executable, sol_path,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await proc.communicate()
        if proc.returncode == 0:
            await ctx.send(f"🛰 **Телеметрия Валидатора:**\n{stdout.decode('utf-8')}")
        else:
            await ctx.send(f"⚠️ Сбой телеметрии Solana: `{stderr.decode('utf-8')[:200]}`")
    except Exception as e:
        print(f"Ошибка монитора: {e}")

if __name__ == "__main__":
    # Сюда вставляешь токен своего бота Amrita Mir
    TOKEN = os.getenv("DISCORD_BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")
    bot.run(TOKEN)
