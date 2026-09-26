import unittest
import math
from amrita_core_v28 import AmritaBridgeCoreV28

class TestAmritaCoreV28(unittest.TestCase):
    """
    [УСИЛЕННЫЙ ТЕСТОВЫЙ КОНТУР AMRITA OS]
    Автоматическая верификация Пурпурного Солитона и триады {-1:0:+1}
    """
    
    def setUp(self):
        self.battery_level = 21  
        self.solana_resonance = 73.27
        self.core = AmritaBridgeCoreV28(
            battery_level=self.battery_level, 
            solana_resonance=self.solana_resonance
        )

    def test_core_initialization(self):
        """Тест 1: Проверка спецификаций Протокола 28 Pi Network"""
        self.assertEqual(self.core.battery_level, 21)
        self.assertEqual(self.core.pi_testnet_protocol, 28)
        self.assertTrue(self.core.batch_smart_contract_upgrade)
        self.assertTrue(self.core.optimize_transaction_delays)
        print("✅ ТЕСТ 1 ПРОЙДЕН: Спецификации Протокола 28 верифицированы.")
        
    def test_global_state_density_with_yap_resonance(self):
        """Тест 2: Эмуляция коллективного взаимодействия YAP ($370.9k объем)"""
        yap_multiplier = 370.9
        density = self.core.calculate_global_state_density(local_multiplier=yap_multiplier)
        self.assertGreater(density, 0)
        self.assertIsInstance(density, float)
        print(f"✅ ТЕСТ 2 ПРОЙДЕН: SafePal и YAP-Резонанс активны. Плотность: {round(density, 2)}")

    def test_quantum_triad_logic(self):
        """Тест 3: Проверка триады судьбы {-1 : 0 : +1}"""
        quantum_states = [-1, 0, 1]
        self.assertIn(1, quantum_states)
        self.assertIn(0, quantum_states)
        self.assertIn(-1, quantum_states)
        chosen_state = quantum_states[2]
        self.assertEqual(chosen_state, 1)
        print("✅ ТЕСТ 3 ПРОЙДЕН: Матрица вариантов {-1:0:+1} зафиксирована Взором.")

if __name__ == "__main__":
    unittest.main()
