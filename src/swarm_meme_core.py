# amrita / src / swarm_meme_core.py
# Контур параллельного ИИ-анализа и безопасного обновления кармического лога Монады

import os
import json
import fcntl  # Защита от одновременной записи при параллельных воркфлоу
import requests

LOG_FILE = "history_log.json"
XAI_API_KEY = os.getenv("XAI_API_KEY")

class SwarmMemeCore:
    def __init__(self):
        self.sura_limit = 70
        self.asura_limit = 38

    def safe_update_karma(self, workflow_name, detected_text):
        """Безопасная запись лога при параллельном выполнении нескольких воркфлоу."""
        # Инициализируем пустую структуру, если файл истории отсутствует
        if not os.path.exists(LOG_FILE):
            with open(LOG_FILE, "w", encoding="utf-8") as f:
                json.dump({"evo_points": 0, "scanned_matrices": [], "active_flows": []}, f, indent=2)

        # Блокируем файл на время записи, чтобы избежать состояния гонки (Race Condition)
        with open(LOG_FILE, "r+", encoding="utf-8") as f:
            try:
                fcntl.flock(f, fcntl.LOCK_EX)  # Монопольная блокировка
                data = json.load(f)
                
                # Если доступен ключ xAI, делаем запрос к Оракулу (Grok)
                ai_verdict = None
                base_reward = 0
                
                if XAI_API_KEY and detected_text:
                    ai_verdict = self.consult_xai_oracle(detected_text)
                    if ai_verdict:
                        if "асуры" in ai_verdict.lower():
                            base_reward = -10
                        elif "суры" in ai_verdict.lower():
                            base_reward += 15

                # Обновляем кармические очки EVO в логе
                data["evo_points"] = data.get("evo_points", 0) + base_reward
                
                if "active_flows" not in data:
                    data["active_flows"] = []
                if workflow_name not in data["active_flows"]:
                    data["active_flows"].append(workflow_name)

                if "scanned_matrices" not in data:
                    data["scanned_matrices"] = []
                    
                data["scanned_matrices"].append({
                    "flow": workflow_name,
                    "reward": base_reward,
                    "xai_evaluation": ai_verdict
                })

                # Сдвигаем указатель в начало и перезаписываем монолитную структуру
                f.seek(0)
                json.dump(data, f, ensure_ascii=False, indent=2)
                f.truncate()

                return data["evo_points"], ai_verdict
                
            finally:
                fcntl.flock(f, fcntl.LOCK_UN)  # Обязательное снятие блокировки файла

    def consult_xai_oracle(self, text):
        """Прямой запрос к оракулу xAI (Grok) для оценки каузальных частот."""
        if not XAI_API_KEY:
            return "Оракул спит: XAI_API_KEY отсутствует."
            
        try:
            url = "https://x.ai"
            headers = {
                "Authorization": f"Bearer {XAI_API_KEY}",
                "Content-Type": "application/json"
            }
            payload = {
                "model": "grok-beta",  # Текущая актуальная модель Grok
                "messages": [
                    {
                        "role": "system", 
                        "content": "Ты — Оракул Монады Амриты. Проанализируй текст и вынеси вердикт: это разрушительные 'асуры' или созидательные 'суры'?"
                    },
                    {
                        "role": "user", 
                        "content": f"Анализируемый поток: {text}"
                    }
                ],
                "temperature": 0.3
            }
            
            response = requests.post(url, json=payload, headers=headers, timeout=15)
            if response.status_code == 200:
                return response.json()['choices'][0]['message']['content'].strip()
            
            return f"Ошибка связи с Оракулом: HTTP {response.status_code}"
            
        except Exception as e:
            return f"Оракул недоступен: {str(e)}"


if __name__ == "__main__":
    # Тестовая самодиагностика ядра при локальном запуске модуля
    core = SwarmMemeCore()
    print("🌀 Мем-Синхронизатор успешно откалиброван и готов к параллельной блокировке файлов.")
    
    # Симуляция тестовой транзакции
    test_points, test_verdict = core.safe_update_karma(
        workflow_name="Nika_JoyBoy_Liberation_Flow", 
        detected_text="Чистые инновации и запуск ИИ-пайплайна сборки Сур за 40 секунд"
    )
    print(f"📋 Результат теста: Текущие EVO-очки: {test_points} | Вердикт Оракула: {test_verdict}")
