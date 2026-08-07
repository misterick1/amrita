import os
import json
import logging
import urllib.request
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("AMRITA_Repairman")

class GitHubWorkflowRepairman:
    def __init__(self, repo_owner="misterick1", repo_name="amrita"):
        self.repo_owner = repo_owner
        self.repo_name = repo_name
        # Используем встроенный токен GitHub Actions или твой локальный персональный токен
        self.token = os.getenv("GITHUB_TOKEN")
        self.base_url = f"https://github.com{repo_owner}/{repo_name}/actions/runs"

    def _send_request(self, url, method="GET"):
        if not self.token:
            logger.error("❌ [REPAIRMAN] Критическая ошибка: Переменная GITHUB_TOKEN не найдена в окружении!")
            return None
        
        req = urllib.request.Request(url, method=method)
        req.add_header("Authorization", f"Bearer {self.token}")
        req.add_header("Accept", "application/vnd.github+json")
        req.add_header("User-Agent", "AMRITA-OS-Repairman")
        
        try:
            with urllib.request.urlopen(req, timeout=10) as response:
                if method == "GET":
                    return json.loads(response.read().decode())
                return response.status
        except Exception as e:
            logger.warning(f"⚠️ Ошибка запроса к {url}: {e}")
            return None

    def cancel_stuck_workflows(self):
        """ Находит все зависшие сборки в очереди и принудительно их отменяет """
        logger.info("🌌 [AMRITA OS] Запуск программы-ремонтника... Сканирование заторов полей...")
        
        # Запрашиваем только те сборки, которые стоят в очереди
        url = f"{self.base_url}?status=queued"
        data = self._send_request(url)
        
        if not data or "workflow_runs" not in data:
            logger.info("🔱 Зависших сборок в очереди не обнаружено. Поле чисто.")
            return

        stuck_runs = data["workflow_runs"]
        logger.info(f"📡 Обнаружено {len(stuck_runs)} потенциально зависших воркфлоу.")

        for run in stuck_runs:
            run_id = run["id"]
            run_number = run["run_number"]
            display_name = run.get("name", "Unknown Workflow")
            
            logger.info(f"💥 Схлопывание заклинившей волны #{run_number} (ID: {run_id}) [{display_name}]...")
            
            # Шлем команду отмены для конкретной сборки
            cancel_url = f"{self.base_url}/{run_id}/cancel"
            status = self._send_request(cancel_url, method="POST")
            
            if status in:
                logger.info(f"✅ Сборка #{run_number} успешно аннигилирована из очереди!")
            else:
                logger.warning(f"❌ Не удалось отменить сборку #{run_number}.")

if __name__ == "__main__":
    # Запуск программы ремонта
    repairman = GitHubWorkflowRepairman()
    repairman.cancel_stuck_workflows()
