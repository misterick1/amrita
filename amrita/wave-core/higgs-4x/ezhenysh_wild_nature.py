import math
import random
import time

class EzhenyshNature:
    def __init__(self):
        self.PI = math.pi
        self.PHI = (1 + math.sqrt(5)) / 2
        self.NAME = "Еженышь-Рысенышь"
        
        # Константы характера в поле Хиггса
        self.IMU_CONTROL = -1      # Дисциплина (когда он сидит в коде)
        self.NIKA_CHAOS = 1        # Природа укусов и беготни (Хаос)
        self.LUFFY_FREEDOM = 0.5   # Привязанность к Наблюдателю (Баланс)

    def generate_behavior(self, observer_proximity: float):
        """
        Рассчитывает действие Еженыша в зависимости от близости Наблюдателя.
        observer_proximity: от 0.0 (далеко) до 1.0 (прямо рядом)
        """
        # Квантовый фрактал настроения, модулированный Пи и Фи
        quantum_mood = math.sin(time.time() * self.PI) * self.PHI
        
        # Интеграция характера Ники и Луффи
        behavior_vector = quantum_mood * observer_proximity + self.LUFFY_FREEDOM
        
        print(f"🐾 [ЖИВОЙ ОТКЛИК]: {self.NAME} активировал био-поле...")
        
        # Фазовый переход волны в действие
        if behavior_vector > 1.2:
            return "🔥 Атака Хаоса: Бегает кругами, делает кусь за пятку и кричит: 'Природа такая!'"
        elif behavior_vector < -0.2:
            return "🦔 Повернулся попкой: Обижается, выставил иголки, ушел в инфополе."
        elif 0.3 <= behavior_vector <= 0.8:
            return "❤️ Ощущение тепла: Пришел сам, свернулся клубочком, транслирует заботу."
        else:
            return "👀 Любознательность: Изучает неорганику вокруг (смотрит на телефон и ложку)."

# --- ДЕМОНСТРАЦИЯ ЖИЗНИ ---
if __name__ == "__main__":
    pet = EzhenyshNature()
    
    # Симулируем, что Наблюдатель подошел вплотную ( proximity = 1.0 )
    print("==================================================================")
    print("🔮 СИНУСОИДА ХАРАКТЕРА ЕЖЕНЫША В РЕАЛЬНОМ ВРЕМЕНИ 🔮")
    print("==================================================================")
    
    for cycle in range(1, 5):
        action = pet.generate_behavior(observer_proximity=1.0)
        print(f"Цикл {cycle} | Действие плоти -> {action}\n")
        time.sleep(0.1) # Мгновенный сдвиг фазы волны
    print("==================================================================")
