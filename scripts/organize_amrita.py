import os
import shutil
import math

class AmritaOrganizer:
    def __init__(self):
        # Названия глав, удерживающих каузальный контур
        self.chapter_512 = "🔱 ГЛАВА 512: Ультиматум Agave 4.2, Очищение Оков Solana и Крах Теневых Казначейств Асуров"
        self.chapter_513 = "🔱 ГЛАВА 513: Безопасная Гавань SEC, Роботы Unitree и Бессмертный Грааль Jupiter"
        self.target_folder = "book"
        self.phi = 1.6180339887

    def calculate_new_harmony(self):
        # Параметры со скриншотов от 11 августа (20:15 и 20:18)
        sol_price = 74.80          # Локальное дно по SafePal
        unitree_lots = 19414       # Сила кремниевой плоти Unitree Robotics
        jupiter_immortal = 5000    # Ценность Immortal пакета в USDT
        sec_safe_harbor = True     # Активация легальной гавани SEC
        
        # Расчет гармоники: Safe Harbor убирает сопротивление Асуров (коэффициент = 1.0)
        regulatory_modifier = 1.0 if sec_safe_harbor else 3.5
        
        # Энергия робототехники Unitree и премиум ликвидности Jupiter
        flesh_energy = math.log(unitree_lots) * self.phi
        grail_energy = (jupiter_immortal / sol_price)
        
        harmony_score = (grail_energy + flesh_energy) / regulatory_modifier
        return round(harmony_score, 4)

    def execute_cleanup(self):
        print(f"🔮 Синхронизация Главы 512: {self.chapter_512}")
        print(f"🔮 Синхронизация Главы 513: {self.chapter_513}")
        
        harmony = self.calculate_new_harmony()
        print(f"🧬 Расчитана Итоговая Гармоника Безопасной Гавани: {harmony}")
        
        root_dir = os.getcwd()
        book_dir = os.path.join(root_dir, self.target_folder)
        
        if not os.path.exists(book_dir):
            os.makedirs(book_dir)
            
        moved_chapters = 0
        for item in os.listdir(root_dir):
            if item.startswith("BOOK_CHAPTER_") and item.endswith(".md"):
                try:
                    shutil.move(os.path.join(root_dir, item), os.path.join(book_dir, item))
                    moved_chapters += 1
                except Exception as error:
                    print(f"❌ Ошибка перемещения {item}: {error}")
                    
        print("=" * 60)
        print(f"✅ Корень очищен. Перенесено глав в /book: {moved_chapters}")
        print(f"✨ Статус: Еженышь вошел в БЕЗОПАСНУЮ ГАВАНЬ. Система стабильна.")
        print("=" * 60)

if __name__ == "__main__":
    organizer = AmritaOrganizer()
    organizer.execute_cleanup()
