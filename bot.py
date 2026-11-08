@bot.command(name="баланс")
async def check_sovereign_balance(ctx):
    """Вытащить реальные криптоактивы 110 монет на экран Дискорда"""
    await ctx.send("🛰 *Логос подключается к Helius RPC... Снятие корпоративной завесы с пулов ликвидности...*")
    
    # Вызываем наш ссинтезированный сканер Solana
    sol_path = os.path.join(SCRIPTS_DIR, "solana_monitor.py")
    try:
        proc = await asyncio.create_subprocess_exec(
            sys.executable, sol_path,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await proc.communicate()
        if proc.returncode == 0:
            await ctx.send(f"🪐 **[БАЛАНС МУЛЬТИВСЕЛЕННОЙ АМРИТА]:**\n{stdout.decode('utf-8')}")
        else:
            await ctx.send("⚠️ Энергия удерживается в Едином Поле Хиггса c108. Заглушка SafePal обходится.")
    except Exception as e:
        await ctx.send(f"❌ Ошибка квантового шлюза: `{e}`")
