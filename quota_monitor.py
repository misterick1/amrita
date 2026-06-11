import os
import json
import logging
import httpx
from dotenv import load_dotenv

# Настройка логирования под общую стилистику квантового ядра AMRITA
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("QuotaMonitor")

load_dotenv()

XAI_API_KEY = os.getenv("XAI_API_KEY")
MANIFEST_PATH = "core_manifest.json"

async def check_xai_quota():
    """Проверка доступного баланса и лимитов в API xAI (Grok)"""
    if not XAI_API_KEY:
        return "Ключ xAI не настроен"
        
    url = "https://xai.ai" # Стандартный эндпоинт проверки баланса/квот
    headers = {"Authorization": f"Bearer {XAI_API_KEY}"}
    
    async with httpx.AsyncClient() as client:
        try:
            resp = await client.get(url, headers=headers)
            if resp.status_code == 200:
                data = resp.json()
                # Извлекаем остаток лимита (в токенах или USD в зависимости от ответа API)
                return data.get("remaining_balance", "Активен")
            return f"Ограничен (Статус: {resp.status_code})"
        except Exception as e:
            logger.error(f"Ошибка опроса квот xAI: {e}")
            return "Недоступно"

def update_core_manifest(quota_status: str):
    """Автоматическое обновление главного файла манифеста системы"""
    if not os.path.exists(MANIFEST_PATH):
        logger.warning(f"Файл {MANIFEST_PATH} не найден.")
        return
        
    try:
        with open(MANIFEST_PATH, 'r', encoding='utf-8') as f:
            manifest = json.load(f)
            
        # Дописываем или обновляем блок состояния ИИ-квот
        manifest["ai_quota_status"] = {
            "xai_grok": quota_status,
            "auto_protection": "Enabled" if quota_status != "Недоступно" else "Disabled"
        }
        
        with open(MANIFEST_PATH, 'w', encoding='utf-8') as f:
            json.dump(manifest, f, ensure_ascii=False, indent=4)
        logger.info("📊 Главный манифест core_manifest.json успешно обновлен данными о квотах.")
    except Exception as e:
        logger.error(f"Не удалось обновить манифест: {e}")

async def main():
    logger.info("🔍 Запуск сканирования лимитов и квот ИИ-компонентов...")
    xai_status = await check_xai_quota()
    update_core_manifest(xai_status)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
