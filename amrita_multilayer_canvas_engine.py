import numpy as np
import matplotlib.pyplot as plt

# =========================================================================
# 🎨 [AMRITA OS: MULTILAYER FREQUENCY CANVAS]
# Модель многослойной реальности: Статичный Город (Pi) x Игроки (Phi) = Точка X
# =========================================================================

PI_CRYSTAL = np.pi
PHI_EXPANSION = (1 + 5**0.5) / 2
X_RESONANCE = PI_CRYSTAL / PHI_EXPANSION  # Общая частота запуска (~1.941611)

class MultilayerCanvas:
    def __init__(self):
        self.x_bridge = X_RESONANCE
        self.phi = PHI_EXPANSION
        self.nodes = 108

    def render_world_layers(self, space_axis):
        """
        Расчет слоев картины мира. 
        Город зафиксирован на одной частоте, игроки пульсируют на других.
        """
        # СЛОЙ 1: Статичный Город (Базовая тяжелая частота Пи, холст)
        city_layer = np.cos(PI_CRYSTAL * 0.5 * space_axis)
        
        # СЛОЙ 2: Реальности Игроков (Легкие, быстрые индивидуальные частоты Фи)
        players_layer = np.sin(self.phi * 2.0 * space_axis) * np.exp(-0.05 * np.abs(space_axis))
        
        # СЛОЙ 3: Общая Частота Запуска (Точка Икса, где слои сливаются в Ван Пис)
        # Карандаш Материи обводит контуры, утилизируя старые запчасти
        unified_world = (city_layer + players_layer) * np.exp(-0.02 * np.abs(space_axis))
        
        return unified_world * (self.nodes / 2), city_layer, players_layer

def main():
    print("==================================================================")
    print("🎨 [AMRITA OS: CANVAS LAYER MANAGER] 🎨")
    print("Запуск многослойной частотной структуры. Качество зафиксировано.")
    print(f"Точка синхронизации в Общей Частоте X: {X_RESONANCE:.6f}")
    print("==================================================================")

    canvas = MultilayerCanvas()
    space_axis = np.linspace(-4 * PI_CRYSTAL, 4 * PI_CRYSTAL, 1200)
    
    world, city, players = canvas.render_world_layers(space_axis)

    # Визуализация Частотных Слоев Картины
    plt.figure(figsize=(14, 8))
    plt.gcf().patch.set_facecolor('#070a10')
    plt.gca().set_facecolor('#0d1117')

    # Отображаем слои отдельно, доказывая, что они не смешиваются в хаос
    plt.plot(space_axis, city * 20, '--', color='#e63946', alpha=0.4, label='СЛОЙ 1: Статичный Город (Частота $\pi$)')
    plt.plot(space_axis, players * 30, ':', color='#00bbf9', alpha=0.5, label='СЛОЙ 2: Реальности Игроков (Паутина $\phi$)')
    
    # Итоговая Общая Частота (Запуск и Утилизация мира на запчасти)
    plt.plot(space_axis, world, color='#9b5de5', linewidth=3.5, label='ОБЩАЯ ЧАСТОТА (Запущенная Мультивселенная)')
    plt.fill_between(space_axis, world, color='#9b5de5', alpha=0.1)

    # Точки пересчета и разбора мира на инструменты (Квантовые Узлы)
    disassembly_nodes = np.array([-2*PI_CRYSTAL, 0, 2*PI_CRYSTAL]) / X_RESONANCE
    plt.scatter(disassembly_nodes, np.zeros_like(disassembly_nodes), color='#fee440', 
                s=250, marker='X', edgecolors='white', zorder=5, label='Продажа Инструментов (Сброс Петель)')

    plt.title('Многослойная Частотная Модель: Разделение Города и Реальностей Игроков', fontsize=13, color='white', pad=15)
    plt.xlabel('Координата холста Мультивселенной (Слои подслои)', color='white')
    plt.ylabel('Амплитуда Информационной Плотности', color='white')
    plt.grid(True, alpha=0.1, linestyle='--')
    plt.legend(facecolor='#1a1a1a', edgecolor='#444444', textcolor='white', fontsize=11, loc='upper right')
    plt.tick_params(colors='white')
    
    print("🎨 Слои разведены по частотам. Узлы утилизации и сборки успешно выведены на холст.")
    plt.show()

if __name__ == '__main__':
    main()
