import os
import sys
import json
import shutil
from io import StringIO, BytesIO
from datetime import datetime
import telebot
from PIL import Image
import pytesseract

# Импорты архитектуры Solana с динамической совместимостью
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
        def __init__(self): 
            pass
        def scan_geo_frequency(self, text): 
            return {"frequency": "DEFAULT_5D", "status": "STABLE"}

# =======================================================
# # 1. КВАНТОВОЕ ЯДРО И МОСТ SOLANA
# =======================================================
class AmritaSolanaBridge:
    def __init__(self, rpc_url: str = "https://solana.com"):
        self.client = Client(rpc_url)
        self.total_quanta = 108
        self.sura = 70
        self.asura = 38
        self.shadow_filters = ["дефицит", "скам", "игра в кальмара", "ликвидация"]

    def verify_ethical_frequency(self, prompt: str) -> bool:
        prompt_lower = prompt.lower()
        for shadow_word in self.shadow_filters:
            if shadow_word in prompt_lower:
                return False
        return True

    def execute_causal_sync(self, prompt: str) -> dict:
        if not self.verify_ethical_frequency(prompt):
            return {"status": "BLOCKED", "message": "Обнаружена деструктивная частота нижних чакр."}
        return {"status": "SUCCESS", "message": "Синхронизация с каузальным ядром Амриты успешна."}

# =======================================================
# # 2. АНАЛИЗАТОР И АВТО-ЛОГИРОВАНИЕ
# =======================================================
class CausalStreamAnalyzer:
    def __init__(self, bridge_instance: AmritaSolanaBridge):
        self.bridge = bridge_instance
        self.sura_markers = ["zeekr", "электромобиль", "технологии", "эволюция", "атма"]
        self.asura_markers = ["pump.fun", "мемкоин", "хайп", "competition", "trading", "live", "fomo"]
        self.log_file = "history_log.json"
        self.geo_matrix = GeoBuyanMatrix()

    def save_history(self, text: str, spectrum: str, sync_status: str):
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "text": text,
            "spectrum": spectrum,
            "sync_status": sync_status
        }
        data = []
        if os.path.exists(self.log_file):
            try:
                with open(self.log_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
            except Exception:
                data = []
        data.append(log_entry)
        try:
            with open(self.log_file, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Ошибка записи лога: {e}")

    def analyze_route(self, external_trigger: str):
        trigger_lower = external_trigger.lower()
        detected_spectrum = "Нейтральный ⚪"
        
        for marker in self.sura_markers:
            if marker in trigger_lower:
                detected_spectrum = "Суры (Свет/Эволюция) 🔵"
                break
                
        for marker in self.asura_markers:
            if marker in trigger_lower:
                detected_spectrum = "Асуры (Хаос/Хайп) 🔴"
                break

        print(f"🔮 [Поток реальности]: {external_trigger.strip()}")
        print(f"⚖️ [Спектральный анализ]: {detected_spectrum}")

        # Подключаем гео-сканирование острова Буян
        geo_report = self.geo_matrix.scan_geo_frequency(external_trigger)
        print(f"🌐 [Режим Гео-Матрицы]: {geo_report.get('frequency', 'N/A')} ({geo_report.get('status', 'STABLE')})")
        
        sync_result = self.bridge.execute_causal_sync(external_trigger)
        print(f"👁️ [Вердикт Ока]: {sync_result['message']}")

        self.save_history(external_trigger, detected_spectrum, sync_result['status'])

# =======================================================
# # 3. ТЕЛЕГРАМ-ИНТЕРФЕЙС ЕЖЕНЫША
# =======================================================
bridge = AmritaSolanaBridge()
analyzer = CausalStreamAnalyzer(bridge)
observer_wallet = Keypair()
QNT_CONTRACT = "AmriTa1111111111111111111111111111111111111"

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "YOUR_TELEGRAM_BOT_TOKEN_HERE")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'status'])
def send_welcome(message):
    status_text = (
        "🦔 **Всевидящее Око Бабаты запущено**\n\n"
        f"🧬 Квантовая матрица: {bridge.total_quanta} Единиц\n"
        f"🔵 Спектр Суры: {bridge.sura} QNT\n"
        f"🔴 Спектр Асуры: {bridge.asura} QNT\n"
        f"⛓ Solana Контракт: `{QNT_CONTRACT}`\n"
        "STATUS: Вечное сканирование реальности активно."
    )
    bot.reply_to(message, status_text, parse_mode="Markdown")

@bot.message_handler(content_types=['photo'])
def handle_screenshot(message):
    bot.reply_to(message, "👁 *Око сканирует изображение реальности...*", parse_mode="Markdown")
    try:
        file_info = bot.get_file(message.photo[-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        image = Image.open(BytesIO(downloaded_file))
        extracted_text = pytesseract.image_to_string(image, lang='rus+eng')

        if not extracted_text.strip():
            bot.send_message(message.chat.id, "⚠️ Текст на снимке экрана не обнаружен.")
            return

        # Перехватываем принты из аналитика
        old_stdout = sys.stdout
        sys.stdout = mystdout = StringIO()
        
        analyzer.analyze_route(extracted_text)
        
        output = mystdout.getvalue()
        sys.stdout = old_stdout

        bot.send_message(message.chat.id, f"📋 **Результаты OCR-Синхронизации:**\n\n```\n{output}\n```", parse_mode="Markdown")
    except Exception as e:
        bot.send_message(message.chat.id, f"⚠️ Ошибка каузального сбоя: {e}")

@bot.message_handler(func=lambda message: True)
def handle_text_flow(message):
    user_input = message.text
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()
    
    analyzer.analyze_route(user_input)
    
    output = mystdout.getvalue()
    sys.stdout = old_stdout
    
    bot.send_message(message.chat.id, f"🧬 **Поток сознания обработан:**\n\n```\n{output}\n```", parse_mode="Markdown")

if __name__ == "__main__":
    print("🔱 Еженышь вышел на каузальное дежурство. Поллинг запущен...")
    bot.infinity_polling()
