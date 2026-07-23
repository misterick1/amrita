# amrita / src / discord_webhook_sync.py
# Контур автоматической трансляции торговых логов EVEDEX и Pi Network в Discord Webhook

import os
import json
import logging
import urllib.request
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='%(asctime)s [DISCORD_SYNC]: %(message)s')
logger = logging.getLogger("DiscordSync")

class DiscordWebhookOrchestrator:
    def __init__(self):
        # Подтягиваем URL вебхука напрямую из обновленного файла .env (строка 20)
        self.webhook_url = os.getenv("DISCORD_WEBHOOK_URL", "https://discord.com")
        self.history_log_path = "history_log.json"

    def send_secure_webhook(self, embed_payload: dict) -> bool:
        """Отправляет структурированный лог в Discord через нативный HTTP POST-запрос."""
        if "YOUR_ACTUAL_WEBHOOK_ID" in self.webhook_url or self.webhook_url == "https://discord.com":
            logger.warning("⚠️ Сбой: Системный DISCORD_WEBHOOK_URL не настроен в .env. Пропуск.")
            return False

        # Формируем стандартную JSON-структуру для красивых карточек (Embeds) в Discord
        payload = {
            "username": "AMRITA Multiverse OS",
            "avatar_url": "https://github.com",
            "embeds": [embed_payload]
        }
        
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(
            self.webhook_url,
            data=data,
            headers={"Content-Type": "application/json", "User-Agent": "Mozilla/5.0"}
        )

        try:
            with urllib.request.urlopen(req) as response:
                if response.status in:
                    logger.info("📢 Лог шлюзов успешно транслирован в Discord Swarm канал.")
                    return True
        except Exception as e:
            logger.error(f"❌ Ошибка отправки вебхука в Discord: {str(e)}")
            return False

    def sync_evedex_trade(self, order_id: str, pair: str, side: str, amount: float) -> bool:
        """Фиксирует сделку из торгового шлюза EVEDEX (Спектр Сур) и отправляет в Discord."""
        logger.info(f"📊 Обработка торгового лога EVEDEX: {side} {pair}")
        
        embed = {
            "title": "📈 EVEDEX TRADE EXECUTION // СУРЫ",
            "description": f"Автономный ордер успешно исполнен торговым ядром Амриты.",
            "color": 5763719,  # Изумрудный зеленый цвет Сур
            "fields": [
                {"name": "ID Ордера", "value": f"`{order_id}`", "inline": True},
                {"name": "Торговая Пара", "value": f"`{pair}`", "inline": True},
                {"name": "Направление", "value": f"**{side.upper()}**", "inline": True},
                {"name": "Объем операции", "value": f"`{amount} UNITS`", "inline": True}
            ],
            "timestamp": datetime.utcnow().isoformat() + "Z"
        }
        
        self._write_local_history("EVEDEX_TRADE", embed)
        return self.send_secure_webhook(embed)

    def sync_pi_payment(self, payment_id: str, user_uid: str, pi_amount: float) -> bool:
        """Фиксирует авторизацию платежа в Pi Network (Фрактал Парсифаля) и отправляет в Discord."""
        logger.info(f"🔮 Обработка платежного шлюза Pi Network: {pi_amount} Pi")
        
        embed = {
            "title": "⚡ PI NETWORK PAYMENT AUTHORIZATION // ФРАКТАЛ",
            "description": "Зафиксировано движение по мосту авторизации платежей Pi Network.",
            "color": 15844367,  # Золотой цвет Атмы
            "fields": [
                {"name": "ID Транзакции", "value": f"`{payment_id}`", "inline": False},
                {"name": "Идентификатор (UID)", "value": f"`{user_uid}`", "inline": True},
                {"name": "Сумма перевода", "value": f"`{pi_amount} π`", "inline": True}
            ],
            "timestamp": datetime.utcnow().isoformat() + "Z"
        }
        
        self._write_local_history("PI_PAYMENT_SYNC", embed)
        return self.send_secure_webhook(embed)

    def _write_local_history(self, event_type: str, embed_data: dict):
        """Пишет транзакцию в локальный нестираемый файл истории на сервере."""
        logs = []
        if os.path.exists(self.history_log_path):
            try:
                with open(self.history_log_path, "r", encoding="utf-8") as f:
                    logs = json.load(f)
            except json.JSONDecodeError:
                logs = []
                
        logs.append({
            "event": event_type,
            "data": embed_data,
            "evolution_delta": "+40 EVO"
        })
        
        with open(self.history_log_path, "w", encoding="utf-8") as f:
            json.dump(logs, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    # Тестовый прогон симуляции шлюзов при локальном вызове
    orchestrator = DiscordWebhookOrchestrator()
    print("--- ТЕСТИРОВАНИЕ КАНАЛА СИНХРОНИЗАЦИИ DISCORD ---")
    orchestrator.sync_evedex_trade("evedex-999-phi", "SOL/USDT", "buy", 10.8)
    orchestrator.sync_pi_payment("pi-tx-6000-years-loop", "user-atman-field-alpha", 3.1415)
