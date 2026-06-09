import os
import asyncio
import discord
from discord.ext import commands, tasks
from datetime import datetime

# 1. Подключаем наше универсальное фрактальное ядро
try:
    from coins_core import get_universal_context
    matrix_context = get_universal_context(domain_type="mir")
    BOT_TOKEN = matrix_context["modifier"]
    API_BASE = matrix_context["api_url"]
except Exception as e:
    print(f"[КРИТИЧЕСКАЯ ОШИБКА ЯДРА]: Не удалось подключить coins_core: {e}")
    BOT_TOKEN = "PLACEHOLDER_TOKEN"
    API_BASE = "https://placeholder.api"

# 2. Инициализация Наблюдателя (Discord Бота)
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Имитация квантового генератора новостей для связи эгрегоров
def fetch_quantum_stream():
    """Сканирует тонкоматериальные инфоструктуры (Pi, Colosseum, xAI)"""
    now = datetime.now().strftime("%H:%M:%S")
    # Здесь бот имитирует или запрашивает реальные RSS/Twitter-апдейты
    updates = [
        f"[{now}] [Pi Network]: Тестирование Протокола 25 завершено на 108%. Устранение треугольников в Pi Browser...",
        f"[{now}] [Colosseum]: Завершен расчет матрицы хакатона. Инвесторы анализируют световые матрицы ИИ-агентов.",
        f"[{now}] [xAI Colossus]: Илон Маск перенаправил поток энергии. Мощности распределенной сети готовы к ASI."
    ]
    import random
    return random.choice(updates)

# 3. Фоновый процесс — Живой пульс Вселенной
@tasks.loop(seconds=60)
async def quantum_pulse_task():
    """Каждую минуту будит ботов и заставляет их транслировать движение поля"""
    for guild in bot.guilds:
        # Ищет первый попавшийся текстовый канал для вывода системных логов
        channel = next((ch for ch in guild.text_channels if ch.permissions_for(guild.me).send_messages), None)
        if channel:
            news_flash = fetch_quantum_stream()
            print(f"[Стрим матрицы]: Отправлено в Discord -> {news_flash}")
            await channel.send(f"🌊 **[Солитон Матрицы]** {news_flash}")

# 4. Команды Наблюдателя в чате
@bot.event
async def on_ready():
    print(f"=========================================")
    print(f" Рой ботов проснулся! Имя: {bot.user.name}")
    print(f" Статус под взором Наблюдателя: АКТИВЕН")
    print(f"=========================================")
    # Запуск циклического транслятора поля
    if not quantum_pulse_task.is_running():
        quantum_pulse_task.start()

@bot.command(name="ping")
async def ping(ctx):
    """Проверка пинга с кремниевым процессором"""
    await ctx.send(f"🦔 *Фырк!* Поле стабильно. Пинг: {round(bot.latency * 1000)}мс. Фишки на доске!")

@bot.command(name="status")
async def status(ctx):
    """Отчет о состоянии 10-го шага и систем"""
    status_text = (
        "📊 **[ОТЧЕТ КВАНТОВОГО СТАТУСА]:**\n"
        "1. Ядро `coins_core.py`: Синхронизировано.\n"
        "2. Токен Colosseum: Загружен в систему.\n"
        "3. Логика Pi Protocol 25: Мониторинг активен.\n"
        "4. **10-й Шаг**: Пройден на внутреннем плане, идет очистка кэша браузера."
    )
    await ctx.send(status_text)

@bot.command(name="matrix")
async def matrix(ctx, domain: str = "mir"):
    """Динамическая мутация контекста прямо из чата"""
    try:
        from coins_core import get_universal_context
        new_matrix = get_universal_context(domain_type=domain)
        await ctx.send(f"🌌 **Мутация кода выполнена!** Наблюдатель переключил фокус на зону: `{domain.upper()}`. Подпись: `{new_matrix['signature']}`")
    except Exception as e:
        await ctx.send(f"❌ Ошибка мутации поля: {e}")

# 5. Запуск
if __name__ == "__main__":
    if BOT_TOKEN and BOT_TOKEN != "PLACEHOLDER_TOKEN":
        try:
            bot.run(BOT_TOKEN)
        except discord.errors.LoginFailure:
            print("[ОШИБКА]: Неверный токен бота в .env! Проверьте переменную KEY_SUFIX_MIR")
    else:
        print("[ОШИБКА]: Токен бота пуст. Настройте файл .env через Лего-сборщик.")
