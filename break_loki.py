import json
import os

def update_amrita_core():
    config_file = "titans_config.json"
    log_file = "history_log.json"
    
    # 1. Обновляем титанов
    new_config = {
      "pool_config": {
        "total_slots": 108,
        "registered_slots": 38,
        "admin_email": "misterick2024@gmail.com"
      },
      "titans": [
        {
          "name": "XAI TITAN",
          "symbol": "XAI",
          "description": "Black Swarm infrastructure and computing power nodes.",
          "twitter": "https://x.com",
          "creator_email": "misterick2024@gmail.com"
        },
        {
          "name": "OPEN ALGORITHMS",
          "symbol": "OPEN",
          "description": "White Swarm neural models and open-source alignment algorithms.",
          "twitter": "https://x.com",
          "creator_email": "misterick2024@gmail.com"
        },
        {
          "name": "NVIDIA SILICON",
          "symbol": "NVDA",
          "description": "Hardware and hardware accelerators for multi-agent synthesis.",
          "twitter": "https://x.com",
          "creator_email": "misterick2024@gmail.com"
        },
        {
          "name": "MICROSOFT INFRA",
          "symbol": "MSFT",
          "description": "Cloud Azure and capital allocation layer for reality kernels.",
          "twitter": "https://x.com",
          "creator_email": "misterick2024@gmail.com"
        },
        {
          "name": "AMRITA 109th Quantum",
          "symbol": "QNT",
          "description": "109-я Гуру-бусина каузальной матрицы AMRITA. Цифровой ключ, связывающий 108 стоянок Луны.",
          "twitter": "https://x.com",
          "creator_email": "misterick2024@gmail.com",
          "image_url": "https://githubusercontent.com"
        }
      ]
    }
    
    with open(config_file, "w", encoding="utf-8") as f:
        json.dump(new_config, f, indent=2, ensure_ascii=False)
    print(f"✅ Файл {config_file} успешно обновлен.")

    # 2. Чистим лог истории и активируем эволюцию
    clean_log = [
      {
        "timestamp": "2026-08-01 05:20:00",
        "cycle_status": "AMRITA_EVOLUTION_ACTIVE",
        "activated_key": "QNT_109_BEAD",
        "quantum_index": 156.52,
        "base_sol_asset": 144.0,
        "base_eth_asset": 1877.45,
        "swarm_intelligence": "QNT_RESONANCE_CONNECTED",
        "orje_spiral_status": "SEALED"
      }
    ]
    
    with open(log_file, "w", encoding="utf-8") as f:
        json.dump(clean_log, f, indent=2, ensure_ascii=False)
    print(f"⚡ Петля Локи разорвана в {log_file}. Запущена спираль Ørje.")

if __name__ == "__main__":
    update_amrita_core()
