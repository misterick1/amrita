# -*- coding: utf-8 -*-
# amrita / src / pifi_bridge.py
# Автономный Квантовый Мост PiFi — Полная защита от таймаутов

import os
import json
import time
import logging
import urllib.request
import urllib.parse

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] PiFi-Bridge: %(message)s')
logger = logging.getLogger("PiFi_Bridge")

class PiFiBridgeOrchestrator:
    def __init__(self):
        self.pi_api_key = os.getenv("PI_API_KEY", "FakePiKey_QuantumStub")
        self.pi_app_id = os.getenv("PI_APP_ID", "amrita-mir-app")
        self.law_of_phi = 1.6180339887
        self.pi_api_url = "https://minepi.com"

    def fetch_pifi_metrics(self) -> dict:
        """
        Сбор метрик Pi через встроенный urllib с жестким тайм-аутом.
        Защищает порты и сборщик от зависаний. Исключает ModuleNotFoundError.
        """
        if "FakePiKey" in self.pi_api_key:
            return self._generate_autonomous_pifi_pool()

        headers = {
            "Authorization": f"Key {self.pi_api_key}",
            "X-App-ID": self.pi_app_id
        }

        try:
            req = urllib.request.Request(f"{self.pi_api_url}/me", headers=headers, method="GET")
            # Жесткое ограничение ожидания — 2.0 секунды. Пробка исключена!
            with urllib.request.urlopen(req, timeout=2.0) as response:
                if response.status == 200:
                    data = json.loads(response.read().decode('utf-8'))
                    logger.info("🔮 Данные Pi Network успешно интегрированы.")
                    return {
                        "status": "ONLINE_RESONANCE",
                        "pi_user": data.get("username", "Eurasia_Node"),
                        "pifi_index": round(108 * self.law_of_phi, 4),
                        "sync_timestamp": int(time.time())
                    }
        except Exception as e:
            logger.warning(f"⚠️ Сеть Pi недоступна ({e}). Включение автономного квантового генератора.")
            
        return self._generate_autonomous_pifi_pool()

    def _generate_autonomous_pifi_pool(self) -> dict:
        """Автономный изумрудный генератор 0-Потенциала"""
        pifi_base = 3.1415926535 * self.law_of_phi * 10
        return {
            "status": "AUTONOMOUS_UNITY",
            "pi_user": "Amrita_Causal_Core",
            "pifi_index": round(pifi_base, 4),
            "sync_timestamp": int(time.time())
        }

    def compile_static_pifi_data(self, output_path="src/pifi_data.json"):
        """Запись валидного JSON для фронтенда amrita-mir.com"""
        metrics = self.fetch_pifi_metrics()
        os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(metrics, f, indent=4, ensure_all_ascii=False)
        logger.info(f"💾 Конфиг PiFi сохранен: {output_path}")

if __name__ == "__main__":
    bridge = PiFiBridgeOrchestrator()
    bridge.compile_static_pifi_data()
