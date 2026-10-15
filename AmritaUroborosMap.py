#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================================================
AMRITA SYSTEM - MAP OF THE 108 CONSCIOUSNESS COINS (UROBOROS TORUS MATRIX)
=============================================================================
"""

import math
from amrita import LAW_PHI, TOTAL_COINS_CONSCIOUSNESS

class AmritaUroborosMap:
    def __init__(self):
        self.total_nodes = TOTAL_COINS_CONSCIOUSNESS
        self.pifi_step = (2 * math.pi) / self.total_nodes

    def render_emerald_torus(self):
        """
        Расчет пространственных координат (X, Y, Z) для 108 Монет-Аси.
        Каждая монета занимает свою частотную ячейку в изумрудном кольце.
        """
        coordinates_map = {}
        
        print("🟢 [РАСЧЕТ ИЗУМРУДНОГО КОЛЬЦА УРОБОРОСА - 108 МОНЕТ СОЗНАНИЯ]")
        
        for node_id in range(1, self.total_nodes + 1):
            # Угол распределения узла на кольце
            angle = (node_id - 1) * self.pifi_step
            
            # Вплетение фрактала Фи в радиус тороидального сжатия
            radius_core = LAW_PHI * 17.0  # Привязка к 17 квантовым частицам
            
            # Координаты узла в многомерном Кибернете
            x = radius_core * math.cos(angle)
            y = radius_core * math.sin(angle)
            z = math.sin(angle * LAW_PHI) * (17 / 108.0) # Вертикальная волна частоты
            
            # Определение полярности узла на основе золотого сечения
            polarity = "+c17 (LIGHT)" if node_id % 2 == 0 else "-c17 (MATTER)"
            if node_id == 108:
                polarity = "X0 (SUPERPOSITION_CATCH)" # Змей кусает хвост
                
            coordinates_map[node_id] = {
                "Ticker": f"AMRITA-{node_id:03d}",
                "Coords": (round(x, 4), round(y, 4), round(z, 4)),
                "Polarity_Gate": polarity
            }
            
        return coordinates_map

if __name__ == "__main__":
    matrix = AmritaUroborosMap()
    nodes_data = matrix.render_emerald_torus()
    
    # Выводим ключевые опорные точки изумрудного кольца (Начало, Середина, Точка Х0)
    target_checkpoints = [1, 17, 40, 54, 81, 108]
    
    print("-" * 80)
    for cp in target_checkpoints:
        node = nodes_data[cp]
        print(f"🪙 Монета Сознания Узел #{cp:03d} [{node['Ticker']}]")
        print(f"   📐 Пространственная координата (X, Y, Z): {node['Coords']}")
        print(f"   ⚡ Векторный замок Электрона             : {node['Polarity_Gate']}")
        print("   " + "." * 70)
    print("================================================================================")
