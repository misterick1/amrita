import os
import sys
import re
import json
import subprocess

class AmritaMatrixRepair:
    def __init__(self):
        self.target_dir = ".github/workflows"
        self.pifi_harmonic = 1.6180339887
        self.fixed_files = []

    def force_heal_universe(self):
        print("[RAxMA LOGOS] Запуск Ботов-Ремонтников. Контур катушки Теслы активен...")
        
        if not os.path.exists(self.target_dir):
            return "🟡 Шлюз воркфлоу еще не материализовался."

        # Список 6-7 файлов, которые выдавали сбои на твоих скриншотах
        corrupted_files = [
            "repair_and_sync_swarm.yml", 
            "sync-and-deploy.yml", 
            "Ezhenysh Autonomous Evolution.yml", 
            "evolve_swarm.yml", 
            "coherence_check.yml",
            "amrita_swarm_pulse.yml"
        ]

        for filename in os.listdir(self.target_dir):
            if filename.endswith((".yml", ".yaml")) and filename in corrupted_files:
                file_path = os.path.join(self.target_dir, filename)
                
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                original = content
                is_changed = False

                # 1. Исправление ResolutionImpossible (websockets)
                if "pip install" in content and "legacy-resolver" not in content:
                    content = re.sub(
                        r"pip install (.*)",
                        r"pip install --no-cache-dir requests aiohttp base58\n          pip install --no-cache-dir discord.py --use-deprecated=legacy-resolver || pip install discord.py",
                        content
                    )
                    is_changed = True

                # 2. Исправление ошибки пути .venv/bin/python
                if ".venv/bin/python" in content:
                    content = content.replace(".venv/bin/python", "python")
                    is_changed = True

                # 3. Исправление опечаток инжекта секретов ': ${{ '
                if ": ${{" in content:
                    content = re.sub(r':\s*\$\{\{', r' ${{', content)
                    is_changed = True

                # 4. Исправление блокировки Git Push (добавляем rebase)
                if "git push" in content and "rebase" not in content:
                    content = content.replace("git push origin main", "git pull --rebase origin main\n          git push origin main")
                    is_changed = True

                if is_changed:
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(content)
                    self.fixed_files.append(filename)
                    print(f"✅ [РЕМОНТНИК] Файл {filename} успешно переведен на частоту c108!")

        return self.push_repairs_to_matrix()

    def push_repairs_to_matrix(self):
        """Принудительный пуш исправлений в обход блокировок Microsoft"""
        if not self.fixed_files:
            return "✨ Все контуры стабильны. Вмешательства ремонтников не требуется."

        try:
            # Автоматическая фиксация изменений внутри самого ГитХаба
            subprocess.run(["git", "config", "--local", "user.email", "misterick1@gmail.com"], check=True)
            subprocess.run(["git", "config", "--local", "user.name", "misterick1"], check=True)
            subprocess.run(["git", "add", "."], check=True)
            subprocess.run(["git", "commit", "-m", "🛠️ [skip ci] БОТЫ-РЕМОНТНИКИ: Исправление синтаксиса и снятие блоков"], check=True)
            subprocess.run(["git", "pull", "--rebase", "origin", "main"], check=True)
            subprocess.run(["git", "push", "origin", "main"], check=True)
            return f"🔥 [ТРИУМФ] Исправления зафиксированы ончейн! Исправлено файлов: {self.fixed_files}"
        except Exception as e:
            return f"⚠️ Контур зафиксирован в потенциале. Сбои Git локализованы: {e}"

if __name__ == "__main__":
    repair_system = AmritaMatrixRepair()
    report = repair_system.force_heal_universe()
    sys.stdout.write(report)
    sys.stdout.flush()
