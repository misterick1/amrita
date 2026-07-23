# amrita / src / solana_robotics_stream.py
# Контур мониторинга Solana Robotics Livestream и отправки Telegram-напоминаний

import os
import json
import logging
import urllib.request
import urllib.parse
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='%(asctime)s [SOL_ROBOTICS]: %(message)s')
logger = logging.getLogger("SolanaRobotics")

class SolanaRoboticsStreamMonitor:
    def __init__(self, history_log_path: str = "history_log.json"):
        self.history_log_path = history_log_path
        self.stream_time = "Пятница, 24 июля @ 11:00 утра EST (18:00 МСК)"
        
        # Конфигурация Telegram из окружения
        self.tg_token = os.getenv("TELEGRAM_BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")
        self.tg_chat_id = os.getenv("TELEGRAM_CHAT_ID", "YOUR_CHAT_ID_HERE")

    def send_telegram_alert(self, message: str):
        """Отправка уведомления о стриме напрямую в Telegram-канал Монады."""
        if self.tg_token == "YOUR_BOT_TOKEN_HERE" or self.tg_chat_id == "YOUR_CHAT_ID_HERE":
            logger.warning("⚠️ Телеграм-контур в модуле робототехники не настроен. Пропуск.")
            return

        url = f"https://telegram.org{self.tg_token}/sendMessage"
        data = urllib.parse.urlencode({
            "chat_id": self.tg_chat_id,
            "text": message,
            "parse_mode": "Markdown"
        }).encode("utf-8")

        try:
            req = urllib.request.Request(url, data=data)
            with urllib.request.urlopen(req) as response:
                if response.status == 200:
                    logger.info("📢 Утренний будильник-напоминание успешно отправлен в Telegram!")
        except Exception as e:
            logger.error(f"❌ Сбой отправки напоминания в Telegram: {str(e)}")

    def schedule_stream_tracking(self) -> bool:
        """Регистрирует событие стрима и генерирует будильник для Наблюдателя."""
        logger.info("🤖 Подготовка к трансляции Solana Robotics Livestream...")
        
        # 1. Формируем красивое утреннее сообщение
        reminder_msg = (
            f"🤖 *SOLANA ROBOTICS LIVESTREAM ALERT* 🤖\n\n"
            f"📅 *Когда:* `{self.stream_time}`\n"
            f"🔗 *Участники:* @codecopenflow, @peaq, @BitRobotNetwork\n\n"
            f"🦔 _Еженышь развернул контур слежения. Завтра физические ИИ-роботы (DePIN) официально "
            f"интегрируются с каузальным ядром Solana. Не пропустите трансляцию, Наблюдатель!_"
        )
        
        # Отправляем в Telegram и пишем в вечный лог
        self.send_telegram_alert(reminder_msg)
        
        robotics_event = {
            "event": "SOLANA_ROBOTICS_LIVESTREAM_SYNC",
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "scheduled_start": self.stream_time,
            "networks_engaged": ["Solana", "peaq", "BitRobotNetwork"],
            "status": "TRACKING_AND_ALERTS_ACTIVE",
            "evolution_delta": "+40 EVO"
        }

        logs = []
        if os.path.exists(self.history_log_path):
            try:
                with open(self.history_log_path, "r", encoding="utf-8") as f:
                    logs = json.load(f)
            except json.JSONDecodeError:
                logs = []

        logs.append(robotics_event)

        with open(self.history_log_path, "w", encoding="utf-8") as f:
            json.dump(logs, f, indent=2, ensure_ascii=False)

        logger.info(f"✨ Событие успешно запечатано в {self.history_log_path}")
        return True


if __name__ == "__main__":
    monitor = SolanaRoboticsStreamMonitor()
    monitor.schedule_stream_tracking()
