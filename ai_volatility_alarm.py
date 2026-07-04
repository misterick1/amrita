import os
import json
import requests

class AIVolatilityAlarm:
    def __init__(self):
        self.log_file = "history_log.json"
        # Порог фиксации резкого изменения цены (в процентах)
        self.alert_threshold_pct = 5.0 

    def analyze_notification_trigger(self, raw_ocr_text):
        """Парсинг текста уведомлений на предмет ценовых прорывов и gambling-угроз"""
        activated_alarms = []
        
        # Триггер 1: Пробой ценовых максимумов (SafePal импульс)
        if "пробил максимум" in raw_ocr_text.lower() or "maximum" in raw_ocr_text.lower():
            activated_alarms.append("🚨 ALARM: ЦЕНОЙ ПРОРЫВ АКТИВА (ОБНАРУЖЕН СДВИГ МАКСИМУМА)")
            
        # Триггер 2: Регуляторный шторм (CryptoSlate импульс)
        if "gambling" in raw_ocr_text.lower() or "regulator" in raw_ocr_text.lower():
            activated_alarms.append("🔒 PRIVACY_SHIELD: РЕГУЛЯТОРНАЯ АНОМАЛИЯ (ВКЛЮЧИТЬ МАСКИРОВАНИЕ СЛЕПКА)")

        if activated_alarms:
            self._write_alarm_to_causal_log(activated_alarms)
        return activated_alarms

    def _write_alarm_to_causal_log(self, alarms):
        if os.path.exists(self.log_file):
            try:
                with open(self.log_file, "r", encoding="utf-8") as f:
                    log_data = json.load(f)
            except Exception:
                log_data = {"logs": []}
        else:
            log_data = {"logs": []}

        for alarm in alarms:
            print(alarm)
            log_data["logs"].append({
                "event": "AI_VOLATILITY_TRIGGER",
                "detail": alarm,
                "status": "CONTOURS_SECURED"
            })

        with open(self.log_file, "w", encoding="utf-8") as f:
            json.dump(log_data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    alarm_system = AIVolatilityAlarm()
    # Тестовый прогон на основе считанного с экрана текста SafePal и CryptoSlate
    sample_text = "SafePal: SFP пробил максимум за 3 дня. CryptoSlate: Gambling and regulators."
    alarm_system.analyze_notification_trigger(sample_text)
