import subprocess
import os
import sys

def get_git_changes():
    try:
        # Получаем статистику изменений между текущим коммитом и предыдущим
        stats = subprocess.check_output(["git", "diff", "HEAD~1", "HEAD", "--shortstat"], stderr=subprocess.STDOUT).decode("utf-8")
        print(f"Статистика коммита: {stats.strip()}")
        
        insertions = 0
        parts = stats.split(",")
        for part in parts:
            if "insertion" in part:
                # Извлекаем только цифры из подстроки с добавлениями
                insertions = int(''.join(filter(str.isdigit, part)))
        return insertions
    except Exception as e:
        print(f"Предупреждение при чтении git diff: {e}. Используем базовый объем.")
        return 15 # Дефолтное среднее значение строк, если предыдущий коммит недоступен

def calculate_score(lines):
    # Логика градации сложности архитектуры проекта роем
    if lines < 10:
        return 1  # Быстрый багфикс / правка конфига
    elif lines < 50:
        return 2  # Локальное обновление функций / новая команда бота
    elif lines < 150:
        return 3  # Средний рефакторинг ядра медиа-системы
    elif lines < 500:
        return 4  # Архитектурный апдейт движка / новый крупный модуль
    else:
        return 5  # Масштабный деплой / глобальный релиз квантового ядра

if __name__ == "__main__":
    print("🤖 Рой Fractal Lego Builder оценивает интеллектуальный вклад...")
    changed_lines = get_git_changes()
    complexity_score = calculate_score(changed_lines)
    print(f"✅ Оценка сложности утверждена роем: {complexity_score} из 5")
    
    # Сохраняем результат в правильную папку с большой буквы Github
    os.makedirs("Github/scripts", exist_ok=True)
    with open("Github/scripts/score.txt", "w") as f:
        f.write(str(complexity_score))
