# amrita / src / swarm_meme_core.py
# Исправленная версия: Ликвидация ошибки пустого оператора "in:"

import os
import requests
import json
import time

OPENAI_API_KEY = os.getenv("OAI_API_KEY")
RPC_URL = os.getenv("SOLANA_RPC_URL", "https://solana.com")
DIRECTORY_ID = "amrita-mir-labs"

CORE_MONETS = [
    {"name": "AMRITA (MIR)", "role": "Core Organizational Node of Multiverse OS"},
    {"name": "MIR1 (Wings of Soliton)", "role": "Quantum Blockchain Anchor and Liquidity Hub"},
    {"name": "AANG", "role": "Ecosystem Balancer and Avatar of 5 Elements"},
    {"name": "D-REAM (Digital Dream)", "role": "Digital Reality Cloud Storage Protocol"}
]

def ask_ai_to_format_description(monet_name, role):
    if not OPENAI_API_KEY:
        return f"Foundational node for {monet_name}. Asset role: {role}."
    url = "https://openai.com"
    headers = {"Authorization": f"Bearer {OPENAI_API_KEY}", "Content-Type": "application/json"}
    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "Format professional crypto asset descriptions."},
            {"role": "user", "content": f"Token: {monet_name}. Role: {role}."}
        ]
    }
    try:
        res = requests.post(url, headers=headers, json=payload, timeout=10)
        return res.json()['choices'][0]['message']['content'].strip()
    except Exception:
        return f"Autonomous Web3 module representing {monet_name}."

def push_to_partnerpage(partner_node):
    url = f"https://partnerpage.io{DIRECTORY_ID}/nodes"
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    payload = {
        "company_name": partner_node["name"],
        "description": partner_node["description"],
        "website": "https://github.com",
        "partner_type": "Technology Partner",
        "contact_email": "misterick108@gmail.com",
        "metadata": {"source": "Amrita_Solana_Swarm", "sync_time": int(time.time())}
    }
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=10)
        # РЕШЕНИЕ: Убран пустой оператор "in:", заменено на прямую проверку кода ответа
        if response.status_code == 200 or response.status_code == 201:
            print(f"✅ Успешно отправлено: {partner_node['name']}")
        else:
            print(f"⚠️ Статус: {response.status_code}")
    except Exception as e:
        print(f"❌ Ошибка сети: {str(e)}")

def run_swarm_sync():
    print("🚀 Запуск синхронизации...")
    for monet in CORE_MONETS:
        description = ask_ai_to_format_description(monet['name'], monet['role'])
        push_to_partnerpage({"name": monet['name'], "description": description})
        time.sleep(2)

if __name__ == "__main__":
    run_swarm_sync()
