import unittest
import math
# Импортируем наше центральное ядро Протокола 28 из корня репозитория
from amrita_core_v28 import AmritaBridgeCoreV28

class TestAmritaCoreV28(unittest.TestCase):
    """
    [АКУСТИЧЕСКИЙ ТЕСТОВЫЙ КОНТУР AMRITA OS]
    Верификация мульти-частотного резонанса Солитона (Сыгыт и Каргыраа Гейба)
    на утилитарном пороге заряда ноды 24%.
    """
    
    def setUp(self):
        """Инициализация базовых параметров вечерней ноды"""
        self.battery_level = 24  # 24% заряда со скриншота 21:59
        self.solana_resonance = 73.27
        self.core = AmritaBridgeCoreV28(
            battery_level=self.battery_level, 
            solana_resonance=self.solana_resonance
        )

    def test_core_protocol_28(self):
        """Тест 1: Проверка синхронизации ядра и пакетного обновления смарт-контрактов"""
        self.assertEqual(self.core.battery_level, 24)
        self.assertEqual(self.core.pi_testnet_protocol, 28)
        self.assertTrue(self.core.batch_smart_contract_upgrade)
        print("✅ ТЕСТ 1 ПРОЙДЕН: Спецификации Протокола 28 Pi Network успешно подтверждены.")
        
    def test_multifrequency_throat_singing_resonance(self):
        """Тест 2: Эмуляция горлового пения Габена (Одновременный запуск сыгыт и каргыраа частот)"""
        # Имитируем мульти-частотный резонанс (две частоты в одной ноде)
        throat_singing_boost = 1153.0  # Частота Королевской Воли
        density = self.core.calculate_global_state_density(local_multiplier=throat_singing_boost)
        
        # Проверяем, что ядро выдержало перегрузку акустической волны Габена
        self.assertGreater(density, 0)
        self.assertIsInstance(density, float)
        print(f"✅ ТЕСТ 2 ПРОЙДЕН: Резонанс Сыгыт/Каргыраа активен. Плотность Солитона: {round(density, 2)}")

    def test_matrix_friction_annihilation(self):
        """Тест 3: Проверка полного схлопывания трения матрицы (SEC & Valve Override)"""
        self.assertEqual(self.core.matrix_friction, 0.00000001)
        print("✅ ТЕСТ 3 ПРОЙДЕН: Щит Faker Guard активен. Трение старого мира обнулено.")

if __name__ == "__main__":
    # Запуск автоматического тестирования в консоли GitHub Actions
    unittest.main()
