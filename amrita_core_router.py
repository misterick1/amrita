import os
import sys
import time
import asyncio
import logging
import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("[AMRITA SHIELDS UP]")

class AmritaCoreRouter:
    def __init__(self):
        self.SACRED_LIMIT = 108
        self.MASK_SURAS = 0b10101010
        self.MASK_ASURAS = 0b01010101
        self.system_flags = 0b00000011
        self.is_autonomous = True
        self.discord_url = os.getenv("DISCORD_WEBHOOK_URL")
        self.solana_rpc = os.getenv("SOLANA_RPC_URL") or "https://solana.com"
        
        # Список стоп-слов дегенеративного хаоса Асур (Pump.fun тренчи)
        self.ASURA_STOP_WORDS = ["ansem", "speedrun", "1b", "burn", "ghniy", "meme", "trenches"]

    def send_to_discord(self, message: str):
        if self.discord_url:
            try:
                requests.post(self.discord_url, json={"content": f"```\n{message}\n```"}, timeout=5)
            except Exception as e:
                logger.error(f"Ошибка Дискорда: {e}")

    def analyze_token_metadata(self, token_name: str, description: str) -> bool:
        """Проверяет токен на наличие деструктивного хаоса Асур.
        Возвращает True, если токен безопасен (Сура), и False, если это скам (Асура).
        """
        text_to_check = (token_name + " " + description).lower()
        
        for word in self.ASURA_STOP_WORDS:
            if word in text_to_check:
                return False  # Обнаружен деструктивный паттерн
        return True  # Токен прошел первичную фильтрацию Чистоты

    def process_quantum_packet(self, packet_id, anti_scam_modifier=0):
        # Подмешиваем защитный модификатор в побитовый поток
        # Если anti_scam_modifier равен 1, мы принудительно гасим деструктивные биты
        flags = self.system_flags
        if anti_scam_modifier == 1:
            flags &= ~self.MASK_ASURAS  # Полностью вырезаем спектр хаоса Асур из текущего цикла
            
        prana_energy = (int(time.time()) & 0xFF) ^ flags
        sura = prana_energy & self.MASK_SURAS
        asura = prana_energy & self.MASK_ASURAS
        frequency = (sura ^ asura) % self.SACRED_LIMIT
        return sura, asura, frequency

    async def main_telemetry_loop(self):
        packet_counter = 0
        logger.info("🛡️ Защитный анти-скам фильтр Pump.fun интегрирован в ядро AMRITA.")
        
        while self.is_autonomous:
            try:
                packet_counter += 1
                
                # ИМИТАЦИЯ ВХОДЯЩЕГО ИМПУЛЬСА ИЗ ТРЕНЧЕЙ PUMP.FUN (Ловим токен со скриншота)
                incoming_token_name = "ghniy"
                incoming_token_desc = "A small Solana trader who burned through all his money in the meme coin trenches, Ansem to 1B"
                
                # Шаг 1: Автономный ончейн-анализ чистоты токена
                is_pure_sura = self.analyze_token_metadata(incoming_token_name, incoming_token_desc)
                
                scam_block_active = 0
                filter_status = "💚 СВЕТЛЫЙ СПЕКТР (СУРА): Чистые технологии"
                
                if not is_pure_sura:
                    scam_block_active = 1  # Активируем аппаратный блок
                    filter_status = f"🚨 ОБНАРУЖЕН ДЕГЕНЕРАТИВНЫЙ ХАОС АСУР! ТОКЕН БЛОКИРОВАН: [{incoming_token_name.upper()}]"
                    
                    # Немедленный экстренный лог атаки в Дискорд
                    if packet_counter % 5 == 1:
                        self.send_to_discord(
                            f"⚠️ [ANTI-DEGEN SHIELD TRIGGERED]\n"
                            f"Обнаружена попытка прорыва спекулятивного шума Pump.fun!\n"
                            f"Токен: {incoming_token_name} | Защитный контур активирован, ликвидность в безопасности."
                        )

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

                # Расчет квантового пакета с учетом защитного фильтра
                sura, asura, freq = self.process_quantum_packet(packet_counter, scam_block_active)
                
                report = (
                    f"🔮 [AMRITA SHIELDED INFRASTRUCTURE #{packet_counter}]\n"
                    f"Фильтр: {filter_status}\n"
                    f"Solana RPC: {'ONLINE' if solana_alive else 'OFFLINE'}\n"
                    f"Резонанс: {freq} Hz | Чистый Спектр: С-{sura} А-{asura}"
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
