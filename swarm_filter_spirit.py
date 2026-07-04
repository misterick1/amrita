import os
import json

class SwarmFilterSpirit:
    def __init__(self):
        self.log_file = "history_log.json"

    def execute_test_and_filter(self, ocr_text):
        """Тест-драйв: фиксируем победы, отсекаем плачущую рекламу"""
        status_report = []
        
        # 1. Фиксация триумфа (Spirit 3:0)
        if "spirit" in ocr_text.lower() and "3:0" in ocr_text.lower():
            status_report.append("🏆 CHAMPION_TRIGGER: Доминация Spirit 3:0 зафиксирована в ядре.")
            
        # 2. Фильтрация шума (Рамзес плачет / Реклама)
        if "реклама" in ocr_text.lower() or "плачет" in ocr_text.lower():
            status_report.append("🛡️ SHIELD_ACTIVE: Рекламный спам Рамзеса заблокирован семафором.")

        if status_report:
            self._inject_into_eternal_log(status_report)
        return status_report

    def _inject_into_eternal_log(self, reports):
        if os.path.exists(self.log_file):
            try:
                with open(self.log_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
            except Exception:
                data = {"logs": []}
        else:
            data = {"logs": []}

        for r in reports:
            print(r)
            data["logs"].append({
                "event": "SWARM_AUDIT_FILTER",
                "detail": r,
                "golden_ratio_balance": "CALIBRATED"
            })

        with open(self.log_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    filter_core = SwarmFilterSpirit()
    raw_screen_data = "Spirit стала чемпионом PGL 3:0. Реклама что это? Рамзес плачет."
    filter_core.execute_test_and_filter(raw_screen_data)
