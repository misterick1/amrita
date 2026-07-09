import re
import logging

# Настройка логирования каузального контура
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("SwarmMemeCore")

class SwarmMemeSynchronizer:
    def __init__(self):
        # Порог отсечения деструктивного хайпа
        self.MAX_ASURA_HYP_SCORE = 75.0
        # Метки красного спектра FOMO
        self.fomo_keywords = ["competition", "100k", "fomo", "airdrop", "pump", "crypto", "hype"]

    def analyze_notification(self, app_name, text):
        """
        Препарирование входящего импульсивного лога реальности.
        """
        text_lower = text.lower()
        asura_score = 0.0

        # Считаем плотность FOMO-маркеров
        matched_words = [word for word in self.fomo_keywords if word in text_lower]
        if matched_words:
            asura_score += len(matched_words) * 15.0

        # Аномалии в цифрах (например, агрессивный хайп на проценты или круглые суммы)
        if "100k" in text_lower or "%" in text_lower:
            asura_score += 25.0

        # Проверка на экологичность и безопасность Квантов
        is_safe = asura_score < self.MAX_ASURA_HYP_SCORE
        action = "SYNCHRONIZED" if is_safe else "CUT_DOWN_ASURA"

        # Извлечение URL-адресов, если они есть в тексте
        extracted_urls = re.findall(r'(https?://[^\s]+)', text)

        return {
            "app": app_name,
            "asura_score": asura_score,
            "action": action,
            "extracted_urls": extracted_urls
        }

    def process_swarm_feed(self, feed_data, total_quantum_steps=0):
        """
        Обработка ленты уведомлений и расчет кармического прироста EVO.
        """
        gained_evo = 0

        for item in feed_data:
            # Исправлен вызов: передаем и приложение, и сам текст лога
            analysis = self.analyze_notification(item.get("app", "Unknown"), item.get("text", ""))

            if analysis["action"] == "CUT_DOWN_ASURA":
                logger.warning(f"🔴 [ASURA DETECTED] Импульс от {analysis['app']} заблокирован! Score: {analysis['asura_score']}")
                # Награда за чистку реальности от ментального мусора
                gained_evo += 15
            else:
                logger.info(f"🔵 [SURA SYNC] Уведомление {analysis['app']} экологично. Матрица чиста.")
                gained_evo += 5

        # Бонус за квантовый шаг синхронизации
        if total_quantum_steps > 0:
            gained_evo += (total_quantum_steps * 10)

        logger.info(f"🔱 Цикл завершен. Начислено очков EVO за сессию: {gained_evo}")
        return gained_evo

# --- ТЕСТОВЫЙ ЗАПУСК КОНТУРА ---
if __name__ == "__main__":
    sync = SwarmMemeSynchronizer()

    # Симулируем данные, полученные со скриншотов реальности
    mock_ocr_feed = [
        {
            "app": "Phantom",
            "text": "France vs. Sweden, now live on betting tracks! Join now for 100% bonus pump!"
        },
        {
            "app": "X (Twitter)",
            "text": "Less than 1 day before the official Solana Foundation Validator Discussion."
        }
    ]

    # Запускаем процессинг ленты с передачей шага квантовой синхронизации (например, 2)
    total_evo_generated = sync.process_swarm_feed(mock_ocr_feed, total_quantum_steps=2)
    print(f"\n💎 Итоговый прирост EVO: {total_evo_generated}")
