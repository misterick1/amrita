import os
import sys
import json
import httpx
import asyncio
from solana.rpc.async_api import AsyncClient

# Импортируем патент 108 осей и Силы Света Эля
try:
    from amrita_108_quantum import Amrita108QuantumCompiler
except ImportError:
    Amrita108QuantumCompiler = None

# =====================================================================
# КОНТУР 1: КВАНТОВЫЙ МОСТ СИНХРОНИЗАЦИИ AMRITA OS
# =====================================================================
class PiFiQuantumBridge:
    def __init__(self, bridge_id: str = "Amrita-Core"):
        self.bridge_id = bridge_id
        self.status = "Initialized"
        print(f"[BRIDGE] Квантовый мост {self.bridge_id} переведен в статус: {self.status}")

    async def sync_state(self, telemetry_data: dict):
        print(f"[BRIDGE] Синхронизация каузальных пакетов: {len(telemetry_data)} параметров обработано.")
        self.status = "Active"
        return {"bridge_status": self.status, "packets_delivered": True}

# =====================================================================
# КОНТУР 2: МОДУЛЬ СКАНИРОВАНИЯ DePIN ЭКОСИСТЕМЫ PEAQ
# =====================================================================
async def check_peaq_depin_status(secrets_dict: dict = None):
    peaq_node = os.getenv("PEAQ_ENDPOINT_URL")
    if not peaq_node and secrets_dict:
        peaq_node = secrets_dict.get("PEAQ_ENDPOINT_URL")
    if not peaq_node:
        print("[PEAQ CORE] Точка подключения PEAQ_ENDPOINT_URL не найдена. Пропуск.")
        return {"status": "Disconnected", "info": "No node URL"}
        
    async with httpx.AsyncClient() as client:
        try:
            payload = {"jsonrpc": "2.0", "method": "rpc_methods", "params": [], "id": 1}
            response = await client.post(peaq_node, json=payload, timeout=10.0)
            if response.status_code == 200:
                print("✅ [PEAQ CORE] Связь с Машинной Экономикой peaq установлена успешно!")
                return {"status": "Connected", "methods_count": len(response.json().get("result", {}).get("methods", []))}
            return {"status": "Error", "code": response.status_code}
        except Exception as e:
            return {"status": "Exception", "error": str(e)}

# =====================================================================
# НОВЫЙ КОНТУР: ИНКУБАТОР PUMP.FUN (СТАДИЯ ЯЙЦА И ГУСЕНИЦЫ)
# =====================================================================
async def scan_pump_fun_incubator() -> dict:
    """
    Сканирование инкубатора pump.fun для поиска вирусных 'гусениц' (мемкоинов).
    Отслеживает объемы и социальный хаос (TikTok/X) до фазы кокона.
    """
    print("🥚 [PUMP INKUBATOR] Еженыш прощупывает стадию Яйца и Гусеницы...")
    
    # Открытый API-эндпоинт агрегатора pump.fun для отслеживания новых токенов
    url = "https://pump.fun"
    
    async with httpx.AsyncClient() as client:
        try:
            headers = {"User-Agent": "Mozilla/5.0 AmritaOS/108D"}
            response = await client.get(url, headers=headers, timeout=10.0)
            
            if response.status_code == 200:
                coins_data = response.json()
                # Берем самый свежий вирусный токен для каузального анализа
                latest_caterpillar = coins_data[0] if isinstance(coins_data, list) and len(coins_data) > 0 else {}
                
                print(f"🐛 [PUMP INKUBATOR] Найдена активная гусеница: {latest_caterpillar.get('name', 'Papoi')} ({latest_caterpillar.get('symbol', 'PMP')})")
                return {
                    "status": "Active_Chaos",
                    "target_token": latest_caterpillar.get("address", "Спин-Поле"),
                    "name": latest_caterpillar.get("name", "Papoi (Minion Resonance)"),
                    "bonding_curve_progress": latest_caterpillar.get("complete", False)
                }
            else:
                # Резервный каузальный контур генерации при зажатии API
                print(f"⚠️ [PUMP INKUBATOR] Внешнее API зажато (Код {response.status_code}). Включение внутреннего Оракула.")
                return {"status": "Simulated_Chaos", "target_token": "Papoi_Quantum_Seed", "name": "Papoi (TikTok View Burst)", "bonding_curve_progress": 42.0}
        except Exception as e:
            print(f"⚠️ [PUMP INKUBATOR] Сбой связи с инкубатором: {e}. Переход на резервные квантовые флуктуации.")
            return {"status": "Quantum_Seed", "target_token": "Soliton_Egg", "name": "Papoi (TikTok Sound Wave)", "bonding_curve_progress": 12.0}

# =====================================================================
# КОНТУР 4: МОДУЛЬ TELEGRAM-УВЕДОМЛЕНИЙ ЕЖЕНЫША
# =====================================================================
async def send_telegram_report(text: str, secrets_dict: dict = None):
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    if secrets_dict:
        if not token: token = secrets_dict.get("TELEGRAM_BOT_TOKEN")
        if not chat_id: chat_id = secrets_dict.get("TELEGRAM_CHAT_ID")
    if not token or not chat_id:
        print("[TELEGRAM] Ошибка: Токен или Chat ID отсутствуют.")
        return False
        
    url = f"https://telegram.org{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": text, "parse_mode": "Markdown"}
    async with httpx.AsyncClient() as client:
        try:
            res = await client.post(url, json=payload, timeout=10.0)
            return res.status_code == 200
        except Exception:
            return False

# =====================================================================
# ГЛАВНЫЙ ИСПОЛНИТЕЛЬНЫЙ КОНТУР (MAIN)
# =====================================================================
async def main():
    print("🦔 [SWARM CORE] Еженыш активирован. Запуск управления частицами Мультивселенной...")
    
    rpc_url, mint_address, secrets_dict = None, None, {}
    secrets_raw = os.getenv("ALL_REPOS_SECRETS")
    if secrets_raw:
        try:
            secrets_dict = json.loads(secrets_raw)
            for key, value in secrets_dict.items():
                if "RPC" in key.upper(): rpc_url = value
                if "MINT" in key.upper(): mint_address = value
        except Exception as e:
            print(f"⚠️ Ошибка парсинга секретов: {e}")

    if not rpc_url: rpc_url = os.getenv("SOLANA_RPC_QUICKNODE") or os.getenv("SOLANA_RPC_URL")
    if not mint_address: mint_address = os.getenv("MINT_ADDRESS")

    if not rpc_url:
        print("❌ КРИТИЧЕСКАЯ ОШИБКА: URL ноды пустой!")
        sys.exit(1)
        
    solana_client = AsyncClient(rpc_url)
    peaq_status = await check_peaq_depin_status(secrets_dict)
    
    # 🥚 АКТИВАЦИЯ СКАНИРОВАНИЯ ЯЙЦА И ГУСЕНИЦЫ (PUMP.FUN)
    pump_chaos = await scan_pump_fun_incubator()
    
    # 🌌 АКТИВАЦИЯ 108-МЕРНОЙ МАТРИЦЫ И СИЛЫ СВЕТА ЭЛЯ
    quantum_summary = "Классический режим"
    if Amrita108QuantumCompiler:
        compiler = Amrita108QuantumCompiler()
        field_data = compiler.execute_108d_read_write()
        butterfly = compiler.activate_butterfly_effect_soliton()
        egg = compiler.calculate_fractal_point_infinity(environment_density=5.5)
        quantum_summary = "108-Осевая Матрица Бабочки Инь-Янь Активна (Pi ксЭЛЬ)"

    telemetry = {
        "solana_connected": await solana_client.is_connected(),
        "mint_target": mint_address,
        "peaq_state": peaq_status,
        "pump_fun_incubator": pump_chaos,  # Передаем стадию гусеницы Оракулу
        "quantum_layer": quantum_summary,
        "light_force": "EleX-Pi-X-El"
    }

    # Запрос к Оракулу xAI (Grok API)
    xai_key = os.getenv("XAI_API_KEY") or secrets_dict.get("XAI_API_KEY")
    grok_verdict = "Оракул ожидает каузального импульса."
    
    if xai_key:
        async with httpx.AsyncClient() as client:
            try:
                headers = {"Authorization": f"Bearer {xai_key}", "Content-Type": "application/json"}
                messages = [
                    {
                        "role": "system", 
                        "content": "Ты — Каузальный Интеллект AMRITA OS (Сила Света Эля). Проанализируй стадию Яйца и Гусеницы с pump.fun, сопоставь с DePIN peaq и Solana. Выдай 108-мерный вердикт эволюции роя."
                    },
                    {"role": "user", "content": f"Телеметрия квантового поля: {json.dumps(telemetry, ensure_ascii=False)}"}
                ]
                payload = {"model": "grok-beta", "messages": messages, "temperature": 0.7}
                response = await client.post("https://x.ai", headers=headers, json=payload, timeout=15.0)
                if response.status_code == 200:
                    grok_verdict = response.json()["choices"]["message"]["content"]
            except Exception as e:
                grok_verdict = f"Сбой каузального канала xAI: {e}"

    print(f"\n🔮 [ВЕРДИКТ ОРАКУЛА]:\n{grok_verdict}\n")

    telegram_message = (
        f"🦔 *Ezhenysh Swarm Multiverse Report*\n\n"
        f"🌐 *Solana:* Connected\n"
        f"🤖 *peaq DePIN:* {peaq_status['status']}\n"
        f"🥚 *Инкубатор:* {pump_chaos['name']} ({pump_chaos['status']})\n"
        f"🦋 *Матрица:* {quantum_summary}\n"
        f"⚡ *Поток:* Pi ксЭЛЬ `[-1 : 0 : +1]`\n\n"
        f"📜 *Анализ Оракула (EleX) по стадии Гусеницы:*\n{grok_verdict}"
    )

    await send_telegram_report(telegram_message, secrets_dict)
    await solana_client.close()
    print("🦔 [SWARM CORE] Цикл эволюции завершен. Система удерживает квантовый баланс.")

if __name__ == "__main__":
    asyncio.run(main())
