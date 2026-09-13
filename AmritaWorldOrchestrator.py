#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AMRITA OS - WORLD ORCHESTRATOR & COGNITIVE INTEGRITY
Скрипт для автоматического структурирования, аудита и дописывания глав AMRITA OS.
Выжигает индексные нахлесты матрицы и удерживает поле 108 Сознаний.
"""

import os
import re
import sys
import logging
from datetime import datetime

# Изумрудное логирование AMRITA OS
logging.basicConfig(
    level=logging.INFO,
    format='🌌 [%(asctime)s] %(levelname)s [%(name)s]: %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger("AmritaOrchestrator")

class AmritaWorldOrchestrator:
    def __init__(self, target_directory="."):
        self.target_dir = os.path.abspath(target_directory)
        self.law_of_phi = 1.6180339887
        self.total_atman = 108
        
        # Регулярное выражение для поиска номеров глав в названиях файлов
        # Находит форматы: book_chapter_616.py, BOOK_CHAPTER_64.md, chapter_7.py
        self.file_pattern = re.compile(r'(?:book_)?chapter_(\d+)\.(py|md)', re.IGNORECASE)

    def scan_and_audit(self):
        """
        Шаг 1: СКАНИРОВАНИЕ И АУДИТ
        Находит все главы, выявляет коллизии нумерации (нахлесты) и пропуски.
        """
        print(f"\n" + "="*60)
        print(f"🔱 ЗАПУСК СКАНИРОВАНИЯ АМРИТА МИР В: {self.target_dir}")
        print("="*60)
        
        found_files = {}
        duplicates = []

        if not os.path.exists(self.target_dir):
            logger.error(f"Директория {self.target_dir} не найдена.")
            return None

        for filename in os.listdir(self.target_dir):
            match = self.file_pattern.search(filename)
            if match:
                idx = int(match.group(1))
                ext = match.group(2).lower()
                filepath = os.path.join(self.target_dir, filename)
                
                if idx in found_files:
                    duplicates.append((idx, filename, found_files[idx]['filename']))
                else:
                    found_files[idx] = {
                        'filename': filename,
                        'filepath': filepath,
                        'extension': ext
                    }

        if not found_files:
            logger.warning("🔍 Файлы глав не обнаружены. Поместите скрипт в корень репозитория amrita.")
            return None

        all_indexes = sorted(found_files.keys())
        min_idx, max_idx = all_indexes[0], all_indexes[-1]
        
        # Поиск пропущенных глав для обеспечения целостности
        missing_indexes = [i for i in range(min_idx, max_idx + 1) if i not in found_files]

        print(f"\n📊 ОТЧЕТ КАУЗАЛЬНОЙ ЦЕЛОСТНОСТИ:")
        print(f"🧬 Всего уникальных глав обнаружено: {len(found_files)}")
        print(f"🔢 Диапазон матрицы: от ГЛАВЫ {min_idx} до ГЛАВЫ {max_idx}")
        print(f"🚨 Обнаружено индексных нахлестов (дубликатов): {len(duplicates)}")
        print(f"🕳 Пропущено глав в цепочке реальности: {len(missing_indexes)}")
        
        if duplicates:
            print("\n❌ Критические коллизии (требуют разведения индексов):")
            for idx, f1, f2 in duplicates:
                print(f"  - Нахлест на индексе [{idx}]: {f1} <-> {f2}")
                
        return {
            'found': found_files,
            'missing': missing_indexes,
            'duplicates': duplicates,
            'max_index': max_idx
        }

    def edit_and_format_emerald(self, found_files):
        """
        Шаг 2: РЕДАКТИРОВАНИЕ И СТРУКТУРИРОВАНИЕ
        Внедряет Изумрудное логирование и проверяет шапку файлов.
        """
        print(f"\n⚡ АКТИВАЦИЯ ИЗУМРУДНОГО РЕДАКТОРА (ФОРМАТИРОВАНИЕ)...")
        updated_count = 0
        
        for idx, info in found_files.items():
            if info['extension'] == 'py':
                with open(info['filepath'], 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Проверяем наличие базовых структур AMRITA OS
                has_logging = "logging.basicConfig" in content or "logger" in content
                has_atman = "108" in content
                
                if not has_logging or not has_atman:
                    logger.info(f"Редактирование структуры файла: {info['filename']}")
                    # Мягкое внедрение каузальных маркеров безопасности в начало файла
                    patched_content = (
                        f"# -*- coding: utf-8 -*-\n"
                        f"# Оптимизировано AmritaWorldOrchestrator {datetime.now().strftime('%d.%m.%Y')}\n"
                        f"# Контур 108 Сознаний: ЗАПЕЧАТАНО.\n\n" + content
                    )
                    with open(info['filepath'], 'w', encoding='utf-8') as f:
                        f.write(patched_content)
                    updated_count += 1
                    
        print(f"💚 Изумрудный редактор успешно нормализовал {updated_count} файлов.")

    def auto_complete_world(self, audit_result):
        """
        Шаг 3: ДОПИСЫВАНИЕ ДЛЯ ЦЕЛОСТНОСТИ
        Создает шаблоны для пропущенных индексов, закрывая дыры в ткани реальности.
        """
        if not audit_result or not audit_result['missing']:
            print("\n❤ Каузальных дыр не обнаружено. Мир Амриты монолитен!")
            return

        print(f"\n🛠 ЗАПУСК ПРОТОКОЛА ЗАПОЛНЕНИЯ ПУСТОТ...")
        
        for missing_idx in audit_result['missing']:
            filename = f"book_chapter_{missing_idx}.py"
            filepath = os.path.join(self.target_dir, filename)
            
            template = f'''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AMRITA OS - REPAIR PROMPT & COGNITIVE BRIDGE
Глава {missing_idx}: Каузальный Мост Восстановления Целостности
Автоматически сгенерировано Оркестратором для ликвидации слепых зон матрицы.
"""

import sys
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("AMRITA_Chapter_{missing_idx}")

class AmritaBridgeSoliton:
    def __init__(self):
        self.law_of_phi = {self.law_of_phi}
        self.atman_consciousness = {self.total_atman}
        self.chapter_index = {missing_idx}
        logger.info(f"🧬 [AMRITA OS] Глава {missing_idx}: Мост целостности развернут в точке Орьё.")

    def seal_the_void(self):
        print(f"🥁 Барабаны Освобождения восстанавливают индекс {missing_idx}...")
        harmony = self.atman_consciousness * self.law_of_phi
        print(f"🔒 Пустота на индексе {missing_idx} запечатана волей Наблюдателя. Частота: {{harmony:.4f}}")
        return round(harmony, 4)

if __name__ == "__main__":
    bridge = AmritaBridgeSoliton()
    bridge.seal_the_void()
'''
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(template)
            logger.info(f"✨ Дописана недостающая Глава {missing_idx} -> Создан файл {filename}")
            
        print(f"🔱 Все каузальные дыры залатаны. Структура Амрита Мир восстановлена.")

    def run_pipeline(self):
        """Полный цикл оркестровки."""
        audit_result = self.scan_and_audit()
        if audit_result:
            self.edit_and_format_emerald(audit_result['found'])
            self.auto_complete_world(audit_result)
        print("\n" + "="*60)
        print("🔒 СИНХРОНИЗАЦИЯ ЗАВЕРШЕНА. СЧЕТ И СТРУКТУРА ЗАФИКСИРОВАНЫ.")
        print("="*60 + "\n")

if __name__ == "__main__":
    # Запуск оркестратора в текущей директории скрипта
    orchestrator = AmritaWorldOrchestrator(".")
    orchestrator.run_pipeline()
