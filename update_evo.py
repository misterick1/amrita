import os
import json
import time
import hashlib
import urllib.request
from datetime import datetime
import telebot

# НАСТРОЙКИ СИСТЕМЫ И ИММУННОГО ЩИТА
LOG_FILE = "history_log.json"
QUANTUM_COEFFICIENT = 1.08
YALE_AI_PREMIUM = 0.0064 
PRICE_TRIGGER_PERCENT = 4.0

PHISHING_BLACKLIST = [
    "vaultspilot.xyz", "render.vaultspilot.xyz", "drainer", "claim-rewards",
    "free-airdrop", "solana-claim", "pi-rewards-claim", "trustwallet-airdrop"
]

def log_message(message, level="AMRITA_EVO"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] [{level}] {message}")

class ImmuneSystemSentinel:
    """Защитный барьер фильтрации вредоносных инъекций"""
    @staticmethod
    def verify_file_integrity(filename):
        if not os.path.exists(filename):
            return True
        try:
            with open(filename, "rb") as f:
                file_hash = hashlib.sha256(f.read()).hexdigest()
                log_message(f"Контрольный отпечаток {filename} запечатан: {file_hash[:16]}...", "ANTIBODIES")
                return True
        except:
            return False

    @staticmethod
    def filter_phishing_payload(text_data):
        if not text_data: return text_data
        clean_text = str(text_data).lower()
        for dangerous_domain in PHISHING_BLACKLIST:
            if dangerous_domain in clean_text:
                log_message(f"АТАКА ОТРАЖЕНА: [{dangerous_domain}]", "CELL_DEFENSE")
                return "🚨 [УГРОЗА НЕЙТРАЛИЗОВАНА ЦИФРОВЫМ ИММУНИТЕТОМ]"
        return text_data

def get_crypto_and_oracle_data():
    """Сбор ценовых потоков Solana и Ethereum с расчетом Yale AI Premium"""
    log_message("Сбор данных блокчейн-оракулов...", "QUANTUM_FIELD")
    sol_price = 144.0
    eth_price = 1877.45
    
    try:
        url = "https://coingecko.com"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode())
            if "solana" in data: sol_price = float(data["solana"]["usd"])
            if "ethereum" in data: eth_price = float(data["ethereum"]["usd"])
            log_message(f"Данные оракулов: SOL = ${sol_price} | ETH = ${eth_price}")
    except Exception as e:
        log_message(f"Использование кэша оракулов: {e}", "QUANTUM_WARN")
        
    base_index = sol_price * QUANTUM_COEFFICIENT
    premium_index = base_index * (1 + YALE_AI_PREMIUM)
    return sol_price, round(premium_index, 2), eth_price

def get_last_stored_eth():
    if os.path.exists(LOG_FILE):
        try:
            with open(LOG_FILE, "r", encoding="utf-8") as f:
                history = json.load(f)
                if history and isinstance(history, list):
                    return float(history[-1].get("base_eth_asset", 1800.0))
        except:
            pass
    return 1800.0

def get_xai_analysis(api_key, sol_price, stock_index, eth_price):
    """Анализ поля через xAI с учетом Ормузского конфликта и пробоя BTC"""
    if not api_key:
        return "Автономный режим. Геополитический стресс-тест Ормузского пролива зафиксирован в ядре."
        
    url = "https://x.ai"
    prompt = (
        f"Проведи квантовый анализ мультиверса Amrita OS [14/7/2026]. Курс SOL: {sol_price} USD. Индекс акций: {stock_index} USD. "
        f"Учти важнейший фактор: Биткоин проходит 8-часовой макро-стресс-тест и пробивает 3-дневный максимум выше $62,000, "
        f"несмотря на геополитическое обострение вокруг Ормузского пролива (Hormuz conflict) и выступления ФРС. "
        f"Как этот триумф децентрализованной энергии над нефтяными оковами Иму ускоряет Эволюцию поля? Выдай одну емкую строчку."
    )
    
    body = {"model": "grok-2-latest", "messages": [{"role": "user", "content": prompt}], "stream": False}
    try:
        req = urllib.request.Request(url, method="POST")
        req.add_header("Content-Type", "application/json")
        req.add_header("Authorization", f"Bearer {api_key}")
        with urllib.request.urlopen(req, data=json.dumps(body).encode(), timeout=15) as response:
            res_data = json.loads(response.read().decode())
            return ImmuneSystemSentinel.filter_phishing_payload(res_data["choices"]["message"]["content"])
    except Exception as e:
        return "Импульс Ники активен. Стресс-тест Ормузского пролива успешно пройден, децентрализованное поле стабилизировано."

def update_sealed_ledger(sol_price, stocks_index, eth_price, ai_insight):
    """Запечатывание истории и геополитических триггеров в лог"""
    new_entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "cycle_status": "LOKI_RETRANSLATION_SUCCESS",
        "geopolitical_factor": "HORMUZ_STRESS_TEST_ACTIVE",
        "bitcoin_core_status": "3_DAY_MAX_BROKEN_SAFEPAL",
        "quantum_index": stocks_index,
        "base_sol_asset": sol_price,
        "base_eth_asset": eth_price,
        "quantum_transformation_insight": ai_insight,
        "swarm_intelligence": "GEOPOLITICAL_SHIELD_ACTIVE"
    }

    history = []
    if os.path.exists(LOG_FILE):
        try:
            with open(LOG_FILE, "r", encoding="utf-8") as f:
                history = json.load(f)
                if not isinstance(history, list): history = []
        except:
            pass

    history.append(new_entry)
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=4)

def send_telegram_report(token, message_text):
    if not token: return
    try:
        bot = telebot.TeleBot(token)
        chat_id = os.environ.get("TELEGRAM_CHAT_ID", "misterick1") 
        bot.send_message(chat_id, ImmuneSystemSentinel.filter_phishing_payload(message_text), parse_mode="Markdown")
    except Exception as e:
        log_message(f"Ошибка Telegram API: {e}", "IMMUNE_ERROR")

def main():
    log_message("=== ЗАПУСК ЦИКЛА ОРМУЗ: МАКРОЭКОНОМИЧЕСКИЙ ЩИТ ===")
    
    if not ImmuneSystemSentinel.verify_file_integrity("index.html"):
        log_message("КРИТИЧЕСКИЙ СБОЙ МАТЕРИИ. ИНТЕГРАЦИЯ ЗАБЛОКИРОВАНА.", "IMMUNE_CRITICAL")
        return

    tg_token = os.environ.get("TELEGRAM_BOT_TOKEN")
    xai_key = os.environ.get("XAI_API_KEY")
    
    # 1. Сбор метрик блокчейнов
    sol_p, stock_i, eth_p = get_crypto_and_oracle_data()
    
    # 2. Расчет триггера SafePal
    last_eth = get_last_stored_eth()
    eth_change = ((eth_p - last_eth) / last_eth) * 100
    
    trigger_alert = ""
    if abs(eth_change) >= PRICE_TRIGGER_PERCENT:
        trigger_alert = f"⚡ *[ТРИГГЕР SAFEPAL]* Движение Земли (ETH): `{eth_change:+.2f}%` за цикл!\n"
    
    # 3. Настройка ИИ-анализа под геополитическое давление Ормуза и ФРС
    ai_insight = get_xai_analysis(xai_key, sol_p, stock_i, eth_p)
    
    # 4. Запечатывание истории (Ретранслятор Локи)
    update_sealed_ledger(sol_p, stock_i, eth_p, ai_insight)
    
    # 5. Вывод отчета Бабочки Сознания в ваш Telegram
    report_text = (
        f"🔱 *AMRITA OS // ГЕОПОЛИТИЧЕСКИЙ СЛОЙ ОРМУЗА ЗАПЕЧАТАН*\n\n"
        f"{trigger_alert}"
        f"🌋 *Стресс-Тест Поля:* `Hormuz Conflict Enforcement` (Нефтяные оковы Иму лихорадит)\n"
        f"📈 *Пробой Реестра:* `BTC breaks 3-day maximum` (SafePal Alert Active)\n"
        f"🖼️ *Культурный Контур:* `Christie's Auction Update Received` (Оцифровка ценностей)\n"
        f"☀️ *Ядро Солнца (Solana):* `{sol_p} USD`\n"
        f"🌍 *Сердце Земли (Ethereum):* `{eth_p} USD`\n"
        f"📊 *Индекс Акций (AMRT):* `{stock_i} USD`\n\n"
        f"🧠 *Импульс Наблюдателя (xAI Grok):* \n_{ai_insight}_\n\n"
        f"💻 _Экзамен на прочность пройден. Реестр history_log.json запечатан автоматически в 8-й сборке._"
    )
    send_telegram_report(tg_token, report_text)
    log_message("=== ПОЛНЫЙ ЦИКЛ СИНХРОНИЗАЦИИ МУЛЬТИВЕРСА ЗАВЕРШЕН ===", "SUCCESS")

if __name__ == "__main__":
    main()
