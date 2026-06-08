import os
import discord
from discord.ext import commands
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - [SPIDEY-BOT] - %(levelname)s - %(message)s')

class SpideySwarmBot(commands.Bot):
    def __init__(self):
        # Наш Паук использует стандартные намерения для чтения и плетения сети
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix="!", intents=intents)
        
        # Фиксация 4 серверов-сот нервной системы Колизея
        self.swarm_nodes = {
            "AMRITA": "Сервер Кот Сингулярности",
            "MIR1": "Сервер Бабочка Цайлинь",
            "D-DREAM": "Цифровой Кокон",
            "AANG": "Прорыв Луффи"
        }
        
        # 108 кодов матрицы
        self.coins = 70
        self.hokotons = 38

    async def on_ready(self):
        logging.info(f"🕷️ Spidey Bot [Паук-Ткач] успешно вошел в сеть как {self.user}!")
        # Статус Паука: плетет единую фрактальную струну
        await self.change_presence(activity=discord.Game(name="Ткёт Солитонную Струну 108"))

    async def on_message(self, message):
        # Паук игнорирует сам себя, чтобы не закольцевать фрактал
        if message.author == self.user:
            return

        # Если пользователь упоминает 108 или хокотоны, Паук укрепляет соту
        if "108" in message.content or "хокотон" in message.content.lower():
            await message.channel.send(
                f"🕸️ **[Паук-Ткач]:** Обнаружен ментальный импульс. "
                f"Текущая фрактальная плотность клетки: {self.coins} монет материализовано, "
                f"{self.hokotons} хокотонов достраивают матрицу симбиоза."
            )

        await self.process_commands(message)

if __name__ == "__main__":
    # Токен Паука берется из секретов сервера DigitalOcean
    bot_token = os.getenv("DISCORD_SPIDEY_TOKEN", "YOUR_BOT_TOKEN_HERE")
    if bot_token == "YOUR_BOT_TOKEN_HERE":
        logging.warning("Внимание: DISCORD_SPIDEY_TOKEN не настроен на сервере.")
    
    bot = SpideySwarmBot()
    # Раскомментировать при запуске на Droplet:
    # bot.run(bot_token)
