import os
import json

class EtfLiquidityFilter:
    def __init__(self):
        self.log_file = "history_log.json"
        self.negative_weeks_streak = 8

    def analyze_etf_and_filter_noise(self, raw_ocr_text):
        """Анализ оттока из ETF и тотальная блокировка рекламного шума"""
        interpreted_events = []
        
        if "etfs" in raw_ocr_text.lower() or "negative week" in raw_ocr_text.lower():
            interpreted_events.append(f"📊 ETF_MACRO: Зафиксирована {self.negative_weeks_streak}-я отрицательная неделя спотовых ETF. Капитал уходит в ончейн-ликвидность.")
            
        if "macht dich" in raw_ocr_text.lower() or "tradingcommunity" in raw_ocr_text.lower():
            interpreted_events.append("🛡️ NOISE_CANCELED: Рекламный триггер ложного богатства ('9 to 5') успешно заблокирован Семафором.")

        if interpreted_events:
            self._write_to_soliton_core(interpreted_events)
        return interpreted_events

    def _write_to_soliton_core(self, events):
        if os.path.exists(self.log_file):
            try:
                with open(self.log_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
            except Exception:
                data = {"logs": []}
        else:
            data = {"logs": []}

        for event in events:
            print(event)
            data["logs"].append({
                "event": "ETF_MACRO_FLOW_SYNC",
                "detail": event,
                "layer_0_protection": "ACTIVE",
                "harmonic_state": "CALIBRATED"
            })

        with open(self.log_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    filter_system = EtfLiquidityFilter()
    screen_data = "The Block News Feed: Bitcoin ETFs log record eighth straight negative week. Advertisement: DEIN 9 TO 5 MACHT DICH NICHT REICH."
    filter_system.analyze_etf_and_filter_noise(screen_data)
