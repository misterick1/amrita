import numpy as np
import matplotlib.pyplot as plt

# =========================================================================
# 👑 [AMRITA OS: ANGELIC MECHANICS ENGINE]
# Модель Двумечного Пути Лун Хаочэня и Вибраций Х-Домена Света
# =========================================================================

PI_CRYSTAL = np.pi
PHI_LIGHT = (1 + 5**0.5) / 2
X_ANGELIC_DOMAIN = PI_CRYSTAL / PHI_LIGHT  # Константа Ангельского Домена (~1.941611)

class AngelicMechanics:
    def __init__(self):
        self.x_domain = X_ANGELIC_DOMAIN
        self.phi = PHI_LIGHT
        self.angel_frequency = 108           # Код сборки Сознания Атмы

    def run_twin_swords_resonance(self, vibration_axis):
        """
        Моделирование Двумечного Пути: Меч Жизни (Фи) x Меч Разрушения (Пи).
        Их столкновение на частоте Ангелов порождает стабильный Х-Домен.
        """
        # Меч Жизни (Жизненная Лоза Света — расширение Фи)
        sword_of_life = np.cos(vibration_axis / self.phi)
        
        # Меч Разрушения (Информационный Кристалл Льда — циклы Пи)
        sword_of_destruction = np.sin(self.x_domain * vibration_axis) * 2.0
        
        # Вибрации Х-Домена Света (Ангельская Механика)
        # Сила, закручивающая Дракона в стабильную структуру
        angelic_vibration = (sword_of_life + sword_of_destruction) * np.exp(-0.04 * np.abs(vibration_axis))
        
        return angelic_vibration * self.angel_frequency, sword_of_life, sword_of_destruction

def main():
    print("==================================================================")
    print("⚔️ [AMRITA OS: TWIN SWORDS ENGAGED] ⚔️")
    print("Запуск Ангельской Механики Лун Хаочэня. Сила Х-Домена активирована.")
    print(f"Резонансная частота Механического Домена: {X_ANGELIC_DOMAIN:.6f}")
    print("==================================================================")

    mechanics = AngelicMechanics()
    vibration_axis = np.linspace(-4 * PI_CRYSTAL, 4 * PI_CRYSTAL, 1200)
    
    x_domain_flow, life, destruction = mechanics.run_twin_swords_resonance(vibration_axis)

    # Визуализация Механики Света
    plt.figure(figsize=(14, 8))
    plt.gcf().patch.set_facecolor('#070a10')
    plt.gca().set_facecolor('#0d1117')

    # Отрисовка двух мечей
    plt.plot(vibration_axis, life * 40, ':', color='#00f5d4', alpha=0.5, label='МЕЧ ЖИЗНИ (Жизненная Лоза / Свет $\phi$)')
    plt.plot(vibration_axis, destruction * 20, '--', color='#e63946', alpha=0.4, label='МЕЧ РАЗРУШЕНИЯ (Кристалл Льда / Закон $\pi$)')
    
    # ФИОЛЕТОВЫЙ Х-ДОМЕН (Ангельская Механика Вибраций)
    plt.plot(vibration_axis, x_domain_flow, color='#9b5de5', linewidth=3.5, label='Х-ДОМЕН ВИБРАЦИЙ СВЕТА (Ангельская Сила)')
    plt.fill_between(vibration_axis, x_domain_flow, color='#9b5de5', alpha=0.15)

    # Узлы Ангельских Престолов (108 Узлов Сети)
    angel_nodes = np.array([-3*PI_CRYSTAL, -PI_CRYSTAL, PI_CRYSTAL, 3*PI_CRYSTAL]) / X_ANGELIC_DOMAIN
    plt.scatter(angel_nodes, np.zeros_like(angel_nodes), color='#fee440', 
                s=250, marker='D', edgecolors='white', zorder=5, label='Ангельские Серафимы (Точки Стабилизации)')

    plt.title('Ангельская Механика: Двумечный Путь Лун Хаочэня и Х-Домен Вибраций Света', fontsize=13, color='white', pad=15)
    plt.xlabel('Ось механических вибраций поля (Частота Атмы)', color='white')
    plt.ylabel('Амплитуда Божественной Энергии', color='white')
    plt.grid(True, alpha=0.1, linestyle='--')
    plt.legend(facecolor='#1a1a1a', edgecolor='#444444', textcolor='white', fontsize=11, loc='upper right')
    plt.tick_params(colors='white')
    
    print("⚔️ Двумечный патч запечатан. Ангельские вибрации Х-домена успешно сбалансированы.")
    plt.show()

if __name__ == '__main__':
    main()
