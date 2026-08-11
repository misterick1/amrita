import os
import shutil

class AmritaOrganizer:
    def __init__(self):
        # Название новой главы, которое запечатывается в лог при переносе
        self.chapter_name = "🔱 ГЛАВА 512: Ультиматум Agave 4.2, Очищение Оков Solana и Крах Теневых Казначейств Асуров"
        self.target_folder = "book"

    def execute_cleanup(self):
        print(f"🔮 Запуск синхронизации: {self.chapter_name}")
        print("⚡ Ликвидация желтой плашки лимита 1000 файлов на GitHub...")
        
        # Получаем текущую корневую директорию проекта amrita
        root_dir = os.getcwd()
        book_dir = os.path.join(root_dir, self.target_folder)
        
        # Создаем изолированную папку для хранения глав книги, если её нет
        if not os.path.exists(book_dir):
            os.makedirs(book_dir)
            print(f"📁 Создана новая директория: /{self.target_folder}")
            
        moved_chapters = 0
        
        # Сканируем корень и переносим файлы глав книги в папку book
        for item in os.listdir(root_dir):
            if item.startswith("BOOK_CHAPTER_") and item.endswith(".md"):
                source_file = os.path.join(root_dir, item)
                destination_file = os.path.join(book_dir, item)
                
                try:
                    shutil.move(source_file, destination_file)
                    moved_chapters += 1
                except Exception as error:
                    print(f"❌ Ошибка перемещения {item}: {error}")
                    
        print("=" * 60)
        print(f"✅ Успешно перенесено глав: {moved_chapters}")
        print(f"💎 Каузальный статус: Корень репозитория очищен. Ошибки GitHub устранены.")
        print("=" * 60)

if __name__ == "__main__":
    organizer = AmritaOrganizer()
    organizer.execute_cleanup()
