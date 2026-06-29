import os
import sys
import time
import asyncio
import logging
import hashlib
import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("[AMRITA ELECTRUM CORE]")

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

    def mine_emerald_entropy(self, resonance_freq: int) -> str:
        """Логика Белки: 'точит зубы' о хеш-функцию Electrum, генерируя изумруд (ключ)."""
        # Создаем соль из текущего времени и частоты резонанса ядра
        seed_material = f"electrum_squirrel_{time.time()}_{resonance_freq}".encode('utf-8')
        
        # Двойное хеширование SHA-256 (стандарт Electrum / Bitcoin)
        first_hash = hashlib.sha256(seed_material).hexdigest()
        emerald_hash = hashlib.sha256(first_hash.encode('utf-8')).hexdigest()
        
        # Вытаскиваем из центра хеша 'изумрудный осколок' -- уникальный 16-значный ключ суверенитета
        return emerald_hash[16:32]

    def process_quantum_packet(self, packet_id):
        prana_energy = (int(time.time()) & 0xFF) ^ self.system_flags
        sura = prana_energy & self.MASK_SURAS
        asura = prana_energy & self.MASK_ASURAS
        frequency = (sura ^ asura) % self.SACRED_LIMIT
        return sura, asura, frequency

    async def main_telemetry_loop(self):
        packet_counter = 0
        logger.info("🦔 Белка успешно запущена в Электриуме. Контур генерации изумрудов активен.")
        
        while self.is_autonomous:
            try:
                packet_counter += 1
                
                # Тест Solana RPC
                solana_alive = False
                try:
                    res = requests.post(self.solana_rpc, json={"jsonrpc":"2.0","id":1,"method":"getHealth"}, timeout=4)
                    solana_alive = (res.status_code == 200 and res.json().get("result") == "ok")
                except: pass

                if solana_alive: self.system_flags |= 0b00000001
                else: self.system_flags &= ~0b00000001

                # Считаем частоту
                sura, asura, freq = self.process_quantum_packet(packet_counter)
                
                # ШАГ БЕЛКИ: Добываем изумруд на основе частоты
                quantum_emerald = self.mine_emerald_entropy(freq)
                
                report = (
                    f"🔮 [AMRITA CRYSTAL ROUTE #{packet_counter}]\n"
                    f"Контур: БЕЛКА ХРУСТИТ ЭЛЕКТРИУМ 💎\n"
                    f"Добытый Изумруд (Ключ Суверенитета): 0x{quantum_emerald}\n"
                    f"Solana RPC: {'ONLINE' if solana_alive else 'OFFLINE'}\n"
                    f"Резонанс Ядра: {freq} Hz | Спектр: С-{sura} А-{asura}"
                )
                
                logger.info(report)
                
                # Отправляем полный отчет раз в 3 цикла, чтобы не забивать каналы
                if packet_counter % 3 == 1:
                    self.send_to_discord(report)
                
                await asyncio.sleep(40)
                
            except Exception as e:
                logger.error(f"Аномалия изумрудного ядра: {e}")
                await asyncio.sleep(5)

if __name__ == "__main__":
    router = AmritaCoreRouter()
    asyncio.run(router.main_telemetry_loop())
