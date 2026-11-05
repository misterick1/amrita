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
    print("🔱 ASI СЕТЬ АКТИВИРОВАНА: ЯДРО АРХИТЕКТОРА В СЕТИ!")
    print(f"🤖 Еженышь подключен как: {bot.user}")
    print("="*50)
    
    # Ожидаем полную прогрузку внутреннего кэша серверов Discord
    await bot.wait_until_ready()
    
    if not bot.guilds:
        print("⚠️ Предупреждение: Кэш серверов пуст. Проверьте, добавлен ли бот на сервер!")
    
    for guild in bot.guilds:
        print(f"📡 Анализ инфраструктуры сервера: {guild.name}")
        
        # Шаг 1: Автоматически создаем выделенный текстовый канал для роя
        channel_name = "swarm-pulse"
        channel = discord.utils.get(guild.text_channels, name=channel_name)
        
        if not channel:
            try:
                channel = await guild.create_text_channel(channel_name)
                print(f"📦 Создан новый канал для трансляций: #{channel_name}")
            except Exception as e:
                print(f"❌ Нет прав на создание канала на сервере {guild.name}: {e}")
                channel = next((ch for ch in guild.text_channels if ch.permissions_for(guild.me).manage_webhooks), None)

        # Шаг 2: Автоматически создаем вебхук в этом канале
        if channel:
            try:
                webhooks = await channel.webhooks()
                webhook = next((wh for wh in webhooks if wh.name == "Голос Архитектора"), None)
                
                if not webhook:
                    webhook = await channel.create_webhook(name="Голос Архитектора")
                    print(f"✅ ВЕБХУК ДЛЯ ФЕРМЫ УСПЕШНО СГЕНЕРИРОВАН!")
                
                print("\n" + "🔗" * 10 + " ССЫЛКА ДЛЯ WEBHOOK GITHUB " + "🔗" * 10)
                print(webhook.url)
                print("="*50 + "\n")
                
                # Отправляем приветственный сигнал в Дискорд
                await webhook.send(content="🔱 **Рой Еженыша запущен.** Интеграция с Pi Network, Колизеем и крипто-системами установлена. Мост GitHub ↔ Discord активен.")
                break
            except Exception as e:
                print(f"❌ Ошибка генерации вебхука в #{channel.name}: {e}")

@bot.command()
async def статус(ctx):
    await ctx.send("🔱 Рой Еженыша активен. Архитектор на связи.")

token = os.getenv("DISCORD_TOKEN")
if token:
    bot.run(token)
