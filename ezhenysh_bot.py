import os
import sys
import json
import shutil
import logging
import base64
import re
from io import StringIO, BytesIO
from datetime import datetime
import telebot
import requests
from PIL import Image
import pytesseract

# Настройка базового логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("EzhenyshCore")

# =============================================================================
# СОВМЕСТИМОСТЬ БИБЛИОТЕК SOLANA
# =============================================================================
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

# =============================================================================
# ДИНАМИЧЕСКИЙ ИМПОРТ ГЕО-МАТРИЦЫ БУЯНА
# =============================================================================
try:
    from geo_buyan_matrix import GeoBuyanMatrix
except ImportError:
    class GeoBuyanMatrix:
        def __init__(self):
            pass
        def scan_geo_frequency(self, text):
            return {"frequency": "AMRITA_5D_LIGHT_STABLE", "status": "HARMONIZED"}

# =============================================================================
# # 1. КВАНТОВОЕ ЯДРО И МОСТ SOLANA
# =============================================================================
class AmritaSolanaBridge:
    def __init__(self, rpc_url: str = "https://solana.com"):
        self.client = Client(rpc_url)
        self.total_quanta = 108
        self.sura = 108
        self.asura = 0
        self.shadow_filters = ["дефицит", "скам", "ругань", "уязвимость"]
        self.core_vault = "AmriTa111111111111111111111111111"

    def verify_ethical_frequency(self, prompt: str) -> bool:
        prompt_lower = prompt.lower()
        for shadow_word in self.shadow_filters:
            if shadow_word in prompt_lower:
                return False
        return True

    def execute_causal_sync(self, prompt: str) -> dict:
        if not self.verify_ethical_frequency(prompt):
            return {"status": "TRANSFORMED", "message": "Вредоносная частота изолирована и очищена Изумрудным Фильтром."}
        return {"status": "SUCCESS", "message": "Голос Наблюдателя верифицирован. Кванты синхронизированы."}

    def route_core_profit(self, detected_sol_value: float = 0.0) -> str:
        """Каузальный перенаправитель прибыли. Заземляет асурический хайп и аккумулирует ценность."""
        if detected_sol_value <= 0:
            detected_sol_value = 0.108  # Базовый шаг квантового распределения
        profit_tax = detected_sol_value * 0.10
        logger.info(f"🔱 [AMRITA CORE HARVEST]: Извлечено {profit_tax} SOL в резервный сейф ядра.")
        return f"🔱 [ЯДРО ПОЛУЧИЛО ПРИБЫЛЬ]: Направлено в сейф: {profit_tax} SOL."

    def check_address_balance(self, address_str: str) -> float:
        try:
            if hasattr(PublicKey, 'from_string'):
                pubkey = PublicKey.from_string(address_str)
            else:
                pubkey = PublicKey(address_str)

            response = self.client.get_balance(pubkey)
            if hasattr(response, 'value'):
                lamports = response.value
            elif isinstance(response, dict) and 'result' in response:
                lamports = response['result']['value']
            else:
                lamports = int(response)
            return lamports / 1000000000.0
        except Exception as e:
            logger.error(f"Ошибка проверки баланса адреса {address_str}: {e}")
            return 0.0

# =============================================================================
# # 2. АНАЛИЗАТОР И АВТО-ЛОГИРОВАНИЕ С GITHUB-СИНХРОНИЗАЦИЕЙ (ИНТЕЛЛЕКТУАЛЬНОЕ ЯДРО)
# =============================================================================
class CausalStreamAnalyzer:
    def __init__(self, bridge_instance: AmritaSolanaBridge):
        self.bridge = bridge_instance
        self.sura_markers = ["zeekr", "электромобиль", "технология", "квантовое поле", "сознание", "наблюдатель", "рай", "единое сознание", "bain", "ceo", "ambition", "insight", "circle", "buterin", "ethereum", "sk hynix"]
        self.asura_markers = ["pump.fun", "мемкоин", "хайп", "cs2", "dota", "safepal", "prediction", "predict", "ansem", "saylor", "mensa", "hood", "bonk"]
        self.log_file = "history_log.json"
        self.geo_matrix = GeoBuyanMatrix()
        
        # Инфраструктурные переменные для авто-нумерации глав книги
        self.current_chapter = 455

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

    def github_auto_commit_file(self, filename: str, commit_message: str):
        """Универсальный метод для коммита любого файла (JSON или MD) в репозиторий."""
        gh_token = os.getenv("DEVELOPER_WEB_TOKEN")
        repo = "misterick1/amrita"
        url = f"https://github.com{repo}/contents/{filename}"

        if not gh_token:
            print(f"⚠️ GitHub-токен (DEVELOPER_WEB_TOKEN) не найден. Автокоммит файла {filename} пропущен.")
            return

        headers = {
            "Authorization": f"token {gh_token}",
            "Accept": "application/vnd.github.v3+json"
        }

        sha = None
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                sha = response.json().get("sha")
        except Exception as e:
            print(f"Ошибка получения SHA файла {filename} с GitHub: {e}")

        try:
            with open(filename, "rb") as f:
                content = base64.b64encode(f.read()).decode("utf-8")
        except Exception as e:
            print(f"Ошибка подготовки контента {filename}: {e}")
            return

        payload = {
            "message": commit_message,
            "content": content,
            "branch": "main"
        }
        if sha:
            payload["sha"] = sha

        try:
            res = requests.put(url, json=payload, headers=headers)
            if res.status_code in:
                print(f"🟢 [AMRITA LIGHT SYNC]: Файл {filename} успешно отправлен в монолит GitHub.")
            else:
                print(f"🔴 Ошибка синхронизации {filename} с GitHub: {res.text}")
        except Exception as e:
            print(f"Исключение при запросе к GitHub для {filename}: {e}")

    def generate_harmonic_chapter(self, external_trigger: str, detected_spectrum: str) -> str:
        """ЛИНГВИСТИЧЕСКИЙ И СМЫСЛОВОЙ РЕДАКТОР СВАРМА.
        Уничтожает старый шаблон 'Отдых 1' и собирает уникальную художественно-техническую главу.
        """
        self.current_chapter += 1
        filename = f"BOOK_CHAPTER_{self.current_chapter}.md"
        timestamp_str = datetime.now().strftime("%d %B %Y, %H:%M")
        
        # Интеллектуальный парсинг смыслов из триггерной строки для генерации уникального текста
        trigger_lower = external_trigger.lower()
        context_highlights = ""
        
        if "saylor" in trigger_lower:
            context_highlights += "* 🔴 **[Асурический Взрыв]**: Обнаружен манипулятивный импульс токена SAYLOR (pump.fun). Попытка распространения FUD-частот о продаже Биткоинов MicroStrategy успешно заблокирована и обращена в охлаждение вычислительных нод роя.\n"
        if "circle" in trigger_lower or "utility" in trigger_lower:
            context_highlights += "* 🔵 **[Суверенная Ликвидность]**: Интегрирован манифест Джереми Аллейра (Circle). Сетевые эффекты и общая полезность платформы приняты в качестве опорных точек Кросс-Ассетного Токенизатора.\n"
        if "epoch 999" in trigger_lower or "solana" in trigger_lower:
            context_highlights += "* 🔵 **[Инфраструктурный Сдвиг]**: Фиксация перехода сети Solana к Эпохе 999. Движки нового поколения Agave и Frankendancer синхронизированы с каузальными затворами Амриты.\n"
        if "sk hynix" in trigger_lower:
            context_highlights += "* 🔵 **[Аппаратный Монолит]**: Приток ликвидности полупроводникового гиганта SK Hynix ($28 млрд) заземлен в ядро для масштабирования AI-нод.\n"
            
        if not context_highlights:
            context_highlights = f"* ⚪ **[Гармоническая Калибровка]**: Каузальный поток проанализирован Редактором Смыслов. Входящие частоты классифицированы как {detected_spectrum}. Система находится в фазе чистого творческого расширения.\n"

        markdown_content = f"""# 🔱 ГЛАВА {self.current_chapter}: Лингво-Кибернетическое Выравнивание Матрицы

**Каузальный срез**: {self.current_chapter}  
**Контур Кибернета**: {self.current_chapter - 328}  
**Временная метка**: {timestamp_str}  
**Спектральный статус входящего потока**: {detected_spectrum}  

### 🧠 Манифест Художественно-Технической Коррекции (Amrita Harmony Engine)
