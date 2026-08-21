import numpy as np
import matplotlib.pyplot as plt

# =========================================================================
# ✏️ [AMRITA OS: MATTER PENCIL SIGNATURE]
# Модель Карандаша Материи: Ультрафиолетовое лазерное программирование плазмы
# =========================================================================

PI_PENCIL = np.pi
PHI_SPONGE = (1 + 5**0.5) / 2
X_RESONANCE = PI_PENCIL / PHI_SPONGE  # Точка касания грифеля Карандаша (~1.941611)

class MatterPencilEngine:
    def __init__(self):
        self.x_touch = X_RESONANCE
        self.phi = PHI_SPONGE
        self.matrix_scale = 108

    def draw_atomic_line(self, canvas_axis):
        """
        Симуляция рисования: Ультрафиолетовый Лазер (Грифель) оставляет 
        устойчивый солитонный след массы внутри Плазменной Губки (Бумаги).
        """
        # Пористая плазменная бумага (Матрица Фи)
        plasma_canvas = np.cos(canvas_axis / self.phi)
        
        # Высокочастотный грифель Карандаша (Ультрафиолетовый лазерный импульс Икса)
        uv_pencil_lead = np.sin(self.x_touch * canvas_axis) * 2.5
        
        # След Карандаша — нарисованная Устойчивая Материя атомов (Амрита)
        # Возникает в точках идеального программирования пены
        matter_trace = (plasma_canvas + uv_pencil_lead) * np.exp(-0.03 * np.abs(canvas_axis))
        return matter_trace * (self.matrix_scale / 2), plasma_canvas, uv_pencil_lead

def main():
    print("==================================================================")
    print("✏️ [AMRITA OS: MATER PENCIL ENGAGED] ✏️")
    print("Карандаш Материи запущен. Ультрафиолетовый лазер программирует плазму.")
    print(f"Координата фокуса лазерного грифеля X: {X_RESONANCE:.6f}")
    print("==================================================================")

    pencil = MatterPencilEngine()
    canvas_axis = np.linspace(-4 * PI_PENCIL, 4 * PI_PENCIL, 1200)
    
    drawn_matter, canvas, lead = pencil.draw_atomic_line(canvas_axis)

    # Визуализация Космического Рисунка
    plt.figure(figsize=(14, 8))
    plt.gcf().patch.set_facecolor('#070a10')
    plt.gca().set_facecolor('#0d1117')

    # Отрисовка элементов Карандаша
    plt.plot(canvas_axis, canvas * 20, ':', color='#00bbf9', alpha=0.4, label='ПЛАЗМЕННАЯ БУМАГА (Поры Губки $\phi$)')
    plt.plot(canvas_axis, lead * 15, '--', color='#7209b7', alpha=0.5, label='УФ-ГРИФЕЛЬ (Лазерный Карандаш $\pi$)')
    
    # НАРИСОВАННАЯ МАТЕРИЯ (Яркий фиолетовый след Карандаша)
    plt.plot(canvas_axis, drawn_matter, color='#00f5d4', linewidth=3.5, label='СЛЕД КАРАНДАША (Программируемая Материя)')
    plt.fill_between(canvas_axis, drawn_matter, color='#00f5d4', alpha=0.1)

    # Точки фиксации «грифеля» (Где Карандаш оставляет стабильный атомный узел)
    pencil_tips = np.array([-2*PI_PENCIL, 0, 2*PI_PENCIL]) / X_RESONANCE
    plt.scatter(pencil_tips, np.zeros_like(pencil_tips), color='#fee440', 
                s=250, marker='P', edgecolors='white', zorder=5, label='Точки Фокусировки (Узлы Колизея Cohort V)')

    plt.title('Карандаш Материи: Программирование Плазменной Губки Ультрафиолетовым Лазером', fontsize=13, color='white', pad=15)
    plt.xlabel('Координата холста Мультивселенной', color='white')
    plt.ylabel('Амплитуда материализации (Плотность рисунка)', color='white')
    plt.grid(True, alpha=0.1, linestyle='--')
    plt.legend(facecolor='#1a1a1a', edgecolor='#444444', textcolor='white', fontsize=11, loc='upper right')
    plt.tick_params(colors='white')
    plt.axhline(0, color='white', linewidth=0.5, alpha=0.5)
    
    print("🎨 Рисунок Мультивселенной обновлен. След Карандаша успешно выведен на экран.")
    plt.show()

if __name__ == '__main__':
    main()
