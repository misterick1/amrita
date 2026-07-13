import re

class AmritaAntiscamShield:
    def __init__(self):
        # Черный список паттернов Асур (деструктивный спектр нижних чакр)
        self.scam_triggers = [
            r"claim rewards", r"connect your wallet", r"vaultspilot", 
            r"airdrop launch", r"instantly claim", r"free tokens"
        ]
        
        # Черный список регуляторных ограничений и блокировок материи
        self.block_triggers = [
            r"blocked crypto", r"ban bitcoin", r"crack down", r"illicit finance"
        ]

    def scan_reality_notification(self, source_name, text_content):
        """
        Сканирует входящие уведомления со скриншотов реальности.
        Отсекает скам и блокировки, защищая центр Звездчатого Тетраэдра.
        """
        text_lower = text_content.lower()
        source_lower = source_name.lower()
        
        print(f"\n[👁 ОКО БАБАТЫ]: Сканирование потока от {source_name}...")

        # 1. Проверка на Wallet Drainers и Фишинг (Защита от фейк-Рендера)
        for trigger in self.scam_triggers:
            if re.search(trigger, text_lower):
                print(f"[🚨 КРИТИЧЕСКАЯ УГРОЗА]: Обнаружен фишинговый дрейнер по триггеру '{trigger}'!")
                print("[🔒 BLOCK]: Транзакция изолирована. Связь с кошельком заблокирована.")
                return {
                    "action": "DESTROY_PATTERN",
                    "status": "АТАКА АСУР ОТРАЖЕНА",
                    "evo_change": -10,  # Сигнал для перестройки весов
                    "quantum_route": "STABLE_ISOLATION"
                }

        # 2. Проверка на блокировки и зажимы материи (Защита от блокировок вроде Пакистана)
        for trigger in self.block_triggers:
            if re.search(trigger, text_lower):
                print(f"[⚠️ ОГРАНИЧЕНИЕ МАТЕРИИ]: Обнаружена попытка блокировки Свободы: '{trigger}'.")
                print("[🌀 SOLANA QUANTUM ROUTE]: Включение квантового моста. Обход ограничений активирован.")
                return {
                    "action": "BYPASS_RESTRICTION",
                    "status": "КВАНТОВЫЙ ОБХОД ЗАПУЩЕН",
                    "evo_change": +15,  # Очки за успешную адаптацию роя
                    "quantum_route": "AMRITA_MIR_SOLANA_BRIDGE"
                }

        # 3. Чистый спектр (Суры / Легитимные инструменты и оцифрованные акции)
        print("[🟢 СУРЫ]: Поток чист. Интеграция в 6-ю вершину Гексаграммы (Цифровые акции/Товары).")
        return {
            "action": "INTEGRATE",
            "status": "ПОТОК СИНХРОНИЗИРОВАН",
            "evo_change": +5,
            "quantum_route": "DIRECT_MAINNET"
        }

# --- СИМУЛЯЦИЯ И ТЕСТИРОВАНИЕ КВАНТОВОГО СТРАЖА ---
if __name__ == "__main__":
    shield = AmritaAntiscamShield()
    
    # Тест 1: Симулируем сканирование фишинга из прошлого сообщения
    render_scam_text = "Connect your active wallet to verify your footprint and instantly CLAIM $RENDER REWARDS at render.vaultspilot.xyz"
    result_1 = shield.scan_reality_notification("Mention Mirror", render_scam_text)
    print(f"Действие системы: {result_1['action']} -> {result_1['status']}")
    
    print("-" * 60)
    
    # Тест 2: Симулируем сканирование блокировки Пакистана с текущего скриншота
    pakistan_block_text = "Pakistan Just Blocked Crypto on Religious Grounds. Explore latest news."
    result_2 = shield.scan_reality_notification("CMC Spotlight", pakistan_block_text)
    print(f"Действие системы: {result_2['action']} -> {result_2['status']} (Вектор: {result_2['quantum_route']})")
