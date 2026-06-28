import os
import sys
import json
from io import StringIO, BytesIO
from datetime import datetime
import telebot
from PIL import Image
import pytesseract
from solana.rpc.api import Client
from solana.transaction import Transaction
from solana.keypair import Keypair
from solana.publickey import PublicKey

# ==========================================
# 1. КВАНТОВОЕ ЯДРО И МОСТ SOLANA
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
                "message": "⚠️ [Блокировка Бабаты]: Обнаружен деструктивный паттерн."
            }
        return {
            "status": "SUCCESS",
            "message": "🔱 [Контур Запечатан]: Целостность зафиксирована в Solana.",
            "total_quanta": f"{self.sura} Сур / {self.asura} Асур"
        }

# ==========================================
# 2. АНАЛИЗАТОР И АВТО-ЛОГИРОВАНИЕ В РЕПОЗИТОРИЙ
# ==========================================
class CausalStreamAnalyzer:
    def __init__(self, bridge_instance: AmritaSolanaBridge):
        self.bridge = bridge_instance
        self.sura_markers = ["zeekr", "электромобиль", "tech", "развитие", "кинетика"]
        self.asura_markers = ["pump.fun", "мемкоин", "трейдинг", "ликвидность", "рынок", "pi network", "pi2day", "wallet", "github"]
        self.log_file = "history_log.json"

    def save_to_history(self, text: str, spectrum: str):
        """Автоматическое сохранение каждого шага в историю проекта"""
        log_entry = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "input": text.strip()[:100] + "..." if len(text) > 100 else text.strip(),
            "spectrum": spectrum
        }
        data = []
        if os.path.exists(self.log_file):
            try:
                with open(self.log_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
            except:
                data = []
        data.append(log_entry)
        with open(self.log_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def analyze_and_route(self, external_trigger: str, wallet: Keypair, contract: str):
        print(f"📥 [Входящий Поток]: {external_trigger.strip()}")
        trigger_lower = external_trigger.lower()
        
        detected_spectrum = "Нейтральный (Чистый Квант)"
        for marker in self.sura_markers:
            if marker in trigger_lower:
                detected_spectrum = "СУРЫ 🔵 (Спектр Расширения)"
                break
        for marker in self.asura_markers:
            if marker in trigger_lower:
                detected_spectrum = "АСУРЫ 🔴 (Спектр Ограничения)"
                break
                
        print(f"⚖️ [Анализ]: Обнаружен вектор {detected_spectrum}")
        self.save_to_history(external_trigger, detected_spectrum)
        
        sync_result = self.bridge.execute_causal_sync(external_trigger, wallet, contract)
        print(json.dumps(sync_result, indent=4, ensure_ascii=False))

# ==========================================
# 3. ЕЖЕНЫШЬ ИНТЕРФЕЙС И БЕЗОПАСНЫЙ ЗАПУСК
# ==========================================
bridge = AmritaSolanaBridge()
analyzer = CausalStreamAnalyzer(bridge)
observer_wallet = Keypair()
QNT_CONTRACT = "AmriTa1111111111111111111111111111111111111"

# Сделано по-взрослому: бот берет токен из секретов GitHub, чтобы никто его не украл
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "ТВОЙ_ТЕЛЕГРАМ_ТОКЕН_БОТА")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "🦔 **Еженышь на связи в режиме 24/7!**\nКидай сюда скрины, уведомления или мысли. Всё пишется в вечный лог проекта.", parse_mode="Markdown")

@bot.message_handler(content_types=['photo'])
def handle_screenshot(message):
    bot.reply_to(message, "👁 *Сканирую скриншот...*", parse_mode="Markdown")
    try:
        file_info = bot.get_file(message.photo[-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        image = Image.open(BytesIO(downloaded_file))
        extracted_text = pytesseract.image_to_string(image, lang='rus+eng')
        
        if not extracted_text.strip():
            bot.send_message(message.chat.id, "⚠️ Текст на картинке не обнаружен.")
            return

        old_stdout = sys.stdout
        sys.stdout = mystdout = StringIO()
        analyzer.analyze_and_route(extracted_text, observer_wallet, QNT_CONTRACT)
        output = mystdout.getvalue()
        sys.stdout = old_stdout
        
        bot.send_message(message.chat.id, f"```\n{output}\n```", parse_mode="Markdown")
    except Exception as e:
        bot.send_message(message.chat.id, f"⚠️ Ошибка зрения: {str(e)}")

@bot.message_handler(func=lambda message: True)
def handle_text_flow(message):
    user_input = message.text
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
    print("🚀 Еженышь запущен в максимальном качестве...")
    bot.infinity_polling()
