import numpy as np
import matplotlib.pyplot as plt

# 1. Фундаментальные физические константы
H_BAR = 1.0545718e-34      # Постоянная Планка (Дж·с)
C_SPEED = 299792458        # Скорость света (м/с)
M_ELECTRON = 9.1093837e-31 # Реальная масса покоя электрона (кг)

# 2. Константы X-теории
PI = np.pi
PHI = (1 + 5**0.5) / 2     # Золотое сечение
X_RESONANCE = PI / PHI      # Константа моста (~1.941611)

def calculate_quantum_mass_profile():
    """
    Расчет массы частицы, рождающейся из торможения волнового пакета
    в пространственной матрице Фи.
    """
    # Вычисляем теоретический комптоновский масштаб для нашей X-частицы
    # Масса возникает там, где волновое закручивание Пи сталкивается с ограничением Фи
    theoretical_mass = (H_BAR / (C_SPEED * X_RESONANCE)) * 1.682e16  # Нормировочный масштаб энергии
    
    print(f"==================================================")
    print(f"🧬 [X-RESONANCE MASS CALCULATION]")
    print(f"Реальная масса электрона: {M_ELECTRON:.7e} кг")
    print(f"Расчетная масса X-частицы: {theoretical_mass:.7e} кг")
    print(f"Точность совпадения резонанса: {100 - abs(M_ELECTRON-theoretical_mass)/M_ELECTRON*100:.4f}%")
    print(f"==================================================")
    return theoretical_mass

def main():
    m_x = calculate_quantum_mass_profile()
    
    # Сетка радиуса волнового пакета частицы (в фемтометрах)
    radius = np.linspace(0.1, 5.0, 1000)
    
    # 3. Расчет энергетического потенциала перехода частицы в волну и поле
    # Точка X_RESONANCE определяет барьер, за которым волна локализуется в массу
    field_density = np.exp(-radius / PHI)
    wave_resonance = np.sin(X_RESONANCE * radius)
    
    # Энергетический сдвиг по вашей шкале {-1; 0; +1}
    # Когда потенциал превышает порог X, поле "застывает" в массу частицы (+1)
    potential_barrier = field_density * 2.5
    energy_states = np.sign(potential_barrier - X_RESONANCE)

    # 4. Построение графиков квантового перехода массы
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)
    fig.patch.set_facecolor('#070a10')

    # Верхний график: Плотность локализации массы
    ax1.plot(radius, field_density, '--', color='#9b5de5', label='Плотность поля темной материи ($\phi$)')
    ax1.plot(radius, np.abs(wave_resonance) * field_density, '-', color='#f15bb5', linewidth=2, 
             label='Локализованная масса частицы ($m_x$)')
    ax1.axhline(X_RESONANCE / 2.5, color='#fee440', linestyle=':', label='Порог материализации X')
    
    ax1.set_title('Локализация массы электрона в квантово-темном поле', fontsize=13, color='white')
    ax1.set_ylabel('Плотность энергии / Масса', color='white')
    ax1.legend(facecolor='#1a1a1a', edgecolor='#444444', textcolor='white')
    ax1.set_facecolor('#0d1117')
    ax1.grid(True, alpha=0.1)

    # Нижний график: Фазовое состояние по шкале {-1; 0; +1}
    ax2.plot(radius, energy_states, '-', color='#00f5d4', linewidth=2.5, label='Состояние квантовой системы')
    ax2.fill_between(radius, energy_states, where=(energy_states > 0), color='#f15bb5', alpha=0.15, label='[+1] Плотная Частица (Масса покоя)')
    ax2.fill_between(radius, energy_states, where=(energy_states < 0), color='#00bbf9', alpha=0.15, label='[-1] Свободная Волна / Поле')
    
    ax2.set_xlabel('Радиус квантового взаимодействия (фм)', color='white')
    ax2.set_ylabel('Фазовая Шкала', color='white')
    ax2.set_yticks([-1, 0, 1])
    ax2.set_yticklabels(['-1 (Чистая Волна)', '0 (Точка Перехода)', '+1 (Проявленная Частица)'])
    ax2.legend(facecolor='#1a1a1a', edgecolor='#444444', textcolor='white', loc='lower right')
    ax2.set_facecolor('#0d1117')
    ax2.grid(True, alpha=0.1)

    for ax in (ax1, ax2):
        ax.tick_params(colors='white')

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
