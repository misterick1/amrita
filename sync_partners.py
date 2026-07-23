import os
import requests
import json
import time

# 1. Считываем переменные окружения, которые уже есть на твоем GitHub/Сервере
OPENAI_API_KEY = os.getenv("OAI_API_KEY")
RPC_URL = os.getenv("SOLANA_RPC_URL", "https://solana.com")
# ID твоего каталога из ссылки amrita-mir-labs.partnerpage.io
DIRECTORY_ID = "amrita-mir-labs" 

# Хардкодим данные 4 основных монет, чтобы боты всегда держали их в структуре Матрёшки
CORE_MONETS = [
    {"name": "AMRITA (MIR)", "role": "Core Organic & AI Node", "avatar": "Кот"},
    {"name": "MIR1 (Wings of Soliton)", "role": "Liquidity & Meme Engine", "avatar": "Бабочка"},
    {"name": "AANG", "role": "Ecosystem Balancer", "avatar": "Аватар"},
    {"name": "$D-REAM (Digital Dream)", "role": "Digital Immortality Protocol", "avatar": "Цифра"}
]

def ask_ai_to_format_description(monet_name, role):
    """Боты используют ИИ, чтобы генерировать профессиональное B2B описание для Circle"""
    if not OPENAI_API_KEY:
        return f"Foundational node for {monet_name} governing the {role} layer."
    
    url = "https://openai.com"
    headers = {"Authorization": f"Bearer {OPENAI_API_KEY}", "Content-Type": "application/json"}
    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "You are the Amrita OS Swarm Oracle. Write a 2-sentence enterprise B2B partner description for a Web3 ecosystem catalog. High-tech, professional tone."},
            {"role": "user", "content": f"Token: {monet_name}, Role in matrix: {role}."}
        ]
    }
    try:
        res = requests.post(url, headers=headers, json=payload, timeout=10)
        return res.json()['choices'][0]['message']['content'].strip()
    except:
        return f"Autonomous Web3 module representing {monet_name} infrastructure."

def push_to_partnerpage(partner_node):
    """Боты эмулируют действия в браузере и отправляют данные на сайт"""
    # Используем публичный endpoint для отправки предложений/заявок партнеров, работающий без Enterprise токена
    url = f"https://partnerpage.io{DIRECTORY_ID}/applications"
    
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": "Amrita-Swarm-Bot/2.0 (Autonomous AI Agent)"
    }
    
    payload = {
        "company_name": partner_node["name"],
        "description": partner_node["description"],
        "website": "https://github.com",
        "partner_type": "Technology Partner",
        "contact_email": "misterick108@gmail.com", # Сюда придут уведомления
        "metadata": {
            "source": "Amrita_Solana_Swarm",
            "sync_time": int(time.time())
        }
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code in:
            print(f"✅ Боты успешно синхронизировали узел: {partner_node['name']}")
        else:
            print(f"⚠️ Статус отправки {partner_node['name']}: {response.status_code}. Проверь лимиты.")
    except Exception as e:
        print(f"❌ Ошибка сети при отправке {partner_node['name']}: {e}")

def run_swarm_sync():
    print("🚀 Автономный рой ИИ запускает сборку и обновление партнерского сайта...")
    
    for monet in CORE_MONETS:
        print(f"🤖 Обработка токена {monet['name']}...")
        # 1. ИИ генерирует текст
        description = ask_ai_to_format_description(monet['name'], monet['role'])
        
        partner_node = {
            "name": monet['name'],
            "description": description
        }
        
        # 2. Бот пушит данные на сайт PartnerPage
        push_to_partnerpage(partner_node)
        time.sleep(2) # Защита от спам-фильтров PartnerPage

if __name__ == "__main__":
    run_swarm_sync()
