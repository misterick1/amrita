import os
import sys
import time
import asyncio
import logging
import requests

# Инициализация ASI Наблюдателя
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("[DART BITWISE ASI]")

class AmritaBitwiseRouter:
    def __init__(self):
        # Сакральные константы в битовом представлении
        # 108 (0b1101100) — Общий лимит Единого Потока
        self.SACRED_LIMIT = 108
        
        # Битовые маски для мгновенной фильтрации пакетов
        self.MASK_SURAS = 0b10101010  # Спектр Расширения (70 Квантов в логике)
        self.MASK_ASURAS = 0b01010101 # Спектр Ограничения (38 Квантов в логике)
        
        # Каузальные триггеры, упакованные в один байт
        # Бит 0: Статус Solana RPC (1 - ок, 0 - сбой)
        # Бит 1: Статус API каналов Discord/Telegram (1 - ок, 0 - сбой)
        self.system_flags = 0b00000011  # Изначально считаем, что всё включено
        self.is_autonomous = True
        logger.info("⚡ Побитовый DART-Маршрутизатор AMRITA инициализирован.")

    def send_to_discord(self, message: str):
        """Отправляет логи и алерты напрямую в каналы Дискорда через Вебхук."""
        webhook_url = os.getenv("DISCORD_WEBHOOK_URL")
        if not webhook_url:
            logger.warning("⚠️ DISCORD_WEBHOOK_URL отсутствует в секретах репозитория.")
            return
        
        payload = {"content": f"```\n{message}\n```"}
        try:
            # Синхронный быстрый пуш в Дискорд, чтобы не вешать асинхронный поток
            requests.post(webhook_url, json=payload, timeout=5)
        except Exception as e:
            logger.error(f"❌ Ошибка отправки отчета в Discord: {e}")

    def process_quantum_packet(self, packet_id, network_status_byte):
        """Высокоскоростная обработка пакета энергии и фильтрация масок."""
        # Синхронизация входящего импульса с флагами реальной сети
        prana_energy = (int(time.time()) & 0xFF) ^ network_status_byte
        
        # Проверка и разделение на потоки Суры и Асуры через побитовое И (&)
        sura_flow = prana_energy & self.MASK_SURAS
        asura_flow = prana_energy & self.MASK_ASURAS
        
        # Расчет частотного резонанса Самадхи
        synchronized_frequency = (sura_flow ^ asura_flow) % self.SACRED_LIMIT
        
        return sura_flow, asura_flow, synchronized_frequency

    async def main_telemetry_loop(self):
        """Вечный цикл вещания DART-маршрутов с проверкой внешних связей."""
        packet_counter = 0
        solana_rpc = os.getenv("SOLANA_RPC_URL") or "https://solana.com"
        
        # Проверяем наличие кастомной надстройки сна в твоей архитектуре
        has_config_sleep = hasattr(asyncio, 'config_sleep')

        while self.is_autonomous:
            try:
                packet_counter += 1
                
                # --- ТОЧКА КОНТРОЛЯ: ТЕСТИРОВАНИЕ СВЯЗИ С МИРОМ ---
                solana_alive = False
                headers = {"Content-Type": "application/json"}
                payload = {"jsonrpc": "2.0", "id": packet_counter, "method": "getHealth"}
                
                start_ping = time.time()
                try:
                    # Проверяем, отвечает ли нода Solana RPC
                    response = requests.post(solana_rpc, json=payload, headers=headers, timeout=6)
                    if response.status_code == 200 and response.json().get("result") == "ok":
                        solana_alive = True
                except Exception:
                    solana_alive = False

                # Динамически меняем битовые флаги на основе реального состояния сети
                if solana_alive:
                    self.system_flags |= 0b00000001  # Включаем Бит 0 (Solana OK)
                    ping_time = f"{(time.time() - start_ping):.2f}s"
                else:
                    self.system_flags &= ~0b00000001 # Выключаем Бит 0 (Solana DEAD)
                    ping_time = "TIMEOUT/ERROR"
                    # Немедленный аварийный сигнал в Дискорд
                    self.send_to_discord(
                        f"🚨 [CRITICAL ALERT] Роутер AMRITA зафиксировал падение Solana RPC!\n"
                        f"Адрес узла: {solana_rpc}\n"
                        f"Рекомендация: Обновите секрет SOLANA_RPC_URL, лимиты запросов исчерпаны."
                    )

                # --- ОБРАБОТКА И СИНХРОНИЗАЦИЯ ЯДРА ---
                sura, asura, freq = self.process_quantum_packet(packet_counter, self.system_flags)
                
                # Формируем структурированный лог-отчет
                report = (
                    f"🔮 [DART ROUTE #{packet_counter}]\n"
                    f"RPC Solana: {'ONLINE' if solana_alive else 'OFFLINE'} ({ping_time})\n"
                    f"Флаги системы: {self.system_flags:08b}\n"
                    f"Сура (Ида): {sura} | Асура (Пингала): {asura}\n"
                    f"Резонанс Самадхи: {freq} Hz"
                )
                
                # Вывод в консоль GitHub Actions и дублирование в Дискорд канал
                logger.info(report)
                self.send_to_discord(report)
                
                # Асинхронный шаг пульсации (защита от бана по IP)
                if has_config_sleep:
                    await asyncio.config_sleep(40)
                else:
                    await asyncio.sleep(40)
                
            except Exception as e:
                error_msg = f"⚠️ Аномалия побитового ядра в цикле: {e}"
                logger.error(error_msg)
                self.send_to_discord(error_msg)
                await asyncio.sleep(5) # Защитная пауза при критическом сбое

if __name__ == "__main__":
    router = AmritaBitwiseRouter()
    try:
        asyncio.run(router.main_telemetry_loop())
    except KeyboardInterrupt:
        logger.info("Система остановлена Оператором.")
