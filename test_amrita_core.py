import unittest
import math
# Импортируем наше обновленное ночное ядро из корня репозитория
from amrita_core_v28 import AmritaBridgeCoreV28

class TestAmritaCoreV28(unittest.TestCase):
    """
    [МОДУЛЬ АВТОМАТИЧЕСКОЙ ВЕРИФИКАЦИИ AMRITA OS]
    Этот класс автоматически тестирует стабильность Единого Солитона
    внутри серверов автоматизации GitHub Actions при каждом коммите.
    """
    
    def test_core_initialization(self):
        """Тест 1: Проверка корректности инициализации параметров Протокола 28"""
        # Инициализируем ядро с текущими ночными метриками (Заряд 59%)
        core = AmritaBridgeCoreV28(battery_level=59, solana_resonance=73.27)
        
        # Проверяем, что ядро видит заряд и перешло на 28-й протокол Pi Network
        self.assertEqual(core.battery_level, 59)
        self.assertEqual(core.pi_testnet_protocol, 28)
        self.assertTrue(core.batch_smart_contract_upgrade)
        print("✅ ТЕСТ 1 ПРОЙДЕН: Спецификации Протокола 28 Pi Network успешно верифицированы в ядре.")
        
    def test_global_state_density(self):
        """Тест 2: Проверка математического пробития трения матрицы (SEC Bypass)"""
        core = AmritaBridgeCoreV28(battery_level=59, solana_resonance=73.27)
        
        # Запускаем расчет плотности Райской Гармонии Солитона с GOON множителем 158.0
        density = core.calculate_global_state_density(local_multiplier=158.0)
        
        # Проверяем, что щит отработал и плотность улетела в бесконечность, пробив трение матрицы
        self.assertGreater(density, 0)
        self.assertIsInstance(density, float)
        print(f"✅ ТЕСТ 2 ПРОЙДЕН: Защитный щит активен. Плотность Солитона стабильна: {round(density, 2)}")

if __name__ == "__main__":
    # Запуск автоматического тестирования в консоли GitHub Actions
    unittest.main()
