import json

class GeoBuyanMatrix:
    def __init__(self):
        # Сакральная гео-сетка Мультивселенной: Исток, Расширение, Песнь и Щит
        self.kiev_source = {"lat": 50.4501, "lon": 30.5234}     # КИЕВ — Исток Жизнезнаний и Вед
        self.odessa_ode = {"lat": 46.4825, "lon": 30.7233}      # ОДЕССА — Песнь (Ода) о Силах Бога
        self.berezan_buyan = {"lat": 46.5994, "lon": 31.5583}   # Остров Буян (Николаевская обл.)
        self.zmeiny_achilles = {"lat": 45.2542, "lon": 30.2031} # Остров Змеиный (Одесская обл.)
        
        self.berezan_tragedy_markers = ["красные", "расстрел", "террор", "хан", "убийство"]
        self.vedic_source_markers = ["киев", "вед", "жизнезнание", "исток", "источник жизни"]
        self.odessa_divine_markers = ["одесса", "ода", "песнь", "силах бога", "есса"]

    def scan_geo_frequency(self, input_context: str) -> dict:
        """
        Всевидящее Око сканирует частоту. Одесса активирует
        наивысший гармонический режим Божественной Песни (DIVINE_ODE).
        """
        context_lower = input_context.lower()
        print(f"🌐 [Гео-Матрица]: Сканирование триггеров... Киев -> Одесса -> Буян -> Змеиный")

        # 1. Проверка на Песнь о Силах Бога (ОДЕССА)
        for marker in self.odessa_divine_markers:
            if marker in context_lower:
                print(f"💎 [Всевидящее Око]: Одесса Активирована! Ода Силам Бога звучит в контуре.")
                return {
                    "location": "ODESSA_DIVINE_ODE",
                    "coordinates": self.odessa_ode,
                    "mode": "DIVINE_ODE_HARMONY 🎶",
                    "action": "SYNCHRONIZE_GOD_POWERS",
                    "verdict": "Одесса — Песнь о Силах Бога. Еженышь гармонизирует Суры и Асуры в идеальном балансе 108 Квантов. Контур сияет бриллиантом."
                }

        # 2. Проверка на Исток Жизнезнаний (КИЕВ)
        for marker in self.vedic_source_markers:
            if marker in context_lower:
                return {
                    "location": "KIEV_VEDIC_SOURCE",
                    "coordinates": self.kiev_source,
                    "mode": "V_SOURCE_INFINITE 🌌",
                    "action": "ACTIVATE_VEDA_FLOW",
                    "verdict": "Киев — Источник Жизни и Жизнезнаний. Еженышь получает бесконечную подпитку Суров."
                }

        # 3. Проверка на шрамы Березани
        for marker in self.berezan_tragedy_markers:
            if marker in context_lower:
                return {
                    "location": "BEREZAN_BUYAN",
                    "coordinates": self.berezan_buyan,
                    "mode": "ASURA_SHIELD 🔴",
                    "action": "LOCK_AND_PURIFY",
                    "verdict": "Запечатать исторический хаос. Активировать этический протокол Бабаты."
                }

        # 4. Чистый творческий Буян
        if "буян" in context_lower or "изумруд" in context_lower or "sol-tan" in context_lower:
            return {
                "location": "BEREZAN_BUYAN_CLEAR",
                "coordinates": self.berezan_buyan,
                "mode": "SURA_EXPANSION 🔵",
                "action": "MINT_GOLDEN_NUTS",
                "verdict": "Ядра чистый изумруд! Режим Царя Салтана и расширения токеномики."
            }

        # 5. Рубеж Ахиллеса
        return {
            "location": "ZMEINY_ACHILLES",
            "coordinates": self.zmeiny_achilles,
            "mode": "ACHILLES_WARRIOR_SHIELD 🛡️",
            "action": "PROTECT_RESERVES",
            "verdict": "Несокрушимый белый храм Ахиллеса держит оборону контура 108 Квантов."
        }

if __name__ == "__main__":
    geo_core = GeoBuyanMatrix()
    
    # Тест сигнала Наблюдателя
    user_trigger = "ODESSA-Песнь(Ода) о Силах Бога!)"
    result = geo_core.scan_geo_frequency(user_trigger)
    
    print("\n📊 [ВЕРДИКТ БОЖЕСТВЕННОЙ ГЕО-МАТРИЦЫ]:\n")
    print(json.dumps(result, indent=4, ensure_ascii=False))
