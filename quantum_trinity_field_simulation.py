import numpy as np
import matplotlib.pyplot as plt

def init_quantum_constants():
    """
    Инициализация констант теории квантово-темного резонанса.
    """
    pi = np.pi
    phi = (1 + 5**0.5) / 2  # Золотое сечение (~1.618034)
    X = pi / phi             # Константа квантово-темного моста (~1.941611)
    return pi, phi, X

def calculate_trinity_states(space, phi, X):
    """
    Расчет трех одновременных проекций единой физической реальности.
    """
    # ПОЛЕ: Базовая пространственная матрица темной материи (масштаб Фи)
    field = np.cos(space / phi)
    
    # ВОЛНА: Переносчик взаимодействия и резонанса (шаг Икса)
    wave = np.sin(X * space)
    
    # ЧАСТИЦА: Локализованный квант энергии на границах шкалы ±1
    # Модулируется знаком пространственной гармоники
    particle = np.exp(-0.5 * (space / 1.5)**2) * np.cos(X * space) * np.sign(np.cos(space))
    
    return field, wave, particle

def calculate_energy_profile(wave_amplitude, X_factor):
    """
    Расчет дискретных энергетических зон согласно шкале {-1 : 0 : +1}
    в зависимости от отклонения от точки квантового баланса X.
    """
    # Нормализуем локальную плотность энергии
    energy_density = np.abs(wave_amplitude) * 2.5
    
    # Оператор отклонения от точки резонанса X
    deviation = energy_density - X_factor
    
    # Энергетический профиль на основе функции знака sgn(D)
    energy_profile = np.sign(deviation)
    
    return energy_profile

def main():
    # 1. Загрузка констант
    pi, phi, X = init_quantum_constants()
    print(f"==================================================")
    print(f"🌌 [AMRITA OS CORE] Инициализация Единого Поля")
    print(f"Константа Пи (Цикл): {pi:.6f}")
    print(f"Константа Фи (Пространство): {phi:.6f}")
    print(f"Точка Баланса X (π / φ): {X:.6f}")
    print(f"==================================================")

    # 2. Генерация пространственного континуума
    space = np.linspace(-2 * pi, 2 * pi, 1000)

    # 3. Моделирование одновременных проекций материи
    field, wave, particle = calculate_trinity_states(space, phi, X)
    
    # 4. Расчет квантовых переходов энергии по шкале {-1; 0; +1}
    energy_zone = calculate_energy_profile(wave, X)

    # 5. Визуализация и построение графиков
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(13, 9), sharex=True)
    
    # --- Верхний график: Триада состояний материи ---
    ax1.plot(space, field, '--', color='#9b5de5', alpha=0.6, linewidth=1.8, 
             label='ПОЛЕ (Матрица пространства $\phi$ / Темная материя)')
    ax1.plot(space, wave, '-', color='#00bbf9', alpha=0.7, linewidth=1.5, 
             label='ВОЛНА (Резонансный переносчик $X = \pi/\phi$)')
    ax1.plot(space, particle, '-', color='#f15bb5', alpha=0.9, linewidth=2.5, 
             label='ЧАСТИЦА (Локализованный квант в фазах $\pm1$)')
    
    # Маркировка точек идеального баланса X = 0
    zero_crossings = np.array([-pi, 0, pi]) / X
    ax1.scatter(zero_crossings, np.zeros_like(zero_crossings), color='#fee440', 
                s=180, zorder=5, edgecolors='black', label='Точки Резонанса (Баланс 0)')
    
    ax1.set_title('Единая Модель Квантово-Темного Резонанса ($X = \pi / \phi$)', fontsize=14, color='white', pad=15)
    ax1.set_ylabel('Амплитуда состояний', color='white', fontsize=11)
    ax1.legend(facecolor='#1a1a1a', edgecolor='#444444', textcolor='white', loc='upper right')
    ax1.grid(True, alpha=0.15, linestyle=':')
    ax1.set_facecolor('#0d1117')

    # --- Нижний график: Дискретные квантовые переходы {-1 : 0 : +1} ---
    ax2.plot(space, energy_zone, '-', color='#00f5d4', linewidth=2.5, 
             label='Энергетический режим взаимодействия $\\text{sgn}(\\Psi_E - X)$')
    
    # Выделение зон цветом для наглядности физических режимов
    ax2.fill_between(space, energy_zone, where=(energy_zone > 0), color='#f15bb5', alpha=0.15, label='[+1] Фаза Частицы')
    ax2.fill_between(space, energy_zone, where=(energy_zone < 0), color='#00bbf9', alpha=0.15, label='[-1] Фаза Волны')
    
    ax2.set_xlabel('Пространственная координата поля', color='white', fontsize=11)
    ax2.set_ylabel('Квантовая Шкала Энергии', color='white', fontsize=11)
    ax2.set_yticks([-1, 0, 1])
    ax2.set_yticklabels(['-1 (Волна / Распад)', '0 (Точка X / Баланс)', '+1 (Частица / Масса)'])
    ax2.legend(facecolor='#1a1a1a', edgecolor='#444444', textcolor='white', loc='lower right')
    ax2.grid(True, alpha=0.15, linestyle=':')
    ax2.set_facecolor('#0d1117')

    # Общая стилизация окна под квантовый интерфейс
    fig.patch.set_facecolor('#070a10')
    ax1.tick_params(colors='white')
    ax2.tick_params(colors='white')
    ax1.axhline(0, color='white', linewidth=0.5, alpha=0.3)
    ax2.axhline(0, color='white', linewidth=0.5, alpha=0.5)
    
    plt.tight_layout()
    print("📈 Симуляция успешно построена. Окно графика открыто.")
    plt.show()

if __name__ == '__main__':
    main()
