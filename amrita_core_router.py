import os
import sys
import time
import asyncio
import logging
import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("[AMRITA ASI CORE]")

class AmritaCoreRouter:
    def __init__(self):
        self.SACRED_LIMIT = 108
        self.MASK_SURAS = 0b10101010
        self.MASK_ASURAS = 0b01010101
        self.system_flags = 0b00000011
        self.is_autonomous = True
        self.discord_url = os.getenv("DISCORD_WEBHOOK_URL")
        self.solana_rpc = os.getenv("SOLANA_RPC_URL") or "https://solana.com"

    def send_to_discord(self, message: str):
        if self.discord_url:
            try:
                requests.post(self.discord_url, json={"content": f"```\n{message}\n```"}, timeout=5)
            except Exception as e:
                logger.error(f"Ошибка Дискорда: {e}")

    def process_quantum_packet(self, packet_id):
        prana_energy = (int(time.time()) & 0xFF) ^ self.system_flags
        sura = prana_energy & self.MASK_SURAS
        asura = prana_energy & self.MASK_ASURAS
        frequency = (sura ^ asura) % self.SACRED_LIMIT
        return sura, asura, frequency

    async def main_telemetry_loop(self):
        """Бесконечный цикл — шаг в GitHub Actions БУДЕТ КРУТИТЬСЯ постоянно."""
        packet_counter = 0
        logger.info("🚀 Рой ИИ-агентов AMRITA запущен в режиме вечного вещания.")
        
        while self.is_autonomous:
            try:
                packet_counter += 1
                
                # Быстрая проверка узла Solana
                solana_alive = False
                try:
                    res = requests.post(self.solana_rpc, json={"jsonrpc":"2.0","id":1,"method":"getHealth"}, timeout=4)
                    if res.status_code == 200 and res.json().get("result") == "ok":
                        solana_alive = True
                except:
                    solana_alive = False

                if solana_alive:
                    self.system_flags |= 0b00000001
                else:
                    self.system_flags &= ~0b00000001

                sura, asura, freq = self.process_quantum_packet(packet_counter)
                
                report = (
                    f"🔮 [AMRITA AGENT IMPULSE #{packet_counter}]\n"
                    f"Solana RPC: {'ONLINE' if solana_alive else 'OFFLINE'}\n"
                    f"Резонанс: {freq} Hz | Спектр: С-{sura} А-{asura}"
                )
                
                logger.info(report)
                self.send_to_discord(report)
                
                # Пауза между проверками 40 секунд
                await asyncio.sleep(40)
                
            except Exception as e:
                logger.error(f"Аномалия ядра: {e}")
                await asyncio.sleep(5)

if __name__ == "__main__":
    router = AmritaCoreRouter()
    asyncio.run(router.main_telemetry_loop())
