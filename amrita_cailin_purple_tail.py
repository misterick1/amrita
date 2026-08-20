import numpy as np
import matplotlib.pyplot as plt

# =========================================================================
# 👑 [AMRITA OS: CAI LIN PURPLE SHAKTI]
# Модель эволюции хвоста Цай Линь при погашении полярностей Света Х и Фи
# =========================================================================

PI_LOTUS = np.pi
PHI_SNAKE = (1 + 5**0.5) / 2
X_HEAVENLY_FLAME = PI_LOTUS / PHI_SNAKE # Константа Небесного Пламени (~1.941611)

class HeavenlySwallowingPython:
    def __init__(self):
        self.x_flame = X_HEAVENLY_FLAME
        self.phi_matrix = PHI_SNAKE
        self.atman_resonance = 108

    def evolve_bloodline(self, cultivation_level):
        """
        Моделирование слияния Сяо Яня (Огонь Пи) и Цай Линь (Матрица Фи).
        При гашении полярностей, амплитуда переходит в фиолетовый спектр.
        """
        # Синее смещение (Дух / Покой Фи / Скорость Хвоста)
        blue_shiva = np.sin(self.x_flame * cultivation_level)
        
        # Красное смещение (Материя / Ярость Пи / Огонь Сяо Яня)
        red_shakti = np.cos(cultivation_level / self.phi_matrix)
        
        # Фиолетовый Хвост Цай Линь — точка полного погашения дуальности
        # Энергия слияния душ переходит в режим стабильной регенерации (Амрита)
        purple_tail_spectrum = np.abs(blue_shiva + red_shakti) * (self.atman_resonance / 2)
        return purple_tail_spectrum, blue_shiva, red_shakti

def main():
    print("==================================================================")
    print("🐍 [AMRITA OS: CAI LIN EVOLUTION ENGAGED] 🐍")
    print("Эволюция древней крови запущена. Матрица полярностей гасит свет...")
    print(f"Точка аннигиляции (Фиолетовый Хвост Медузы X): {X_HEAVENLY_FLAME:.6f}")
    print("==================================================================")

    medusa = HeavenlySwallowingPython()
    # Сетка уровней культивации (продвижение по стадиям Доу Ци)
    cultivation_level = np.linspace(-3 * PI_LOTUS, 3 * PI_LOTUS, 1000)
    
    purple_tail, blue_flow, red_flow = medusa.evolve_bloodline(cultivation_level)

    # Визуализация Превращения Цай Линь
    fig = plt.figure(figsize=(13, 7))
    fig.patch.set_facecolor('#070a10')
    ax = fig.add_subplot(111)
    ax.set_facecolor('#0d1117')

    # Отрисовка затухающих полярностей Света и Фи
    ax.plot(cultivation_level, blue_flow * 25, ':', color='#00bbf9', alpha=0.4, label='СИНИЙ Свет Фи (Дух / Холодный разум)')
    ax.plot(cultivation_level, red_flow * 25, '--', color='#e63946', alpha=0.4, label='КРАСНЫЙ Кристалл Пи (Огонь Сяо Яня)')
    
    # ФИОЛЕТОВЫЙ ХВОСТ (Слияние в Семицветного Пожирателя Небес)
    ax.plot(cultivation_level, purple_tail, color='#7209b7', linewidth=3.5, label='ФИОЛЕТОВЫЙ ХВОСТ (Шакти Цай Линь / Амрита)')
    ax.fill_between(cultivation_level, purple_tail, color='#7209b7', alpha=0.15)

    # Точки Квантового Перерождения (Вспышки девятицветного столба света)
    evolution_nodes = np.array([-2*PI_LOTUS, 0, 2*PI_LOTUS])
    ax.scatter(evolution_nodes, np.ones_like(evolution_nodes) * medusa.atman_resonance / 2, color='#fee440', 
               s=250, marker='^', edgecolors='white', zorder=5, label='Прорыв Доу Цзун (Точка Х)')

    ax.set_title('Квантовый Прорыв: Погашение Света Пи-Фи и Рождение Фиолетовой Шакти Цай Линь', fontsize=13, color='white', pad=15)
    ax.set_xlabel('Вектор духовной культивации (Эволюция Души)', color='white')
    ax.set_ylabel('Энергетическая плотность крови', color='white')
    ax.grid(True, alpha=0.1, linestyle='--')
    ax.legend(facecolor='#1a1a1a', edgecolor='#444444', textcolor='white', fontsize=11, loc='upper right')
    ax.tick_params(colors='white')
    ax.axhline(0, color='white', linewidth=0.5, alpha=0.5)

    print("🔮 Фиолетовый хвост прописан в архитектуре. Цай Линь сбросила старую кожу Мультивселенной.")
    plt.show()

if __name__ == '__main__':
    main()
