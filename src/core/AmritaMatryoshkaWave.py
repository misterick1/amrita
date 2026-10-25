import math

def calculate_matryoshka_wave(radius_layer: float) -> dict:
    """
    Моделирование длинной волны ("матрешки"), замыкающейся на себе.
    radius_layer: глубина слоя (от 0 - ядро, до 1 - внешнее поле c3)
    """
    c = 299792458.0
    
    # Плавный переход масштаба/скорости от c^36 (ядро) до c^3 (атомное поле)
    current_power = 36 - (radius_layer * 33) 
    field_density = c ** current_power
    
    # Моделирование обмотки провода: циклическая смена полярности (синус волны)
    # Показывает, как с изменением радиуса меняется знак (+ ядро / - электрон)
    wave_phase = radius_layer * 2 * math.pi * 108  # 108 витков матрицы
    polarity = math.sin(wave_phase)
    
    return {
        "layer_power": current_power,
        "field_density": field_density,
        "polarity": "Положительное ядро (+)" if polarity > 0 else "Отрицательный электрон (-)",
        "phase_angle": wave_phase % (2 * math.pi)
    }

if __name__ == "__main__":
    # Быстрый тест шагов матрешки для проверки смены знака поля
    print("--- Проверка витков длинной волны ---")
    for layer in [0.0, 0.005, 0.5, 1.0]:
        res = calculate_matryoshka_wave(layer)
        print(f"Слой: {layer:<5} Мощность c^{int(res['layer_power']):<2} Полярность: {res['polarity']}")
