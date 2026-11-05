import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("\n" + "="*50)
    print("🔥 ЯДРО АРХИТЕКТОРА АКТИВИРОВАНО!")
    print(f"🤖 Еженышь вошёл в сеть как: {bot.user}")
    print("="*50)
    
    for guild in bot.guilds:
        # Ищем канал, где у бота есть права на вебхуки
        channel = next((ch for ch in guild.text_channels if ch.permissions_for(guild.me).manage_webhooks), None)
        if channel:
            try:
                webhooks = await channel.webhooks()
                webhook = next((wh for wh in webhooks if wh.name == "Голос Архитектора"), None)
                if not webhook:
                    webhook = await channel.create_webhook(name="Голос Архитектора")
                
                print("\n🚀 ВЕБХУК НАЙДЕН / СОЗДАН УСПЕШНО!")
                print(f"📍 Канал: #{channel.name} на сервере '{guild.name}'")
                print("🔗 СКОПИРУЙТЕ ЭТУ ССЫЛКУ СНИЗУ И ВСТАВЬТЕ В НАСТРОЙКИ GITHUB:")
                print(webhook.url)
                print("="*50 + "\n")
                break
            except Exception as e:
                print(f"❌ Ошибка вебхука в #{channel.name}: {e}")

@bot.command()
async def статус(ctx):
    await ctx.send("🔱 Рой Еженыша активен. Архитектор на связи.")

token = os.getenv("DISCORD_TOKEN")
if token:
    bot.run(token)
