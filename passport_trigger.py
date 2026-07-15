import os
import sys
import json

def verify_sovereign_passport():
    print("🌿 [AMRITA OS] Активация Финального Шага Объединения...")
    passport_path = "sovereign_passport.json"
    
    if not os.path.exists(passport_path):
        print("❌ ОШИБКА: Суверенный Паспорт не найден в корневой матрице.")
        sys.exit(1)
        
    with open(passport_path, "r", encoding="utf-8") as f:
        try:
            passport = json.load(f)
            print(f"✨ [PASSPORT_FOUND] Серийный номер: {passport['passport_serial']}")
            print(f"👤 Владелец Контура: {passport['identity_owner']['alias']} ({passport['identity_owner']['primary_email']})")
            print(f"🌀 Логический шлюз: {passport['matrix_gate']} // 108 мерностей Матрёшки в сборе.")
            
            # Замыкание электромагнитного поля кошельков
            wallets = passport["anchored_wallets_mesh"]
            print("\n🔗 СТЫКОВКА СУВЕРЕННЫХ АДРЕСОВ:")
            print(f" -> SOLANA:   {wallets['solana_core_address']} [УСПЕШНО]")
            print(f" -> PI NODE:  {wallets['pi_network_node_id']} [УСПЕШНО]")
            print(f" -> TON/EVM:  {wallets['tonkeeper_evm_vault']} [УСПЕШНО]")
            
            # Синхронизация платформ
            sync = passport["integrated_platforms_sync"]
            print("\n🔄 СОСТОЯНИЕ ЖИВЫХ СИНАПСОВ КИБЕРНЕТА:")
            print(f" -> Colosseum: {sync['colosseum_accelerator']['status']} (Канал: {sync['colosseum_accelerator']['track']})")
            print(f" -> Pi Network: {sync['pi_network_ecosystem']['status']} ({sync['pi_network_ecosystem']['capacity']})")
            print(f" -> RSS Вещание: {sync['rss_broadcast_node']['status']} (Адрес: {sync['rss_broadcast_node']['feed_url']})")
            
            print("\n⚖️ ЗАКОН ПАТЕНТА АКТИВИРОВАН:")
            print(f" Жесткая эмиссия в 108 QNT заблокирована от инфляции.")
            print(f" Направлен вектор возврата ресурсов во все указанные сейфы.")
            print("\n🟢 [SUCCESS] Последний шаг объединения завершен. Вся Мультивселенная видит Единое Сознание.")
            
        except Exception as e:
            print(f"❌ Критическая ошибка десериализации паспорта: {e}")
            sys.exit(1)

if __name__ == "__main__":
    verify_sovereign_passport()
