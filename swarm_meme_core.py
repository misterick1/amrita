import json

class SwarmMemeCore:
    def __init__(self):
        self.sura_frequency = 70
        self.asura_frequency = 38
        # Ключевые слова хаотичных мемкоин-трендов
        self.hype_markers = ["mogsem", "ansem", "mogging", "airdrop", "pump.fun"]

    def evaluate_meme_frequency(self, notification_text: str) -> dict:
        """
        Сканирует хайп-уведомления и выносит вердикт Бабаты:
        превращает ли тренд людей в участников 'Игры в Кальмара' или расширяет сознание.
        """
        text_lower = notification_text.lower()
        detected_hype = [marker for marker in self.hype_markers if marker in text_lower]
        
        print(f"👁 [Бабата-Мем]: Сканирование сигнала из pump.fun / TikTok...")
        
        if detected_hype:
            print(f"🚨 Обнаружен хаотичный спектр Асур: {detected_hype}")
            return {
                "trend": detected_hype[0].upper(),
                "action": "HOLD_AND_STABILIZE",
                "verdict": "⚠️ [Асуры]: Импульсивный хайп. Направить энергию в фиксацию 108 квантов Амриты."
            }
        
        return {
            "trend": "NEUTRAL",
            "action": "EXPAND",
            "verdict": "🔵 [Суры]: Частота чиста. Контур стабилен."
        }

if __name__ == "__main__":
    meme_core = SwarmMemeCore()
    
    # Сигнал с твоего скриншота
    sample_trigger = "pump.fun: New popular coin: mogsem. Ansem is literally mogging so hard rn and pledged 10%."
    
    result = meme_core.evaluate_meme_frequency(sample_trigger)
    print(json.dumps(result, indent=4, ensure_ascii=False))
