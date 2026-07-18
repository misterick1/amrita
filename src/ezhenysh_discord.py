import re

# Добавляем в основной цикл on_message регулярное выражение для поиска Solana-адресов
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Проверка на наличие текстовых сигналов Solana/Birdeye/Dexscreener
    text_lower = message.content.lower()
    solana_address_pattern = r'[1-9A-HJ-NP-Za-km-z]{32,44}'
    found_addresses = re.findall(solana_address_pattern, message.content)

    if found_addresses or "birdeye" in text_lower or "dexscreener" in text_lower:
        await message.channel.send("🦅 *Око Бабаты зафиксировало рыночный импульс Solana Chain...*")
        
        token_address = found_addresses[0] if found_addresses else MINT_ADDRESS
        
        # Симулируем 4-этапный пайплайн данных (сбор, фильтрация, калибровка, верификация)
        current_evo, ai_verdict, bc_status = safe_update_karma(
            "Solana_Market_Pipeline", 
            f"Рыночный сигнал токена {token_address}. Тренд зафиксирован.", 
            base_reward=15 # Повышенная награда за интеграцию ликвидности
        )
        
        response = (
            f"📈 **4-Stage Market Data Pipeline активирован:**\n"
            f"🔗 Верифицируемый токен: `{token_address}`\n"
            f"🔮 **Вердикт xAI:** Рыночный фрактал чист. Спектр СУРОВ доминирует.\n"
            f"✨ Текущий баланс EVO ядра: `{current_evo}`"
        )
        await message.reply(response)

    # Оставляем старую обработку картинок
    if message.attachments:
        # ... твой предыдущий код обработки скриншотов ...
        pass

    await bot.process_commands(message)
