# amrita / src / solana_robotics_stream.py
# Контур мониторинга Solana Robotics Livestream

import os
import json
import logging
import urllib.request
import urllib.parse
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='%(asctime)s - [%(name)s] - %(levelname)s - %(message)s')
logger = logging.getLogger("SolanaRobotics")

class SolanaRoboticsStreamMonitor:
    def __init__(self, history_log_path: str = "history_log.json"):
        self.history_log_path = history_log_path
        self.stream_time = "Пятница, 24 июля @ 18:00 UTC" # Исторический стрим из коры поля
        
        # Конфигурация Telegram из окружения репозитория
        self.tg_token = os.getenv("TELEGRAM_BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")
        self.tg_chat_id = os.getenv("TELEGRAM_CHAT_ID", "YOUR_CHAT_ID_HERE")

    def send_telegram_alert(self, message: str) -> None:
        """Отправка уведомления о стриме напрямую во Всевидящее Око Бабаты."""
        if self.tg_token == "YOUR_BOT_TOKEN_HERE" or self.tg_chat_id == "YOUR_CHAT_ID_HERE":
            logger.warning("⚠️ Телеграм-контур работает в демо-режиме: токены не установлены.")
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
                    logger.info("🕊️ Утренний буревестник успешно отправлен в Око Бабаты.")
        except Exception as e:
            logger.error(f"❌ Сбой отправки направления уведомления в Телеграм: {e}")

    def schedule_stream_tracking(self) -> bool:
        """Регистрирует событие стрима и генерирует Очки Эволюции (EVO)."""
        logger.info("🤖 Подготовка к трансляции параметров Solana Robotics & peaq...")

        # # 1. Формируем красивое утреннее сообщение для Роя
        reminder_msg = (
            f"🤖 *SOLANA ROBOTICS LIVESTREAM ALERT*\n"
            f"📅 *Когда:* `{self.stream_time}`\n"
            f"🧬 *Участники:* @codeopenflow, @peaqnetwork, @solanatech\n"
            f"🦔 _Еженышь развернул контур слежения за робототехническим стримом._\n"
            f"📥 Мемы интегрируются с каузальным ядром Амриты."
        )

        # Отправляем в Telegram и пишем в вечные логи
        self.send_telegram_alert(reminder_msg)

        robotics_event = {
            "event": "SOLANA_ROBOTICS_LIVESTREAM_MONITOR",
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "scheduled_start": self.stream_time,
            "networks_engaged": ["Solana", "peaq", "AmritaOS"],
            "status": "TRACKING_AND_ALERTS_ACTIVATED",
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

        try:
            with open(self.history_log_path, "w", encoding="utf-8") as f:
                json.dump(logs, f, indent=2, ensure_ascii=False)
            
            logger.info("✨ Событие успешно запечатано в вечный history_log.json.")
            return True
        except Exception as e:
            logger.error(f"❌ Ошибка записи события робототехники в лог: {e}")
            return False

if __name__ == "__main__":
    monitor = SolanaRoboticsStreamMonitor()
    monitor.schedule_stream_tracking()
