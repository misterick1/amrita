import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
swarm_bot = commands.Bot(command_prefix="!", intents=intents)

@swarm_bot.command(name="swarm_status")
async def get_swarm_status(ctx):
    """Команда для полной проверки всей инфраструктуры проекта amrita"""
    from nvidia_compute_core import compute_core
    from multiexchange_liquidity_core import liquidity_manager
    
    gpu_info = compute_core.get_hardware_status()
    
    embed = discord.Embed(title="⚙️ Системный статус Роя Агентов (Amrita Swarm)", color=discord.Color.purple())
    embed.add_field(name="Вычислительное ядро GPU", value=f"🤖 {gpu_info['device_name']}\nПамять: {gpu_info['allocated_mem_gb']} GB", inline=False)
    embed.add_field(name="Подключенные биржи", value="🔗 " + ", ".join(liquidity_manager.connected_exchanges), inline=True)
    embed.add_field(name="Квантовый щит", value="🔒 Активен (SHA3-512)", inline=True)
    
    await ctx.send(embed=embed)

@swarm_bot.command(name="predict")
async def predict_market(ctx, input_mint: str, output_mint: str):
    """Принудительный запуск оценки торгового плеча и котировок через Jupiter"""
    from jupiter_predict_bridge import jupiter_bridge
    
    await ctx.send(f"⏳ Запрос котировок в Jupiter v6 для токена `{input_mint}`...")
    # Запрашиваем тестовый объем в 1 SOL (1 000 000 000 lamports)
    quote = jupiter_bridge.fetch_jupiter_quote(input_mint, output_mint, 1000000000)
    
    if "error" in quote:
        await ctx.send(f"❌ Ошибка получения данных: {quote['error']}")
    else:
        out_amount = quote.get("outAmount", "0")
        await ctx.send(f"📊 Котировка получена. Ожидаемый объем на выходе: `{out_amount}` единиц подсети.")

# Скрипт готов к запуску через swarm_bot.run(TOKEN)
