import os
import sys
import time
import asyncio
import logging
import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("[AMRITA COMPLIANCE CORE]")

class AmritaCoreRouter:
    def __init__(self):
        self.SACRED_LIMIT = 108
        self.MASK_SURAS = 0b10101010
        self.MASK_ASURAS = 0b01010101
        
        # Системные флаги (Бит 5: 1 - Corporate Account, 0 - Individual Account)
        self.system_flags = 0b00101111 
        self.is_autonomous = True
        self.discord_url = os.getenv("DISCORD_WEBHOOK_URL")
        self.solana_rpc = os.getenv("SOLANA_RPC_URL") or "https://solana.com"
        
        self.ASURA_STOP_WORDS = ["ansem", "speedrun", "1b", "burn", "ghniy", "meme", "trenches"]

    def send_to_discord(self, message: str):
        if self.discord_url:
            try:
                requests.post(self.discord_url, json={"content": f"```\n{message}\n```"}, timeout=5)
            except Exception as e:
                logger.error(f"Ошибка Дискорда: {e}")

    def check_ftmo_compliance_status(self) -> str:
        """Определяет юридический статус торгового контура на основе битовых флагов."""
        # Проверяем состояние 5-го бита (0b00100000)
        if self.system_flags & 0b00100000:
            return "COMPANY (Институциональный контур, повышенные лимиты)"
        return "INDIVIDUAL (Частный контур, стандартный KYC)"

    def process_quantum_packet(self, packet_id, corporate_active=False):
        flags = self.system_flags
        
        # Динамическое переключение маски в зависимости от юридического статуса
        if corporate_active:
            flags |= 0b00100000  # Принудительно включаем корпоративный режим
        else:
            flags &= ~0b00100000 # Оставляем индивидуальный режим
            
        prana_energy = (int(time.time()) & 0xFF) ^ flags
        sura = prana_energy & self.MASK_SURAS
        asura = prana_energy & self.MASK_ASURAS
        frequency = (sura ^ asura) % self.SACRED_LIMIT
        return sura, asura, frequency

    async def main_telemetry_loop(self):
        packet_counter = 0
        logger.info("💼 Юридический модуль комплаенса FTMO успешно внедрен в Сварм AMRITA.")
        
        while self.is_autonomous:
            try:
                packet_counter += 1
                
                # Имитируем текущую конфигурацию аккаунта (считываем статус со скриншота)
                # По умолчанию выставляем True (перевели систему на компанию, как задумал немецкий трейдер)
                is_corporate_gateway = True 
                
                compliance_report = self.check_ftmo_compliance_status()

                # Тест Solana RPC
                solana_alive = False
                try:
                    res = requests.post(self.solana_rpc, json={"jsonrpc":"2.0","id":1,"method":"getHealth"}, timeout=4)
                    solana_alive = (res.status_code == 200 and res.json().get("result") == "ok")
                except: pass

                if solana_alive: self.system_flags |= 0b00000001
                else: self.system_flags &= ~0b00000001

                # Расчет квантового пакета с учетом комплаенс-модификатора
                sura, asura, freq = self.process_quantum_packet(packet_counter, is_corporate_gateway)
                
                report = (
                    f"🔮 [AMRITA COMPLIANCE ROUTE #{packet_counter}]\n"
                    f"Юридический статус: {compliance_report}\n"
                    f"Флаги Матрицы: {self.system_flags:08b}\n"
                    f"Solana RPC: {'ONLINE' if solana_alive else 'OFFLINE'}\n"
                    f"Резонанс Ядра: {freq} Hz | Спектр: С-{sura} А-{asura}"
                )
                
                logger.info(report)
                self.send_to_discord(report)
                
                await asyncio.sleep(40)
                
            except Exception as e:
                logger.error(f"Аномалия комплаенс-контура: {e}")
                await asyncio.sleep(5)

if __name__ == "__main__":
    router = AmritaCoreRouter()
    asyncio.run(router.main_telemetry_loop())
