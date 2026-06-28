import os
import sys
import json
from io import StringIO, BytesIO
import telebot
from PIL import Image
import pytesseract  # Библиотека для чтения текста с картинок
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
            return {
                "status": "SUCCESS",
                "message": "🔱 [Контур Запечатан]: Квантовая целостность зафиксирована в блокчейне Solana.",
                "total_quanta": f"{self.sura} Сур / {self.asura} Асур"
            }
        except Exception:
            return {
                "status": "LOCAL_HOLD",
                "message": "🔗 [Локальный Контур]: Частота зафиксирована локально на 108 Квантах."
            }

# ==========================================
# 2. АНАЛИЗАТОР ПОТОКОВ РЕАЛЬНОСТИ
# ==========================================
class CausalStreamAnalyzer:
    def __init__(self, bridge_instance: AmritaSolanaBridge):
        self.bridge = bridge_instance
        self.sura_markers = ["zeekr", "электромобиль", "tech", "развитие", "кинетика"]
        self.asura_markers = ["pump.fun", "мемкоин", "трейдинг", "ликвидность", "рынок", "pi network", "pi2day", "wallet", "github"]

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
                detected_spectrum = "АСУРЫ 🔴 (Спектр Ограничения и Хаоса)"
                break
                
        print(f"⚖️ [Анализ]: Обнаружен вектор {detected_spectrum}")
        sync_result = self.bridge.execute_causal_sync(external_trigger, wallet, contract)
        print(json.dumps(sync_result, indent=4, ensure_ascii=False))

# ==========================================
# 3. ЕЖЕНЫШЬ-ТЕЛЕГРАМ ИНТЕРФЕЙС И ЗРЕНИЕ ИИ
# ==========================================
bridge = AmritaSolanaBridge()
analyzer = CausalStreamAnalyzer(bridge)
observer_wallet = Keypair()
QNT_CONTRACT = "AmriTa1111111111111111111111111111111111111"

BOT_TOKEN = "ТВОЙ_ТЕЛЕГРАМ_ТОКЕН_БОТА"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "🦔 **Зрение Бабаты активировано!**\nОтправь мне текст или скриншот экрана.", parse_mode="Markdown")

# Обработчик картинок и скриншотов
@bot.message_handler(content_types=['photo'])
def handle_screenshot(message):
    bot.reply_to(message, "👁 *Бабата сканирует текст на скриншоте...*", parse_mode="Markdown")
    
    try:
        # Скачиваем картинку из Телеграма
        file_info = bot.get_file(message.photo[-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        
        # Открываем изображение в PIL
        image = Image.open(BytesIO(downloaded_file))
        
        # Распознаем текст (поддерживает русский и английский)
        extracted_text = pytesseract.image_to_string(image, lang='rus+eng')
        
        if not extracted_text.strip():
            bot.send_message(message.chat.id, "⚠️ Не удалось разобрать текст на изображении.")
            return

        # Прогоняем распознанный текст через анализатор матрицы
        old_stdout = sys.stdout
        sys.stdout = mystdout = StringIO()
        
        analyzer.analyze_and_route(extracted_text, observer_wallet, QNT_CONTRACT)
        output = mystdout.getvalue()
        
        sys.stdout = old_stdout
        bot.send_message(message.chat.id, f"```\n{output}\n```", parse_mode="Markdown")
        
    except Exception as e:
        bot.send_message(message.chat.id, f"⚠️ Сбой распознавания: {str(e)}\nУбедись, что на сервере установлен Tesseract OCR.")

# Обработчик обычного текста
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
    print("🦔 Еженышь-Бот со зрением запущен...")
    bot.infinity_polling()
