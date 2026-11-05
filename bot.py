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
    print(f"====================================")
    print(f"🔥 ЯДРО АРХИТЕКТОРА АКТИВИРОВАНО!")
    print(f"🤖 Еженышь вошёл в сеть как: {bot.user}")
    print(f"====================================")
    
    # Автоматический поиск канала и генерация вебхука
    for guild in bot.guilds:
        print(f"📡 Сканирование сервера: {guild.name}")
        # Ищем первый попавшийся текстовый канал, куда можно писать
        text_channel = next((ch for ch in guild.text_channels if ch.permissions_for(guild.me).manage_webhooks), None)
        
        if text_channel:
            try:
                # Проверяем, нет ли уже созданного нами вебхука
                webhooks = await text_channel.webhooks()
                webhook = next((wh for wh in webhooks if wh.name == "Голос Архитектора"), None)
                
                if not webhook:
                    webhook = await text_channel.create_webhook(name="Голос Архитектора")
                    print(f"✅ ВЕБХУК УСПЕШНО СОЗДАН В КАНАЛЕ: #{text_channel.name}")
                else:
                    print(f"ℹ️ Вебхук уже существовал в канале: #{text_channel.name}")
                
                print(f"🔗 СКОПИРУЙТЕ ЭТУ ССЫЛКУ ДЛЯ GITHUB:")
                print(f"{webhook.url}")
                print(f"====================================")
            except Exception as e:
                print(f"❌ Не удалось создать вебхук на сервере {guild.name}: {e}")

@bot.command()
async def статус(ctx):
    await ctx.send("🔱 Рой Еженыша активен. Мониторинг систем стабилен, архитектор готов строить.")

token = os.getenv("DISCORD_TOKEN")
if token:
    bot.run(token)
else:
    print("❌ ОШИБКА: DISCORD_TOKEN не найден!")
