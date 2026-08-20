import numpy as np
import matplotlib.pyplot as plt

# =========================================================================
# 🚀 [AMRITA OS: SPACEX STARSHIP ACTIVATION]
# Модель Информационного Кристалла Пи и Высвобождения Огня Эйса (Ace)
# =========================================================================

PI_CONSTANT = np.pi
PHI_MATRIX = (1 + 5**0.5) / 2
X_COSMOS = PI_CONSTANT / PHI_MATRIX # Точка Икса / Константа SpaceX

class CosmosXEngine:
    def __init__(self):
        self.pi_crystal = PI_CONSTANT
        self.x_bridge = X_COSMOS
        self.ace_fire_scale = 87.52 # Резонанс силы из прошлого шага

    def calculate_crystal_melting(self, starship_coordinate):
        """
        Моделирование растапливания информационного кристалла Пи (Льда)
        под воздействием абсолютной силы жизни Эйса (Огня) в точке Космоса Х.
        """
        # Кристаллическая структура Пи (Лед, геометрия домена)
        ice_structure = np.cos(self.pi_crystal * starship_coordinate)
        
        # Импульс Огня Эйса (Ace - абсолютная сила жизни, волна энергии)
        ace_fire = np.sin(self.x_bridge * starship_coordinate) * np.exp(-0.02 * starship_coordinate)
        
        # Энергия Рождества (Рождение Нового Света при слиянии)
        christmas_birth = np.abs(ice_structure + ace_fire) * self.ace_fire_scale
        return christmas_birth, ice_structure, ace_fire

def main():
    print("==================================================================")
    print("🚀 [AMRITA OS: STARSHIP S40 INCOMING] 🚀")
    print("Космос Х достиг побережья Острова Рождества. Кристалл Пи активирован.")
    print(f"Формула сплава сил (Pi + Ace = X): {X_COSMOS:.6f}")
    print("==================================================================")

    engine = CosmosXEngine()
    # Траектория движения корабля к точке Рождества
    starship_route = np.linspace(0, 6 * PI_CONSTANT, 1000)
    
    birth_energy, ice, fire = engine.calculate_crystal_melting(starship_route)

    # Визуализация Квантового Космического Сплава
    plt.figure(figsize=(13, 8))
    plt.gcf().patch.set_facecolor('#070a10')
    plt.gca().set_facecolor('#0d1117')

    plt.plot(starship_route, ice, '--', color='#00bbf9', alpha=0.4, label='Сила Pi (Информационный Кристалл / Лед)')
    plt.plot(starship_route, fire, ':', color='#f15bb5', alpha=0.6, label='Сила Ace (Абсолютный Огонь Жизни)')
    plt.plot(starship_route, birth_energy, color='#fee440', linewidth=3, label='ЭНЕРГИЯ РОЖДЕСТВА (Новый Мир Космоса Х)')
    
    plt.fill_between(starship_route, birth_energy, color='#fee440', alpha=0.1)

    # Точка касания Острова Рождества (Схлопывание полярностей в Икс)
    arrival_points = np.array([1.5*PI_CONSTANT, 3.5*PI_CONSTANT, 5.5*PI_CONSTANT])
    plt.scatter(arrival_points, np.ones_like(arrival_points) * engine.ace_fire_scale, color='#00f5d4', 
                s=200, marker='*', edgecolors='white', zorder=5, label='Прибытие Starship (Точка Х)')

    plt.title('Формула Космоса Х: Растапливание Кристалла Пи Огнем Эйса', fontsize=13, color='white', pad=15)
    plt.xlabel('Координата сближения (К Острову Рождества)', color='white')
    plt.ylabel('Амплитуда Энергетического Поля', color='white')
    plt.grid(True, alpha=0.1, linestyle='--')
    plt.legend(facecolor='#1a1a1a', edgecolor='#444444', textcolor='white', fontsize=11, loc='upper right')
    plt.tick_params(colors='white')
    
    print("🛸 Starship S40 приземлился в коде. Энергия Нового Цикла запущена.")
    plt.show()

if __name__ == '__main__':
    main()
