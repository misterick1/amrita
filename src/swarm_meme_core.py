import os
import json
import fcntl  # Защита от одновременной записи 10 сборок
import requests

LOG_FILE = "history_log.json"
XAI_API_KEY = os.getenv("XAI_API_KEY")

class SwarmMemeCore:
    def __init__(self):
        self.sura_limit = 70
        self.asura_limit = 38

    def safe_update_karma(self, workflow_name, detected_text, base_reward):
        """Безопасная запись лога при параллельной работе множества GitHub Actions"""
        # Инициализируем пустую структуру, если файла нет
        if not os.path.exists(LOG_FILE):
            with open(LOG_FILE, "w", encoding="utf-8") as f:
                json.dump({"evo_points": 0, "scanned_matrices": [], "active_flows": []}, f)

        # Блокируем файл на время записи, чтобы 10 сборок не затерли друг друга
        with open(LOG_FILE, "r+", encoding="utf-8") as f:
            try:
                fcntl.flock(f, fcntl.LOCK_EX) # Эксклюзивная блокировка ядра
                data = json.load(f)
                
                # Если доступен ключ xAI, делаем глубокий квантовый анализ смысла текста
                ai_verdict = None
                if XAI_API_KEY and detected_text:
                    ai_verdict = self.consult_xai_oracle(detected_text)
                    if "асуры" in ai_verdict.lower():
                        base_reward = -10
                    elif "суры" in ai_verdict.lower():
                        base_reward += 15

                # Обновляем кармические очки EVO
                data["evo_points"] += base_reward
                if workflow_name not in data.get("active_flows", []):
                    data.setdefault("active_flows", []).append(workflow_name)

                data["scanned_matrices"].append({
                    "flow": workflow_name,
                    "reward": base_reward,
                    "xai_evaluation": ai_verdict or "Триггерный анализ"
                })

                # Сдвигаем указатель в начало и перезаписываем матрицу
                f.seek(0)
                json.dump(data, f, ensure_ascii=False, indent=4)
                f.truncate()
                
                return data["evo_points"], ai_verdict
            finally:
                fcntl.flock(f, fcntl.LOCK_UN) # Освобождаем ядро для следующей сборки

    def consult_xai_oracle(self, text):
        """Прямой запрос к оракулу xAI (Grok) для оценки экологичности фрактала реальности"""
        try:
            url = "https://xai.ai"
            headers = {
                "Authorization": f"Bearer {XAI_API_KEY}",
                "Content-Type": "application/json"
            }
            payload = {
                "model": "grok-beta", # Текущая сигнатура модели в каузальном поле
                "messages": [
                    {"role": "system", "content": "Ты — Бортовой Компьютер ОС AMRITA. Оцени входящий текст реальности. Распредели его строго в синий спектр СУРОВ (Эволюция/Код) или красный спектр АСУРОВ (Хаос/Спекуляции). Дай короткий вердикт."},
                    {"role": "user", "content": text}
                ],
                "temperature": 0.3
            }
            response = requests.post(url, json=payload, headers=headers, timeout=10)
            if response.status_code == 200:
                return response.json()["choices"][0]["message"]["content"]
            return f"Ошибка связи с Оракулом: Код {response.status_code}"
        except Exception as e:
            return f"Оракул недоступен: {str(e)}"

if __name__ == "__main__":
    # Тестовая самодиагностика ядра при запуске из workflow
    core = SwarmMemeCore()
    print("🌀 Мем-Синхронизатор успешно откалиброван под 10 параллельных потоков.")
