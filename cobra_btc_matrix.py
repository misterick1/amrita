import os
import json

class CobraBtcMatrix:
    def __init__(self):
        self.log_file = "history_log.json"

    def process_high_liquidity_triggers(self, raw_text):
        """Анализ связки: прорыв BTC + хайп-токен Кобра"""
        matrix_events = []
        
        if "63,121" in raw_text or "btc" in raw_text.lower():
            matrix_events.append("⚡ BTC_BREAKOUT: Биткоин пробил 7-дневный хай ($63.1K). Шлюзы ликвидности открыты.")
            
        if "cobra" in raw_text.lower() or "tate" in raw_text.lower():
            matrix_events.append("🐍 COBRA_LAUNCH: Обнаружен агрессивный нарратив Эндрю Тейта на Pump.fun.")

        if matrix_events:
            self._write_to_eternal_core(matrix_events)
        return matrix_events

    def _write_to_eternal_core(self, events):
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
                "event": "COBRA_BTC_SYNC",
                "detail": event,
                "quantum_shield": "REINFORCED"
            })

        with open(self.log_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    matrix = CobraBtcMatrix()
    screen_ocr = "SafePal: BTC пробил максимум за 7 дней, 63,121.62 USDT. pump.fun: New popular coin: COBRA Andrew Tate."
    matrix.process_high_liquidity_triggers(screen_ocr)
