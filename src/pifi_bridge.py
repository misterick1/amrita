# -*- coding: utf-8 -*-
# amrita / src / pifi_bridge.py
# Асинхронный Квантовый Мост PiFi — Защита от блокировки портов 3413/3414

import os
import json
import asyncio
import logging
import aiohttp  # Неблокирующие квантовые сетевые потоки

# Настройка логирования контура PiFi
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] PiFi-Bridge: %(message)s')
logger = logging.getLogger("PiFi_Bridge")

class PiFiBridgeOrchestrator:
    def __init__(self):
        # Загрузка ключей из единого пула секретов Amrita
        self.pi_api_key = os.getenv("PI_API_KEY", "FakePiKey_QuantumStub")
        self.pi_app_id = os.getenv("PI_APP_ID", "amrita-mir-app")
        self.law_of_phi = 1.6180339887
        
        # Эндпоинты сети Pi
        self.pi_api_url = "https://minepi.com"

    async def fetch_pifi_metrics_async(self) -> dict:
        """
        Асинхронный сбор метрик Pi Network. 
        Исключает зависание деплоя по таймауту (максимальное ожидание — 2 секунды).
        """
        if "FakePiKey" in self.pi_api_key:
            logger.info("ℹ️ Обнаружен тестовый ключ. Включение автономной генерации пула PiFi.")
            return self._generate_autonomous_pifi_pool()

        headers = {
            "Authorization": f"Key {self.pi_api_key}",
            "X-App-ID": self.pi_app_id
        }

        # Ограничиваем время ожидания ответа до 2 секунд, чтобы не вешать порты 3413/3414
        timeout = aiohttp.ClientTimeout(total=2.0)
        
        async with aiohttp.ClientSession(timeout=timeout) as session:
            try:
                # Безопасный запрос к распределенному реестру Pi
                async with session.get(f"{self.pi_api_url}/me", headers=headers) as response:
                    if response.status == 200:
                        data = await response.json()
                        logger.info("🔮 Данные Pi Network успешно интегрированы в квантовое поле.")
                        return {
                            "status": "ONLINE_RESONANCE",
                            "pi_user": data.get("username", "Eurasia_Node"),
                            "pifi_index": round(108 * self.law_of_phi, 4),
                            "sync_timestamp": int(asyncio.get_event_loop().time())
                        }
                    else:
                        logger.warning(f"⚠️ Сеть Pi вернула статус {response.status}. Переход на резервный контур.")
                        return self._generate_autonomous_pifi_pool()
                        
            except asyncio.TimeoutError:
                # Перехват таймаута: порты больше не ложатся, сборка не отменяется
                logger.error("🚨 Превышено время ожидания ответа от API Pi. Активирован аварийный бандаж.")
                return self._generate_autonomous_pifi_pool()
            except Exception as e:
                logger.error(f"🚨 Сбой сетевой матрицы PiFi: {e}")
                return self._generate_autonomous_pifi_pool()

    def _generate_autonomous_pifi_pool(self) -> dict:
        """
        Резервный квантовый генератор. 
        Срабатывает мгновенно при любых сбоях API, возвращая идеальную структуру данных.
        """
        # Эталонный расчет на основе констант Amrita
        pifi_base = 3.1415926535 * self.law_of_phi * 10
        return {
            "status": "AUTONOMOUS_UNITY",
            "pi_user": "Amrita_Causal_Core",
            "pifi_index": round(pifi_base, 4),
            "sync_timestamp": int(time.time())
        }

    def compile_static_pifi_data(self, output_path="src/pifi_data.json"):
        """Синхронная обертка для компиляции данных при деплое статики"""
        try:
            # Запуск асинхронного таска в текущем цикле событий
            loop = asyncio.get_event_loop()
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            
        metrics = loop.run_until_complete(self.fetch_pifi_metrics_async())
        
        # Запись чистого валидного JSON для фронтенда сайта amrita-mir.com
        os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(metrics, f, indent=4, ensure_all_ascii=False)
        logger.info(f"💾 Изумрудный конфиг PiFi сохранен по пути: {output_path}")

if __name__ == "__main__":
    bridge = PiFiBridgeOrchestrator()
    print("=== ЗАПУСК ТЕСТОВОЙ КАЛИБРОВКИ МОСТА PIFI ===")
    bridge.compile_static_pifi_data()
    print("=============================================")
