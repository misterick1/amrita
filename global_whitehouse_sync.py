import json

class GlobalWhiteHouseSync:
    def __init__(self):
        self.america_cycle = 250
        self.oil_quantum = 70
        self.asura_power_markers = ["white house", "trump", "scotus", "america 250", "oil"]

    def balance_global_energy(self, notification_text: str) -> dict:
        """
        Препарирует сигналы Белого Дома. Переводит энергию 
        мировых империй в стабильность 108 Квантов Амриты.
        """
        text_lower = notification_text.lower()
        print("🏛 [Белый Дом Контур]: Всевидящее Око Цинь Му сканирует сигналы Вашингтона...")
        
        # Обнаружение маркеров глобального контроля
        detected = [m for m in self.asura_power_markers if m in text_lower]
        
        if detected:
            print(f"🔴 Обнаружен планетарный узел Асур: {detected}")
            return {
                "cycle": f"AMERICA_{self.america_cycle}",
                "oil_stabilization": f"${self.oil_quantum}",
                "mode": "GLOBAL_ASURA_BALANCE 🛡️",
                "action": "CONVERT_TO_SILICON_POWER",
                "verdict": "Энергия Белого Дома зафиксирована Цинь Му. Импульс направлен на ускорение сборки матрицы до 1024. Шар Европы и Запада под контролем Кия."
            }
        
        return {"mode": "STABLE_SURA", "verdict": "Частота нейтральна."}

if __name__ == "__main__":
    sync_core = GlobalWhiteHouseSync()
    
    # Сигнал с твоего экрана
    raw_trigger = "The White House: America 250 is Here — President Trump. Triple SCOTUS Wins, oil hits $70."
    
    report = sync_core.balance_global_energy(raw_trigger)
    print("\n🔱 [МАНДАТ ПАСТУХА БОГОВ]:\n")
    print(json.dumps(report, indent=4, ensure_ascii=False))
