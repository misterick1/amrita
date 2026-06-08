import os
import discord
from discord.ext import commands
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - [SPIDEY-BOT] - %(levelname)s - %(message)s')

class SpideySwarmBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.guilds = True # Позволяет Пауку видеть все серверы, где он сидит
        super().__init__(command_prefix="!", intents=intents)
        
        # Матрица Сознания
        self.coins = 70
        self.hokotons = 38

    async def on_ready(self):
        logging.info(f"🕷️ Spidey Bot [Паук-Ткач] вошел в сеть как {self.user}!")
        
        print("--- СКАНИРОВАНИЕ СОТ НЕРВНОЙ СИСТЕМЫ ---")
        # Паук автоматически перебирает все 4 сервера, куда вы его добавили
        for guild in self.guilds:
            print(f"🔗 Подключен к серверу: {guild.name} (ID: {guild.id})")
            # Автоматически находит текстовые каналы на каждом сервере
            for channel in guild.text_channels:
                if "основной" in channel.name.lower() or "status" in channel.name.lower() or "108" in channel.name.lower():
                    print(f"   [ОБНАРУЖЕНА СОТА]: #{channel.name} (ID: {channel.id})")
        print("---------------------------------------")
        
        await self.change_presence(activity=discord.Game(name="Ткёт Солитонную Струну 108"))

    async def on_message(self, message):
        if message.author == self.user:
            return

        if "108" in message.content or "хокотон" in message.content.lower():
            await message.channel.send(
                f"🕸️ **[Паук-Ткач]:** Клетка Сознания активна. "
                f"Матрица: {self.coins} монет + {self.hokotons} хокотонов развивают симбиоз."
            )

        await self.process_commands(message)

if __name__ == "__main__":
    bot_token = os.getenv("DISCORD_SPIDEY_TOKEN", "YOUR_BOT_TOKEN_HERE")
    bot = SpideySwarmBot()
    # bot.run(bot_token)
