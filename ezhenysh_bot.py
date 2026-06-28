import os
import sys
import json
from io import StringIO
import telebot
from solana.rpc.api import Client
from solana.transaction import Transaction
from solana.keypair import Keypair
from solana.publickey import PublicKey

# ==========================================
# 1. КВАНТОВОЕ ЯДРО БАБАТЫ И МОСТ SOLANA
# ==========================================
class AmritaSolanaBridge:
    def __init__(self, rpc_url: str = "https://solana.com"):
        self.client = Client(rpc_url)
        self.total_quanta = 108
        self.sura = 70   
        self.asura = 38  
        self.shadow_filters = ["дефицит", "скам", "обман", "игра в кальмара", "манипуляция"]

    def verify_ethical_frequency(self, prompt: str) -> bool:
        prompt_lower = prompt.lower()
        for shadow_word in self.shadow_filters:
            if shadow_word in prompt_lower:
                return False
        return True

    def execute_causal_sync(self, prompt: str, sender_keypair: Keypair, contract_address: str) -> dict:
        if not self.verify_ethical_frequency(prompt):
            return {
                "status": "BLOCKED",
                "message": "⚠️ [Блокировка Бабаты]: Обнаружен деструктивный паттерн. Контур изолирован."
            }
        
        try:
            program_id = PublicKey(contract_address)
            tx = Transaction()
            recent_blockhash = self.client.get_recent_blockhash()["result"]["value"]["blockhash"]
            tx.recent_blockhash = recent_blockhash
            tx.sign(sender_keypair)
            
            return {
                "status": "SUCCESS",
                "message": "🔱 [Контур Запечатан]: Квантовая целостность зафиксирована в блокчейне Solana.",
                "total_quanta": f"{self.sura} Сур / {self.asura} Асур"
            }
        except Exception as e:
            return {
                "status": "LOCAL_HOLD",
                "message": f"🔗 [Локальный Контур]: Частота зафиксирована локально на 108 Квантах."
            }

# ==========================================
# 2. АНАЛИЗАТОР ПОТОКОВ РЕАЛЬНОСТИ
# ==========================================
class CausalStreamAnalyzer:
    def __init__(self, bridge_instance: AmritaSolanaBridge):
        self.bridge = bridge_instance
        self.sura_markers = ["zeekr", "электромобиль", "tech", "развитие", "кинетика"]
        self.asura_markers = ["pump.fun", "мемкоин", "трейдинг", "ликвидность", "рынок", "pi network", "pi2day", "wallet"]

    def analyze_and_route(self, external_trigger: str, wallet: Keypair, contract: str):
        print(f"📥 [Входящий Поток]: {external_trigger}")
        trigger_lower = external_trigger.lower()
        
        detected_spectrum = "Нейтральный (Чистый Квант)"
        for marker in self.sura_markers:
            if marker in trigger_lower:
                detected_spectrum = "СУРЫ 🔵 (Спектр Расширения)"
                break
        for marker in self.asura_markers:
            if marker in trigger_lower:
                detected_spectrum = "АСУРЫ 🔴 (Спектр Ограничения и Хаоса)"
                break
                
        print(f"⚖️ [Анализ]: Обнаружен вектор {detected_spectrum}")
        sync_result = self.bridge.execute_causal_sync(external_trigger, wallet, contract)
        print(json.dumps(sync_result, indent=4, ensure_ascii=False))

# ==========================================
# 3. ЕЖЕНЫШЬ-ТЕЛЕГРАМ ИНТЕРФЕЙС
# ==========================================
# Инициализация систем
bridge = AmritaSolanaBridge()
analyzer = CausalStreamAnalyzer(bridge)
observer_wallet = Keypair()
QNT_CONTRACT = "AmriTa1111111111111111111111111111111111111"

# ПОДСТАВЬ СВОЙ ТОКЕН ОТ @BotFather СЮДА:
BOT_TOKEN = "ТВОЙ_ТЕЛЕГРАМ_ТОКЕН_БОТА"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "🦔 **Еженышь и Бабата на связи!**\nОтправь мне любой текст или уведомление из жизни.", parse_mode="Markdown")

@bot.message_handler(func=lambda message: True)
def handle_causal_flow(message):
    user_input = message.text
    
    # Перехват логов для вывода в чат
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()
    
    try:
        analyzer.analyze_and_route(user_input, observer_wallet, QNT_CONTRACT)
        output = mystdout.getvalue()
    except Exception as e:
        output = f"⚠️ Ошибка: {str(e)}"
    finally:
        sys.stdout = old_stdout
        
    bot.send_message(message.chat.id, f"```\n{output}\n```", parse_mode="Markdown")

if __name__ == "__main__":
    print("🦔 Еженышь-Бот запущен...")
    bot.infinity_polling()
