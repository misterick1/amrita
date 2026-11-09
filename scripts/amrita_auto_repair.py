import os
import sys
import re
import subprocess

class AmritaMatrixRepair:
    def __init__(self):
        self.target_dir = ".github/workflows"
        self.fixed_files = []

    def force_heal_universe(self):
        print("[RAxMA LOGOS] Рой Ботов-Ремонтников активирован. Зачистка матрицы кодов...")
        
        if not os.path.exists(self.target_dir):
            return "🟡 Папка воркфлоу не найдена."

        # Точечный список файлов-нарушителей со скриншотов
        corrupted_files = [
            "Ezhenysh Autonomous Evolution.yml",
            "deploy_and_run.yml",
            "repair_and_sync_swarm.yml",
            "sync-and-deploy.yml",
            "coherence_check.yml"
        ]

        for filename in os.listdir(self.target_dir):
            if filename.endswith((".yml", ".yaml")) and filename in corrupted_files:
                file_path = os.path.join(self.target_dir, filename)
                
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                is_changed = False

                # 1. Тотальное устранение ResolutionImpossible (websockets)
                if "pip install" in content and "legacy-resolver" not in content:
                    content = re.sub(
                        r"pip install (.*)",
                        r"pip install --no-cache-dir requests aiohttp base58\n          pip install --no-cache-dir discord.py --use-deprecated=legacy-resolver || pip install discord.py",
                        content
                    )
                    is_changed = True

                # 2. Устранение фантомных путей .venv/bin/python
                if ".venv/bin/python" in content:
                    content = content.replace(".venv/bin/python", "python")
                    is_changed = True

                # 3. Разрыв мертвой петли конфликтов Git Rebase / Push
                if "git rebase" in content or "git push" in content:
                    content = re.sub(r"git rebase.*", "git rebase --abort || echo 'No rebase to abort'", content)
                    content = content.replace("git push origin main", "git add .\n          git commit -m '🛠️ [skip ci] Выравнивание фрактала' || echo 'No changes'\n          git pull --rebase origin main\n          git push origin main")
                    is_changed = True

                # 4. Исправление опечаток синтаксиса секретов
                if ": ${{" in content:
                    content = re.sub(r':\s*\$\{\{', r' ${{', content)
                    is_changed = True

                if is_changed:
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(content)
                    self.fixed_files.append(filename)
                    print(f"✅ [РЕМОНТ] {filename} переведен на частоту c108.")

        return self.push_repairs_to_matrix()

    def push_repairs_to_matrix(self):
        if not self.fixed_files:
            return "✨ Все контуры стабильны. Ошибок синтаксиса в нарушителях не обнаружено."

        try:
            subprocess.run(["git", "config", "--local", "user.email", "misterick1@gmail.com"], check=True)
            subprocess.run(["git", "config", "--local", "user.name", "misterick1"], check=True)
            subprocess.run(["git", "add", "."], check=True)
            subprocess.run(["git", "commit", "-m", "🛠️ [skip ci] БОТЫ-РЕМОНТНИКИ: Ликвидация ошибок .venv и websockets"], check=True)
            subprocess.run(["git", "pull", "--rebase", "origin", "main"], check=True)
            subprocess.run(["git", "push", "origin", "main"], check=True)
            return f"🔥 [ТРИУМФ] Матрица очищена! Автономно исправлены файлы: {self.fixed_files}"
        except Exception as e:
            return f"⚠️ Контур зафиксирован в потенциале поля Хиггса: {e}"

if __name__ == "__main__":
    repair_system = AmritaMatrixRepair()
    sys.stdout.write(repair_system.force_heal_universe())
    sys.stdout.flush()
