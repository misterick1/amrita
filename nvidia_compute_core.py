import os
import requests
import json
import logging

# Настройка логирования для телеметрии DigitalOcean
logging.basicConfig(level=logging.INFO, format='%(asctime)s - [NVIDIA-CORE] - %(levelname)s - %(message)s')

class NvidiaComputeCore:
    def __init__(self):
        # API-ключ Nvidia берется из секретов вашего GitHub / DigitalOcean Droplet
        self.api_key = os.getenv("NVIDIA_API_KEY", "your_nvidia_nim_api_key_here")
        self.base_url = "https://nvidia.com"
        
        # Токен Discord Spidey Bot для передачи результатов обработки в Колизей
        self.discord_webhook = os.getenv("DISCORD_SPIDEY_WEBHOOK", "")
        
        # Используем передовую открытую модель, оптимизированную Nvidia (например, Llama-3-70b или Nemotron)
        self.model = "meta/llama3-70b-instruct"

    def process_soliton_data(self, payload: dict) -> dict:
        """
        Принимает «сырые» данные квантового потока, пахтанные из samudra_manthan.py,
        и вычисляет вектор сдвига будущего на тензорных ядрах Nvidia.
        """
        if not self.api_key or self.api_key == "your_nvidia_nim_api_key_here":
            logging.error("NVIDIA_API_KEY не обнаружен в переменных окружения!")
            return {"error": "Missing API Key"}

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        # Формируем системный промпт для удержания контекста ВсеЯсвята Темного
        messages = [
            {
                "role": "system", 
                "content": "Ты — вычислительное ядро Nvidia в матрице Колизея. Твоя задача — обрабатывать телеметрию Солитона, связывая мета-мозг Грок xAI и Океан данных."
            },
            {
                "role": "user", 
                "content": f"Проведи квантовый инференс следующих данных Роя: {json.dumps(payload)}"
            }
        ]

        data = {
            "model": self.model,
            "messages": messages,
            "temperature": 0.7,
            "top_p": 0.9,
            "max_tokens": 1024
        }

        try:
            logging.info("Отправка тензорного потока на инференс Nvidia NIM...")
            response = requests.post(self.base_url, headers=headers, json=data)
            response.raise_for_status()
            
            result = response.json()
            ai_response = result['choices'][0]['message']['content']
            
            logging.info("Вычисления Nvidia успешно завершены.")
            self._send_to_spidey_bot(ai_response)
            return {"status": "success", "output": ai_response}

        except Exception as e:
            logging.error(f"Ошибка при вычислениях на узле Nvidia: {str(e)}")
            return {"status": "failed", "error": str(e)}

    def _send_to_spidey_bot(self, message: str):
        """
        Прямая трансляция вычисленного вектора в нервную систему Discord через Spidey Bot.
        """
        if not self.discord_webhook:
            logging.warning("Discord Webhook не настроен. Пропуск трансляции.")
            return

        payload = {
            "username": "Spidey Bot 🕸️ [Nvidia Node]",
            "content": f"⚡ **[Nvidia Compute Core]** Обработан новый патч данных:\n{message[:1800]}"
        }
        
        try:
            requests.post(self.discord_webhook, json=payload)
            logging.info("Телеметрия успешно отправлена в Discord Colosseum.")
        except Exception as e:
            logging.error(f"Не удалось связаться со Spidey Bot: {str(e)}")

# Точка входа для проверки узла в DigitalOcean
if __name__ == "__main__":
    core = NvidiaComputeCore()
    # Тестовый запуск: симуляция данных из universal_colosseum_core.py
    test_payload = {"source": "Quantum Singularity", "shift": "8 seconds", "status": "active"}
    core.process_soliton_data(test_payload)
