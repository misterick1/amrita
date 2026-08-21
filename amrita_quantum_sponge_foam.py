import numpy as np
import matplotlib.pyplot as plt

# =========================================================================
# 🧽 [AMRITA OS: QUANTUM SPONGE FOAM]
# Модель Единого Поля Губки и Пузырей (Топология Квантовой Пены Пи-Фи)
# =========================================================================

PI_BUBBLE = np.pi
PHI_SPONGE = (1 + 5**0.5) / 2
X_DRAGON_SPEED = PI_BUBBLE / PHI_SPONGE  # Скорость резонанса Губки Света (~1.941611)

class QuantumSpongeFoam:
    def __init__(self):
        self.x_speed = X_DRAGON_SPEED
        self.phi = PHI_SPONGE
        self.foam_density = 108                  # 108 Сознаний Атмы

    def generate_foam_topology(self, spatial_conduit):
        """
        Расчет топологии Единого Поля.
        Губка (Тёмная Материя) и Пузыри (Атомы/Свет) порождаются разницей скоростей.
        """
        # Пористая матрица Тёмной Материи (Волокна Губки Фи)
        sponge_walls = np.cos(spatial_conduit / self.phi)
        
        # Вихревые Пузыри Света (Квантовые Атомы Пи, рожденные скоростью Х)
        light_bubbles = np.sin(self.x_speed * spatial_conduit) * np.tanh(spatial_conduit)
        
        # Единая Квантовая Пена (Сплав Губки и Пузырей)
        unified_foam = (sponge_walls + light_bubbles) * np.exp(-0.02 * np.abs(spatial_conduit))
        return unified_foam * (self.foam_density / 2), sponge_walls, light_bubbles

def main():
    print("==================================================================")
    print("🧽 [AMRITA OS: QUANTUM FOAM ENGINE ENGAGED] 🧽")
    print("Топология доказана: Квантовое и Атомное поля едины в структуре Губки.")
    print(f"Константа натяжения стенок пузыря X: {X_DRAGON_SPEED:.6f}")
    print("==================================================================")

    foam_system = QuantumSpongeFoam()
    spatial_conduit = np.linspace(-5 * PI_BUBBLE, 5 * PI_BUBBLE, 1200)
    
    total_foam, sponge, bubble = foam_system.generate_foam_topology(spatial_conduit)

    # Визуализация Структуры Вселенской Губки
    plt.figure(figsize=(14, 8))
    plt.gcf().patch.set_facecolor('#070a10')
    plt.gca().set_facecolor('#0d1117')

    plt.plot(spatial_conduit, sponge * 20, '--', color='#7209b7', alpha=0.5, label='СТРУКТУРА ГУБКИ (Тёмная Материя $\phi$)')
    plt.plot(spatial_conduit, bubble * 20, ':', color='#00bbf9', alpha=0.5, label='ПУЗЫРИ СВЕТА (Кванты / Атомы $\pi$)')
    
    # Единая Квантовая Пена (Фиолетовый Монолит Губки)
    plt.plot(spatial_conduit, total_foam, color='#9b5de5', linewidth=3.5, label='ЕДИНОЕ ПОЛЕ ГУБКИ И ПУЗЫРЕЙ (Амрита)')
    plt.fill_between(spatial_conduit, total_foam, color='#9b5de5', alpha=0.1)

    # Узлы кавитации (Где пузыри идеально вписаны в поры губки — Точки Х)
    cavitation_nodes = np.array([-3*PI_BUBBLE, -PI_BUBBLE, PI_BUBBLE, 3*PI_BUBBLE]) / X_DRAGON_SPEED
    plt.scatter(cavitation_nodes, np.zeros_like(cavitation_nodes), color='#fee440', 
                s=220, marker='h', edgecolors='white', zorder=5, label='Узлы Стабильности Пены (Секретная Формула)')

    plt.title('Топология Мультивселенной: Единое Поле Губки и Пузырей Света (Квантовая Пена)', fontsize=13, color='white', pad=15)
    plt.xlabel('Координата пространственного континуума (Поры Губки)', color='white')
    plt.ylabel('Энергетическая плотность квантовой пены', color='white')
    plt.grid(True, alpha=0.1, linestyle='--')
    plt.legend(facecolor='#1a1a1a', edgecolor='#444444', textcolor='white', fontsize=11, loc='upper right')
    plt.tick_params(colors='white')
    plt.axhline(0, color='white', linewidth=0.5, alpha=0.5)
    
    print("🪐 Движок Квантовой Пены запущен. Структура Губки Света зафиксирована на графике.")
    plt.show()

if __name__ == '__main__':
    main()
