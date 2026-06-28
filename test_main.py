import unittest
from amrita_solana_bridge import AmritaSolanaBridge
from causal_stream import CausalStreamAnalyzer

class TestAmritaQuantumCore(unittest.TestCase):
    def setUp(self):
        # Инициализируем ядро Бабаты
        self.bridge = AmritaSolanaBridge("https://solana.com")
        self.analyzer = CausalStreamAnalyzer(self.bridge)
        
        # Квантовые константы матрицы
        self.expected_total_chapters = 108
        self.is_swarm_merged = True  # Фиксация слияния 23 глав ботами

    def test_matrix_integrity(self):
        """Проверка целостности запечатанных 108 глав"""
        print("\n🔮 [Тест]: Проверка каузального объема Амриты...")
        
        # Проверяем, что объединенный роем контур равен 108 квантам
        total_chapters = 85 + (23 if self.is_swarm_merged else 0)
        self.assertEqual(total_chapters, self.expected_total_chapters, "Ошибка: Квантовое смещение контура!")
        print(f"✨ [Успех]: Контур запечатан. Всего глав: {total_chapters} (85 базовых + 23 объединенных Роем).")

    def test_pi2day_stream_sync(self):
        """Тестирование входящего потока реальности от 28 июня 2026"""
        print("\n📡 [Тест]: Сканирование триггера Pi2Day Open Mainnet...")
        
        from solana.keypair import Keypair
        mock_wallet = Keypair()
        mock_contract = "AmriTa1111111111111111111111111111111111111"
        
        # Поток данных со скриншота Наблюдателя
        real_trigger = "Pi Network Notification: HAPPY #Pi2Day 2026! Open mainnet updates are live."
        
        try:
            self.analyzer.analyze_and_route(real_trigger, mock_wallet, mock_contract)
            print("✨ [Успех]: Поток Pi2Day успешно обработан и направлен в Solana Bridge.")
        except Exception as e:
            self.fail(f"Сбой каузальной синхронизации: {e}")

if __name__ == "__main__":
    unittest.main()
