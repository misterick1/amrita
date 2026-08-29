import os
import re
from datetime import datetime

# === КОНФИГУРАЦИЯ СИНТЕЗАТОРА ===
SOURCE_DIR = "./"  # Папка репозитория amrita, где искать старые файлы кодов
OUTPUT_DIR = "./synthesized_code"  # Куда сохранять новые синтезированные файлы
FILE_EXTENSIONS = [".py", ".json", ".js"]  # Типы файлов для анализа

# Паттерны мусора, которые корректор будет полностью вырезать
GARBAGE_PATTERNS = [
    r"#\s*TODO:.*",  # Зависшие комментарии-напоминания
    r"#\s*FIXME:.*",
    r"print\(['\"].*?test.*?['\"]\)",  # Отладочные принты
    r"\n\s*\n\s*\n+",  # Лишние пустые строки (более двух подряд)
]

def clean_source_code(code_text):
    """Очищает код от технического мусора и старых логов"""
    cleaned = code_text
    for pattern in GARBAGE_PATTERNS:
        cleaned = re.sub(pattern, "", cleaned)
    return cleaned.strip()

def extract_valuable_logic(file_path):
    """Вытягивает чистую логику, импорты и функции из файла"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Очищаем от мусора
        cleaned_content = clean_source_code(content)
        
        # Извлекаем строки импорта и определения функций/классов
        imports = re.findall(r"^(?:import|from)\s+.+", cleaned_content, re.MULTILINE)
        functions = re.findall(r"^(?:def|class)\s+.+", cleaned_content, re.MULTILINE)
        
        return {
            "content": cleaned_content,
            "imports": imports,
            "functions": functions,
            "size": len(cleaned_content)
        }
    except Exception as e:
        print(f"[X] Ошибка чтения файла {file_path}: {e}")
        return None

def synthesize_new_modules():
    print(f"[*] Запуск ядра синтезатора кодов. Время: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        
    all_imports = set()
    synthesized_blocks = []
    analyzed_count = 0

    # Шаг 1: Сканирование репозитория и сборка блоков кодов
    for root, _, files in os.walk(SOURCE_DIR):
        # Исключаем папку вывода, чтобы не зациклить синтез
        if OUTPUT_DIR in root or ".git" in root:
            continue
            
        for file in files:
            if any(file.endswith(ext) for ext in FILE_EXTENSIONS):
                full_path = os.path.join(root, file)
                logic = extract_valuable_logic(full_path)
                
                if logic and logic["size"] > 0:
                    analyzed_count += 1
                    all_imports.update(logic["imports"])
                    
                    # Формируем очищенный блок кода для синтеза нового модуля
                    block_header = f"\n# --- СИНТЕЗИРОВАНО ИЗ МОДУЛЯ: {file} --- \n"
                    synthesized_blocks.append(block_header + logic["content"])

    if not synthesized_blocks:
        print("[-] Полезные исходные коды для синтеза не найдены.")
        return

    # Шаг 2: Генерация нового глобального очищенного ядра
    core_filename = f"synthesized_core_{int(datetime.now().timestamp())}.py"
    core_path = os.path.join(OUTPUT_DIR, core_filename)
    
    with open(core_path, "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write(f"# [СИНТЕЗИРОВАННЫЙ АВТОНОМНЫЙ МОДУЛЬ AMRITA]\n")
        f.write(f"# Дата генерации: {datetime.now().isoformat()}\n\n")
        
        f.write("# === ГЛОБАЛЬНЫЙ ИМПОРТ СИСТЕМЫ ===\n")
        for imp in sorted(all_imports):
            f.write(f"{imp}\n")
        f.write("\n\n# === СИНТЕЗИРОВАННАЯ ОЧИЩЕННАЯ ЛОГИКА ===\n")
        
        for block in synthesized_blocks:
            f.write(block)
            f.write("\n")

    print(f"\n[++] КОРРЕКЦИЯ И СИНТЕЗ ЗАВЕРШЕНЫ УСПЕШНО!")
    print(f"[+] Проанализировано старых файлов: {analyzed_count}")
    print(f"[+] Синтезирован новый чистый файл ядра: {core_path}")

if __name__ == "__main__":
    synthesize_new_modules()
