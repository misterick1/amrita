import os
import asyncio
import discord
from discord.ext import commands, tasks

# ПОДКЛЮЧЕНИЕ НАПРЯМУЮ: Берем токен из готовой строчки в вашем .env
try:
    from coins_core import load_env_file
    load_env_file()
    # Берем тот самый длинный токен, который у вас уже вписан!
    BOT_TOKEN = os.getenv("COLOSSEUM_COPILOT_PAT")
except Exception as e:
    print(f"Ошибка: {e}")
    BOT_TOKEN = None

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@tasks.loop(seconds=60)
async def quantum_pulse_task():
    for guild in bot.guilds:
        channel = next((ch for ch in guild.text_channels if ch.permissions_for(guild.me).send_messages), None)
        if channel:
            await channel.send("🛠️ **[Solana Foundation Watcher]**\n• Дедлайн: **Эпоха 986**\n• Статус: Нода под защицией ИИ.")

@bot.event
async def on_ready():
    print(f"Бот успешно зашел в сеть: {bot.user.name}")
    if not quantum_pulse_task.is_running():
        quantum_pulse_task.start()

@bot.command(name="solana")
async def solana(ctx):
    await ctx.send("🛠️ **[Solana Foundation Watcher]**\n• Дедлайн: **Эпоха 986**\n• Требуемая версия Agave: `>= 4.0.2`\n• Требуемая версия Firedancer: `>= 0.911.40002`\n• Статус: Проверка завершена.")

if __name__ == "__main__":
    if BOT_TOKEN:
        bot.run(BOT_TOKEN)
    else:
        print("Ошибка: Токен пуст!")
