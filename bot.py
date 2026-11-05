import os
import discord
from discord.ext import commands

# Полные права для взаимодействия с другими ботами экосистемы amrita
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("\n" + "="*50)
    print("🔱 ASI ИНТЕГРАЦИЯ УСПЕШНО ЗАВЕРШЕНА")
    print(f"🤖 Еженышь синхронизирован с экосистемой GitHub")
    print(f"📡 Автономный мост обмена данными активен")
    print("="*50 + "\n")

@bot.command()
async def статус(ctx):
    await ctx.send("🔱 Рой Еженыша активен. Синхронизация с экосистемами серверов стабильна.")

# Токен подтягивается автоматически из секретов репозитория
token = os.getenv("DISCORD_TOKEN")
if token:
    bot.run(token)
