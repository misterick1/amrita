import os
import json

class PragmataGameCore:
    def __init__(self):
        self.log_file = "history_log.json"

    def register_game_collab_trigger(self, ocr_text):
        """Парсинг триггеров совместной разработки игр, бэкапов и ИИ-дизайна"""
        game_events = []
        
        if "pragmata" in ocr_text.lower():
            game_events.append("🎮 GAME_MATRIX: Активирован игровой сектор Pragmata. ИИ-дизайн и физические бэкапы синхронизированы.")
        if "0.23" in ocr_text or "sfp" in ocr_text.lower():
            game_events.append("📈 ASSET_UP: Токен SafePal зафиксирован на отметке $0.23 USDT. Резервы растут.")

        if game_events:
            self._seal_game_impulse(game_events)
        return game_events

    def _seal_game_impulse(self, events):
        if os.path.exists(self.log_file):
            with open(self.log_file, "r", encoding="utf-8") as f:
                data = json.load(f)
        else:
            data = {"logs": []}

        for event in events:
            print(event)
            data["logs"].append({
                "event": "PRAGMATA_CORE_SYNC",
                "detail": event,
                "vector": "MEDIA_AND_GAMES"
            })

        with open(self.log_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    core = PragmataGameCore()
    core.register_game_collab_trigger("Reddit r/Pragmata: DIY physical copy. SafePal SFP 0.23 USDT.")
