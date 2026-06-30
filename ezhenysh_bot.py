import os
import sys
import json
import shutil
import logging
import base64
from io import StringIO, BytesIO
from datetime import datetime
import telebot
import requests
from PIL import Image
import pytesseract

# Настройка базового логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("EzhenyshCore")

# =======================================================
# СОВМЕСТИМОСТЬ БИБЛИОТЕК SOLANA
# =======================================================
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

# =======================================================
# ДИНАМИЧЕСКИЙ ИМПОРТ ГЕО-МАТРИЦЫ БУЯНА
# =======================================================
try:
    from geo_buyan_matrix import GeoBuyanMatrix
except ImportError:
    class GeoBuyanMatrix:
        def __init__(self): 
            pass
        def scan_geo_frequency(self, text): 
            return {"frequency": "DEFAULT_5D", "status": "STABLE"}

# =======================================================
# 1. КВАНТОВОЕ ЯДРО И МОСТ SOLANA
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

    def check_observer_balance(self, wallet_keypair) -> float:
        """
        Проверка реального баланса кошелька Еженыша в Mainnet Solana.
        """
        try:
            pubkey = wallet_keypair.pubkey() if hasattr(wallet_keypair, 'pubkey') else wallet_keypair.public_key
            response = self.client.get_balance(pubkey)
            
            if hasattr(response, 'value'):
                lamports = response.value
            elif isinstance(response, dict) and 'result' in response:
                lamports = response['result']['value']
            else:
                lamports = int(response)
                
            sol_balance = lamports / 1000000000.0
            return sol_balance
        except Exception as e:
            logger.error(f"Ошибка подключения к Solana RPC: {e}")
            return 0.0

# =======================================================
# 2. АНАЛИЗАТОР И АВТО-ЛОГИРОВАНИЕ С GITHUB-СИНХРОНИЗАЦИЕЙ
# =======================================================
class CausalStreamAnalyzer:
    def __init__(self, bridge_instance: AmritaSolanaBridge):
        self.bridge = bridge_instance
        self.sura_markers = ["zeekr", "электромобиль", "технологии", "эволюция", "атма"]
        self.asura_markers = ["pump.fun", "мемкоин", "хайп", "competition", "trading", "live", "fomo", "solana", "бесплатно", "breakpoint", "ftmo", "oil"]
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
            print(f"Ошибка записи локального лога: {e}")

    def github_auto_commit_log(self):
        """
        Автоматический пуш логов напрямую в репозиторий через API GitHub.
        Подтягивает токен из ваших секретов окружения (DEVELOPER_WEB_TOKEN).
        """
        gh_token = os.getenv("DEVELOPER_WEB_TOKEN")
        repo = "misterick1/amrita"
        path = "history_log.json"
        url = f"https://github.com{repo}/contents/{path}"

        if not gh_token:
            print("⚠️ GitHub-токен (DEVELOPER_WEB_TOKEN) не обнаружен в окружении.")
            return

        headers = {
            "Authorization": f"token {gh_token}",
            "Accept": "application/vnd.github.v3+json"
        }

        sha = None
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                sha = response.json().get("sha")
        except Exception as e:
            print(f"Ошибка получения SHA лога с GitHub: {e}")

        try:
            with open(self.log_file, "rb") as f:
                content = base64.b64encode(f.read()).decode("utf-8")
        except Exception as e:
            print(f"Ошибка подготовки контента для GitHub: {e}")
            return

        payload = {
            "message": f"🧬 [Ezhenysh Auto-Loop]: Sync history_log.json | {datetime.now().strftime('%d/%m/%Y %H:%M')}",
            "content": content,
            "branch": "main"
        }
        if sha:
            payload["sha"] = sha

        try:
            res = requests.put(url, json=payload, headers=headers, timeout=10)
            if res.status_code in:
                print("🟢 [GITHUB AUTO-SYNC]: Логи успешно закоммичены в репозиторий на автомате!")
            else:
                print(f"🔴 Ошибка синхронизации с GitHub: {res.status_code} | {res.text}")
        except Exception as e:
            print(f"Исключение при запросе к GitHub API: {e}")

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
        self.github_auto_commit_log()

# =======================================================
# 3. ТЕЛЕГРАМ-ИНТЕРФЕЙС ЕЖЕНЫША И СИСТЕМНЫЕ ГЛОБАЛЫ
# =======================================================
bridge = AmritaSolanaBridge()
analyzer = CausalStreamAnalyzer(bridge)
observer_wallet = Keypair()
QNT_CONTRACT = "AmriTa1111111111111111111111111111111111111"

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "YOUR_TELEGRAM_BOT_TOKEN_HERE")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'status'])
def send_welcome(message):
    balance = bridge.check_observer_balance(observer_wallet)
    status_text = (
        "🦔 **Всевидящее Око Бабаты запущено**\n\n"
        f"🧬 Квантовая матрица: {bridge.total_quanta} Единиц\n"
        f"🔵 Спектр Суры: {bridge.sura} QNT\n"
        f"🔴 Спектр Асуры: {bridge.asura} QNT\n"
        f"🌌 Баланс Наблюдателя: `{balance} SOL`\n"
        f"⛓ Solana Контракт: `{QNT_CONTRACT}`\n\n"
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

        old_stdout = sys.stdout
        sys.stdout = mystdout = StringIO()
        
        analyzer.analyze_route(extracted_text)
        
        output = mystdout.getvalue()
        sys.stdout = old_stdout

        balance = bridge.check_observer_balance(observer_wallet)
        final_response = (
            f"📋 **Результаты OCR-Синхронизации:**\n\n```\n{output}\n```\n"
            f"💰 Текущий баланс сети: `{balance} SOL`"
        )
        bot.send_message(message.chat.id, final_response, parse_mode="Markdown")
    except Exception as e:
        bot.send_message(message.chat.id, f"⚠️ Ошибка каузального сбоя при обработке фото: {e}")

@bot.message_handler(func=lambda message: True)
def handle_text_flow(message):
    user_input = message.text
    
    old_stdout = sys.stdout
