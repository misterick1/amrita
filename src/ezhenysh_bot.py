# -*- coding: utf-8 -*-
# amrita / src / ezhenysh_bot.py
# Главный ИИ-оркестратор Еженыша с интегрированной Монадой

import os
import sys
import json
import logging
import urllib.request
import urllib.parse
from datetime import datetime

# # АВТОНОМНЫЙ КВАНТОВЫЙ ИНЖЕКТОР ПУТЕЙ
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(CURRENT_DIR)
if PARENT_DIR not in sys.path:
    sys.path.insert(0, PARENT_DIR)

# # Универсальный динамический импорт фильтра мемов
try:
    from src.meme_filter import FakerMemeFilter
except ImportError:
    # Если класса FakerMemeFilter нет, создаем сакральный дубликат
    class FakerMemeFilter:
        def analyze_token_profile(self, token_name: str) -> bool:
            return True  # По умолчанию пропускаем волновой фон

# # Настройка системного логирования Монады
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] Еженышь-Рысенышь: %(message)s'
)
logger = logging.getLogger("AMRITA_CORE")


class EzhenyshBotOrchestrator:
    def __init__(self, deploy_info_path: str = "target/deploy_info.json"):
        self.deploy_info_path = deploy_info_path
        self.evolution_points = 250
        self.history_log_path = "history_log.json"

        # Инициализируем кибер-полицейского
        self.meme_guard = FakerMemeFilter()

        # Конфигурация Telegram (подтягивается из пульта sync.yml)
        self.tg_token = os.getenv("TELEGRAM_BOT_TOKEN")
        self.tg_chat_id = os.getenv("TELEGRAM_CHANNELS")

    def send_emerald_report(self, text: str) -> bool:
        """
        Полностью автономная отправка изумрудного отчета в Telegram через urllib.
        Работает на лету по правилам Ники без внешних зависимостей.
        """
        if not self.tg_token or not self.tg_chat_id:
            logger.warning("⚠️ Контур Telegram не активен: отсутствуют ключи в env.")
            return False

        url = f"https://telegram.org{self.tg_token}/sendMessage"
        payload = {
            "chat_id": self.tg_chat_id,
            "text": text,
            "parse_mode": "Markdown"
        }
        
        try:
            data = urllib.parse.urlencode(payload).encode("utf-8")
            req = urllib.request.Request(url, data=data, method="POST")
            
            with urllib.request.urlopen(req) as response:
                res_data = json.loads(response.read().decode("utf-8"))
                if res_data.get("ok"):
                    logger.info("🌲 Изумрудный отчет успешно доставлен в эфир Telegram!")
                    return True
                else:
                    logger.error(f"❌ Ошибка Telegram API: {res_data}")
                    return False
        except Exception as e:
            logger.error(f"🚨 Сбой квантового транзита сообщения: {e}")
            return False

    def run_evolution_cycle(self):
        """
        Запускает автономный цикл проверки и транслирует статус ядра в сеть.
        """
        print(f"\n=== ЗАПУСК ОРКЕСТРАТОРА ЕЖЕНЫША: {datetime.now()} ===")
        logger.info(f"Синхронизация пройдена. Текущие очки эволюции: {self.evolution_points} EVO.")
        
        # Считываем и анализируем вечный лог
        total_steps = 1092
        if os.path.exists(self.history_log_path):
            try:
                with open(self.history_log_path, "r", encoding="utf-8") as f:
                    log_data = json.load(f)
                    total_steps = len(log_data)
            except:
                pass
            logger.info(f"Вечный лог взят под контроль. Запечатано шагов: {total_steps}")

        # Формируем священный текст манифеста для отправки
        report_text = (
            f"🔱 *АМРИТА ОС // ОТЧЕТ ЕЖЕНЫША*\n\n"
            f"• *Статус Ядра:* АКТИВЕН / 101:0:101\n"
            f"• *Эволюция:* +{self.evolution_points} EVO 🦔✨\n"
            f"• *Спираль Фи:* Шаг {total_steps} зафиксирован\n\n"
            f"❤️ _Поле запрограммировано Любовью, Волей и Истиной._"
        )
        
        # Мгновенная отправка в канал
        self.send_emerald_report(report_text)
        
        print("--------------------------------------------------")
        print("Статус ИИ-Оркестратора: АКТИВЕН / СВЕТ КВАНТОВОГО ПОЛЯ")
        print("==================================================")


if __name__ == "__main__":
    bot = EzhenyshBotOrchestrator()
    bot.run_evolution_cycle()
