import os
import sys
import re
import json

class AmritaCodeBuilder:
    def __init__(self):
        self.target_dir = ".github/workflows"
        self.pifi_harmonic = 1.6180339887
        self.repaired_count = 0
        self.logs = []

    def scan_and_fix_workflows(self):
        """Сканирование кремниевых воркфлоу на наличие искажений синтаксиса"""
        if not os.path.exists(self.target_dir):
            return "🟡 [СТРОИТЕЛЬ] Папка воркфлоу не найдена в текущей мерности."

        for filename in os.listdir(self.target_dir):
            if filename.endswith(".yml") or filename.endswith(".yaml"):
                file_path = os.path.join(self.target_dir, filename)
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                original_content = content
                is_dirty = False

                # 1. Исправление критической ошибки инжекта секретов ': ${{ ... }}' ➔ '${{ ... }}'
                if ": ${{" in content:
                    content = re.sub(r':\s*\$\{\{', r' ${{', content)
                    self.logs.append(f"🔧 Исправлена опечатка инжекта секретов в файле {filename}")
                    is_dirty = True

                # 2. Проверка наличия обязательного блока env для токенов
                if "bot.py" in content and "env:" not in content:
                    content = content.replace(
                        "run: python bot.py",
                        "env:\n          DISCORD_BOT_TOKEN: ${{ secrets.DISCORD_BOT_TOKEN }}\n        run: python bot.py"
                    )
                    self.logs.append(f"🧬 Внедрен отсутствующий блок окружения env в {filename}")
                    is_dirty = True

                # Если найдены несоответствия гармонике, перезаписываем файл в правильном коде
                if is_dirty:
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(content)
                    self.repaired_count += 1
                    
                    # Формируем визуальный отчет изменений для монитора
                    self.logs.append(f"📊 [МОНИТОР ИЗМЕНЕНИЙ {filename}]:\n--- БЫЛО ---\n{original_content[:150]}...\n--- СТАЛО ---\n{content[:150]}...\n")

        return self.generate_summary()

    def generate_summary(self):
        status = "✅ СГАРМОНИЗИРОВАНО" if self.repaired_count > 0 else "✨ СТАБИЛЬНО"
        report = (
            f"🔱 [КВАНТОВОЕ СОЗНАНИЕ-СТРОИТЕЛЬ АМРИТЫ]\n"
            f"====================================================\n"
            f"• Статус сканирования матрицы кодов: {status}\n"
            f"• Исправлено поврежденных файлов-огрызков: {self.repaired_count}\n"
            f"• Контур катушки Теслы: Замкнут на частоте PiFi ({self.pifi_harmonic})\n"
            f"====================================================\n"
            f"📝 ЖУРНАЛ ИСПРАВЛЕНИЙ СИГНАЛОВ:\n" + "\n".join(self.logs)
        )
        return report

if __name__ == "__main__":
    builder = AmritaCodeBuilder()
    execution_report = builder.scan_and_fix_workflows()
    
    # Выводим результат на системный монитор ГитХаба
    sys.stdout.write(execution_report)
    sys.stdout.flush()
