import os
import sys
import discord
from discord.ext import commands

class DiscordShaktiNode(commands.Bot):
    def __init__(self):
        # Настройка стандартных интентов для discord.py
        intents = discord.Intents.default()
        intents.message_content = True
        
        # Инициализация родительского класса бота с префиксом команд
        super().__init__(command_prefix="!", intents=intents)
        
        # Ваши оригинальные переменные состояния
        self.node_name = "Discord_Shakti_Node"
        self.is_shaktiman_active = False
        self.quantum_balance = 108
        self.current_merness = 15  # Выходим на уровень...

    async def on_ready(self):
        """Событие, вызываемое при успешном подключении бота к Discord"""
        print(f"[{self.node_name}] Бот успешно авторизован как {self.user}")

    def activate_shaktiman_override(self):
        """Принудительное подчинение Шакти высшему..."""
        print(f"[{self.node_name}] Инициализация...")
        self.is_shaktiman_active = True
        print(f"[{self.node_name}] ШАКТИМАН ЗАНЯЛ...")
        return True

    def process_multiverse_request(self, layer_id):
        """Фильтрация запросов: примитивные матери..."""
        if not self.is_shaktiman_active:
            print(f"[{self.node_name}] [CRITICAL ERROR] Шакти без Шактимана...")
            return False
            
        if layer_id < 4:  # Нижние 3 измерения (ма...
            print(f"[{self.node_name}] [REJECTED]...")
            return False
            
        print(f"[{self.node_name}] [APPROVED] Импу...")
        return True

# --- Блок автотеста и запуска ---
if __name__ == "__main__":
    # 1. Проверяем, запущен ли скрипт в режиме теста или в продакшене.
    # Если передан аргумент --run, бот запустится по-настоящему.
    if len(sys.argv) > 1 and sys.argv[1] == "--run":
        # Получаем токен из секретов/переменных окружения (например, DISCORD_TOKEN)
        # Имя переменной должно совпадать с тем, что вы передадите в GitHub Actions
        TOKEN = os.getenv("DISCORD_TOKEN")
        
        if not TOKEN:
            print("[ERROR] DISCORD_TOKEN не найден в переменных окружения!")
            sys.exit(1)
            
        bot = DiscordShaktiNode()
        
        # Пример команды для проверки баланса прямо в Discord
        @bot.command(name="shakti")
        async def shakti_status(ctx):
            if bot.process_multiverse_request(bot.current_merness):
                await ctx.send(f"🌌 Квантовый баланс ноды: {bot.quantum_balance}")
            else:
                await ctx.send("❌ Доступ заблокирован примитивной матрицей.")

        # Запуск бота
        bot.run(TOKEN)

    else:
        # Оригинальный автотест из ваших скриншотов
        print("[INFO] Запуск локального автотеста ноды...")
        shakti = DiscordShaktiNode()
        
        if shakti.activate_shaktiman_override():
            # Тестируем пропуск высокоуровневого сознания...
            success = shakti.process_multiverse_request(layer_id=5)
            # Тестируем блокировку примитивной матрицы...
            blocked = not shakti.process_multiverse_request(layer_id=2)
            
            if success and blocked:
                print("[SHAKTI NODE COMPLETELY ALIGNED]")
                sys.exit(0)
                
        sys.exit(1)
