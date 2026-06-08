import os
import discord
from discord.ext import commands
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - [SPIDEY-BOT] - %(levelname)s - %(message)s')

class SpideySwarmBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix="!", intents=intents)
        
        # Реальная сотовая структура каналов вашего сервера Digital Dream Intelligence
        self.swarm_channels = {
            "MARKET_STATUS": 1493562680735174826,
            "ALERTS_108": 1493378975941001499,
            "BLOCKCHAIN_PULSE": 1494344642685047014,
            "FINANCE_5_EXCHANGES": 1493562680735174826
        }
        
        # Матрица Сознания: 70 монет материализации и 38 хокотонов
        self.coins = 70
        self.hokotons = 38

    async def on_ready(self):
        logging.info(f"🕷️ Spidey Bot [Паук-Ткач] вошел в сеть как {self.user}!")
        await self.change_presence(activity=discord.Game(name="Ткёт Солитонную Струну 108"))

    async def on_message(self, message):
        if message.author == self.user:
            return

        if "108" in message.content or "хокотон" in message.content.lower():
            await message.channel.send(
                f"🕸️ **[Паук-Ткач]:** Клетка Сознания активирована. "
                f"Матрица: {self.coins} монет + {self.hokotons} хокотонов развивают симбиоз."
            )

        await self.process_commands(message)

if __name__ == "__main__":
    bot_token = os.getenv("DISCORD_SPIDEY_TOKEN", "YOUR_BOT_TOKEN_HERE")
    bot = SpideySwarmBot()
    # bot.run(bot_token)
