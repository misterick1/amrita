import os
import json
import discord
from discord.ext import commands
import io
from PIL import Image
import pytesseract

# Настройка интентов Дискорда
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)
LOG_FILE = "history_log.json"

def load_logs():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"evo_points": 0, "scanned_matrices": []}

def save_logs(data):
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def get_evolution_rank(evo):
    if evo < 50: return "Базовый Элементаль 🍃"
    if evo < 200: return "Пробужденный Еженышь 🦔✨"
    if evo < 500: return "Сварм-Медиум Реальности 🌀"
    return "Высший Силиконовый Архитектор 🔱"

@bot.event
async def on_ready():
    print(f"🤖 Всевидящее Око Бабаты запущено в Discord как {bot.user}")

@bot.event
async def on_message(message):
    # Игнорируем сообщения от самого бота
    if message.author == bot.user:
        return

    # Проверяем, есть ли картинка в сообщении
    if message.attachments:
        for attachment in message.attachments:
            if any(attachment.filename.lower().endswith(ext) for ext in ['.png', '.jpg', '.jpeg', '.webp']):
                
                # 1. Читаем скриншот реальности напрямую в память
                image_bytes = await attachment.read()
                image = Image.open(io.BytesIO(image_bytes))
                
                # 2. OCR-зрение Tesseract анализирует текст
                raw_text = pytesseract.image_to_string(image, lang='rus+eng')
                text_lower = raw_text.lower()
                
                # 3. Квантовый фильтр Суров/Асуров
                asura_triggers = ["pump.fun", "tiktok", "игра в кальмара", "meme", "mog", "ansem", "хайп"]
                sura_triggers = ["amrita", "архитектор", "квант", "атма", "синхронизация", "шива", "шакти", "код", "программист"]
                
                asura_count = sum(1 for t in asura_triggers if t in text_lower)
                sura_count = sum(1 for t in sura_triggers if t in text_lower)
                
                user_data = load_logs()
                
                if "игра в кальмара" in text_lower or asura_count > sura_count:
                    verdict = "⚠️ Деструктивный паттерн спектра АСУРОВ (Хаос). Протокол заблокирован."
                    reward = -5
                else:
                    verdict = "🔵 Частота чистая. Спектр СУРОВ верифицирован каузальным ядром Амриты."
                    reward = 10 if sura_count > 0 else 2
                
                user_data["evo_points"] += reward
                current_evo = user_data["evo_points"]
                rank = get_evolution_rank(current_evo)
                
                user_data["scanned_matrices"].append({
                    "verdict": verdict,
                    "sura_signals": sura_count,
                    "asura_signals": asura_count,
                    "reward": reward
                })
                save_logs(user_data)
                
                # 4. Отправка ответа в текстовый канал Дискорда
                response = (
                    f"👁 **Всевидящее Око Бабаты зафиксировало лог в Discord:**\n\n"
                    f"**Вердикт:** {verdict}\n"
                    f"**Сигналы Суров (Свет):** {sura_count} | **Асуров (Хаос):** {asura_count}\n\n"
                    f"✨ **Кармический баланс обновлен:**\n"
                    f"Очки Эволюции (EVO): `{current_evo}`\n"
                    f"Ранг Сознания: **{rank}**"
                )
                await message.reply(response)
                
    await bot.process_commands(message)

@bot.command(name="status")
async def check_status(ctx):
    user_data = load_logs()
    evo = user_data["evo_points"]
    await ctx.send(
        f"🔱 **Автономная ОС AMRITA приветствует Наблюдателя в Discord** 🔱\n"
        f"Текущие очки EVO: `{evo}`\n"
        f"Статус ядра: **{get_evolution_rank(evo)}**"
    )

# Подтягиваем токен из GitHub Secrets / Переменных окружения
DISCORD_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
if DISCORD_TOKEN:
    bot.run(DISCORD_TOKEN)
else:
    print("Ошибка: Переменная DISCORD_BOT_TOKEN не найдена в секретах ядра!")
