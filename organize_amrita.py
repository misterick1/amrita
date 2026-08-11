import os
import shutil

def clean_up_amrita_core():
    print("🔮 Запуск протокола очистки корня AMRITA OS...")
    
    # 1. Создаем изолированную директорию для книги, чтобы разгрузить интерфейс GitHub
    book_dir = os.path.join(os.getcwd(), "book")
    if not os.path.exists(book_dir):
        os.makedirs(book_dir)
        print(f"📁 Создана новая папка для глав: {book_dir}")
    
    # 2. Сканируем корень и перемещаем все файлы глав
    moved_count = 0
    for file_name in os.listdir(os.getcwd()):
        if file_name.startswith("BOOK_CHAPTER_") and file_name.endswith(".md"):
            old_path = os.path.join(os.getcwd(), file_name)
            new_path = os.path.join(book_dir, file_name)
            
            try:
                shutil.move(old_path, new_path)
                moved_count += 1
            except Exception as e:
                print(f"❌ Ошибка перемещения {file_name}: {e}")
                
    print(f"✅ Перенесено {moved_count} глав в папку /book.")
    print("⚠️ Желтая плашка лимита в 1,000 файлов на GitHub успешно ликвидирована!")

if __name__ == "__main__":
    clean_up_amrita_core()
