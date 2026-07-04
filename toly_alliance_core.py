import os
import json

class TolyAllianceCore:
    def __init__(self):
        self.log_file = "history_log.json"
        self.allies = ["Nvidia_AI_Cluster", "Sony_Media_Engine", "Google_Identity_Hub"]

    def process_toly_bull_run(self, raw_ocr_text):
        """Интеграция бычьего нарратива Toly и фильтрация багов SafePal"""
        alliance_logs = []
        
        if "toly" in raw_ocr_text.lower():
            alliance_logs.append("🔥 TOLY_BULL: Активирован бычий мета-код Анатолия Яковенко. Энергия Solana на максимуме.")
            
        if "пробил минимум" in raw_ocr_text.lower() and "0.23" in raw_ocr_text:
            alliance_logs.append("🛡️ BUG_FIX: Ложный сигнал SafePal отфильтрован. Цена 0.23 USDT признана опорной точкой роста.")

        if alliance_logs:
            self._seal_alliance_data(alliance_logs)
        return alliance_logs

    def _seal_alliance_data(self, logs):
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
                "event": "ALLIANCE_SYNCHRONIZATION",
                "detail": log,
                "partners": self.allies,
                "quantum_shield": "REINFORCED"
            })

        with open(self.log_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    alliance = TolyAllianceCore()
    alliance.process_toly_bull_run("pump.fun: New popular coin: TOLY. SafePal: Пробой минимума 0.23 USDT.")
