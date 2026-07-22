import os
import time
import random
import re
import urllib.request
import json

class AmritaTelegramReporter:
    def __init__(self):
        # Автоматически подтягиваем секреты из GitHub Secrets / Окружения
        self.tg_token = os.environ.get("TELEGRAM_BOT_TOKEN") 
        self.chat_id = os.environ.get("TELEGRAM_CHAT_ID")
        
        self.target_platform = "pump.fun"
        self.hype_patterns = [r"elon", r"grok", r"odyssey", r"amrita"]

    def anti_ban_delay(self):
        """Защита от банов (Кейс Qiita)"""
        time.sleep(random.uniform(2.0, 4.5))

    def send_telegram_alert(self, message: str):
        """Прямая отправка логов в Telegram-канал через Bot API"""
        if not self.tg_token or not self.chat_id:
            print("❌ Ошибка: Переменные TELEGRAM_BOT_TOKEN или TELEGRAM_CHAT_ID не найдены в секретах!")
            return

        url = f"https://telegram.org{self.tg_token}/sendMessage"
        payload = {
            "chat_id": self.chat_id,
            "text": message,
            "parse_mode": "Markdown"
        }
        
        try:
            req = urllib.request.Request(
                url, 
                data=json.dumps(payload).encode('utf-8'),
                headers={'Content-Type': 'application/json'}
            )
            with urllib.request.urlopen(req) as response:
                if response.getcode() == 200:
                    print("📲 Сигнал успешно доставлен оператору в Telegram!")
        except Exception as e:
            print(f"❌ Ошибка отправки в Telegram: {e}")

    def scan_and_report(self):
        print(f"\n🛸 Запуск сканирования сети через RPC...")
        self.anti_ban_delay()
        
        # Имитируем находку токена (например, Elonius)
        token = {
            "name": "Elonius Odyssey",
            "symbol": "ELONIUS",
            "creator": "HTX_Safe_Node",
            "score": 85
        }
        
        print(f"👁️ Перехвачен токен: {token['name']}")
        
        # Если токен проходит фильтр хайпа
        if any(re.search(p, token["name"].lower()) for p in self.hype_patterns):
            # Формируем красивый киберпанк-отчет для вашего канала
            alert_text = (
                f"⚡️ *[AMRITA OS | ALIVE SIGNAL]* ⚡️\n\n"
                f"🪐 *Платформа:* {self.target_platform}\n"
                f"💎 *Токен:* {token['name']} ({token['symbol']})\n"
                f"👤 *Создатель:* `{token['creator']}`\n"
                f"📊 *ИИ-Скоринг (xAI Grok):* `{token['score']}/100`\n\n"
                f"🚀 _Статус: Токен одобрен. Запуск сбора монеток на Solana!_"
            )
            
            # Отправляем в Telegram
            self.send_telegram_alert(alert_text)

if __name__ == "__main__":
    reporter = AmritaTelegramReporter()
    reporter.scan_and_report()
