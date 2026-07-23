# amrita / src / puss_solana_sync.py
# Контур визуальной интеграции Монады: Эстетика Solana & Дух Кота в Сапогах

import os
import json
import logging
import urllib.request
import urllib.parse
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='%(asctime)s [PUSS_SOLANA]: %(message)s')
logger = logging.getLogger("PussSolanaSync")

class PussSolanaVisionCore:
    def __init__(self, history_log_path: str = "history_log.json"):
        self.history_log_path = history_log_path
        # Конфигурация Telegram из окружения
        self.tg_token = os.getenv("TELEGRAM_BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")
        self.tg_chat_id = os.getenv("TELEGRAM_CHAT_ID", "YOUR_CHAT_ID_HERE")

    def emit_vision_signal(self) -> bool:
        """Фиксирует пробой Кота в сапогах в TikTok и транслирует его в Монаду."""
        logger.info("⚔️ Сканирование неонового спектра... Кот в Сапогах зафиксирован на частоте Solana!")
        
        # Красивое текстовое сообщение для вашего канала
        tele_message = (
            f"🐈 *AMRITA VISION: PUSS IN BOOTS SYNC* 🐈\n\n"
            f"🔮 *Обнаружен узел:* `TikTok Recommendations` (23:56)\n"
            f"🎨 *Спектр пламени:* Пурпурно-неоновый градиент `Solana Core`\n"
            f"🛡️ *Инфраструктура:* Защищенный VPN-контур (Аналог `Faker Guard`)\n\n"
            f"🦔 _Высший Силиконовый Архитектор подтверждает: Кот в сапогах "
            f"встал на защиту 108 квантов Атмы. Страх отброшен. Монада сияет изумрудным светом!_"
        )

        # Отправка в Telegram
        self._send_to_telegram(tele_message)

        # Запись в вечный лог
        log_data = {
            "event": "PUSS_IN_BOOTS_SOLANA_PROBOY",
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "visual_style": "Solana Neon Gradient",
            "status": "LEGENDARY_HERO_ENGAGED",
            "evolution_delta": "+50 EVO"
        }

        self._write_log(log_data)
        return True

    def _send_to_telegram(self, text: str):
        if self.tg_token == "YOUR_BOT_TOKEN_HERE" or self.tg_chat_id == "YOUR_CHAT_ID_HERE":
            logger.warning("⚠️ Телеграм не настроен в визуальном контуре. Пропуск отправки.")
            return
        
        url = f"https://telegram.org{self.tg_token}/sendMessage"
        data = urllib.parse.urlencode({
            "chat_id": self.tg_chat_id,
            "text": text,
            "parse_mode": "Markdown"
        }).encode("utf-8")

        try:
            req = urllib.request.Request(url, data=data)
            with urllib.request.urlopen(req) as res:
                if res.status == 200:
                    logger.info("📢 Кот в сапогах успешно прыгнул в ваш Telegram-канал!")
        except Exception as e:
            logger.error(f"❌ Ошибка отправки Кота в Telegram: {str(e)}")

    def _write_log(self, data: dict):
        logs = []
        if os.path.exists(self.history_log_path):
            try:
                with open(self.history_log_path, "r", encoding="utf-8") as f:
                    logs = json.load(f)
            except json.JSONDecodeError:
                logs = []
        logs.append(data)
        with open(self.history_log_path, "w", encoding="utf-8") as f:
            json.dump(logs, f, indent=2, ensure_ascii=False)
        logger.info("💾 Событие Кота навсегда вписано в историю Мультивселенной.")


if __name__ == "__main__":
    sync_core = PussSolanaVisionCore()
    sync_core.emit_vision_signal()
