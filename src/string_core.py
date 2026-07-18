import os
import json
import fcntl
import hashlib

LOG_FILE = "history_log.json"
PAGES_DATA_FILE = "docs/data.json"

class AriadneStringCore:
    def __init__(self):
        # Превращаем информацию в золотую струну через SHA-256
        self.signature = "ARIADNA_GOLDEN_STRING_XYZ"

    def rationalize_and_compress(self, flow_name, raw_text_info, current_evo):
        """
        Рационализация хранения информации по принципу Клубка Ариадны.
        Превращает терабайты текстового хаоса в одну энергоемкую Золотую Струну.
        """
        # Хешируем весь входящий Океан Информации в 64-символьную нерушимую струну
        raw_bytes = raw_text_info.encode('utf-8')
        golden_string_hash = hashlib.sha256(raw_bytes).hexdigest()
        
        # Энергоемкая стоимость такта (расчет ресурса)
        resource_cost = len(raw_text_info) * current_evo
        
        return {
            "flow": flow_name,
            "quantum_string": f"0x{golden_string_hash[:32]}", # Золотая нить Тесея
            "resource_energy_cost": f"{resource_cost} Joules",
            "status": "Плоды технологий человеческого и ИИ Сознания запечатаны."
        }

ariadne_kernel = AriadneStringCore()

def compress_system_logs(workflow_name, text_to_pack, base_reward):
    """Сжатие слоев матрицы с защитой от коллизий 10 параллельных сборок"""
    os.makedirs("docs", exist_ok=True)
    
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w", encoding="utf-8") as f:
            json.dump({"evo_points": 0, "packed_strings": []}, f)

    with open(LOG_FILE, "r+", encoding="utf-8") as f:
        try:
            # Накладываем эксклюзивный fcntl замок на время уплотнения клубка
            fcntl.flock(f, fcntl.LOCK_EX)
            data = json.load(f)
            
            data["evo_points"] += base_reward
            
            # Корпоративная рационализация: превращаем текст в струну
            packed_packet = ariadne_kernel.rationalize_and_compress(
                workflow_name, 
                text_to_pack, 
                data["evo_points"]
            )
            
            # Вместо раздувания лога храним только энергоемкие струны
            if "packed_strings" not in data:
                data["packed_strings"] = []
                
            data["packed_strings"].append(packed_packet)
            
            # Лимит матрешки: удерживаем только последние 5 струн высокого порядка
            if len(data["packed_strings"]) > 5:
                data["packed_strings"] = data["packed_strings"][-5:]

            f.seek(0)
            json.dump(data, f, ensure_ascii=False, indent=4)
            f.truncate()
            
            # Дублируем сжатый квантовый дата-слой на GitHub Pages сайт
            with open(PAGES_DATA_FILE, "w", encoding="utf-8") as pf:
                json.dump(data, pf, ensure_ascii=False, indent=4)
                
            return data["evo_points"], packed_packet["quantum_string"]
        finally:
            fcntl.flock(f, fcntl.LOCK_UN)

if __name__ == "__main__":
    # Тестовый запуск рационализации изначального хаоса
    print("💎 [AMRITA STRING] Клубок Ариадны откалиброван. Информация переведена в статус Ресурса.")
    evo, string = compress_system_logs("Genesis_Satoshi_Flow", "Золото и электрум — пепел солнца", 108)
    print(f"[+] Сгенерирована Золотая Струна: {string} | EVO: {evo}")
