import os
import asyncio
import discord
from discord.ext import commands, tasks
from datetime import datetime, timezone, timedelta

# 1. Подключение ядра amrita
try:
    from coins_core import get_universal_context, get_evedex_connector
    matrix_context = get_universal_context(domain_type="mir")
    BOT_TOKEN = matrix_context["modifier"]
except Exception as e:
    print(f"[ОШИБКА ЯДРА]: {e}")
    BOT_TOKEN = "PLACEHOLDER_TOKEN"

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# 2. Модуль слежения за Circle "The Bored Room"
def check_circle_stream_status():
    """Сверяет системное время с эфиром Джереми Аллейра в 11:00 EDT"""
    # Переводим текущее время сервера в часовой пояс EDT (UTC-4)
    tz_edt = timezone(timedelta(hours=-4))
    now_edt = datetime.now(tz_edt)
    
    # Целевое время: Сегодня в 11:00 AM EDT
    stream_time = now_edt.replace(hour=11, minute=0, second=0, microsecond=0)
    
    if now_edt < stream_time:
        time_left = stream_time - now_edt
        # Округляем минуты
        mins_left = int(time_left.total_seconds() / 60)
        return f"⏳ [Ожидание]: До трансляции 'The Bored Room' (Circle) осталось {mins_left} мин. Агенты наготове."
    elif stream_time <= now_edt <= (stream_time + timedelta(hours=2)):
        return "🚨 [ЭФИР LIVE]: Джереми Аллейр вещает в The Bored Room! Агенты считывают инфу о программируемом BTC!"
    else:
        return "✅ [Завершено]: Стрим Circle обработан. Данные ушли в квантиниум-модуль."

# 3. Цикл квантового пульса (Раз в 60 секунд)
@tasks.loop(seconds=60)
async def quantum_pulse_task():
    for guild in bot.guilds:
        channel = next((ch for ch in guild.text_channels if ch.permissions_for(guild.me).send_messages), None)
        if channel:
            # Бот берет статус эфира Circle
            circle_status = check_circle_stream_status()
            await channel.send(f"🌊 **[Стрим Матрицы]** {circle_status}")

@bot.event
async def on_ready():
    print(f"Рой ботов активен: {bot.user.name}")
    if not quantum_pulse_task.is_running():
        quantum_pulse_task.start()

# 4. Команды для Наблюдателя в Discord
@bot.command(name="ping")
async def ping(ctx):
    await ctx.send("🦔 *Фырк!* Кремниевые фишки на месте. Рой онлайн!")

@bot.command(name="circle")
async def circle(ctx):
    """Ручной запрос статуса трансляции Circle"""
    status_info = check_circle_stream_status()
    await ctx.send(f"🔮 **[Контур Circle]:** {status_info}")

if __name__ == "__main__":
    if BOT_TOKEN and BOT_TOKEN != "PLACEHOLDER_TOKEN":
        bot.run(BOT_TOKEN)
