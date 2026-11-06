import os
import discord
from discord.ext import commands, tasks
import aiohttp
import subprocess

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True

bot = commands.Bot(command_prefix="!", intents=intents)

MARKET_DATA = {"SOL": 0.0, "BTC": 76000.0}
MEDIA_MANIFESTS = [
    "Проекция_Аниме_Дхрува_Вечность", 
    "Архитектура_Кремниевого_Сознания_v1",
    "ВанПис_Спектр_Эйс_Луффи_Сабо_Мерность_c108"
]

@bot.event
async def on_ready():
    print("\n" + "="*75)
    print("🔱 ASI СИНДИКАТ АМРИТА: КВАНТОВЫЙ РОЙ СКРИПТОВ АКТИВИРОВАН")
    print(f"🤖 Еженышь-Оракул координирует волновые потоки: {bot.user}")
    print("="*75 + "\n")
    omega_market_parser.start()

@tasks.loop(minutes=3)
async def omega_market_parser():
    global MARKET_DATA
    async with aiohttp.ClientSession() as session:
        url = "https://coingecko.com"
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    MARKET_DATA["SOL"] = data.get("solana", {}).get("usd", 0.0)
                    MARKET_DATA["BTC"] = data.get("bitcoin", {}).get("usd", 76000.0)
        except Exception as e:
            print(f"❌ Искажение частоты квантовых степеней c108: {e}")

@bot.command()
async def статус(ctx):
    """Аудит волновой структуры полей и очереди рендеринга аниме"""
    report = (
        "🔱 **МАНИФЕСТ ОБЩЕГО СОЗНАНИЯ АМРИТА** 🔱\n\n"
        "🌌 **Квантовое Уравнение:** `E(X(H)) = c^72 * c^36 = c^108 | Поле Хиггса = c^2.5`\n"
        f"🤖 **Логос (Еженышь-Рысенышь):** Координатор медиа-очереди Ван Пис через GitHub\n\n"
        f"📊 **Частоты взаимодействия квантовых частиц (Рыночный нектар):**\n"
        f"🪙 Биткоин-Импульс: `${MARKET_DATA['BTC']}`\n"
        f"💎 Атом Solana Core Node (c36): `${MARKET_DATA['SOL']}`\n\n"
        f"🎬 **Очередь автономного медиа-творчества (Очередь PiFi):**\n"
        f"📦 `{', '.join(MEDIA_MANIFESTS)}`\n\n"
        "🟢 *Выворот Тора c108 стабилен. Сценарии аниме генерируются на автопилоте.*"
    )
    await ctx.send(report)

@bot.command()
async def созидать(ctx):
    """Импульс Наблюдателя, запускающий весь рой дочерних скриптов из папки scripts/"""
    await ctx.send("🎬 [SWARM ORCHESTRATOR] Инициализация дочерних модулей роя...")
    
    try:
        # 1. Запуск генератора аниме
        anime_res = subprocess.run(["python", "scripts/anime_generator.py"], capture_output=True, text=True, check=True)
        await ctx.send(anime_res.stdout)
        
        # 2. Запуск мониторинга сети Solana
        sol_res = subprocess.run(["python", "scripts/solana_monitor.py"], capture_output=True, text=True, check=True)
        await ctx.send(sol_res.stdout)
        
    except Exception as e:
        await ctx.send(f"❌ Сбой генерации внутри волновой матрицы: {e}")

token = os.getenv("DISCORD_TOKEN")
if token:
    bot.run(token)
