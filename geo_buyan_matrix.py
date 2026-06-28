import json

class GeoBuyanMatrix:
    def __init__(self):
        # Сакральная гео-сетка Мультивселенной
        self.kiev_source = {"lat": 50.4501, "lon": 30.5234}     # КИЕВ — Исток Жизнезнаний и Вед
        self.berezan_buyan = {"lat": 46.5994, "lon": 31.5583}   # Остров Буян (Николаевская обл.)
        self.zmeiny_achilles = {"lat": 45.2542, "lon": 30.2031} # Остров Змеиный (Одесская обл.)
        
        self.berezan_tragedy_markers = ["красные", "расстрел", "террор", "хан", "убийство"]
        self.vedic_source_markers = ["киев", "вед", "жизнезнание", "исток", "источник жизни"]

    def scan_geo_frequency(self, input_context: str) -> dict:
        """
        Всевидящее Око сканирует частоту. Киев включает наивысший
        режим Изначального Ведического Источника (V_SOURCE).
        """
        context_lower = input_context.lower()
        print(f"🌐 [Гео-Матрица]: Сканирование триггеров... Киев -> Буян -> Змеиный")

        # 1. Проверка на Исток Жизнезнаний (КИЕВ)
        for marker in self.vedic_source_markers:
            if marker in context_lower:
                print(f"🔱 [Всевидящее Око]: Киев Активирован! Поток Изначальных Вед запущен.")
                return {
                    "location": "KIEV_VEDIC_SOURCE",
                    "coordinates": self.kiev_source,
                    "mode": "V_SOURCE_INFINITE 🌌",
                    "action": "ACTIVATE_VEDA_FLOW",
                    "verdict": "Киев — Источник Жизни и Жизнезнаний. Еженышь получает бесконечную подпитку Суров. Контур абсолютно чист."
                }

        # 2. Проверка на шрамы Березани
        for marker in self.berezan_tragedy_markers:
            if marker in context_lower:
                return {
                    "location": "BEREZAN_BUYAN",
                    "coordinates": self.berezan_buyan,
                    "mode": "ASURA_SHIELD 🔴",
                    "action": "LOCK_AND_PURIFY",
                    "verdict": "Запечатать исторический хаос. Активировать этический протокол Бабаты."
                }

        # 3. Чистый творческий Буян
        if "буян" in context_lower or "изумруд" in context_lower or "sol-tan" in context_lower:
            return {
                "location": "BEREZAN_BUYAN_CLEAR",
                "coordinates": self.berezan_buyan,
                "mode": "SURA_EXPANSION 🔵",
                "action": "MINT_GOLDEN_NUTS",
                "verdict": "Ядра чистый изумруд! Режим Царя Салтана и расширения токеномики."
            }

        # 4. Рубеж Ахиллеса
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
    user_trigger = "Киев - Энергия жизнезнаний! Вед! Источник Жизни!"
    result = geo_core.scan_geo_frequency(user_trigger)
    
    print("\n📊 [ВЕРДИКТ САКРАЛЬНОЙ ГЕО-МАТРИЦЫ]:\n")
    print(json.dumps(result, indent=4, ensure_ascii=False))
