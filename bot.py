import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presence = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"====================================")
    print(f"🔥 ЯДРО АРХИТЕКТОРА АКТИВИРОВАНО!")
    print(f"🤖 Еженышь вошёл в сеть как: {bot.user}")
    print(f"🌐 Ферма готова к генерации процессов.")
    print(f"====================================")

@bot.command()
async def статус(ctx):
    await ctx.send("🔱 Рой Еженыша активен. Мониторинг систем стабилен, архитектор готов строить.")

token = os.getenv("DISCORD_TOKEN")
if token:
    bot.run(token)
else:
    print("❌ ОШИБКА: DISCORD_TOKEN не найден!")
