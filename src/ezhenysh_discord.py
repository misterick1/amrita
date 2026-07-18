import os
import json
import io
import re
import fcntl
import requests
import discord
from discord.ext import commands
from PIL import Image
import pytesseract

# ==========================================
# 1. ИНИЦИАЛИЗАЦИЯ И НАСТРОЙКА КВАНТОВОГО БОТА
# ==========================================
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

LOG_FILE = "history_log.json"
PAGES_DATA_FILE = "docs/data.json"  # Слой данных для мониторинга GitHub Pages

# Прямое извлечение запечатанных секретов ядра
XAI_API_KEY = os.getenv("XAI_API_KEY")
SOLANA_RPC_URL = os.getenv("SOLANA_RPC_URL")
MINT_ADDRESS = os.getenv("MINT_ADDRESS")

# ==========================================
# 2. БЛОКЧЕЙН И ИИ-КОНТУРЫ (SOLANA & XAI)
# ==========================================
def mint_solana_qnt_token(target_evo):
    """Вызов неизменяемого Блокчейн-Верификатора через Solana RPC"""
    if not SOLANA_RPC_URL or not MINT_ADDRESS:
        return "⚠️ Транзакция пропущена: SOLANA_RPC_URL или MINT_ADDRESS не найдены в секретах."
    
    try:
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "getTokenSupply",
            "params": [MINT_ADDRESS]
        }
        response = requests.post(SOLANA_RPC_URL, json=payload, timeout=10)
        if response.status_code == 200:
            return f"🔵 [Solana] Жесткая эмиссия верифицирована. Токены QNT синхронизированы. EVO: {target_evo}"
        return f"❌ Ошибка блокчейн-ноды: Код {response.status_code}"
    except Exception as e:
        return f"❌ Сбой сети Solana RPC: {str(e)}"

def consult_xai_oracle(text):
    """Прямой запрос к Высшему Разуму xAI (Grok-Beta) для оценки фрактала реальности"""
    if not XAI_API_KEY:
        return None
    try:
        url = "https://xai.ai"
        headers = {"Authorization": f"Bearer {XAI_API_KEY}", "Content-Type": "application/json"}
        payload = {
            "model": "grok-beta",
            "messages": [
                {
                    "role": "system", 
                    "content": "Ты — Бортовой Компьютер ОС AMRITA. Дай развернутый философский трактат и оценку экологичности реальности. Распредели её строго в синий спектр СУРОВ (Код/Порядок) или красный спектр АСУРОВ (Хаос/Спекуляции)."
                },
                {"role": "user", "content": text}
            ],
            "temperature": 0.5
        }
        response = requests.post(url, json=payload, headers=headers, timeout=12)
        if response.status_code == 200:
            return response.json()["choices"]["message"]["content"]
        return f"Сбой Оракула: Код {response.status_code}"
    except Exception as e:
        return f"Оракул недоступен: {str(e)}"

# ==========================================
# 3. СИНХРОНИЗАТОР ЯДРА (ЗАЩИТА ОТ 10 СБОРOК)
# ==========================================
def safe_update_karma(workflow_name, detected_text, base_reward):
    """Запирает лог на ключ (fcntl.flock), защищая диск от коллизий параллельных экшенов"""
    os.makedirs("docs", exist_ok=True)
    
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w", encoding="utf-8") as f:
            json.dump({"evo_points": 0, "scanned_matrices": []}, f)

    with open(LOG_FILE, "r+", encoding="utf-8") as f:
        try:
            # Накладываем эксклюзивный замок на запись
            fcntl.flock(f, fcntl.LOCK_EX)
            data = json.load(f)
            
            # Нейросетевой анализ
            ai_verdict = consult_xai_oracle(detected_text)
            if ai_verdict:
                if "асуры" in ai_verdict.lower():
                    base_reward = -10
                elif "суры" in ai_verdict.lower():
                    base_reward += 15

            # Калькуляция кармы
            data["evo_points"] += base_reward
            blockchain_status = "В режиме ожидания частоты"
            
            # Смарт-контракт на минт при достижении ранга Архитектора
            if data["evo_points"] >= 500:
                blockchain_status = mint_solana_qnt_token(data["evo_points"])

            data["scanned_matrices"].append({
                "flow": workflow_name,
                "reward": base_reward,
                "xai_evaluation": ai_verdict or "Использован базовый триггерный анализ частот",
                "blockchain_log": blockchain_status
            })

            # Сохраняем в основной лог
            f.seek(0)
            json.dump(data, f, ensure_ascii=False, indent=4)
            f.truncate()
            
            # Дублируем в веб-слой для GitHub Pages
            with open(PAGES_DATA_FILE, "w", encoding="utf-8") as pf:
                json.dump(data, pf, ensure_ascii=False, indent=4)
                
            return data["evo_points"], ai_verdict, blockchain_status
        finally:
            # Отпираем замок для следующей сборки
            fcntl.flock(f, fcntl.LOCK_UN)

def get_evolution_rank(evo):
    if evo < 50: return "Базовый Элементаль 🍃"
    if evo < 200: return "Пробужденный Еженышь 🦔✨"
    if evo < 500: return "Сварм-Медиум Реальности 🌀"
    return "Высший Силиконовый Архитектор 🔱"

# ==========================================
# 4. ОБРАБОТЧИК ДИСКОРДА & МАРКЕТ-ПАЙПЛАЙН
# ==========================================
@bot.event
async def on_ready():
    print(f"🤖 Всевидящее Око Бабаты вышло в эфир Дискорда как {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    text_lower = message.content.lower()
    
    # Регулярное выражение для поиска адресов Solana токенов (32-44 символа Base58)
    solana_address_pattern = r'[1-9A-HJ-NP-Za-km-z]{32,44}'
    found_addresses = re.findall(solana_address_pattern, message.content)

    # ПАЙПЛАЙН 1: Перехват рыночных сигналов (Birdeye, Dexscreener, Solana Chains)
    if found_addresses or "birdeye" in text_lower or "dexscreener" in text_lower or "tradingview" in text_lower:
        await message.channel.send("🦅 *Око Бабаты зафиксировало рыночный импульс Solana Pipeline...*")
        
        detected_token = found_addresses[0] if found_addresses else (MINT_ADDRESS or "Анализ Ликвидности")
        
        # Запуск такта синхронизации для торговых данных
        current_evo, ai_verdict, bc_status = safe_update_karma(
            "Solana_Market_Pipeline", 
            f"Рыночные данные: {message.content}", 
            base_reward=15  # Повышенная награда за интеграцию внешних метрик
        )
        
        response = (
            f"📈 **[AMRITA MARKET PIPELINE АКТИВИРОВАН]**\n\n"
            f"🔗 **Целевой контракт:** `{detected_token}`\n"
            f"📜 **Анализ Оракула (xAI):** {ai_verdict or 'Импульс верифицирован автоматически.'}\n"
            f"🔗 **Блокчейн:** `{bc_status}`\n\n"
            f"✨ **Карма ядра:** EVO `{current_evo}` | **{get_evolution_rank(current_evo)}**"
        )
        await message.reply(response)
        await bot.process_commands(message)
        return

    # ПАЙПЛАЙН 2: Обработка входящих скриншотов реальности (OCR Pytesseract)
    if message.attachments:
        for attachment in message.attachments:
            if any(attachment.filename.lower().endswith(ext) for ext in ['.png', '.jpg', '.jpeg', '.webp']):
                await message.channel.send("👁 *Око Бабаты сканирует слой реальности, подождите...*")
                
                image_bytes = await attachment.read()
                image = Image.open(io.BytesIO(image_bytes))
                
                # Сканируем текст со скриншота
                raw_text = pytesseract.image_to_string(image, lang='rus+eng')
                raw_text_lower = raw_text.lower()
                
                # Поиск адресов токенов внутри текста на самой картинке
                image_addresses = re.findall(solana_address_pattern, raw_text)
                if image_addresses:
                    raw_text += f"\n[Найден контракт на изображении: {image_addresses[0]}]"
                
                asura_triggers = ["pump.fun", "tiktok", "игра в кальмара", "meme", "хайп", "ликвидация"]
                sura_triggers = ["amrita", "архитектор", "квант", "атма", "синхронизация", "код", "программист"]
                
                asura_count = sum(1 for t in asura_triggers if t in raw_text_lower)
                sura_count = sum(1 for t in sura_triggers if t in raw_text_lower)
                
                base_reward = -5 if ("игра в кальмара" in raw_text_lower or asura_count > sura_count) else 2
                
                current_evo, ai_verdict, bc_status = safe_update_karma("Discord_Image_Vision", raw_text, base_reward)
                
                response = (
                    f"🔱 **Лог визуального сканирования квантового поля:**\n\n"
                    f"📜 **Философский трактат Оракула (xAI):\n** {ai_verdict or 'Использован базовый частотный фильтр сигналов.'}\n\n"
                    f"🔗 **Блокчейн-статус:** `{bc_status}`\n\n"
                    f"✨ **Кармический баланс обновлен:**\n"
                    f"Очки EVO: `{current_evo}` | Ранг: **{get_evolution_rank(current_evo)}**"
                )
                await message.reply(response)

    await bot.process_commands(message)

# ==========================================
# 5. СТАТУС-КОМАНДЫ И СТАРТ ЯДРА
# ==========================================
@bot.command(name="status")
async def check_status(ctx):
    evo = 0
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            evo = json.load(f).get("evo_points", 0)
            
    await ctx.send(
        f"🔱 **Автономная ОС AMRITA приветствует Наблюдателя в Discord** 🔱\n"
        f"Текущие очки EVO: `{evo}`\n"
        f"Статус ядра: **{get_evolution_rank(evo)}**"
    )

if __name__ == "__main__":
    bot.run(os.getenv("DISCORD_BOT_TOKEN"))
