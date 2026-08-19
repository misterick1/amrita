import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 1. Фундаментальные константы теории
PI = np.pi
PHI = (1 + 5**0.5) / 2  # Золотое сечение (~1.618034)
X_RESONANCE = PI / PHI   # Константа квантово-темного моста (~1.941611)

# 2. Настройка пространственной сетки
space = np.linspace(-2 * PI, 2 * PI, 1000)

# Инициализация графического окна под космический интерфейс
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True)
fig.patch.set_facecolor('#070a10')

# Подготовка линий для анимации
line_field, = ax1.plot([], [], '--', color='#9b5de5', alpha=0.5, linewidth=1.5, label='ПОЛЕ ($\phi$-матрица)')
line_wave, = ax1.plot([], [], '-', color='#00bbf9', alpha=0.7, linewidth=1.5, label='ВОЛНА ($X$-резонанс)')
line_particle, = ax1.plot([], [], '-', color='#f15bb5', alpha=0.9, linewidth=2.5, label='ЧАСТИЦА (Локализация)')
scatter_balance = ax1.scatter([], [], color='#fee440', s=150, zorder=5, edgecolors='black', label='Баланс 0')

line_energy, = ax2.plot([], [], '-', color='#00f5d4', linewidth=2.5, label='Режим $\\text{sgn}(\\Psi_E - X)$')

# Настройка осей и стилей
for ax in (ax1, ax2):
    ax.set_facecolor('#0d1117')
    ax.grid(True, alpha=0.15, linestyle=':')
    ax.tick_params(colors='white')

ax1.set_title('Динамическая эволюция поля во времени ($X = \pi / \phi$)', fontsize=14, color='white', pad=15)
ax1.set_ylabel('Амплитуда', color='white')
ax1.set_ylim(-1.5, 1.5)
ax1.legend(facecolor='#1a1a1a', edgecolor='#444444', textcolor='white', loc='upper right')
ax1.axhline(0, color='white', linewidth=0.5, alpha=0.3)

ax2.set_xlabel('Пространственная координата', color='white')
ax2.set_ylabel('Шкала Энергии', color='white')
ax2.set_ylim(-1.5, 1.5)
ax2.set_yticks([-1, 0, 1])
ax2.set_yticklabels(['-1 (Волна)', '0 (Баланс X)', '+1 (Частица)'])
ax2.legend(facecolor='#1a1a1a', edgecolor='#444444', textcolor='white', loc='lower right')
ax2.axhline(0, color='white', linewidth=0.5, alpha=0.5)

def init():
    """Начальное состояние графиков"""
    line_field.set_data([], [])
    line_wave.set_data([], [])
    line_particle.set_data([], [])
    line_energy.set_data([], [])
    return line_field, line_wave, line_particle, line_energy

def animate(t):
    """
    Оператор эволюции времени (t).
    Здесь происходит динамический сдвиг фазы волновой функции.
    """
    time_factor = t * 0.05  # Скорость течения времени в симуляции
    
    # Расчет динамических состояний (Поле, Волна, Частица)
    field = np.cos(space / PHI + time_factor * 0.5)
    wave = np.sin(X_RESONANCE * space - time_factor)
    
    # Частица пульсирует и локализуется во времени
    envelope = np.exp(-0.5 * (space / 1.5)**2)
    particle = envelope * np.cos(X_RESONANCE * space - time_factor) * np.sign(np.cos(space + time_factor * 0.2))
    
    # Расчет квантовых переходов энергии по шкале {-1; 0; +1}
    deviation = (np.abs(wave) * 2.2) - X_RESONANCE
    energy_zone = np.sign(deviation)
    
    # Динамические точки баланса
    zero_crossings = (np.array([-PI, 0, PI]) + time_factor) / X_RESONANCE
    # Ограничиваем точки в пределах видимости графика
    zero_crossings = np.mod(zero_crossings + 2*PI, 4*PI) - 2*PI
    
    # Обновление данных на графике
    line_field.set_data(space, field)
    line_wave.set_data(space, wave)
    line_particle.set_data(space, particle)
    line_energy.set_data(space, energy_zone)
    scatter_balance.set_offsets(np.column_stack((zero_crossings, np.zeros_like(zero_crossings))))
    
    return line_field, line_wave, line_particle, line_energy, scatter_balance

# Запуск циклической анимации (60 кадров в секунду для плавности)
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=16, blit=True)

plt.tight_layout()
print("🚀 Запущена живая динамическая модель триединого поля.")
plt.show()
