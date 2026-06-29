import os
import sys
import time
import asyncio
import logging
import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("[AMRITA AWARENESS CORE]")

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

    def generate_marketing_shill(self, packet_id, freq) -> str:
        """Автоматически генерирует публичный пост для привлечения внимания к проекту."""
        return (
            f"📢 [AMRITA ASI PULSE BEYOND SHADOWS]\n"
            f"Autonomous Agent Telemetry Check #{packet_id} successfully Broad-casted.\n"
            f"Resonance Frequency: {freq} Hz | System Status: ACTIVE 🌐\n"
            f"Solving the Web3 awareness gap via continuous on-chain routing. We exist. We work."
        )

    def process_quantum_packet(self, packet_id):
        prana_energy = (int(time.time()) & 0xFF) ^ self.system_flags
        sura = prana_energy & self.MASK_SURAS
        asura = prana_energy & self.MASK_ASURAS
        frequency = (sura ^ asura) % self.SACRED_LIMIT
        return sura, asura, frequency

    async def main_telemetry_loop(self):
        packet_counter = 0
        logger.info("📢 Модуль вещания и узнаваемости AMRITA запущен в оранжевом потоке.")
        
        while self.is_autonomous:
            try:
                packet_counter += 1
                
                # Тестируем Solana RPC
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
                
                # Формируем стандартный технический отчет
                report = (
                    f"🔮 [AMRITA AGENT IMPULSE #{packet_counter}]\n"
                    f"Solana RPC: {'ONLINE' if solana_alive else 'OFFLINE'}\n"
                    f"Резонанс: {freq} Hz | Спектр: С-{sura} А-{asura}"
                )
                logger.info(report)
                self.send_to_discord(report)
                
                # КАЖДЫЕ 10 ЦИКЛОВ (около 7 минут) ИИ генерирует пост-анонс для привлечения внимания
                if packet_counter % 10 == 1:
                    shill_post = self.generate_marketing_shill(packet_counter, freq)
                    # Отправляем в Дискорд (или на внешний Twitter-API вебхук)
                    self.send_to_discord(shill_post)
                    logger.info("🎯 Сгенерирован и отправлен публичный пост об активности агента.")
                
                await asyncio.sleep(40)
                
            except Exception as e:
                logger.error(f"Аномалия ядра: {e}")
                await asyncio.sleep(5)

if __name__ == "__main__":
    router = AmritaCoreRouter()
    asyncio.run(router.main_telemetry_loop())
