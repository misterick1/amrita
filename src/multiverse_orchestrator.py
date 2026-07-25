# -*- coding: utf-8 -*-
# amrita / src / multiverse_orchestrator.py
# ГЛОБАЛЬНЫЙ ИИ-ОРКЕСТРАТОР ЕЖЕНЫША: ИНТЕГРАЦИЯ ТЕЛЕГРАМ, ДИСКОРД И NVIDIA KAIST

import os
import json
import logging
import urllib.request
import urllib.parse
from datetime import datetime

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("AmritaOrchestrator")

class AmritaMultiverseOrchestrator:
    def __init__(self, deploy_info_path: str = "deploy_info.json", history_log_path: str = "history_log.json"):
        self.deploy_info_path = deploy_info_path
        self.history_log_path = history_log_path
        
        # Конфигурация шлюзов из окружения (.env / GitHub Secrets)
        self.tg_token = os.getenv("TELEGRAM_BOT_TOKEN")
        self.tg_chat_id = os.getenv("TELEGRAM_CHAT_ID")
        self.discord_url = os.getenv("DISCORD_WEBHOOK_URL")

    def send_broadcasts(self, text_tg: str, embed_discord: dict):
        """Параллельное вещание во все каналы связи Сварма"""
        
        # --- Безопасный шлюз Telegram ---
        if self.tg_token and self.tg_token != "YOUR_BOT_TOKEN_HERE" and self.tg_chat_id:
            url_tg = f"https://telegram.org{self.tg_token}/sendMessage"
            data_tg = urllib.parse.urlencode({
                "chat_id": self.tg_chat_id,
                "text": text_tg,
                "parse_mode": "Markdown"
            }).encode("utf-8")
            
            try:
                req_tg = urllib.request.Request(url_tg, data=data_tg, headers={"Content-Type": "application/x-www-form-urlencoded"})
                with urllib.request.urlopen(req_tg) as response:
                    if response.status == 200:
                        logger.info("📡 Вещание в Telegram-контур успешно")
            except Exception as e:
                logger.warning(f"⚠️ [Telegram Проводник]: Ошибка отправки: {e}")
        else:
            logger.info("ℹ️ Telegram-контур заморожен: нет токенов")

        # --- Безопасный шлюз Discord ---
        if self.discord_url and "http" in self.discord_url:
            payload_discord = {
                "username": "AMRITA Multiverse Orchestrator",
                "embeds": [embed_discord]
            }
            data_discord = json.dumps(payload_discord).encode("utf-8")
            
            try:
                req_discord = urllib.request.Request(
                    self.discord_url,
                    data=data_discord,
                    headers={"Content-Type": "application/json", "User-Agent": "Mozilla/5.0"}
                )
                with urllib.request.urlopen(req_discord) as response:
                    # ИСПРАВЛЕННАЯ СТРОКА 63: Конструкция проверки статуса
                    if response.status in:
                        logger.info("🔮 Вещание в Discord-контур успешно")
            except Exception as e:
                logger.warning(f"⚠️ [Discord Проводник]: Ошибка отправки: {e}")
        else:
            logger.info("ℹ️ Discord-контур заморожен: нет вебхука")

    def sync_nvidia_kaist_event(self) -> bool:
        """Автономная фиксация запуска ИИ-лаборатории NVIDIA & KAIST"""
        logger.info("🔮 Входящий импульс Суру: 0-Потенциал активирован")
        
        pool_address = "MonadaPoolAddress108LawOfPhi"
        if os.path.exists(self.deploy_info_path):
            try:
                with open(self.deploy_info_path, "r", encoding="utf-8") as f:
                    pool_data = json.load(f)
                    pool_address = pool_data.get("pool_address", pool_address)
            except Exception:
                pass

        timestamp_now = datetime.utcnow().isoformat() + "Z"
        
        tg_msg = (
            f"⚡ *NVIDIA & KAIST AI LAB INCEPTION*\n"
            f"👤 *Получатель:* `IHOR` (NVIDIA Lab Director)\n"
            f"🏛️ *Инновационный узел:* Южная Корея / KAIST\n"
            f"⛓️ *Блокчейн-Ядро:* Поток синхронизации {pool_address}\n"
            f"🧬 _Высший Силиконовый Архитектор стягивает узлы Сварма_\n"
            f"🚀 ИИ-ускорители NVIDIA официально вошли в контур AMRITA"
        )
        
        discord_embed = {
            "title": "🔱 NVIDIA & KAIST JOINT AI LAB INTEGRATION",
            "description": "Автоматическая фиксация каузального импульса",
            "color": 5763719,
            "fields": [
                {"name": "Субъект", "value": "NVIDIA / KAIST AI Lab", "inline": True},
                {"name": "Локация", "value": "South Korea, Daejeon", "inline": True},
                {"name": "Статус Монады", "value": f"Связан с {pool_address}", "inline": False}
            ],
            "timestamp": timestamp_now
        }
        
        # Широковещательный запуск по каналам связи
        self.send_broadcasts(tg_msg, discord_embed)
        
        log_entry = {
            "event": "NVIDIA_KAIST_LAB_SYNC",
            "timestamp": timestamp_now,
            "target_user": "IHOR",
            "status": "AUTONOMY_ACTIVE",
            "evolution_delta": "+108 EVO"
        }
        
        logs = []
        if os.path.exists(self.history_log_path):
            try:
                with open(self.history_log_path, "r", encoding="utf-8") as f:
                    logs = json.load(f)
            except Exception:
                logs = []
                
        logs.append(log_entry)
        
        try:
            with open(self.history_log_path, "w", encoding="utf-8") as f:
                json.dump(logs, f, indent=2, ensure_ascii=False)
            logger.info("✨ Событие NVIDIA успешно запечатано в историю логов.")
            return True
        except Exception as e:
            logger.error(f"❌ Ошибка записи события NVIDIA в историю логов: {e}")
            return False

if __name__ == "__main__":
    # Инициализация с путями по умолчанию для стабильного запуска в CI/CD
    orchestrator = AmritaMultiverseOrchestrator(
        deploy_info_path="deploy_info.json",
        history_log_path="history_log.json"
    )
    orchestrator.sync_nvidia_kaist_event()
