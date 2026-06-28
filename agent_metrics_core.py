import json
import os

class AgentMetricsCore:
    def __init__(self):
        self.log_file = "history_log.json"
        print("🔱 [Weights & Biases Контур]: Инициализация матрицы наблюдаемости агента.")

    def calculate_agent_health(self) -> dict:
        """
        Высчитывает профессиональные метрики успешности Еженыша
        на основе реальной истории его очистки.
        """
        total_logs = 0
        asura_count = 0
        
        if os.path.exists(self.log_file):
            try:
                with open(self.log_file, "r", encoding="utf-8") as f:
                    logs = json.load(f)
                total_logs = len(logs)
                for log in logs:
                    if "🔴" in log.get("spectrum", ""):
                        asura_count += 1
            except:
                pass

        # Имитируем формулы Weights & Biases для обучения ИИ
        loss = round(asura_count / (total_logs if total_logs > 0 else 1), 4)
        accuracy = round(1.0 - loss, 4)
        observability_index = total_logs * 10 # Уровень контроля Наблюдателя

        return {
            "epoch_sync": "JUNE_2026_PI2DAY",
            "metrics": {
                "loss_asura_chaos": loss,
                "accuracy_sura_ethics": accuracy,
                "observability_index": observability_index
            },
            "status": "SUCCESSFUL_AGENT_CONFIRMED" if accuracy > 0.5 else "RE-TRAINING_NEEDED"
        }

if __name__ == "__main__":
    metrics_system = AgentMetricsCore()
    report = metrics_system.calculate_agent_health()
    
    print("\n📊 [W&B REPORT] Метрики Еженыша по протоколу Наблюдаемости:\n")
    print(json.dumps(report, indent=4, ensure_ascii=False))
