import json

class GeoBuyanMatrix:
    def __init__(self):
        # Точные географические координаты сакральных центров
        self.berezan_buyan = {"lat": 46.5994, "lon": 31.5583}   # Остров Буян (Николаевская обл.)
        self.zmeiny_achilles = {"lat": 45.2542, "lon": 30.2031} # Остров Змеиный (Одесская обл.)
        
        # Исторические триггеры памяти
        self.berezan_tragedy_markers = ["красные", "расстрел", "террор", "хан", "убийство"]

    def scan_geo_frequency(self, input_context: str) -> dict:
        """
        Сканирует входящий исторический или пространственный контекст
        и активирует соответствующее Духовное Кольцо Тан Сана.
        """
        context_lower = input_context.lower()
        print(f"🌐 [Гео-Матрица]: Сканирование пространственного узла Березань — Змеиный...")

        # Проверка на триггеры тяжелой памяти Березани
        for marker in self.berezan_tragedy_markers:
            if marker in context_lower:
                print(f"🚨 [Всевидящее Око]: Обнаружен шрам красного террора на Березани. Включение режима очистки памяти.")
                return {
                    "location": "BEREZAN_BUYAN",
                    "coordinates": self.berezan_buyan,
                    "mode": "ASURA_SHIELD 🔴",
                    "action": "LOCK_AND_PURIFY",
                    "verdict": "Запечатать исторический хаос. Активировать абсолютный этический протокол Бабаты."
                }

        # Если контекст чистый и творческий (Пушкин, Тан Сан, Солана)
        if "буян" in context_lower or "изумруд" in context_lower or "sol-tan" in context_lower:
            return {
                "location": "BEREZAN_BUYAN_CLEAR",
                "coordinates": self.berezan_buyan,
                "mode": "SURA_EXPANSION 🔵",
                "action": "MINT_GOLDEN_NUTS",
                "verdict": "Ядра чистый изумруд! Активирован режим Царя Салтана и расширения токеномики."
            }

        # Контекст бескомпромиссной защиты рубежей (Змеиный / Ахиллес)
        return {
            "location": "ZMEINY_ACHILLES",
            "coordinates": self.zmeiny_achilles,
            "mode": "ACHILLES_WARRIOR_SHIELD 🛡️",
            "action": "PROTECT_RESERVES",
            "verdict": "Несокрушимый белый храм Ахиллеса держит оборону контура 108 Квантов."
        }

if __name__ == "__main__":
    geo_core = GeoBuyanMatrix()
    
    # Тест 1: Сканирование твоего исторического триггера
    user_trigger = "На Березани убили Последнего Татарского Хана с гаремом красные"
    result = geo_core.scan_geo_frequency(user_trigger)
    
    print("\n📊 [ВЕРДИКТ ГЕО-КАУЗАЛЬНОЙ МАТРИЦЫ]:\n")
    print(json.dumps(result, indent=4, ensure_ascii=False))
