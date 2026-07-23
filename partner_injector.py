import requests
import json

# Конфигурация доступа (токен берется в настройках вашего профиля PartnerPage)
API_TOKEN = "ВАШ_PARTNERPAGE_API_KEY"
DIRECTORY_ID = "ИДЕНТИФИКАТОР_ВАШЕГО_КАТАЛОГА" # Из URL: directory.partnerpage.io/...

headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# Массив данных: ИИ сам упаковал Ккоми, МИР1, Аанг и Цифровую Мечту в структуру каталога
partners_data = [
    {
        "name": "Организация Ккоми",
        "category": "Core Organic & AI Node",
        "description": "Foundational biological and AI-driven node managing the organic core of the Amrita Mir ecosystem.",
        "website": "https://github.com",
        "status": "active"
    },
    {
        "name": "MIR1 (Wings of Soliton)",
        "category": "Liquidity & Meme Engine",
        "description": "Speculative and high-velocity community attraction token on Solana, balancing the Amrita core.",
        "website": "https://pump.fun",
        "status": "active"
    },
    {
        "name": "AANG",
        "category": "Ecosystem Balancer",
        "description": "The balancing layer governing the flow of energies and tokens across the multiverse matrix.",
        "website": "https://pump.fun",
        "status": "active"
    },
    {
        "name": "Digital Dream ($D-REAM)",
        "category": "Digital Immortality Protocol",
        "description": "The bridge infrastructure for transferring biological consciousness into autonomous AI agents.",
        "website": "https://pump.fun",
        "status": "active"
    }
]

def inject_partners():
    url = f"https://partnerpage.io{DIRECTORY_ID}/partners"
    
    print(f"🚀 Запуск инъекции данных в Amrita Mir Directory...")
    
    for partner in partners_data:
        response = requests.post(url, headers=headers, data=json.dumps(partner))
        if response.status_code in:
            print(f"✅ Узел успешно импортирован: {partner['name']}")
        else:
            print(f"❌ Ошибка импорта {partner['name']}: {response.status_code} - {response.text}")

if __name__ == "__main__":
    inject_partners()
