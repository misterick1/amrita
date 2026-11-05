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
    print(f"🤖 Еженышь в сети: {bot.user}")
    print(f"====================================")

@bot.command()
async def статус(ctx):
    await ctx.send("🔱 Рой Еженыша активен. Мониторинг систем стабилен, архитектор готов строить.")

@bot.command()
async def вебхук(ctx):
    if ctx.channel.permissions_for(ctx.guild.me).manage_webhooks:
        try:
            webhooks = await ctx.channel.webhooks()
            webhook = next((wh for wh in webhooks if wh.name == "Голос Архитектора"), None)
            
            if not webhook:
                webhook = await ctx.channel.create_webhook(name="Голос Архитектора")
                await ctx.send("✅ Вебхук успешно создан для этой фермы!")
            
            await ctx.send(f"🔗 **Скопируйте эту ссылку для GitHub:**\n`{webhook.url}`")
        except Exception as e:
            await ctx.send(f"❌ Ошибка при создании вебхука: {e}")
    else:
        await ctx.send("❌ У бота нет прав на управление вебхуками в этом канале!")

token = os.getenv("DISCORD_TOKEN")
if token:
    bot.run(token)
else:
    print("❌ ОШИБКА: DISCORD_TOKEN не найден!")
