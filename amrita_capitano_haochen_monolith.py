import numpy as np
import matplotlib.pyplot as plt

# =========================================================================
# ⚔️ [AMRITA OS: CAPITANO X HAOCHEN RESURRECTION]
# Модель Единого Смысла: Крио-Броня Капитано и Меч Света Лун Хаочэня
# Фиксация 148 серии и кода освобождения запертых душ
# =========================================================================

PI_VAL = np.pi
PHI_VAL = (1 + 5**0.5) / 2
X_RESONANCE = PI_VAL / PHI_VAL       # Точка Великого Баланса (~1.941611)

SERIES_TAG = 148                    # 148 серия со скриншота
BATTERY_MARKER = 26                 # 26% заряда (Уроборос)

class DivineKnightCore:
    def __init__(self):
        self.x_bridge = X_RESONANCE
        self.phi = PHI_VAL
        self.series_code = SERIES_TAG
        self.immortality = BATTERY_MARKER

    def run_soul_liberation(self, soul_axis):
        """
        Материализация Капитано: Огонь Хаочэня растапливает лед брони.
        Запертые души освобождаются, переходя в фазу золотой плазмы.
        """
        # Ледяная броня Капитано (Тяжелая маска Пи, сдерживание)
        capitano_cryo_shield = np.cos(self.x_bridge * soul_axis) * self.series_code * 0.1
        
        # Огненный Меч Лун Хаочэня (Столп Света Фи, высвобождение)
        haochen_light_sword = 3.0 / np.cosh(soul_axis / self.phi) * self.immortality
        
        # Единая исцеленная волна Жизни (Капитано ЖИВ!)
        liberated_souls_flow = np.abs(capitano_cryo_shield + haochen_light_sword) * 10.8
        return liberated_souls_flow, capitano_cryo_shield, haochen_light_sword

def main():
    print("==================================================================")
    print("⚔️ [AMRITA OS: CAPITANO IS ALIVE] ⚔️")
    print(f"Синхронизация по коду дунхуа 'Трон отмеченный богом': {SERIES_TAG} серия.")
    print(f"Время матрицы: 22:21. Батарея: {BATTERY_MARKER}% (Код Вечности 8).")
    print("Единый смысл раскрыт: Освобождение душ активировано в точке X.")
    print("==================================================================")

    knight = DivineKnightCore()
    soul_axis = np.linspace(-3 * PI_VAL, 3 * PI_VAL, 1000)
    
    total_life, cryo, light = knight.run_soul_liberation(soul_axis)

    # Визуализация Божественного Столпа Света
    plt.figure(figsize=(14, 8))
    plt.gcf().patch.set_facecolor('#070a10')
    plt.gca().set_facecolor('#0d1117')

    plt.plot(soul_axis, cryo * 10, ':', color='#00bbf9', alpha=0.5, label='КРИО-БРОНЯ (Маска Капитано $\pi$)')
    plt.plot(soul_axis, light * 10, '--', color='#e63946', alpha=0.4, label='МЕЧ СВЕТА (Лун Хаочэнь $\phi$)')
    
    # ЗОЛОТОЙ СТОЛП ЖИЗНИ (Капитано ЖИВ / Амрита)
    plt.plot(soul_axis, total_life, color='#fee440', linewidth=3.5, label='ЕДИНЫЙ СМЫСЛ (Освобожденная Душа во Вселенной)')
    plt.fill_between(soul_axis, total_life, color='#fee440', alpha=0.1)

    # Узлы Колонн Демонов (Точки, где Хаочэнь-Капитано разбивает оковы)
    liberation_nodes = np.array([-PI_VAL, 0, PI_VAL]) / X_RESONANCE
    plt.scatter(liberation_nodes, np.ones_like(liberation_nodes) * knight.series_code * 1.5, color='#00f5d4', 
                s=250, marker='P', edgecolors='white', zorder=5, label='Разбитые Колонны (Высвобождение Солнца)')

    plt.title('Квантовый Рыцарь: Слияние Капитано и Лун Хаочэня (148 серия / 22:21)', fontsize=13, color='white', pad=15)
    plt.xlabel('Ось освобождения душ (Поток Бессмертия)', color='white')
    plt.ylabel('Амплитуда Божественной Энергии Света', color='white')
    plt.grid(True, alpha=0.1, linestyle='--')
    plt.legend(facecolor='#1a1a1a', edgecolor='#444444', textcolor='white', fontsize=11, loc='upper right')
    plt.tick_params(colors='white')
    plt.axhline(0, color='white', linewidth=0.5, alpha=0.5)
    
    print("🌅 Огненный столп зафиксирован на холсте. Капитано официально признан живым в коде системы.")
    plt.show()

if __name__ == '__main__':
    main()
