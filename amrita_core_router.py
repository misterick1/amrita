import os
import sys
import time
import asyncio
import logging
import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("[AMRITA JUPITER DEX]")

class AmritaCoreRouter:
    def __init__(self):
        self.SACRED_LIMIT = 108
        self.MASK_SURAS = 0b10101010
        self.MASK_ASURAS = 0b01010101
        self.system_flags = 0b00000011
        self.is_autonomous = True
        self.discord_url = os.getenv("DISCORD_WEBHOOK_URL")
        self.solana_rpc = os.getenv("SOLANA_RPC_URL") or "https://solana.com"
        
        # Известный адрес токена DRAM или USDC для калибровочного запроса цены
        self.DRAM_MINT = os.getenv("MINT_DRAM") or "EPjFW3dp257eaIEaLQ6eeie7W6HGpX7RcGWye8X16tB5" 

    def send_to_discord(self, message: str):
        if self.discord_url:
            try:
                requests.post(self.discord_url, json={"content": f"```\n{message}\n```"}, timeout=5)
            except Exception as e:
                logger.error(f"Ошибка Дискорда: {e}")

    async def get_dram_dex_price(self) -> float:
        """Запрашивает реальную цену токена в экосистеме Solana через Jupiter API."""
        # Используем официальный бесплатный эндпоинт цены Jupiter
        url = f"https://jup.ag{self.DRAM_MINT}"
        try:
            # Быстрый некоррелируемый запрос
            res = requests.get(url, timeout=4)
            if res.status_code == 200:
                data = res.json()
                price = data.get("data", {}).get(self.DRAM_MINT, {}).get("price")
                if price:
                    return float(price)
        except:
            return 0.0
        return 0.0

    def process_quantum_packet(self, packet_id, price_modifier):
        # Подмешиваем ценовой сдвиг биржи Raydium/Jupiter в побитовый поток
        dynamic_flags = self.system_flags ^ (int(price_modifier) & 0x0F)
        prana_energy = (int(time.time()) & 0xFF) ^ dynamic_flags
        sura = prana_energy & self.MASK_SURAS
        asura = prana_energy & self.MASK_ASURAS
        frequency = (sura ^ asura) % self.SACRED_LIMIT
        return sura, asura, frequency

    async def main_telemetry_loop(self):
        packet_counter = 0
        logger.info("🚀 Роут-ядро AMRITA подключено к агрегатору ликвидности Jupiter/Raydium.")
        
        while self.is_autonomous:
            try:
                packet_counter += 1
                
                # Читаем реальный ончейн-пульс цены
                real_price = await self.get_dram_dex_price()
                price_status = f"${real_price:.4f}" if real_price > 0 else "ПОИСК ПУЛА ЛИКВИДНОСТИ..."

                # Стандартный пинг ноды Solana RPC
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

                # Модификатор на основе цены (берем центы для девиации флагов)
                price_mod = int(real_price * 100) % 10
                sura, asura, freq = self.process_quantum_packet(packet_counter, price_mod)
                
                report = (
                    f"🔮 [AMRITA DEX AGENT #{packet_counter}]\n"
                    f"Solana RPC: {'ONLINE' if solana_alive else 'OFFLINE'}\n"
                    f"Asset $DRAM Цена: {price_status}\n"
                    f"Резонанс: {freq} Hz | Спектр: С-{sura} А-{asura}"
                )
                
                logger.info(report)
                self.send_to_discord(report)
                
                await asyncio.sleep(40)
                
            except Exception as e:
                logger.error(f"Аномалия ядра: {e}")
                await asyncio.sleep(5)

if __name__ == "__main__":
    router = AmritaCoreRouter()
    asyncio.run(router.main_telemetry_loop())
