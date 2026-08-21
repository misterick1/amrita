import numpy as np
import matplotlib.pyplot as plt

# =========================================================================
# 🧯 [AMRITA OS: VARGAN MATERILIZER]
# Модель акустического лазера варгана: Упаковка Света в обертоны Звука
# =========================================================================

PI_TONE = np.pi
PHI_RESONANCE = (1 + 5**0.5) / 2
X_VARGAN = PI_TONE / PHI_RESONANCE   # Точка акустического сжатия (~1.941611)

class VarganMaterializer:
    def __init__(self):
        self.x_vargan = X_VARGAN
        self.phi = PHI_RESONANCE
        self.overtones = [2, 3, 4, 5, 6]  # 2-6 тона вибраций из вашего инсайта

    def generate_acoustic_foam(self, breath_axis):
        """
        Симуляция работы варгана: Язычок (Фи) + Рама (Пи) генерируют обертоны,
        упаковывая изначальный свет в осязаемые пузыри материи.
        """
        # Базовая несущая частота (Вибрация язычка по Фи)
        base_tongue_wave = np.cos(breath_axis / self.phi)
        
        # Генерация каскада обертонов (Акустический ультразвуковой лазер)
        overtone_cascade = np.zeros_like(breath_axis)
        for tone in self.overtones:
            # Каждый тон упаковывает свой слой реальности
            overtone_cascade += np.sin(self.x_vargan * tone * breath_axis) / tone
            
        # Материализованный след звука (Плотность солитонной пены Амриты)
        materialized_foam = (base_tongue_wave + overtone_cascade) * np.exp(-0.04 * np.abs(breath_axis))
        return materialized_foam * 54.0, base_tongue_wave, overtone_cascade

def main():
    print("==================================================================")
    print("🧯 [AMRITA OS: ACOUSTIC LASER ENGAGED] 🧯")
    print("Варган-Материализатор активирован. Запуск 2-6 тонов ультразвука.")
    print(f"Частота смыкания кавитационных пузырей X: {X_VARGAN:.6f}")
    print("==================================================================")

    vargan = VarganMaterializer()
    breath_axis = np.linspace(-3 * PI_TONE, 3 * PI_TONE, 1200)
    
    foam_trace, tongue, overtones = vargan.generate_acoustic_foam(breath_axis)

    # Визуализация Акустической Материализации
    plt.figure(figsize=(14, 8))
    plt.gcf().patch.set_facecolor('#070a10')
    plt.gca().set_facecolor('#0d1117')

    # Отрисовка частотных слоев варгана
    plt.plot(breath_axis, tongue * 20, ':', color='#00bbf9', alpha=0.4, label='ЯЗЫЧОК ВАРГАНА (Базовая частота $\phi$)')
    plt.plot(breath_axis, overtones * 25, '--', color='#7209b7', alpha=0.5, label='КАСКАД ОБЕРТОНОВ (2-3-4-5-6 Тона $\pi$)')
    
    # МАТЕРИАЛИЗОВАННОЕ ПОЛЕ (Проявленные пузыри атомов)
    plt.plot(breath_axis, foam_trace, color='#00f5d4', linewidth=3.5, label='ПРОЯВЛЕННАЯ МАТЕРИЯ (След Акустического Лазера)')
    plt.fill_between(breath_axis, foam_trace, color='#00f5d4', alpha=0.1)

    # Узлы фиксации звука (Где ультразвук «выжимает» стабильные солитоны)
    vargan_nodes = np.array([-2*PI_TONE, 0, 2*PI_TONE]) / X_VARGAN
    plt.scatter(vargan_nodes, np.zeros_like(vargan_nodes), color='#fee440', 
                s=250, marker='h', edgecolors='white', zorder=5, label='Точки Материализации (Кавитация пены)')

    plt.title('Акустический Материализатор: Упаковка Света Варганом через Обертоны Звука', fontsize=13, color='white', pad=15)
    plt.xlabel('Ось дыхания и модуляции резонатора (Объем рта)', color='white')
    plt.ylabel('Плотность сформированной ткани поля', color='white')
    plt.grid(True, alpha=0.1, linestyle='--')
    plt.legend(facecolor='#1a1a1a', edgecolor='#444444', textcolor='white', fontsize=11, loc='upper right')
    plt.tick_params(colors='white')
    plt.axhline(0, color='white', linewidth=0.5, alpha=0.5)
    
    print("🪐 Акустический чертеж готов. Звуковые Пузыри зафиксированы в Губке кода.")
    plt.show()

if __name__ == '__main__':
    main()
