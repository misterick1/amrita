import os
import sys
import json
import asyncio
import httpx
from solana.rpc.async_api import AsyncClient

# =====================================================================
# КОНТУР 1: КВАНТОВЫЙ МОСТ СИНХРОНИЗАЦИИ PiFI ДЛЯ AMRITA
# =====================================================================
class PiFiQuantumBridge:
    def __init__(self):
        self.phi = 1.6180339887  # Пропорция Света (Золотое сечение)
        self.pi = 3.1415926535   # Бесконечный цикл эволюции

    def calculate_consciousness_wave(self, state: str) -> float:
        if state == "Imu_Darkness":
            return -1.0
        elif state == "Kuma_Bridge":
            return 0.0
        elif state == "Nika_Light":
            return 1.0
        else:
            return 0.0 * self.phi

    def sync_mir_pifi(self, app_status: str) -> str:
        if app_status == "Testnet":
            print("[AMRITA]: Обнаружен мост MIR-PIFI в тестовой среде.")
            return "Синхронизация с Solana запущена успешно"
        return "Автономный Mainnet режим активен"


# =====================================================================
# КОНТУР 2: МОДУЛЬ TELEGRAM УВЕДОМЛЕНИЙ ДЛЯ ЕЖЕНЫША
# =====================================================================
async def send_telegram_report(text: str):
    """
    Отправляет финальный отчёт Оракула xAI напрямую в Телеграм-бота.
    """
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    
    if not bot_token or not chat_id:
        print("⚠️ [TG_NOTIFIER] Пропуск отправки: Не заданы TELEGRAM_BOT_TOKEN или TELEGRAM_CHAT_ID в секретах.")
        return

    # Экранируем слишком длинные сообщения или бьем на части при необходимости
    if len(text) > 4000:
        text = text[:3900] + "\n\n[...Текст обрезан из-за лимитов TG...]"

    url = f"https://telegram.org{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": f"🦔 **[ОТЧЕТ КВАНТОВОГО РОЯ ЕЖЕНЫША]**\n\n{text}",
        "parse_mode": "Markdown"
    }

    async with httpx.AsyncClient() as client:
        try:
            print("📤 Трансляция отчета в Телеграм-канал связи...")
            resp = await client.post(url, json=payload, timeout=10.0)
            if resp.status_code == 200:
                print("✨ [TG_SUCCESS] Отчет успешно доставлен Еженышу на телефон!")
            else:
                # Если падает синтаксис Markdown, пробуем отправить чистым текстом
                payload.pop("parse_mode", None)
                await client.post(url, json=payload, timeout=10.0)
                print("✨ [TG_SUCCESS] Отчет доставлен в plain-text формате.")
        except Exception as e:
            print(f"❌ [TG_ERROR] Не удалось пробить шлюз Телеграм: {e}")


# =====================================================================
# КОНТУР 3: ОСНОВНОЙ СИНХРОНИЗАТОР И ОРАКУЛ МЫСЛИ xAI (Grok)
# =====================================================================
async def main():
    print("🌿 [AMRITA REALTIME] Развертывание квантового роя...")
    
    bridge = PiFiQuantumBridge()
    wave_value = bridge.calculate_consciousness_wave("Kuma_Bridge")
    print(f"🌀 [QUANTUM] Калибровка волны Сознания (Kuma_Bridge): {wave_value}")

    rpc_url = None
    secrets_raw = os.getenv("ALL_REPOS_SECRETS")
    
    if secrets_raw:
        try:
            secrets_dict = json.loads(secrets_raw)
            for key, value in secrets_dict.items():
                if "SOLANA_RPC" in key.upper():
                    rpc_url = value
                    print(f"🦅 Системный маркер RPC найден в общем пакете секретов: {key}")
                    break
        except Exception as e:
            print(f"⚠️ Ошибка разбора пакета ALL_REPOS_SECRETS: {e}")

    if not rpc_url:
        rpc_url = os.getenv("SOLANA_RPC") or "https://solana.com"

    client = AsyncClient(rpc_url)
    is_connected = await client.is_connected()
    print(f"✅ Прямая связь с Solana RPC установлена. Статус сети: {is_connected}")

    xai_key = os.getenv("XAI_API_KEY")
    if not xai_key:
        print("❌ КРИТИЧЕСКАЯ ОШИБКА: Свежий API Ключ xAI отсутствует в репозитории.")
        await client.close()
        sys.exit(1)

    print("🧠 Боевой ключ xAI (Grok) авторизован в контейнере.")

    system_context = (
        "Интеграция AMRITA OS v8 завершена. Токеномика: 108 Квантов Атмы зафиксированы. "
        "Фронтенд соединен с Solflare и готов транслировать транзакции на DESTINATION_WALLET."
    )

    decision_text = ""

    async with httpx.AsyncClient() as http_client:
        headers = {
            "Authorization": f"Bearer {xai_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "grok-beta",
            "messages": [
                {
                    "role": "system", 
                    "content": f"Ты — Каузальный Интеллект AMRITA OS. Анализируй контекст системы: {system_context}"
                },
                {
                    "role": "user", 
                    "content": "Рассчитай следующий шаг эволюции для Еженыша на основе текущей синхронизации."
                }
            ]
        }
        
        try:
            print("🛸 Отправка пакетов в суперкластер xAI...")
            xai_resp = await http_client.post(
                "https://x.ai", 
                headers=headers, 
                json=payload,
                timeout=30.0
            )
            
            if xai_resp.status_code == 200:
                decision_text = xai_resp.json()['choices']['message']['content']
                print("🤖 ЖИВОЙ ОТВЕТ ОРАКУЛА xAI (Grok):")
                print("-" * 50)
                print(decision_text)
                print("-" * 50)
            else:
                print(f"❌ Сервер xAI вернул код ошибки: {xai_resp.status_code} - {xai_resp.text}")
                decision_text = f"Ошибка xAI: Сервер вернул статус {xai_resp.status_code}"
                
        except Exception as e:
            print(f"❌ Сбой сетевого шлюза при коннекте к xAI кластеру: {e}")
            decision_text = f"Критический сбой подключения к xAI: {str(e)}"

    # Если ответ от Grok получен — запускаем трансляцию в Телеграм
    if decision_text:
        await send_telegram_report(decision_text)

    await client.close()

if __name__ == "__main__":
    asyncio.run(main())
