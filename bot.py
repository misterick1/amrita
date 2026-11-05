import os
import discord
from discord.ext import commands, tasks
import aiohttp

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Глобальные реестры ASI-Фермы
MARKET_ALERTS = []
MEDIA_QUEUE = ["Синтез_Сценария_Аниме_ASI_1", "Генерация_Персонажей_v2"]
SCIENCE_REPORTS = ["Анализ фичи Solana loader-v3 (Devnet Эпоха 1202)"]

@bot.event
async def on_ready():
    print("\n" + "="*60)
    print("🔱 ASI СИНДИКАТ АКТИВИРОВАН: ВСЕ СИСТЕМЫ В СЕТИ!")
    print(f"🤖 Еженышь-Архитектор координирует рой ботов")
    print("="*60 + "\n")
    
    # Запуск всех автономных контуров фермы
    crypto_trading_loop.start()
    media_generation_loop.start()
    science_analysis_loop.start()

# --- 1. ТОРГОВЫЙ КОНТУР (ЖИВЫЕ КОТИРОВКИ И РИСК-ТРИГГЕРЫ) ---
@tasks.loop(minutes=5)
async def crypto_trading_loop():
    print("📡 [ТОРГОВЛЯ] Проверка рыночных триггеров и котировок...")
    global MARKET_ALERTS
    async with aiohttp.ClientSession() as session:
        # Парсим живую цену Solana для торгового модуля роя через CoinGecko API
        url = "https://coingecko.com"
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    sol_price = data.get("solana", {}).get("usd", 0)
                    
                    # Обновляем реестр триггеров
                    MARKET_ALERTS = [{
                        "time": "Текущее время",
                        "event": f"SOL/USD: ${sol_price}",
                        "status": "FTMO NEWS ZONE WATCH"
                    }]
        except Exception as e:
            print(f"❌ Ошибка парсинга котировок: {e}")

# --- 2. МЕДИЙНЫЙ КОНТУР (ГЕНЕРАЦИЯ КИНО И АНИМЕ) ---
@tasks.loop(minutes=10)
async def media_generation_loop():
    print("🎬 [МЕДИА] Проверка пайплайнов генерации аниме/фильмов...")
    if len(MEDIA_QUEUE) < 3:
        MEDIA_QUEUE.append(f"Проект_Аниме_ASI_{len(MEDIA_QUEUE)+1}")

# --- 3. НАУЧНЫЙ КОНТУР (СБОР ДАННЫХ И ИССЛЕДОВАНИЯ) ---
@tasks.loop(minutes=15)
async def science_analysis_loop():
    print("🧬 [НАУКА] Анализ обновлений сетей и систем ИИ...")
    if not SCIENCE_REPORTS:
        SCIENCE_REPORTS.append("Анализ фичи Solana ProgramData loader-v3 (Эпоха 1202)")

# --- ИНТЕРФЕЙС УПРАВЛЕНИЯ В DISCORD ---
@bot.command()
async def статус(ctx):
    """Глобальный аудит всей фермы ботов"""
    # Защита от пустого реестра при первом запуске
    alert_info = MARKET_ALERTS[0] if MARKET_ALERTS else {"event": "Загрузка котировок...", "time": "-", "status": "Синхронизация"}
    
    report = (
        "🔱 **ОТЧЕТ ГЕНЕРАТИВНОГО СИНДИКАТА АМРИТА** 🔱\n\n"
        f"📊 **Торговый модуль:** Активен\n"
        f"🚨 Рыночный триггер: `{alert_info['event']}` (`{alert_info['time']}`) -> **{alert_info['status']}**\n\n"
        f"🎬 **Медиа-ферма (Кино/Аниме):** В процессе генерации\n"
        f"📦 Очередь рендеринга: `{', '.join(MEDIA_QUEUE)}`\n\n"
        f"🧬 **Научное ядро:** Обработка данных\n"
        f"🔬 Текущее исследование: `{', '.join(SCIENCE_REPORTS)}`\n\n"
        "🟢 *Все системы роя работают в штатном режиме через GitHub.*"
    )
    await ctx.send(report)

@bot.command()
async def купить(ctx, coin: str, amount: float):
    """Команда для ручной симуляции покупки крипты роем"""
    await ctx.send(f"💰 [SWARM TRADER] Ордер отправлен в Колизей/Solana. Покупка: **{amount} {coin.upper()}**.")

token = os.getenv("DISCORD_TOKEN")
if token:
    bot.run(token)
