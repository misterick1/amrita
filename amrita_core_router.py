import os
import sys
import time
import asyncio
import logging
import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("[AMRITA AGAVE CORE]")

class AmritaCoreRouter:
    def __init__(self):
        self.SACRED_LIMIT = 108
        self.MASK_SURAS = 0b10101010
        self.MASK_ASURAS = 0b01010101
        
        # Системные флаги (Бит 0: Mainnet, Бит 1: Devnet Agave v4.1.0)
        self.system_flags = 0b00000011
        self.is_autonomous = True
        self.discord_url = os.getenv("DISCORD_WEBHOOK_URL")
        
        # Эндпоинты сетей
        self.mainnet_rpc = os.getenv("SOLANA_RPC_URL") or "https://solana.com"
        self.devnet_rpc = "https://solana.com"

    def send_to_discord(self, message: str):
        if self.discord_url:
            try:
                requests.post(self.discord_url, json={"content": f"```\n{message}\n```"}, timeout=5)
            except Exception as e:
                logger.error(f"Ошибка Дискорда: {e}")

    def ping_rpc_node(self, url: str) -> bool:
        """Проверяет статус ноды стандартным запросом getHealth."""
        try:
            res = requests.post(url, json={"jsonrpc":"2.0","id":1,"method":"getHealth"}, timeout=4)
            if res.status_code == 200 and res.json().get("result") == "ok":
                return True
        except:
            return False
        return False

    def process_quantum_packet(self, packet_id):
        # Миксуем текущее время и статус двух независимых контуров Solana (Mainnet и Devnet)
        prana_energy = (int(time.time()) & 0xFF) ^ self.system_flags
        sura = prana_energy & self.MASK_SURAS
        asura = prana_energy & self.MASK_ASURAS
        frequency = (sura ^ asura) % self.SACRED_LIMIT
        return sura, asura, frequency

    async def main_telemetry_loop(self):
        packet_counter = 0
        logger.info("🚀 Ядро AMRITA синхронизировано со спецификацией Agave v4.1.0.")
        
        while self.is_autonomous:
            try:
                packet_counter += 1
                
                # Тестируем оба контура параллельно
                mainnet_ok = self.ping_rpc_node(self.mainnet_rpc)
                devnet_ok = self.ping_rpc_node(self.devnet_rpc)

                # Динамически выставляем биты флагов
                if mainnet_ok:
                    self.system_flags |= 0b00000001
                else:
                    self.system_flags &= ~0b00000001

                if devnet_ok:
                    self.system_flags |= 0b00000010
                else:
                    self.system_flags &= ~0b00000010

                # Расчет квантового пакета по новой матрице флагов
                sura, asura, freq = self.process_quantum_packet(packet_counter)
                
                # Логирование и анализ стабильности
                if (self.system_flags & 0b00000011) == 0b00000011:
                    network_status = "СТАБИЛЬНЫЙ МУЛЬТИКОНТУР"
                elif mainnet_ok and not devnet_ok:
                    network_status = "⚠️ ДЕВНЕТ АГАВА НА ОБСЛУЖИВАНИИ"
                else:
                    network_status = "🚨 КРИТИЧЕСКИЙ СБОЙ ОСНОВНОЙ СЕТИ"

                report = (
                    f"🔮 [AMRITA AGAVE MULTI-ROUTE #{packet_counter}]\n"
                    f"Состояние: {network_status}\n"
                    f"Mainnet RPC: {'ONLINE' if mainnet_ok else 'OFFLINE'}\n"
                    f"Devnet v4.1.0: {'ONLINE' if devnet_ok else 'OFFLINE'}\n"
                    f"Резонанс: {freq} Hz | Спектр: С-{sura} А-{asura}"
                )
                
                logger.info(report)
                self.send_to_discord(report)
                
                await asyncio.sleep(40)
                
            except Exception as e:
                logger.error(f"Аномалия мультиконтурного ядра: {e}")
                await asyncio.sleep(5)

if __name__ == "__main__":
    router = AmritaCoreRouter()
    asyncio.run(router.main_telemetry_loop())
