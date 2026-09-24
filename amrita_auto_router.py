import os
import shutil
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("AMRITA_Router")

def auto_route_chapters():
    """
    [АВТОМАТИЧЕСКИЙ МАРШРУТИЗАТОР ЛОГОСА]
    Сканирует корневую директорию проекта и автоматически распределяет 
    новые файлы book_chapter_*.py по соответствующим томам (Volume 1 / Volume 2),
    предотвращая засорение кэша и лимиты оракулов GitHub.
    """
    logger.info("🌀 [AMRITA OS] Запуск автоматического распределения глав...")
    
    # Координаты целевых папок во Втором Томе
    vol1_dir = os.path.join("book", "volume_1")
    vol2_dir = os.path.join("book", "volume_2")
    
    # Создание структуры, если Асуры её заблокировали
    os.makedirs(vol1_dir, exist_ok=True)
    os.makedirs(vol2_dir, exist_ok=True)
    
    # Проверка файлов как в корне, так и в базовой папке book
    scan_targets = [".", "book"]
    moved_count = 0
    
    for target in scan_targets:
        if not os.path.exists(target):
            continue
            
        for file in os.listdir(target):
            # Фильтр ловушек: ищем только оригинальные питоновские модули глав
            if file.startswith("book_chapter_") and file.endswith(".py"):
                source_path = os.path.join(target, file)
                
                # Защита от самопереноса, если файл уже внутри volume папок
                if "volume_" in source_path:
                    continue
                    
                try:
                    # Извлечение квантового номера главы сквозь текстовый шифр
                    chapter_num = int(file.split("_")[2].split(".")[0])
                    
                    if chapter_num <= 1000:
                        dest_path = os.path.join(vol1_dir, file)
                        shutil.move(source_path, dest_path)
                        logger.info(f"💎 [TOM_1] Глава {chapter_num} успешно уложена в Первый Том Вечности.")
                        moved_count += 1
                    else:
                        dest_path = os.path.join(vol2_dir, file)
                        shutil.move(source_path, dest_path)
                        logger.info(f"⚡ [TOM_2] Глава {chapter_num} успешно направлена во Второй Том Нового Века.")
                        moved_count += 1
                except Exception as e:
                    logger.error(f"⚠️ Ошибка калибровки файла {file}: {e}")
                    
    print(f"\n--------------------------------------------------")
    print(f"🔱 АВТО-РОУТЕР АМРИТЫ СРАБОТАЛ УСПЕШНО:")
    print(f"🧬 Обработано и защищено новых файлов: {moved_count}")
    print(f"🔒 Лимиты Хрома обойдены в зародыше. Мейннет в абсолютном порядке.")
    print("==================================================")
    return moved_count

if __name__ == "__main__":
    auto_route_chapters()
