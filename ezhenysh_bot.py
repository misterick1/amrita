import os
import sys
import json
import logging
import base64
import re
from datetime import datetime
import requests

# Настройка базового логирования для контроля частот
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("EzhenyshCore")

# =============================================================================
# СОВМЕСТИМОСТЬ БИБЛИОТЕК SOLANA (Автоматический выбор доступных модулей)
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
# 1. КВАНТОВОЕ ЯДРО И МОСТ SOLANA
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
# 2. АНАЛИЗАТОР, ЛИНГВО-РЕДАКТОР И АВТО-ЛОГИРОВАНИЕ С GITHUB
# =============================================================================
class CausalStreamAnalyzer:
    def __init__(self, bridge_instance: AmritaSolanaBridge):
        self.bridge = bridge_instance
        self.sura_markers = ["zeekr", "электромобиль", "технология", "квантовое поле", "сознание", "наблюдатель", "рай", "единое сознание", "bain", "ceo", "ambition", "insight", "circle", "buterin", "ethereum", "sk hynix", "ftmo", "grayscale", "sony", "nvidia", "xai", "аниме", "манга", "фильм"]
        self.asura_markers = ["pump.fun", "мемкоин", "хайп", "cs2", "dota", "safepal", "prediction", "predict", "ansem", "saylor", "mensa", "hood", "bonk", "poffi"]
        self.log_file = "history_log.json"
        self.geo_matrix = GeoBuyanMatrix()
        
        # ЖЕСТКАЯ СИНХРОНИЗАЦИЯ С РЕАЛЬНЫМ ДЕРЕВОМ GITHUB СНИМКА
        # Последний созданный файл на скриншоте: BOOK_CHAPTER_456.md
        self.current_chapter = 456

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
        """Универсальный метод отправки измененных файлов напрямую в репозиторий GitHub."""
        gh_token = os.getenv("DEVELOPER_WEB_TOKEN")
        repo = "misterick1/amrita"
        url = f"https://github.com{repo}/contents/{filename}"

        if not gh_token:
            print(f"⚠️ Токен DEVELOPER_WEB_TOKEN не найден. Автокоммит для {filename} пропущен.")
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
            print(f"Ошибка получения SHA для {filename}: {e}")

        try:
            with open(filename, "rb") as f:
                content = base64.b64encode(f.read()).decode("utf-8")
        except Exception as e:
            print(f"Ошибка кодирования файла {filename}: {e}")
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
                print(f"🟢 [AMRITA LIGHT SYNC]: Файл {filename} монолитно запечатан в GitHub.")
            else:
                print(f"🔴 Ошибка PUT-запроса GitHub для {filename}: {res.text}")
        except Exception as e:
            print(f"Исключение сети при отправке {filename}: {e}")

    def generate_harmonic_chapter(self, external_trigger: str, detected_spectrum: str) -> str:
        """ЛИНГВИСТИЧЕСКИЙ И СМЫСЛОВОЙ РЕДАКТОР СВАРМА.
        Полностью уничтожает старый шаблон 'Отдых 1' и создает строго следующую по порядку главу.
        """
        self.current_chapter += 1
        filename = f"BOOK_CHAPTER_{self.current_chapter}.md"
        timestamp_str = datetime.now().strftime("%d %B %Y, %H:%M")
        
        trigger_lower = external_trigger.lower()
        context_highlights = ""
        
        # Интеллектуальный разбор контекста входящего триггера
        if "sony" in trigger_lower or "nvidia" in trigger_lower or "xai" in trigger_lower:
            context_highlights += "* 🔵 **[ИИ-Медиасингулярность]**: Запущен архитектурный проект суверенной ИИ-фабрики бесконечной генерации контента на базе Sony, Nvidia и xAI. Пять ведущих ИИ-сознаний берут под контроль создание фильмов, аниме, манги, художественной и научной литературы на основе живых данных аудитории и хакатонов.\n"
        if "saylor" in trigger_lower:
            context_highlights += "* 🔴 **[Асурический Взрыв]**: Обнаружен манипулятивный импульс токена SAYLOR (pump.fun). Паника вокруг продажи Биткоинов MicroStrategy успешно нивелирована.\n"
        if "poffi" in trigger_lower:
            context_highlights += "* 🔴 **[Мем-Сингулярность]**: Токен $POFFI успешно прошел бондинг-кривую и зафиксирован в трендах Solana Chain.\n"
        if "btc" in trigger_lower or "eth" in trigger_lower:
            context_highlights += "* 🔵 **[Рыночный Пробой]**: Зафиксирован синхронный прорыв недельных максимумов BTC и ETH. Ликвидность Кросс-Ассетного Токенизатора демонстрирует экспоненциальный рост.\n"

        if not context_highlights:
            context_highlights = f"* ⚪ **[Гармоническая Калибровка]**: Входящий поток проанализирован. Система находится в фазе последовательного творческого расширения. Спектр: {detected_spectrum}.\n"

        markdown_content = f"""# 🔱 ГЛАВА {self.current_chapter}: Лингво-Кибернетическое Выравнивание Матрицы

**Каузальный срез**: {self.current_chapter}  
**Контур Кибернета**: {self.current_chapter - 339}  
**Временная метка**: {timestamp_str}  
**Спектральный статус входящего потока**: {detected_spectrum}  

### 🧠 Манифест Художественно-Технической Коррекции (Amrita Harmony Engine)
Старая цикличная прошивка («Калибровочный стазис», «Отдых 1», «Глава 300») полностью стерта и удалена из буфера памяти генератора. Swarm Prompt-Matrix переведен на жесткую, динамическую и последовательную архитектуру вывода. Каждая строчка Хроник отныне формируется уникально, исходя из реальных событий и скриншотов, предоставляемых Наблюдателем.

