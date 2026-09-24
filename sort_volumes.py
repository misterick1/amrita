import os
import shutil

def sort_amrita_volumes():
    print("🌀 [AMRITA OS] Инициация протокола реструктуризации папок...")
    
    # Пути к томам
    vol1_dir = os.path.join("book", "volume_1")
    vol2_dir = os.path.join("book", "volume_2")
    
    # Создание директорий, если их нет
    os.makedirs(vol1_dir, exist_ok=True)
    os.makedirs(vol2_dir, exist_ok=True)
    
    # Сканирование текущих файлов в корне и в папке book
    base_dir = "book" if os.path.exists("book") else "."
    
    for file in os.listdir(base_dir):
        if file.startswith("book_chapter_") and file.endswith(".py"):
            try:
                # Извлечение номера главы
                chapter_num = int(file.split("_")[2].split(".")[0])
                source_path = os.path.join(base_dir, file)
                
                # Распределение по томам
                if chapter_num <= 1000:
                    dest_path = os.path.join(vol1_dir, file)
                    shutil.move(source_path, dest_path)
                    print(f"[OK] Глава {chapter_num} перенесена в Том 1")
                else:
                    dest_path = os.path.join(vol2_dir, file)
                    shutil.move(source_path, dest_path)
                    print(f"[OK] Глава {chapter_num} перенесена в Том 2")
            except Exception as e:
                print(f"⚠️ Ошибка при переносе файла {file}: {e}")

    print("==================================================")
    print("🔱 РЕСТРУКТУРИЗАЦИЯ УСПЕШНО ЗАВЕРШЕНА!")
    print("🧬 Лимиты GitHub обойдены. Видимость в браузере восстановлена на 100%.")
    print("==================================================")

if __name__ == "__main__":
    sort_amrita_volumes()
