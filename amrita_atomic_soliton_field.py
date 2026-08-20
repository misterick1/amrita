import numpy as np
import matplotlib.pyplot as plt

# =========================================================================
# ⚛️ [AMRITA OS: ATOMIC SOLITON RESONANCE]
# Модель Единой Природы Ядра, Электрона и Фиолетового Поля Скорости (Х-Драгон)
# =========================================================================

PI_NUCLEUS = np.pi
PHI_ELECTRON = (1 + 5**0.5) / 2
X_DRAGON_SPEED = PI_NUCLEUS / PHI_ELECTRON  # Константа Скорости Дракона (~1.941611)

class AtomicUnifiedField:
    def __init__(self):
        self.x_speed = X_DRAGON_SPEED
        self.phi = PHI_ELECTRON
        self.scale = 108

    def generate_atom_structure(self, radial_distance):
        """
        Расчет единого поля атома. 
        Ядро (Плазма), Электрон (Волна) и Фиолетовое поле скорости имеют общую природу.
        """
        # 1. ПЛАЗМА ЯДРА (+1: Сверхплотный пик в центре, геометрия Пи)
        nucleus_core = 3.0 * (1.0 / np.cosh(radial_distance * 4.0))
        
        # 2. ВОЛНА ЭЛЕКТРОНА (-1: Свободное облако на удалении, масштаб Фи)
        electron_cloud = np.sin(radial_distance * self.phi) * np.exp(-0.5 * (radial_distance - 2.0)**2)
        
        # 3. ФИОЛЕТОВОЕ ПОЛЕ СКОРОСТИ Х-ДРАКОНА (0: Связующий радужный солитон)
        # Проявляется на пиковой скорости вращения полей
        dragon_field = np.sin(self.x_speed * radial_distance) * np.exp(-0.2 * radial_distance)
        
        # Итоговая целостная матрица атома (Ван Пис микромира)
        atomic_monolith = nucleus_core + electron_cloud + (dragon_field * 1.5)
        return atomic_monolith, nucleus_core, electron_cloud, dragon_field

def main():
    print("==================================================================")
    print("⚛️ [AMRITA OS: ATOMIC MONOLITH ENGAGED] ⚛️")
    print("Ядра и электроны объединены в Единое Квантовое Поле Скорости.")
    print(f"Константа вращения вихря Дракона X: {X_DRAGON_SPEED:.6f}")
    print("==================================================================")

    atom_system = AtomicUnifiedField()
    # Радиус атома от центра (ядра) к периферии
    radial_distance = np.linspace(0.01, 5.0, 1000)
    
    total_field, core, electron, dragon = atom_system.generate_atom_structure(radial_distance)

    # Визуализация Единой Природы Атома
    plt.figure(figsize=(14, 8))
    plt.gcf().patch.set_facecolor('#070a10')
    plt.gca().set_facecolor('#0d1117')

    # Отрисовка элементов атома из одной ткани
    plt.plot(radial_distance, core, '--', color='#e63946', linewidth=2, label='+1 ЯДРО (Кварк-глюонная Плазма / Пи)')
    plt.plot(radial_distance, electron, ':', color='#00bbf9', linewidth=2, label='-1 ЭЛЕКТРОН (Волновое Облако / Фи)')
    plt.plot(radial_distance, dragon, '-.', color='#7209b7', alpha=0.6, label=' Скорость Х-Дракона (Поле Связи)')
    
    # Единый Радужный Солитон (Фиолетовое мономерное поле атома)
    plt.plot(radial_distance, total_field, color='#9b5de5', linewidth=3.5, label='ЕДИНОЕ КВАНТОВОЕ ПОЛЕ АТОМА (Амрита)')
    plt.fill_between(radial_distance, total_field, color='#9b5de5', alpha=0.1)

    # Точки квантовых переходов электрона (Орбитали)
    orbitals = np.array([X_DRAGON_SPEED/2, X_DRAGON_SPEED, X_DRAGON_SPEED*2])
    plt.scatter(orbitals, np.zeros_like(orbitals), color='#fee440', 
                s=200, marker='o', edgecolors='white', zorder=5, label='Узлы Стабильности Орбит')

    plt.title('Фрактальный Атом: Единая Природа Плазмы Ядра, Электрона и Поля Х-Дракона', fontsize=13, color='white', pad=15)
    plt.xlabel('Радиус квантового взаимодействия (Расстояние от центра)', color='white')
    plt.ylabel('Плотность энергии единого поля', color='white')
    plt.grid(True, alpha=0.1, linestyle='--')
    plt.legend(facecolor='#1a1a1a', edgecolor='#444444', textcolor='white', fontsize=11, loc='upper right')
    plt.tick_params(colors='white')
    
    print("⚛️ Архитектура атома пересчитана. Фиолетовый солитон скорости успешно удерживает ядро и электрон.")
    plt.show()

if __name__ == '__main__':
    main()
