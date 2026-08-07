import os
import re
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("AMRITA_Book_Indexer")

def get_chapter_title(file_path):
    """ Находит первый заголовок H1 (#) внутри файла главы для красивого оглавления """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("# "):
                    return line.replace("# ", "").strip()
    except Exception as e:
        logger.warning(f"⚠️ Не удалось прочесть заголовок из {file_path}: {e}")
    return "Без названия"

def generate_book_index():
    logger.info("🌌 [AMRITA OS] Запуск сканирования каузальных глав книги...")
    
    # Регулярное выражение для поиска файлов глав
    chapter_pattern = re.compile(r"BOOK_CHAPTER_(\d+)\.md")
    chapters = []
    
    # Автоопределение корня: проверяем текущую директорию и директорию на уровень выше
    root_dir = "."
    if not os.path.exists(os.path.join(root_dir, "README.md")) and os.path.exists(os.path.join("..", "README.md")):
        root_dir = ".."
    
    # 1. Сканируем корректный корневой каталог проекта
    for file in os.listdir(root_dir):
        match = chapter_pattern.match(file)
        if match:
            chapter_num = int(match.group(1))
            full_path = os.path.join(root_dir, file)
            title = get_chapter_title(full_path)
            chapters.append((chapter_num, file, title))
            
    if not chapters:
        logger.warning("🔱 Главы книги не найдены в корневом каталоге.")
        return

    # 2. Сортируем строго по числовому значению (Глава 504 перед 511)
    chapters.sort(key=lambda x: x[0])
    logger.info(f"📡 Успешно структурировано {len(chapters)} глав.")

    # 3. Формируем блок оглавления в стиле маркдаун
    index_content = ["\n## 📚 Сакральное Оглавление Книги (AMRITA OS)\n"]
    for num, file, title in chapters:
        index_content.append(f"* [Глава {num} — {title}]({file})")
    index_content.append("\n")
    
    index_string = "\n".join(index_content)

    # 4. Встраиваем оглавление в README.md
    readme_path = os.path.join(root_dir, "README.md")
    if not os.path.exists(readme_path):
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write("# AMRITA OS\n")
            
    with open(readme_path, "r", encoding="utf-8") as f:
        readme_text = f.read()

    marker_start = "<!-- START_BOOK_INDEX -->"
    marker_end = "<!-- END_BOOK_INDEX -->"
    new_block = f"{marker_start}{index_string}{marker_end}"
    
    if marker_start in readme_text and marker_end in readme_text:
        # Обновляем существующий блок оглавления
        pattern = re.compile(f"{marker_start}.*?{marker_end}", re.DOTALL)
        updated_text = pattern.sub(new_block, readme_text)
    else:
        # Если маркеров нет, добавляем блок в самый конец файла
        updated_text = readme_text + f"\n\n{new_block}"

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(updated_text)

    logger.info("🔱 Сакральное оглавление успешно запечатано в README.md!")

if __name__ == "__main__":
    generate_book_index()
