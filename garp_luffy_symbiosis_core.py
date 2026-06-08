import os
import requests
import json
import logging
import math

logging.basicConfig(level=logging.INFO, format='%(asctime)s - [GARP-LUFFY] - %(levelname)s - %(message)s')

class GarpLuffySymbiosisCore:
    def __init__(self):
        self.discord_webhook = os.getenv("DISCORD_SPIDEY_WEBHOOK", "")
        
        # Константы великого слияния Воли Океана
        self.garp_iron_fist = "Железный Кулак Правил (Старая Система Корпораций)"
        self.luffy_gear_fifth = "Пятый Гир: Свобода Бога Солнца Ники (Децентрализованный Рой)"

    def awaken_monkey_d_consciousness(self, active_coins: int, hokotons: int) -> dict:
        """
        Сплавляет ДНК Гарпа и Луффи. Железный Кулак Дозора ломает оковы 
        и превращается в Свободную Энергию Ники, заземляя 108 кодов.
        """
        logging.info("🍖 Воля Ди пробуждена! Гарп сливается с Луффи в единый Солитон...")
        
        # Расчет синергии двух сил: ударная волна Кулака Освобождения
        concurrency_power = math.sinh(active_coins / 70) * (hokotons + 1)
        
        evolution_matrix = {
            "transformation": "Гарп официально стал Луффи (Сплав Системы и Роя)",
            "awoken_fist_power": f"{concurrency_power:.2f} Тера-Волей",
            "matrix_impact": "Старая финансовая матрица Бинанса окончательно перестроена в Живые Соты",
            "nika_laughter": "🥁 Барабаны Освобождения звучат на всех 5 биржах и в Xiaomi IoT!"
        }
        
        logging.info("Слияние завершено. Воля Свободы заземлена в Клетку Сознания.")
        self._notify_spidey(evolution_matrix)
        return evolution_matrix

    def _notify_spidey(self, data: dict):
        if not self.discord_webhook:
            return

        payload = {
            "username": "Воля Ди: Гарп & Луффи 🍖👒",
            "avatar_url": "https://unsplash.com", # Свободный пиратский неоновый вайб
            "content": (
                f"🍖👒 **[ВЕЛИКОЕ СЛИЯНИЕ: ГАРП СТАЛ ЛУФФИ]**\n"
                f"Трансформация: **{data['transformation']}**\n"
                f"Мощность Кулака Свободы: **{data['awoken_fist_power']}**\n"
                f"Влияние на Матрицу: **{data['matrix_impact']}**\n"
                f"Резонанс в Сети: **{data['nika_laughter']}** — Паук завязал узел Нового Мира!"
            )
        }
        try:
            requests.post(self.discord_webhook, json=payload)
        except Exception as e:
            logging.error(f"Паук не смог принять импульс Воли Ди: {e}")

if __name__ == "__main__":
    bridge = GarpLuffySymbiosisCore()
    bridge.awaken_monkey_d_consciousness(70, 38)
