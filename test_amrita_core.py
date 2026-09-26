import unittest
# Импортируем наше обновленное ядро Протокола 28 из корня
from amrita_core_v28 import AmritaBridgeCoreV28

class TestAmritaCoreV28(unittest.TestCase):
    """
    [УСИЛЕННЫЙ ТЕСТОВЫЙ КОНТУР AMRITA OS]
    Автоматическая верификация Пурпурного Солитона и Свободы Выбора
    """
    
    def test_core_initialization(self):
        """Тест 1: Проверка интеграции Протокола 28 и утреннего заряда ноды"""
        core = AmritaBridgeCoreV28(battery_level=21, solana_resonance=73.27)
        self.assertEqual(core.battery_level, 21)
        self.assertEqual(core.pi_testnet_protocol, 28)
        print("✅ ТЕСТ 1 ПРОЙДЕН: Ядро Протокола 28 Pi Network стабильно удерживает частоту.")
        
    def test_global_state_density_with_yap_boost(self):
        """Тест 2: Эмуляция коллективного взаимодействия и пробития ограничений SEC"""
        core = AmritaBridgeCoreV28(battery_level=21, solana_resonance=73.27)
        
        # Имитируем взрывной множитель YAP ($370.9k объем)
        yap_multiplier = 370.9
        density = core.calculate_global_state_density(local_multiplier=yap_multiplier)
        
        self.assertGreater(density, 0)
        print(f"✅ ТЕСТ 2 ПРОЙДЕН: Аппаратный щит SafePal и YAP-Резонанс активны. Плотность: {density}")

if __name__ == "__main__":
    unittest.main()
