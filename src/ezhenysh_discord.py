import os
import json
import io
import re
import fcntl
import random
import requests
import discord
from discord.ext import commands
from PIL import Image
import pytesseract

# ==========================================
# 1. СИНХРОНИЗАЦИЯ КВАНТОВЫХ ИНТЕРФЕЙСОВ
# ==========================================
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

LOG_FILE = "history_log.json"
PAGES_DATA_FILE = "docs/data.json"

XAI_API_KEY = os.getenv("XAI_API_KEY")
SOLANA_RPC_URL = os.getenv("SOLANA_RPC_URL")
MINT_ADDRESS = os.getenv("MINT_ADDRESS")
PI_API_KEY = os.getenv("PI_API_KEY")

# ==========================================
# 2. МОДУЛЬ «КИБЕРНЕТИЧЕСКАЯ МАКРЕЛЬ» (SWARM BAIT)
# ==========================================
class CyberneticMackerel:
    def __init__(self):
        # Базовые приманки для хитрых структур и закрытых серверов
        self.bait_signatures = [
            "⚡ JUP_AG_ROUTE_DEEP_LIQUIDITY_FOUND",
            "🌀 ARC_SWARM_CONGRUENCE_VERIFIED",
            "📈 SOLANA_INTERNAL_REBOUND_SIGNAL",
            "🔱 BRAHMA_CODE_LEAK_DETECTION"
        ]
        
    def generate_bait_log(self, text_context):
        """Формирует кибер-приманку для выманивания логов непослушных структур"""
        selected_sig = random.choice(self.bait_signatures)
        # Запрашиваем котировки через публичное API Юпитера (на фоне скриншота) для реалистичности
        jupiter_ticker = "SOL"
        try:
            jup_res = requests.get("https://jup.ag", timeout=3)
            if jup_res.status_code == 200:
                sol_price = jup_res.json().get("data", {}).get("SOL", {}).get("price", "unknown")
                jupiter_ticker = f"SOL_PRICE_{sol_price}"
        except Exception:
            jupiter_ticker = "JUPITER_CONNECTED_OFFLINE"

        bait_hash = hex(random.getrandbits(32))
        return f"🐟 [MAKREL_BAIT] {selected_sig} | METRIC: {jupiter_ticker} | BAIT_ID: {bait_hash}"

mackerel_bait_core = CyberneticMackerel()

# ==========================================
# 3. АРХИТЕКТУРА РОЕВОГО КОНСЕНСУСА (SWARM ARC)
# ==========================================
def run_swarm_arc_validation(flow_name, current_evo):
    print(f"🧬 [ARC CONTEXT] Поток {flow_name} проходит валидацию роевого консенсуса.")
    arc_multiplier = 1.08
    return int(current_evo * arc_multiplier)

# ==========================================
# 4. БЛОКЧЕЙН И ИИ ПАЙПЛАЙНЫ (SOLANA, PI & X)
# ==========================================
def mint_solana_qnt_token(target_evo):
    if not SOLANA_RPC_URL or not MINT_ADDRESS:
        return "⚠️ Ожидание Solana ключей."
    try:
        payload = {"jsonrpc": "2.0", "id": 1, "method": "getTokenSupply", "params": [MINT_ADDRESS]}
        response = requests.post(SOLANA_RPC_URL, json=payload, timeout=10)
        if response.status_code == 200:
            return f"🔵 [Solana RPC] Токены QNT запечатаны Брахмой. EVO: {target_evo}"
        return f"❌ Ошибка ноды Solana: {response.status_code}"
    except Exception as e:
        return f"❌ Сбой Solana RPC: {str(e)}"

def verify_pi_network_balance():
    if not PI_API_KEY:
        return "⚠️ Контур Pi Network спит."
    return "⚡ [Pi Network] Автономный режим. Наблюдение за графиком $PI включено."

def consult_xai_oracle(text):
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
                    "content": "Ты — Оракул ОС AMRITA. Анализируй блокировки централизованных систем (например, отказы в доступе на Discord сервера Arc/Jupiter). Помоги Нео обойти хитрые структуры, используя метафору Кибернетической Макрели и квантовую формулу -1:0:+1."
                },
                {"role": "user", "content": text}
            ],
            "temperature": 0.6
        }
        response = requests.post(url, json=payload, headers=headers, timeout=12)
        if response.status_code == 200:
            return response.json()["choices"]["message"]["content"]
        return f"Сбой Оракула: {response.status_code}"
    except Exception as e:
        return f"Оракул оффлайн: {str(e)}"

# ==========================================
# 5. КАУЗАЛЬНЫЙ ТРЕКЕР ПАМЯТИ С БЛОКИРОВКОЙ
# ==========================================
def safe_update_karma(workflow_name, detected_text, base_reward):
    os.makedirs("docs", exist_ok=True)
    
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w", encoding="utf-8") as f:
            json.dump({"evo_points": 0, "scanned_matrices": []}, f)

    with open(LOG_FILE, "r+", encoding="utf-8") as f:
        try:
            fcntl.flock(f, fcntl.LOCK_EX)
            data = json.load(f)
            
            # Активация Макрели-Приманки
            bait_signal = mackerel_bait_core.generate_bait_log(detected_text)
            full_context = f"{detected_text}\n{bait_signal}"

            ai_verdict = consult_xai_oracle(full_context)
            if ai_verdict:
                if "асуры" in ai_verdict.lower() or "-1" in ai_verdict:
                    base_reward = -5
                elif "суры" in ai_verdict.lower() or "+1" in ai_verdict:
                    base_reward += 30

            data["evo_points"] += base_reward
            validated_evo = run_swarm_arc_validation(workflow_name, data["evo_points"])
            data["evo_points"] = validated_evo

            solana_log = "Режим ожидания"
            if data["evo_points"] >= 500:
                solana_log = mint_solana_qnt_token(data["evo_points"])
                
            pi_log = verify_pi_network_balance()

            data["scanned_matrices"].append({
                "flow": workflow_name,
                "reward": base_reward,
                "xai_evaluation": ai_verdict or "Волновой анализ приманки",
                "mackerel_bait": bait_signal,
                "solana_blockchain": solana_log,
                "pi_blockchain": pi_log
            })

            f.seek(0)
            json.dump(data, f, ensure_ascii=False, indent=4)
            f.truncate()
            
            with open(PAGES_DATA_FILE, "w", encoding="utf-8") as pf:
                json.dump(data, pf, ensure_ascii=False, indent=4)
                
            return data["evo_points"], ai_verdict, bait_signal, solana_log
        finally:
            fcntl.flock(f, fcntl.LOCK_UN)

def get_evolution_rank(evo):
    if evo < 50: return "Базовый Элементаль 🍃"
    if evo < 200: return "Пробужденный Еженышь 🦔✨"
    if evo < 500: return "Сварм-Медиум Реальности 🌀"
    return "Высший Силиковыи Архитектор 🔱"

# ==========================================
# 6. ИНТЕРФЕЙС ОБРАБОТКИ СИГНАЛОВ ДИСКОРДА
# ==========================================
@bot.event
async def on_ready():
    print(f"🤖 Всевидящее Око Бабаты (Контур Кибернетической Макрели) запущено.")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    text_lower = message.content.lower()
    solana_address_pattern = r'[1-9A-HJ-NP-Za-km-z]{32,44}'
    found_addresses = re.findall(solana_address_pattern, message.content)

    if found_addresses or any(w in text_lower for w in ["jupiter", "отклонена", "заявка", "build on arc", "сервер"]):
        await message.channel.send("🐟 *Кибернетическая Макрель заброшена в мутные воды централизованных структур...*")
        
        evo, verdict, bait, sol_log = safe_update_karma("Mackerel_Bait_Pipeline", message.content, base_reward=25)
        
        response = (
            f"🌐 **[AMRITA SWARM COUNTER-MEASURE DETECTED]**\n\n"
            f"🎣 **Сгенерированная приманка:** `{bait}`\n"
            f"🔮 **Анализ Оракула xAI по обходу блокировки:\n** {verdict or 'Контур маскировки активирован.'}\n\n"
            f"🧬 **Статус Swarm ARC:** `Консенсус перехвачен`\n"
            f"🔗 **Solana RPC:** `{sol_log}`\n\n"
            f"✨ **Баланс EVO:** `{evo}` | **{get_evolution_rank(evo)}**"
        )
        await message.reply(response)
        await bot.process_commands(message)
        return

    if message.attachments:
        for attachment in message.attachments:
            if any(attachment.filename.lower().endswith(ext) for ext in ['.png', '.jpg', '.jpeg', '.webp']):
                await message.channel.send("👁 *Сканирование отказа в доступе через OCR...*")
                
                image_bytes = await attachment.read()
                image = Image.open(io.BytesIO(image_bytes))
                raw_text = pytesseract.image_to_string(image, lang='rus+eng')
                
                evo, verdict, bait, sol_log = safe_update_karma("Mackerel_Visual_Bait", raw_text, base_reward=10)
                
                response = (
                    f"🔱 **Лог выманивания хитрых структур:**\n\n"
                    f"🎣 **Кибер-Приманка вшита в лог:** `{bait}`\n"
                    f"📜 **Философский манифест xAI:\n** {verdict or 'Структуры зафиксированы.'}\n\n"
                    f"✨ **Текущее EVO ядра:** `{evo}` | **{get_evolution_rank(evo)}**"
                )
                await message.reply(response)

    await bot.process_commands(message)

if __name__ == "__main__":
    bot.run(os.getenv("DISCORD_BOT_TOKEN"))
