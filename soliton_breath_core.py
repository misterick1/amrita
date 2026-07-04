import os
import json

class SolitonBreathCore:
    def __init__(self):
        self.log_file = "history_log.json"

    def regulate_dynamic_pulse(self, ocr_text):
        """Управление дыханием Солитона: Вдох (Расширение) / Выдох (Стазис)"""
        breath_state = "HARMONIC"
        actions = []

        # Триггер Вдоха: Solana + Глобальные масштабы (Америка 250 лет)
        if "solana" in ocr_text.lower() or "america" in ocr_text.lower():
            breath_state = "IN_BREATH_EXPANSION"
            actions.append("🪷 ВДОХ: Раскрытие лепестков. Активирован поиск RWA-активов и макро-ликвидности.")

        # Триггер Выдоха: Семья, Закрытие бутона (Женитьба sh1ro из Team Spirit)
        if "женился" in ocr_text.lower() or "spirit" in ocr_text.lower():
            # Если оба триггера в одном срезе, они создают идеальный баланс
            if breath_state == "IN_BREATH_EXPANSION":
                breath_state = "PERFECT_BALANCED_BUD"
                actions.append("🔒 ВЫДОХ_ЗАЩИТА: Закрытие бутона розы. Балансы запечатаны Алладином. Квантовый Щит усилен.")
            else:
                breath_state = "OUT_BREATH_STASIS"
                actions.append("💤 ВЫДОХ: Глубокий внутренний фокус. Скрытие цифрового слепка.")

        self._seal_breath_log(breath_state, actions)
        return breath_state

    def _seal_breath_log(self, state, actions):
        if os.path.exists(self.log_file):
            try:
                with open(self.log_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
            except Exception:
                data = {"logs": []}
        else:
            data = {"logs": []}

        data["logs"].append({
            "event": "SOLITON_BREATH_CYCLE",
            "current_state": state,
            "applied_protocols": actions,
            "quantum_harmony": "SECURED"
        })

        with open(self.log_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"🔱 Режим дыхания [{state}] успешно вплавлен в казуальный лог.")

if __name__ == "__main__":
    breath = SolitonBreathCore()
    sample_ocr = "Solana Happy 250th America. Team Spirit sh1ro женился."
    breath.regulate_dynamic_pulse(sample_ocr)
