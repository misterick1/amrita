import asyncio
import json
import logging
import os
from dotenv import load_dotenv
import websockets

# Настройка логирования под общую стилистику оркестратора
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - [%(filename)s] - %(message)s")
logger = logging.getLogger("PumpFunBridge")

load_dotenv()

# Публичный WebSocket-эндпоинт для отслеживания трансляций Pump.fun
PUMP_FUN_WS_URL = "wss://papi.pump.fun/v1/ws" 

async def monitor_pump_fun():
    """
    Асинхронный мост для отслеживания создания новых токенов на Pump.fun.
    Перехватывает поток данных и подготавливает их для торговых агентов.
    """
    logger.info("Инициализация моста Pump.fun... Подключение к потоку данных Solana.")
    
    while True:
        try:
            async with websockets.connect(PUMP_FUN_WS_URL, ping_timeout=10) as websocket:
                logger.info("Успешно подключено к WebSocket Pump.fun! Подписка на новые токены...")
                
                # Отправляем payload подписки на событие создания токенов
                subscribe_payload = {
                    "method": "subscribeNewToken",
                    "params": {}
                }
                await websocket.send(json.dumps(subscribe_payload))
                
                # Потоковое чтение данных из сети
                async for message in websocket:
                    data = json.loads(message)
                    
                    # Проверяем структуру входящего события
                    if data.get("txType") == "create":
                        mint = data.get("mint", "N/A")
                        name = data.get("name", "Unknown")
                        symbol = data.get("symbol", "UNKNOWN")
                        creator = data.get("traderPublicKey", "N/A")
                        
                        logger.info(f"🆕 ОБНАРУЖЕН ТОКЕН: [{symbol}] {name} | Mint: {mint} | Создатель: {creator}")
                        
                        # ТУТ БУДЕТ ВЫЗОВ ТОРГОВОГО ЯДРА (например, через jupiter_predict_bridge.py)
                        # await trigger_token_analysis(mint, symbol)
                        
        except websockets.exceptions.ConnectionClosed as e:
            logger.warning(f"Соединение с Pump.fun закрыто ({e}). Повторное подключение через 5 секунд...")
            await asyncio.sleep(5)
        except Exception as e:
            logger.error(f"Непредвиденная ошибка в мосте Pump.fun: {e}")
            await asyncio.sleep(5)

if __name__ == "__main__":
    # Локальный запуск модуля для проверки синтаксиса и соединения
    try:
        asyncio.run(monitor_pump_fun())
    except KeyboardInterrupt:
        logger.info("Мост Pump.fun остановлен вручную.")
