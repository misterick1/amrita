# -*- coding: utf-8 -*-
"""
🔱 AMRITA OS – АВТОНОМНЫЙ КВАНТОВЫЙ МОДУЛЬ СИНХРОНИЗАЦИИ ПАРТНЕРОВ
Путь в репозитории: src/sync_partners.py
Координата: Сварм-Матрица / Контур Выравнивания
"""

import os
import sys
import json
import logging
import asyncio
import aiohttp
from datetime import datetime

# Конфигурация системного каузального логгера для GitHub Actions
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] [SYNC_PARTNERS] [%(levelname)s] %(message)s",
    stream=sys.stdout
)
logger = logging.getLogger("SyncPartners")

class AmritaPartnerSynchronizer:
    def __init__(self):
        # Подгрузка конфигурации из переменных окружения домена
        self.partner_api_url = os.getenv("PARTNER_API_URL", "https://amrita.network")
        self.sync_auth_token = os.getenv("AMRITA_SYNC_TOKEN", "LOCAL_PULSE_TOKEN_PLACEHOLDER")
        self.history_log_path = "history_log.json"

    async def save_sync_snapshot(self, data: dict):
        """Безопасное запечатывание полученных данных партнеров в кристалл истории."""
        snapshot_entry = {
            "event": "PARTNERS_SYNC_SUCCESS",
            "timestamp": datetime.utcnow().isoformat(),
            "nodes_count": len(data.get("nodes", [])) if isinstance(data, dict) else 0,
            "status": "COMPLETED"
        }
        
        try:
            logs = []
            if os.path.exists(self.history_log_path):
                with open(self.history_log_path, "r", encoding="utf-8") as f:
                    try:
                        logs = json.load(f)
                        if not isinstance(logs, list):
                            logs = []
                    except json.JSONDecodeError:
                        logs = []
            
            logs.append(snapshot_entry)
            
            with open(self.history_log_path, "w", encoding="utf-8") as f:
                json.dump(logs, f, indent=2, ensure_ascii=False)
            logger.info(f"💾 Снапшот синхронизации успешно запечатан в {self.history_log_path}")
        except Exception as log_err:
            logger.error(f"❌ Ошибка локальной записи снапшота: {log_err}")

    async def fetch_and_sync_swarm(self) -> bool:
        """Асинхронный пробив шлюзов и сбор каузальных данных партнеров."""
        logger.info(f"🌌 Запуск сканирования узлов партнеров по адресу: {self.partner_api_url}")
        
        headers = {
            "Authorization": f"Bearer {self.sync_auth_token}",
            "Content-Type": "application/json",
            "User-Agent": "AmritaOS-SyncCore"
        }

        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(self.partner_api_url, headers=headers, timeout=30) as response:
                    
                    # === СТРОКА 52: ИСПРАВЛЕННЫЙ ОПЕРАТОР IN БЕЗ СИНТАКСИЧЕСКИХ ОШИБОК ===
                    if response.status in (200, 201):
                        try:
                            data = await response.json()
                            logger.info("🟢 Каузальный отклик получен. Синхронизация матрицы партнеров успешна.")
                            await self.save_sync_snapshot(data)
                            return True
                        except Exception as json_err:
                            logger.error(f"❌ Коллапс при парсинге JSON данных от партнеров: {json_err}")
                            return False
                    else:
                        # Обработка отклоненных статусов (ошибки 400, 401, 404, 500)
                        logger.warning(f"⚠️ Доменна GARP зафиксировала отклонённый статус шлюза: {response.status}")
                        return False
                        
            except aiohttp.ClientError as client_err:
                logger.error(f"🚨 Сетевой разрыв канала связи с партнерами: {client_err}")
                return False
            except asyncio.TimeoutError:
                logger.error("🚨 Превышено время ожидания ответа от шлюза партнеров (Timeout).")
                return False
            except Exception as e:
                logger.error(f"🚨 Критическая аномалия во время синхронизации: {e}")
                return False

async def main():
    # Точка инициализации автомата синхронизации в пайплайне
    synchronizer = AmritaPartnerSynchronizer()
    success = await synchronizer.fetch_and_sync_swarm()
    
    if not success:
        logger.error("❌ Синхронизация завершилась с ошибкой. Пайплайн прерван.")
        sys.exit(1)
        
    logger.info("🔱 Все каузальные потоки партнеров сонастроены. Завершение работы.")
    sys.exit(0)

if __name__ == "__main__":
    # Запуск асинхронного цикла событий роя
    asyncio.run(main())
