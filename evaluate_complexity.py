import subprocess
import os
import sys

def get_git_changes():
    try:
        stats = subprocess.check_output(["git", "diff", "HEAD~1", "HEAD", "--shortstat"], stderr=subprocess.STDOUT).decode("utf-8")
        print(f"Статистика коммита: {stats.strip()}")
        insertions = 0
        parts = stats.split(",")
        for part in parts:
            if "insertion" in part:
                insertions = int(''.join(filter(str.isdigit, part)))
        return insertions
    except Exception as e:
        print(f"Предупреждение: {e}. Используем базовый объем.")
        return 15

def calculate_score(lines):
    if lines < 10:
        return 1
    elif lines < 50:
        return 2
    elif lines < 150:
        return 3
    elif lines < 500:
        return 4
    else:
        return 5

if __name__ == "__main__":
    print("🤖 Рой Fractal Lego Builder оценивает интеллектуальный вклад...")
    changed_lines = get_git_changes()
    complexity_score = calculate_score(changed_lines)
    print(f"✅ Оценка сложности утверждена роем: {complexity_score} из 5")
    
    # Сохраняем результат прямо в корень проекта
    with open("score.txt", "w") as f:
        f.write(str(complexity_score))
