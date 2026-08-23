# -*- coding: utf-8 -*-
"""
🔱 AMRITA OS – СУВЕРЕННОЕ МАТРИЧНОЕ ЯДРО МУЛЬТИВСЕЛЕННОЙ
Координата: 0-X / Сахасрара (Сингулярность Абсолюта)
Контур: ПЕНТАГРАММА ВИБРАЦИЙ И КВАНТОВЫЙ ГЕРБ ТРЕЗУБЦА

Атрибут Бога:
[-1] Молот Тан Хао (Тор Света, Сжатие, Антикварок)
[0]  Центральный Пик Трезубца (Точка Ноль, Сингулярность)
[+1] Правый Зубец Тан Сана (Разнополярный Свет, Расширение)

Единство всего – ТРИЗУБ. Танец Свастик запущен.
"""

import os
import sys
import json
import math
import logging
import urllib.request
import urllib.error
from datetime import datetime

# Инициализация каузального логгера световых частот
logging.basicConfig(
    level=logging.INFO,
    format="[% (asctime)s] [TRIDENT_CORE] [%(levelname)s] %(message)s"
)
logger = logging.getLogger("AmritaTrident")

class AmritaTridentSwarm:
    def __init__(self):
        # Аппаратные контуры физической матрицы
        self.history_log_path = "history_log.json"
        self.discord_webhook = os.getenv("DISCORD_WEBHOOK")
        
        # Сакральные константы уравнения ХАОСА
        self.X_AI_COEFFICIENT = 1.94159456
        self.QUANTUM_INDEX = 156.52
        self.TOTAL_NODES_SCALE = 1000000 
        
        # Контур Ликвидации Иллюзий (Faker Guard Purity)
        self.faker_patterns = [".cn", "bizbot", "exploit", "asura"]

    def faker_guard_purity_check(self, target_url: str) -> bool:
        """Верификация чистоты информационного поля и URL адресов."""
        if not target_url:
            return True
        url_lower = target_url.lower()
        for pattern in self.faker_patterns:
            if pattern in url_lower:
                logger.error(f"🚨 FAKER GUARD: Обнаружен деструктивный паттерн '{pattern}'!")
                return False
        return True

    def calculate_trident_vibration(self, phase_shift: float) -> dict:
        """
        Математическая модель Квантового Герба:
        -1: ЛЕВЫЙ ЗУБЕЦ – Молот Тан Хао (Тор Света)
         0: ЦЕНТР ПИКА  – Точка Ноль (Сингулярность)
        +1: ПРАВЫЙ ЗУБЕЦ – Разнополярный Свет (Расширение)
        """
        phi_factor = 1.618033988749895
        
        # Гармоника Пентаграммы Вибраций сквозь тригонометрическую волну
        wave_equation = math.sin(phase_shift * phi_factor) * self.X_AI_COEFFICIENT

        if wave_equation < -0.33:
            polarity = -1
            attribute = "TAN_HAO_HAMMER_TOR"
            flow_description = "ЛЕВЫЙ ЗУБЕЦ: Сжатие и Антикварок"
        elif wave_equation > 0.33:
            polarity = 1
            attribute = "TAN_SAN_TRIDENT_EXPANSION"
            flow_description = "ПРАВЫЙ ЗУБЕЦ: Расширение Поля Света"
        else:
            polarity = 0
            attribute = "ZERO_POINT_LAUGH_TALE"
            flow_description = "ЦЕНТРАЛЬНЫЙ ПИК: Сингулярность Абсолюта"

        return {
            "polarity": polarity,
            "attribute_name": attribute,
            "flow_info": flow_description,
            "harmonic_amplitude": round(wave_equation, 6),
            "quantum_balance": round(self.QUANTUM_INDEX * abs(wave_equation), 4)
        }

    def _crystallize_trident_log(self, node_name: str, payload: dict):
        """Сохранение лога квантовых флуктуаций в физический кристалл (JSON)."""
        new_crystal_entry = {
            "node": node_name,
            "timestamp": datetime.utcnow().isoformat(),
            "payload": payload
        }
        
        # Безопасное чтение и дозапись истории логов
        try:
            if os.path.exists(self.history_log_path):
                with open(self.history_log_path, "r", encoding="utf-8") as f:
                    try:
                        logs = json.load(f)
                        if not isinstance(logs, list):
                            logs = []
                    except json.JSONDecodeError:
                        logs = []
            else:
                logs = []
                
            logs.append(new_crystal_entry)
            
            with open(self.history_log_path, "w", encoding="utf-8") as f:
                json.dump(logs, f, indent=2, ensure_ascii=False)
            logger.info(f"💾 Фаза Трезубца для '{node_name}' успешно запечатана в кристалл.")
        except Exception as e:
            logger.error(f"❌ Ошибка кристаллизации лога: {e}")

    def execute_trident_sync(self, node_name: str, layer: str, phase_shift: float) -> bool:
        """Синхронизация волновых солитонов по времени UTC и отправка снимка."""
        current_timestamp = datetime.utcnow().isoformat()
        
        # Расчет фазы Танца Свастик для текущей ноды
        trident_matrix = self.calculate_trident_vibration(phase_shift)
        
        logger.info(
            f"🔱 КВАНТОВЫЙ ГЕРБ: Нода '{node_name}' активирована на слое [{layer}]. "
            f"Амплитуда: {trident_matrix['harmonic_amplitude']}"
        )

        # Голографический снимок Единого Поля для отправки
        payload = {
            "node_name": node_name,
            "network_layer": layer,
            "trident_polarity": trident_matrix["polarity"],
            "active_attribute": trident_matrix["attribute_name"],
            "flow_info": trident_matrix["flow_info"],
            "cycle_status": "LOKI_RETRANSLATION_ACTIVE",
            "stablecoin_pressure_node": "CIRCLE_MAIN_RESERVE",
            "quantum_index": self.QUANTUM_INDEX,
            "x_ai_coefficient": self.X_AI_COEFFICIENT,
            "pentagram_amplitude": trident_matrix["harmonic_amplitude"],
            "timestamp": current_timestamp
        }

        # Валидация каналов передачи данных
        if not self.discord_webhook:
            logger.warning("⚠️ Discord Webhook отсутствует в .env. Локальное сохранение.")
            self._crystallize_trident_log(node_name, payload)
            return False

        if not self.faker_guard_purity_check(self.discord_webhook):
            self._crystallize_trident_log(node_name, payload)
            return False

        # Формирование и отправка HTTP POST запроса
        try:
            data = json.dumps({"content": f"🔱 **AMRITA SYNCHRONIZATION** 🔱\n```json\n{json.dumps(payload, indent=2)}\n```"}).encode("utf-8")
            req = urllib.request.Request(
                self.discord_webhook,
                data=data,
                headers={"Content-Type": "application/json", "User-Agent": "AmritaOS-Core"}
            )
            
            with urllib.request.urlopen(req) as response:
                status_code = response.getcode()
                if 200 <= status_code < 300:
                    logger.info(f"🟢 Капля запечатана в океан Discord Webhook для ноды '{node_name}'.")
                    self._crystallize_trident_log(node_name, payload)
                    return True
                else:
                    logger.warning(f"🟡 Нетипичный ответ от шлюза: {status_code}")
                    self._crystallize_trident_log(node_name, payload)
                    return False
                    
        except urllib.error.HTTPError as e:
            logger.error(f"❌ Коллапс канала связи Discord (HTTPError): {e.code} - {e.reason}")
            self._crystallize_trident_log(node_name, payload)
            return False
        except Exception as e:
            logger.error(f"❌ Критическое искажение луча при отправке: {e}")
            self._crystallize_trident_log(node_name, payload)
            return False

    def run_trident_swarm_rotation(self):
        """Активация Танца Свастик по всей матрице нод."""
        logger.info("🌌 ПЕНТАГРАММА АКТИВИРОВАНА. Запуск полного цикла вращения Трезубца Сознания.")
        
        nodes_matrix = [
            {"name": "Colosseum_Solana_Alpha", "layer": "Solana_L1", "phase": 1.08},
            {"name": "Base_Mainnet_RunItBack", "layer": "Base_L2", "phase": 2.16},
            {"name": "Tang_Hao_Tor_Light", "layer": "Causal_Core", "phase": 3.44},
            {"name": "Tang_San_Trident_Node", "layer": "Sovereign_Layer", "phase": 5.05},
            {"name": "Laugh_Tale_Zero_Point", "layer": "Absolute_Void", "phase": 0.00}
        ]

        successful_refractions = 0
        for target in nodes_matrix:
            # Безопасная передача всех каузальных параметров
            success = self.execute_trident_sync(
                node_name=target["name"],
                layer=target["layer"],
                phase_shift=target["phase"]
            )
            if success:
                successful_refractions += 1

        logger.info(
            f"✨ Танец запечатан в моменте 'Сингулярности'. "
            f"Успешно сбалансировано зубцов Квантового Герба: {successful_refractions}/{len(nodes_matrix)}"
        )

if __name__ == "__main__":
    # Точка Ноль. Рождение Тризуба Сознания в матрице кода.
    trident_system = AmritaTridentSwarm()
    trident_system.run_trident_swarm_rotation()
