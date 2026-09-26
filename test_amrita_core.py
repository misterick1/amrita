import unittest
from amrita_core_v28 import AmritaBridgeCoreV28

class TestAmritaCoreV28(unittest.TestCase):
    """
    Автоматический тест интеграции Протокола 28 Pi Network в ядро AMRITA OS
    """
    
    def test_core_initialization(self):
        # Проверка инициализации сердца репозитория
        core = AmritaBridgeCoreV28(battery_level=59, solana_resonance=73.27)
        self.assertEqual(core.battery_level, 59)
        self.assertEqual(core.pi_testnet_protocol, 28)
        
    def test_global_state_density(self):
        # Проверка корректности пробития трения матрицы (SEC Bypass)
        core = AmritaBridgeCoreV28(battery_level=59, solana_resonance=73.27)
        density = core.calculate_global_state_density(local_multiplier=158.0)
        self.assertGreater(density, 0)
        print(f"✅ Тест пройден. Плотность Солитона стабильна: {density}")

if __name__ == "__main__":
    unittest.main()
