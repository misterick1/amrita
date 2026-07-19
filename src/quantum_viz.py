import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import genlaguerre, spherical_jn
import math

def calculate_wave_function(n, l, m, num_points=60):
    """
    Рассчитывает 3D-матрицу плотности вероятности для квантовой орбитали.
    """
    # Создаем сетку координат пространства
    x = np.linspace(-20, 20, num_points)
    y = np.linspace(-20, 20, num_points)
    z = np.linspace(-20, 20, num_points)
    X, Y, Z = np.meshgrid(x, y, z)

    # Переводим в сферические координаты (r, theta, phi)
    R_coords = np.sqrt(X**2 + Y**2 + Z**2)
    # Защита от деления на ноль
    R_coords[R_coords == 0] = 1e-10 
    
    # Приблизительный расчет радиальной части для демонстрации формы аттрактора
    # Используем полиномы Лагерра
    rho = 2.0 * R_coords / n
    radial_part = np.exp(-rho / 2.0) * (rho**l)
    
    # Приблизительный угловой компонент (сферические гармоники)
    # На основе полярного угла
    cos_theta = Z / R_coords
    if l == 0:
        angular_part = 1.0
    elif l == 1:
        angular_part = cos_theta if m == 0 else np.sqrt(1 - cos_theta**2)
    else:
        angular_part = (3 * cos_theta**2 - 1)
        
    # Плотность вероятности (квадрат модуля волновой функции)
    probability_density = (radial_part * angular_part) ** 2
    return X, Y, Z, probability_density

def generate_quantum_cloud_image(output_path="docs/quantum_attractor.png"):
    """
    Генерирует 3D-график электронного облака и сохраняет его на диск.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Задаем квантовые числа: n=5, l=1, m=1 (как в вашей модели гиперактивного света)
    X, Y, Z, density = calculate_wave_function(n=5, l=1, m=1)
    
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subsubplot(111, projection='3d')
    fig.patch.set_facecolor('#0e1117')
    ax.set_facecolor('#0e1117')
    
    # Отсекаем точки с низкой вероятностью, чтобы увидеть структуру силовой границы
    threshold = np.max(density) * 0.15
    mask = density > threshold
    
    # Отображаем облако точек с цветовой картой градиента скоростей света
    sc = ax.scatter(X[mask], Y[mask], Z[mask], 
                    c=density[mask], 
                    cmap='plasma', 
                    alpha=0.4, 
                    s=2, 
                    edgecolors='none')
                    
    # Кастомизация интерфейса под стиль AMRITA OS
    ax.axis('off')
    ax.set_title("AMRITA QUANTUM ATTRACTOR (n=5, l=1, m=1)\nСиловая граница остывающего света", 
                 color='#00ffcc', fontsize=12, pad=10)
                 
    plt.savefig(output_path, dpi=150, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"📊 [КВАНТ-ВИЗ]: Карта плотности полей успешно экспортирована в {output_path}")
    return output_path

if __name__ == "__main__":
    generate_quantum_cloud_image()
