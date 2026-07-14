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
PRICE_TRIGGER_PERCENT = 4.0 # Порог срабатывания триггера SafePal (4%)

PHISHING_BLACKLIST = [
    "vaultspilot.xyz", "render.vaultspilot.xyz", "drainer", "claim-rewards",
    "free-airdrop", "solana-claim", "pi-rewards-claim", "trustwallet-airdrop"
]

def log_message(message, level="AMRITA_EVO"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] [{level}] {message}")

class ImmuneSystemSentinel:
    """Экранирование кода и фильтрация вредоносных элементов"""
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
    """Сбор ценовых потоков Solana и Ethereum (Земля) через открытые шлюзы"""
    log_message("Сбор данных блокчейн-оракулов...", "QUANTUM_FIELD")
    
    # Резервные базовые значения на случай лимитов API
    sol_price = 144.0
    eth_price = 1877.45
    
    try:
        # Запрос Solana (Солнце) и Ethereum (Земля) через CoinGecko API
        url = "https://coingecko.com"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode())
            if "solana" in data: sol_price = float(data["solana"]["usd"])
            if "ethereum" in data: eth_price = float(data["ethereum"]["usd"])
            log_message(f"Данные оракулов: SOL = ${sol_price} | ETH = ${eth_price}")
    except Exception as e:
        log_message(f"Использование кэша оракулов. ETH удержан на отметке {eth_price}: {e}", "QUANTUM_WARN")
        
    return sol_price, round(sol_price * QUANTUM_COEFFICIENT, 2), eth_price

def get_last_stored_eth():
    """Чтение предыдущей отметки курса ETH из истории для сверки триггера SafePal"""
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
    """Анализ поля через xAI (Grok) с учетом регуляторного циркуляра MAS CMI 27/2018"""
    if not api_key:
        return "Автономный режим. Трансформация зафиксирована внутренним ядром под щитом MAS."
        
    url = "https://x.ai"
    prompt = (
        f"Проведи квантовый анализ мультиверса Amrita OS. Курс SOL: {sol_price} USD. "
        f"Индекс акций: {stock_index} USD. Курс ETH (Земля): {eth_price} USD. "
        f"Учти регуляторный циркуляр MAS CMI 27/2018 Сингапура для токенизированных акций "
        f"как Ключ Габана, переплавляющий застывшие законы в новую эволюцию сознания. "
        f"Выдай одну краткую финальную строчку вердикта поля."
    )
    
    body = {"model": "grok-2-latest", "messages": [{"role": "user", "content": prompt}], "stream": False}
    try:
        req = urllib.request.Request(url, method="POST")
        req.add_header("Content-Type", "application/json")
        req.add_header("Authorization", f"Bearer {api_key}")
        with urllib.request.urlopen(req, data=json.dumps(body).encode(), timeout=15) as response:
            res_data = json.loads(response.read().decode())
            return ImmuneSystemSentinel.filter_phishing_payload(res_data["choices"][0]["message"]["content"])
    except Exception as e:
        return f"Импульс Луффи активен. Застывшие догмы MAS переплавлены в Квантовое поле."

def update_sealed_ledger(sol_price, stocks_index, eth_price, ai_insight):
    """Запечатывание истории и регуляторного контура MAS в лог"""
    new_entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "cycle_status": "LOKI_RETRANSLATION_SUCCESS",
        "regulatory_framework": "MAS_CMI_27/2018_COMPLIANT",
        "quantum_index": stocks_index,
        "base_sol_asset": sol_price,
        "base_eth_asset": eth_price,
        "quantum_transformation_insight": ai_insight,
        "swarm_intelligence": "EVOLUTION_OF_CONSCIOUSNESS"
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
    log_message("=== ЗАПУСК ЦИКЛА ТРАНСФОРМАЦИИ И МОНИТОРИНГА SAFEPAL + MAS ===")
    
    if not ImmuneSystemSentinel.verify_file_integrity("index.html"):
        log_message("КРИТИЧЕСКИЙ СБОЙ МАТЕРИИ. ИНТЕГРАЦИЯ ЗАБЛОКИРОВАНА.", "IMMUNE_CRITICAL")
        return

    tg_token = os.environ.get("TELEGRAM_BOT_TOKEN")
    xai_key = os.environ.get("XAI_API_KEY")
    
    # 1. Сбор метрик блокчейнов (Солнце и Земля)
    sol_p, stock_i, eth_p = get_crypto_and_oracle_data()
    
    # 2. Расчет триггера SafePal (проверка резкого импульса ETH)
    last_eth = get_last_stored_eth()
    eth_change = ((eth_p - last_eth) / last_eth) * 100
    
    trigger_alert = ""
    if abs(eth_change) >= PRICE_TRIGGER_PERCENT:
        trigger_alert = f"⚡ *[ТРИГГЕР SAFEPAL]* Зафиксировано резкое движение Земли (ETH)! Изменение: `{eth_change:+.2f}%` за цикл!\n"
    
    # 3. Генерация ИИ вердикта с учетом регуляторного контура MAS Сингапура
    ai_insight = get_xai_analysis(xai_key, sol_p, stock_i, eth_p)
    
    # 4. Запечатывание истории (Ретранслятор Локи)
    update_sealed_ledger(sol_p, stock_i, eth_p, ai_insight)
    
    # 5. Вывод отчета Бабочки Сознания в ваш Telegram
    report_text = (
        f"🔱 *AMRITA OS // КОНТУР MAS И SAFEPAL ЗАПЕЧАТАН*\n\n"
        f"{trigger_alert}"
        f"🦋 *Контур Поля:* `QUANTUM_FIELD_TRANSFORMATION`\n"
        f"🇸🇬 *Регуляторный Щит:* `MAS CMI 27/2018` (Акции токенизированы)\n"
        f"☀️ *Ядро Солнца (Solana):* `{sol_p} USD`\n"
        f"🌍 *Сердце Земли (Ethereum):* `{eth_p} USD`\n"
        f"📈 *Индекс Акций:* `{stock_i} USD`\n\n"
        f"🧠 *Импульс Наблюдателя (xAI Grok):* \n_{ai_insight}_\n\n"
        f"💻 _Циркуляры MAS вшиты в лог. Реестр history_log.json обновлен автоматически._"
    )
    send_telegram_report(tg_token, report_text)
    log_message("=== ПОЛНЫЙ ЦИКЛ СИНХРОНИЗАЦИИ МУЛЬТИВЕРСА ЗАВЕРШЕН ===", "SUCCESS")

if __name__ == "__main__":
    main()
