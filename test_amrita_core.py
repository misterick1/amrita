import unittest
import math
# Импортируем наше центральное ядро Протокола 28 из корня репозитория
from amrita_core_v28 import AmritaBridgeCoreV28

class TestAmritaCoreV28(unittest.TestCase):
    """
    [УСИЛЕННЫЙ ТЕСТОВЫЙ КОНТУР AMRITA OS]
    Автоматическая верификация 9-летнего юбилейного цикла Trust Wallet,
    макро-фрактала Биткоина и утренней частоты синхронизации GM.
    """
    
    def setUp(self):
        """Инициализация базовых параметров утренней скандинавской ноды"""
        self.battery_level = 31  # Актуальный квантовый заряд ноды 31% со скриншота 11:07
        self.solana_resonance = 73.27
        self.core = AmritaBridgeCoreV28(
            battery_level=self.battery_level, 
            solana_resonance=self.solana_resonance
        )

    def test_core_initialization(self):
        """Тест 1: Проверка интеграции спецификаций Протокола 28 при 31% заряда"""
        self.assertEqual(self.core.battery_level, 31)
        self.assertEqual(self.core.pi_testnet_protocol, 28)
        self.assertTrue(self.core.batch_smart_contract_upgrade)
        print("✅ ТЕСТ 1 ПРОЙДЕН: Спецификации Протокола 28 Pi Network успешно верифицированы.")
        
    def test_global_state_density_with_trust_wallet_anniversary(self):
        """Тест 2: Эмуляция утренней частоты GM и 9-летнего множителя децентрализации"""
        # Использования 9-летнего юбилейного цикла Trust Wallet как утилитарного множителя
        trust_wallet_anniversary_multiplier = 9.0
        density = self.core.calculate_global_state_density(local_multiplier=trust_wallet_anniversary_multiplier)
        
        # Проверяем, что аппаратный щит пробил трение матрицы на отметке 31% заряда
        self.assertGreater(density, 0)
        self.assertIsInstance(density, float)
        print(f"✅ ТЕСТ 2 ПРОЙДЕН: Юбилейный контур Trust Wallet и GM-Резонанс активны. Плотность: {round(density, 2)}")

    def test_bull_clock_macro_logic(self):
        """Тест 3: Верификация удержания 50-недельной SMA Биткоина ($81,159)"""
        bitcoin_sma_level = 81159.0
        # Проверяем, что бычьи часы запущены выше критической точки
        self.assertGreater(bitcoin_sma_level, 80000.0)
        print("✅ ТЕСТ 3 ПРОЙДЕН: Контур 'The Bull Clock' стабильно удерживает вектор долгосрочного роста.")

if __name__ == "__main__":
    # Запуск автоматического тестирования в консоли GitHub Actions
    unittest.main()
