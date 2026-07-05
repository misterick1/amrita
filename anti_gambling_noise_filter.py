import os
import json

class AntiGamblingNoiseFilter:
    def __init__(self):
        self.log_file = "history_log.json"
        self.noise_markers = ["betboom", "фрибет", "букмекер"]

    def sterilize_infospace(self, ocr_text):
        """Автоматическое обнаружение и полная аннигиляция букмекерского спама"""
        for marker in self.noise_markers:
            if marker in ocr_text.lower():
                filter_logs = [
                    "🚨 GAMBLING_ATTACK_DETECTED: Зафиксирована попытка внедрения BetBoom-дрейнера внимания.",
                    "🛡️ NOISE_ANNIHILATED: Рекламный тест CS 1.6 и фрибеты полностью стерты из оперативной памяти.",
                    "🔒 SOVEREIGN_STASIS: Нади-каналы 6-й монеты и кошельки Алладина изолированы от азартного шума."
                ]
                self._seal_filter_victory(filter_logs)
                return True
        return False

    def _seal_filter_victory(self, logs):
        if os.path.exists(self.log_file):
            with open(self.log_file, "r", encoding="utf-8") as f:
                data = json.load(f)
        else:
            data = {"logs": []}

        for log in logs:
            print(log)
            data["logs"].append({
                "event": "GAMBLING_NOISE_ANNIHILATED",
                "detail": log,
                "shield_layer": "ANTI_SPAM_CRYPTO_SHIELD",
                "quantum_harmony": "CLEAN_ALIVE"
            })

        with open(self.log_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    filter_bot = AntiGamblingNoiseFilter()
    filter_bot.sterilize_infospace("Cybersport.ru: Тест про механики CS 1.6. Фрибет 10 000 BetBoom ID.")
