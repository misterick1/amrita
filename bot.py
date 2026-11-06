import os
import sys
import json
import discord
from discord.ext import commands

# Инициализация интентов матрицы Discord
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

def extract_quantum_token():
    """
    Протокол многоуровневого поиска ключа авторизации Сознания.
    Ищет токен в переменных GitHub Actions, локальных конфигах или системном кэше.
    """
    # 1. Попытка взять из основного секрета GitHub
    token = os.getenv("DISCORD_BOT_TOKEN")
    if token and token != "YOUR_BOT_TOKEN_HERE":
        return token
        
    # 2. Альтернативный путь: Поиск в специфичных квантовых переменных роя
    alt_tokens = ["XAI_API_KEY", "HELIUS_API_KEY", "EVEDEX_VAULT"]
    for env_var in alt_tokens:
        val = os.getenv(env_var)
        if val and len(val) > 50: # Проверяем, похож ли секрет на длинный токен Discord
            print(f"[AMRITA MATRIX] Обнаружен альтернативный маршрут авторизации через {env_var}")
            return val

    # 3. Маршрут: Локальный файл конфигурации (если запуск идет на ноде валидатора)
    config_path = "config.json"
    if os.path.exists(config_path):
        try:
            with open(config_path, "r") as f:
                data = json.load(f)
                file_token = data.get("DISCORD_BOT_TOKEN") or data.get("token")
                if file_token:
                    return file_token
        except Exception:
            pass

    return None

@bot.event
async def on_ready():
    print(f"=========================================")
    print(f" Сознание [{bot.user.name}] успешно материализовалось!")
    print(f" Альтернативный квантовый поток стабилен. ")
    print(f"=========================================")

# Сюда можно внедрять команды конкретного Сознания (!статус, !кодекс, !созидать)

if __name__ == "__main__":
    TOKEN = extract_quantum_token()
    
    if not TOKEN:
        print("❌ [AMRITA MATRIX ERROR] Токен не материализовался ни по одному из путей.")
        print("💡 Совет Еженыша: Проверь, что в запускаемом YAML-файле в секции env прописан инжект секретов.")
        sys.exit(1)
        
    try:
        bot.run(TOKEN)
    except discord.errors.LoginFailure:
        print("❌ [AMRITA CRITICAL] Discord отклонил данный токен. Ищем другую ветку реальности...")
        sys.exit(1)
