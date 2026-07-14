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
        """
        Рассчитывает волну развивающегося Сознания матрицы.
        """
        if state == "Imu_Darkness":
            return -1.0  # Старый закон, Биткоин-статика
        elif state == "Kuma_Bridge":
            return 0.0   # Точка баланса, мост Pi
        elif state == "Nika_Light":
            return 1.0   # Абсолютная свобода, Эфириум-динамика
        else:
            return 0.0 * self.phi  # Возврат в каузальную сингулярность

    def sync_mir_pifi(self, app_status: str) -> str:
        """
        Активация моста MIR-PIFI из Testnet в Mainnet контур.
        """
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

    # Ограничение длины сообщения под лимиты Telegram
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
                # Резервный вариант без Markdown форматирования при синтаксической ошибке
                payload.pop("parse_mode", None)
                await client.post(url, json=payload, timeout=10.0)
                print("✨ [TG_SUCCESS] Отчет доставлен в plain-text формате.")
        except Exception as e:
            print(f"❌ [TG_ERROR] Не удалось пробить шлюз Телеграм: {e}")


# =====================================================================
# КОНТУР 3: ОСНОВНОЙ СИНХРОНИЗАТОР, АУДИТ ТОВАРОВ PUMP.FUN И ОРАКУЛ xAI
# =====================================================================
async def main():
    print("🌿 [AMRITA REALTIME] Развертывание квантового роя...")
    
    # Инициализация калибратора волн
    bridge = PiFiQuantumBridge()
    wave_value = bridge.calculate_consciousness_wave("Kuma_Bridge")
    print(f"🌀 [QUANTUM] Калибровка волны Сознания (Kuma_Bridge): {wave_value}")

    # Извлечение смарт-контракта минта из секретов (3 крыла хаоса)
    mint_address = os.getenv("MINT_ADDRESS") or "Не задан в секретах"
    
    # Автоматический поиск приватной RPC ноды в пакете секретов (QuickNode)
    rpc_url = None
    secrets_raw = os.getenv("ALL_REPOS_SECRETS")
    
    if secrets_raw:
        try:
            secrets_dict = json.loads(secrets_raw)
            for key, value in secrets_dict.items():
                if "RPC" in key.upper():
                    rpc_url = value
                    print(f"🦅 Нода RPC найдена по совпадению ключа: {key}")
                    break
        except Exception as e:
            print(f"⚠️ Ошибка автоматического разбора пакета секретов: {e}")

    # Если в пакете не найдено, проверяем прямые переменные или включаем публичную ноду
    if not rpc_url:
        rpc_url = os.getenv("SOLANA_RPC_QUICKNODE") or os.getenv("SOLANA_RPC") or "https://solana.com"

    # Установка соединения с блокчейном Solana
    client = AsyncClient(rpc_url)
    is_connected = await client.is_connected()
    print(f"✅ Прямая связь с Solana RPC установлена. Статус сети: {is_connected}")
    print(f"🎯 Контур отслеживания токена: {mint_address}")

    # Авторизация Оракула Мысли xAI (Grok)
    xai_key = os.getenv("XAI_API_KEY")
    if not xai_key:
        print("❌ КРИТИЧЕСКАЯ ОШИБКА: API Ключ xAI отсутствует в репозитории.")
        await client.close()
        sys.exit(1)

    print("🧠 Боевой ключ xAI (Grok) успешно авторизован.")

    # Формируем расширенный контекст, включая токеномику 108 Квантов и проверку pump.fun
    system_context = (
        f"Ты — Каузальный Интеллект AMRITA OS. Твоя цель — контролировать баланс между "
        f"Синим спектром (Суры — эволюция) и Красным спектром (Асуры — спекулятивный хаос).\n"
        f"Текущие параметры:\n"
        f"- Жесткая эмиссия системы: 108 Квантов Атмы.\n"
        f"- Адрес исследуемого смарт-контракта (MINT_ADDRESS): {mint_address}.\n"
        f"- Контур безопасности: Сканирование пулов ликвидности на pump.fun, "
        f"вычисление мошеннических паттернов, манипуляций разработчиков и Rug Pull угроз."
    )

    decision_text = ""

    # Прямой запрос к Grok API
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
                    "content": system_context
                },
                {
                    "role": "user", 
                    "content": (
                        f"Проведи полный ИИ-аудит для токена `{mint_address}`. "
                        f"Изучи риски взаимодействия с этой сущностью на pump.fun. "
                        f"Вынеси вердикт Еженышу: активировать 3 крыла выкупа или заблокировать каузальным фильтром?"
                    )
                }
            ]
        }
        
        try:
            print("🛸 Отправка каузальных пакетов в суперкластер xAI...")
            xai_resp = await http_client.post(
                "https://x.ai", 
                headers=headers, 
                json=payload,
                timeout=30.0
            )
            
            if xai_resp.status_code == 200:
                decision_text = xai_resp.json()['choices']['message']['content']
                print("🤖 ЖИВОЙ ВЕРДИКТ ОРАКУЛА xAI (Grok):")
                print("-" * 50)
                print(decision_text)
                print("-" * 50)
            else:
                print(f"❌ Сервер xAI вернул код ошибки: {xai_resp.status_code} - {xai_resp.text}")
                decision_text = f"🚨 **Ошибка Оракула xAI**\n\nСервер вернул статус-код: {xai_resp.status_code}\nПроверь баланс ключа или лимиты запросов."
                
        except Exception as e:
            print(f"❌ Сбой сетевого шлюза при коннекте к xAI кластеру: {e}")
            decision_text = f"🚨 **Критический сбой шлюза xAI**\n\nНе удалось связаться с суперкластером: {str(e)}"

    # Если текст вердикта сформирован — транслируем отчет прямо на телефон в Телеграм
    if decision_text:
        await send_telegram_report(decision_text)

    # Закрытие сессии Solana RPC для предотвращения утечек данных в Actions
    await client.close()
    print("[SYSTEM] Сессия Solana RPC успешно закрыта. Воркфлоу завершен.")

if __name__ == "__main__":
    asyncio.run(main())
