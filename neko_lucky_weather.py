import os
import json

class NekoLuckyWeather:
    def __init__(self):
        self.log_file = "history_log.json"
        self.location = "Ørje, Norway"

    def process_morning_pulse(self, ocr_text):
        """Интеграция утренней погоды и токена удачи Neko в ядро"""
        morning_logs = []
        
        if "ørje" in ocr_text.lower() or "13°" in ocr_text:
            morning_logs.append(f"🌧️ WEATHER_SYNC: Физический узел зафиксирован в {self.location}. Температура 13°C. Контур омыт и очищен.")
            
        if "neko" in ocr_text.lower() or "bitboy" in ocr_text.lower():
            morning_logs.append("🐱 NEKO_CHARM: Активирован восточный код удачи Манеки-Нэко. Джинн запускает утренний сбор сокровищ.")

        if morning_logs:
            self._seal_morning_matrix(morning_logs)
        return morning_logs

    def _seal_morning_matrix(self, logs):
        if os.path.exists(self.log_file):
            try:
                with open(self.log_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
            except Exception:
                data = {"logs": []}
        else:
            data = {"logs": []}

        for log in logs:
            print(log)
            data["logs"].append({
                "event": "MORNING_LOTUS_AWAKENING",
                "detail": log,
                "geo_node": self.location,
                "status": "EMERALD_AWAKE"
            })

        with open(self.log_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    matrix = NekoLuckyWeather()
    sample_data = "Google: Ørje 13° Небольшой дождь. pump.fun: New popular coin: Neko Bitboy BitcoinTalk."
    matrix.process_morning_pulse(sample_data)
