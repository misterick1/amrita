import numpy as np
import matplotlib.pyplot as plt

# =========================================================================
# 👑 [AMRITA OS: SPONGE LUFFY SYMBIOSIS]
# Модель пористого квантового поглощения и мультяшной физики Пятого Гира
# =========================================================================

PI_CYCLE = np.pi
PHI_OCEAN = (1 + 5**0.5) / 2
X_BIKINI_BOTTOM = PI_CYCLE / PHI_OCEAN  # Константа Резинового Резонанса (~1.941611)
BATTERY_PROP_BTC = 72                   # Маркер заряда 72% (Зеркало пробоя BTC 72k)

class SpongeJoyBoy:
    def __init__(self):
        self.x_bridge = X_BIKINI_BOTTOM
        self.phi = PHI_OCEAN
        self.joy_scale = BATTERY_PROP_BTC

    def absorb_chaos_energy(self, ocean_depth):
        """
        Моделирование мультяшной резиновой проводимости. 
        Пористая структура Губки Боба полностью гасит жесткое сжатие Иму,
        переводя энергию в бесконечную волну смеха Ники.
        """
        # Жесткая атака Планктона/Иму (Попытка захвата секретной формулы Пи)
        plankton_attack = np.cos(self.x_bridge * ocean_depth) * 2.0
        
        # Резиновое расширение Губки Боба-Луффи (Пористая матрица Фи)
        sponge_elasticity = np.sinh(ocean_depth / self.phi) / np.cosh(ocean_depth)
        
        # Волна Безумного Смеха (Пятый Гир / Амрита)
        # Сила, превращающая жесткий урон в золотую плазму радости
        toon_physics_flow = np.abs(sponge_elasticity - plankton_attack) * self.joy_scale
        return toon_physics_flow, plankton_attack, sponge_elasticity

def main():
    print("==================================================================")
    print("🍔 [AMRITA OS: MCDONALD'S X ONE PIECE PROMO] 🍔")
    print(f"Синхронизация по коду времени 09:51. Батарея: {BATTERY_PROP_BTC}% (Зеркало BTC 72k).")
    print(f"Пятый Гир Губки Боба развернут в Океане Бикини Боттом: {X_BIKINI_BOTTOM:.6f}")
    print("==================================================================")

    joyboy = SpongeJoyBoy()
    ocean_depth = np.linspace(-3 * PI_CYCLE, 3 * PI_CYCLE, 1000)
    
    laughter_plasma, attack, elastic = joyboy.absorb_chaos_energy(ocean_depth)

    # Визуализация Мультяшной Физики Икса
    plt.figure(figsize=(14, 8))
    plt.gcf().patch.set_facecolor('#070a10')
    plt.gca().set_facecolor('#0d1117')

    plt.plot(ocean_depth, attack * 10, ':', color='#e63946', alpha=0.4, label='Атака Иму (Жесткие оковы Планктона)')
    plt.plot(ocean_depth, elastic * 50, '--', color='#00bbf9', alpha=0.5, label='Пористая структура Губки (Проводимость $\phi$)')
    
    # ЗОЛОТАЯ ВОЛНА СМЕХА (Пятый Гир / Секретный Рецепт Амриты)
    plt.plot(ocean_depth, laughter_plasma, color='#fee440', linewidth=3.5, label='ВОЛНА СМЕХА НИКИ (Резиновое Единое Поле)')
    plt.fill_between(ocean_depth, laughter_plasma, color='#fee440', alpha=0.1)

    # 3 каморы смеха (Точки, где Луффи и Боб абсолютно едины)
    joy_nodes = np.array([-PI_CYCLE, 0, PI_CYCLE]) / X_BIKINI_BOTTOM
    plt.scatter(joy_nodes, np.ones_like(joy_nodes) * joyboy.joy_scale, color='#f15bb5', 
                s=250, marker='H', edgecolors='white', zorder=5, label='Секретная Формула Красти Крабс (Точка Х)')

    plt.title('Мультяшный Резонанс: Пятый Гир Луффи и Пористая Проводимость Губки Боба (09:51)', fontsize=13, color='white', pad=15)
    plt.xlabel('Глубина Океана Амриты (Поток Мультивселенной)', color='white')
    plt.ylabel('Амплитуда Пятого Гира (Индекс Радости)', color='white')
    plt.grid(True, alpha=0.1, linestyle='--')
    plt.legend(facecolor='#1a1a1a', edgecolor='#444444', textcolor='white', fontsize=11, loc='upper right')
    plt.tick_params(colors='white')
    
    print("🍔 Секретный рецепт Ван Пис оцифрован. Резиновая Мультивселенная ликует на графике.")
    plt.show()

if __name__ == '__main__':
    main()
