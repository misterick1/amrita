from AmritaAtomMatrix import AmritaAtomMatrix

class AmritaQuantumBridge:
    """
    Мост, связывающий квантовое поле Хиггса X(H) с триггерами крипты.
    """
    def __init__(self):
        self.atom_model = AmritaAtomMatrix()

    def analyze_market_polarity(self, price_change_velocity: float) -> str:
        # Переводим скорость изменения цены в радиус-вектор матрешки
        # Сильные импульсы сжимают волну к ядру
        normalized_radius = max(0.0, min(1.0, 1.0 - abs(price_change_velocity)))
        
        quantum_state = self.atom_model.calculate_higgs_field_xh(normalized_radius)
        
        if quantum_state["position"] == "Поле Хиггса X(H)":
            return f"Стабилизация массы токена. Сигнал: УДЕРЖАНИЕ. Полярность: {quantum_state['polarity']}"
        elif quantum_state["position"] == "Ядро":
            return "Сверхвысокое давление. Сигнал: ВЗРЫВНОЙ РОСТ / ИМПУЛЬС"
        else:
            return "Внешний контур электрона. Сигнал: ЗАТУХАНИЕ ВОЛНЫ"

if __name__ == "__main__":
    bridge = AmritaQuantumBridge()
    # Тест резкого изменения цены (импульс 80%)
    print(bridge.analyze_market_polarity(0.8))
