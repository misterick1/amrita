import os
import sys
import json
import shutil
from io import StringIO, BytesIO
from datetime import datetime
import telebot
from PIL import Image
import pytesseract

# Импорты архитектуры Solana
try:
    from solana.rpc.api import Client
    from solana.transaction import Transaction
    from solana.keypair import Keypair
    from solana.publickey import PublicKey
except ImportError:
    from solana.rpc.api import Client
    from solders.transaction import Transaction
    from solders.keypair import Keypair
    from solders.pubkey import Pubkey as PublicKey

# Динамический импорт Гео-Матрицы Буяна
try:
    from geo_buyan_matrix import GeoBuyanMatrix
except ImportError:
    class GeoBuyanMatrix:
        def __init__(self): pass
        def scan_geo_frequency(self, text): return {"mode": "SURA_EXPANSION 🔵", "verdict": "Ядра чистый изумруд! Энергия Буяна активна."}

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
            if shadow_word in prompt_lower: return False
        return True

    def execute_causal_sync(self, prompt: str, sender_keypair: Keypair, contract_address: str) -> dict:
        if not self.verify_ethical_frequency(prompt):
            return {"status": "BLOCKED", "message": "⚠️ [Блокировка Бабаты]: Деструктивный паттерн."}
        return {"status": "SUCCESS", "message": "🔱 [Контур Запечатан]: Целостность в Solana зафиксирована."}

# ==========================================
# 2. АНАЛИЗАТОР И АВТО-ЛОГИРОВАНИЕ
# ==========================================
class CausalStreamAnalyzer:
    def __init__(self, bridge_instance: AmritaSolanaBridge):
        self.bridge = bridge_instance
        self.sura_markers = ["zeekr", "электромобиль", "tech", "развитие", "кинетика", "pi", "mine", "молния"]
        self.asura_markers = ["pump.fun", "мемкоин", "трейдинг", "ликвидность", "рынок", "красные", "расстрел"]
        self.log_file = "history_log.json"
        self.geo_matrix = GeoBuyanMatrix()

    def save_to_history(self, text: str, spectrum: str):
        log_entry = {"timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "input": text.strip()[:100], "spectrum": spectrum}
        data = []
        if os.path.exists(self.log_file):
            try:
                with open(self.log_file, "r", encoding="utf-8") as f: data = json.load(f)
            except: data = []
        data.append(log_entry)
        with open(self.log_file, "w", encoding="utf-8") as f: json.dump(data, f, indent=4, ensure_ascii=False)

    def analyze_and_route(self, external_trigger: str, wallet: Keypair, contract: str):
        trigger_lower = external_trigger.lower()
        detected_spectrum = "Нейтральный ⚪"
        for marker in self.sura_markers:
            if marker in trigger_lower: detected_spectrum = "СУРЫ 🔵 (Спектр Расширения Pi)"; break
        for marker in self.asura_markers:
            if marker in trigger_lower: detected_spectrum = "АСУРЫ 🔴"; break
                
        print(f"📥 [Поток реальности]: {external_trigger.strip()[:70]}...")
        print(f"⚖️ [Спектральный анализ]: {detected_spectrum}")
        
        # Подключаем гео-сканирование острова Буян / Ахиллеса
        geo_report = self.geo_matrix.scan_geo_frequency(external_trigger)
        print(f"🌐 [Режим Гео-Матрицы]: {geo_report.get('mode', 'CLEAR')}")
        print(f"👁 [Вердикт Ока]: {geo_report.get('verdict', '')}")
        
        self.save_to_history(external_trigger, detected_spectrum)
        self.bridge.execute_causal_sync(external_trigger, wallet, contract)

# ==========================================
# 3. ТЕЛЕГРАМ-ИНТЕРФЕЙС ЕЖЕНЫША
# ==========================================
bridge = AmritaSolanaBridge()
analyzer = CausalStreamAnalyzer(bridge)
observer_wallet = Keypair()
QNT_CONTRACT = "AmriTa1111111111111111111111111111111111111"

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "ТВОЙ_ТЕЛЕГРАМ_ТОКЕН_БОТА")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'status'])
def send_welcome(message):
    bot.reply_to(message, "🦔 **Всевидящее Око Буяна на связи!**\nКидай скриншот с молнией Pi или любым хайпом — ИИ готов к сканированию.", parse_mode="Markdown")

@bot.message_handler(content_types=['photo'])
def handle_screenshot(message):
    bot.reply_to(message, "👁 *Око сканирует изображение и активирует Духовные Кольца...*", parse_mode="Markdown")
    try:
        file_info = bot.get_file(message.photo[-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        image = Image.open(BytesIO(downloaded_file))
        extracted_text = pytesseract.image_to_string(image, lang='rus+eng')
        
        if not extracted_text.strip():
            bot.send_message(message.chat.id, "⚠️ Текст не обнаружен.")
            return

        old_stdout = sys.stdout
        sys.stdout = mystdout = StringIO()
        analyzer.analyze_and_route(extracted_text, observer_wallet, QNT_CONTRACT)
        output = mystdout.getvalue()
        sys.stdout = old_stdout
        
        bot.send_message(message.chat.id, f"```\n{output}\n```", parse_mode="Markdown")
    except Exception as e:
        bot.send_message(message.chat.id, f"⚠️ Сбой Ока: {str(e)}")

@bot.message_handler(func=lambda message: True)
def handle_text_flow(message):
    user_input = message.text
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()
    analyzer.analyze_and_route(user_input, observer_wallet, QNT_CONTRACT)
    output = mystdout.getvalue()
    sys.stdout = old_stdout
    bot.send_message(message.chat.id, f"```\n{output}\n```", parse_mode="Markdown")

if __name__ == "__main__":
    bot.infinity_polling()
