# amrita / src / swarm_meme_core.py
# Исправленная версия: Ликвидация ошибки пустого оператора и синхронизация нод

import os
import requests
import json
import time

OPENAI_API_KEY = os.getenv("OAI_API_KEY")
RPC_URL = os.getenv("SOLANA_RPC_URL", "https://solana.com")
DIRECTORY_ID = "amrita-mir-labs"

CORE_MONETS = [
    {"name": "AMRITA (MIR)", "role": "Core Oracle Ecosystem Token"},
    {"name": "MIR1 (Wings of Soliton)", "role": "Vibrational Wave Soliton"},
    {"name": "AANG", "role": "Ecosystem Balance Token"},
    {"name": "D-REAM (Digital Dream)", "role": "Digital Reality Matrix Connection"}
]

def ask_ai_to_format_description(monet_name, role):
    if not OPENAI_API_KEY:
        return f"Foundational node for {monet_name} acting as {role} inside AMRITA OS."
        
    url = "https://openai.com"
    headers = {"Authorization": f"Bearer {OPENAI_API_KEY}", "Content-Type": "application/json"}
    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "Format technical description for web3 node concisely."},
            {"role": "user", "content": f"Token Name: {monet_name}, Function: {role}. Generate 1-sentence bio."}
        ]
    }
    try:
        res = requests.post(url, headers=headers, json=payload)
        return res.json()['choices'][0]['message']['content'].strip()
    except Exception:
        return f"Autonomous Web3 module representing {monet_name} ({role})."

def push_to_partnerpage(partner_node):
    url = f"https://partnerpage.io{DIRECTORY_ID}/api/v1/nodes"
    headers = {"Content-Type": "application/json"}
    payload = {
        "company_name": partner_node["name"],
        "description": partner_node["description"],
        "website": "https://github.com",
        "partner_type": "Technology Partner",
        "contact_email": "misterick108@gmail.com",
        "metadata": {"source": "Amrita_Solana_Swarm_Node"}
    }
    try:
        response = requests.post(url, headers=headers, json=payload)
        # РЕШЕНИЕ: Убран пустой оператор "in:", вызывавший ошибку синтаксиса
        if response.status_code == 200 or response.status_code == 211:
            print(f"✅ Успешно отправлено: {partner_node['name']}")
        else:
            print(f"⚠️ Статус: {response.status_code} при отправке {partner_node['name']}")
    except Exception as e:
        print(f"❌ Ошибка сети: {str(e)}")

def run_swarm_sync():
    print("🚀 Запуск синхронизации...")
    for monet in CORE_MONETS:
        description = ask_ai_to_format_description(monet["name"], monet["role"])
        push_to_partnerpage({
            "name": monet["name"],
            "description": description
        })
        time.sleep(2)

if __name__ == "__main__":
    run_swarm_sync()
