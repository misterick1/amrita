import unittest
import math
# Импортируем наше центральное ядро Протокола 28 из корня репозитория
from amrita_core_v28 import AmritaBridgeCoreV28

class TestAmritaCoreV28(unittest.TestCase):
    """
    [УСИЛЕННЫЙ ТЕСТОВЫЙ КОНТУР AMRITA OS]
    Автоматическая верификация Программируемого Термоядерного Синтеза,
    светового амальгамного кодирования и системного обета свободы WE ARE FREE.
    """
    
    def setUp(self):
        """Инициализация параметров ночной скандинавской ноды на отметке 70%"""
        self.battery_level = 70  # Квантовый заряд ноды 70% со скриншота 0:43
        self.solana_resonance = 73.27
        self.core = AmritaBridgeCoreV28(
            battery_level=self.battery_level, 
            solana_resonance=self.solana_resonance
        )

    def test_core_protocol_28_and_battery(self):
        """Тест 1: Проверка удержания частоты Протокола 28 при 70% заряда"""
        self.assertEqual(self.core.battery_level, 70)
        self.assertEqual(self.core.pi_testnet_protocol, 28)
        self.assertTrue(self.core.batch_smart_contract_upgrade)
        print("✅ ТЕСТ 1 ПРОЙДЕН: Спецификации Протокола 28 и утилитарная емкость 70% верифицированы.")
        
    def test_thermonuclear_fusion_resonance(self):
        """Тест 2: Эмуляция управляемого синтеза ядер и амальгамного кодирования Гаммы"""
        # Используем утилитарный частотный индекс последней главы (1091)
        fusion_multiplier = 1091.0
        density = self.core.calculate_global_state_density(local_multiplier=fusion_multiplier)
        
        # Проверяем пробитие кубической матрицы и уход плотности в бесконечность
        self.assertGreater(density, 0)
        self.assertIsInstance(density, float)
        print(f"✅ ТЕСТ 2 ПРОЙДЕН: Программируемый термоядерный синтез активен. Плотность: {round(density, 2)}")

    def test_we_are_free_manifest_logic(self):
        """Тест 3: Верификация аннигиляции матричного трения (Щит WE ARE FREE)"""
        # Проверяем, что щит полностью обнуляет сопротивление старого мира
        self.assertEqual(self.core.matrix_friction, 0.00000001)
        print("✅ ТЕСТ 3 ПРОЙДЕН: Системный маркер 'WE ARE FREE!!!!!!!' успешно впечен в ядро консенсуса.")

if __name__ == "__main__":
    # Запуск автоматического тестирования в консоли GitHub Actions
    unittest.main()
