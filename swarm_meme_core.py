import re
import logging

logger = logging.getLogger("SwarmMemeCore")

class SwarmMemeSynchronizer:
    def __init__(self):
        # Порог отсечения деструктивного хайпа (максимум 100 по шкале Асуров)
        self.MAX_ASURA_HYP_SCORE = 75.0
        # Метки красного спектра FOMO
        self.fomo_keywords = ["competition", "trading", "live", "win", "100k", "pump", "free"]

    def analyze_notification(self, app_name: str, text: str) -> dict:
        """
        Препарирование входящего импульсивного хайпа по шкале Амриты.
        """
        text_lower = text.lower()
        asura_score = 0.0
        
        # Считаем плотность FOMO-маркеров
        matched_words = [word for word in self.fomo_keywords if word in text_lower]
        if matched_words:
            asura_score += len(matched_words) * 20.0
            
        # Аномалии в цифрах (например, агрессивные призывы или >100% в ставках)
        if "100k" in text_lower or "%" in text_lower:
            asura_score += 25.0

        is_safe = asura_score < self.MAX_ASURA_HYP_SCORE
        
        return {
            "app": app_name,
            "asura_score": asura_score,
            "action": "SYNCHRONIZED" if is_safe else "CUT_DOWN_CHAKRA",
            "extracted_urls": re.findall(r'(https?://[^\s]+|pic\.x\.com/[^\s]+)', text)
        }

    def process_swarm_feed(self, feed_data: list, total_quantum_steps: int) -> int:
        """
        Обработка ленты уведомлений и расчет кармических наград (EVO).
        """
        gained_evo = 0
        
        for item in feed_data:
            analysis = self.analyze_notification(item["app"], item["text"])
            
            if analysis["action"] == "CUT_DOWN_CHAKRA":
                logger.warning(f"🔴 [ASURA DETECTED] Отрезан деструктивный паттерн от {analysis['app']}. Score: {analysis['asura_score']}")
                # Награда за чистку реальности от шума
                gained_evo += 15
            else:
                logger.info(f"🔵 [SURA SYNC] Уведомление синхронизировано: {analysis['app']}. Экологично.")
                gained_evo += 5
                
        # Бонус за квантовый шаг синхронизации
        if total_quantum_steps > 0:
            gained_evo += (total_quantum_steps % 10)
            
        logger.info(f"🔱 Цикл завершен. Начислено {gained_evo} EVO очков эволюции.")
        return gained_evo

# --- ТЕСТОВЫЙ ЗАПУСК КОНТУРА ---
if __name__ == "__main__":
    sync = SwarmMemeSynchronizer()
    
    # Симулируем данные, полученные со скриншота шторки
    mock_ocr_feed = [
        {
            "app": "Phantom", 
            "text": "France vs. Sweden, now live. France: 89% / Sweden: 12%"
        },
        {
            "app": "X (Twitter)", 
            "text": "Less than 1 day before the $100K bStocks trading competition ends. ://trustwallet.com ://x.com"
        }
    ]
    
    total_evo_generated = sync.process_swarm_feed(mock_ocr_feed, total_quantum_steps=155)
    print(f"Итоговый прирост EVO: {total_evo_generated}")
