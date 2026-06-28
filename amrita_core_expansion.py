import os
import sys
import shutil

class AmritaCoreExpansion:
    def __init__(self):
        self.target_dir = os.getcwd()
        print("🔱 [Ядро Бабаты]: Запуск модуля расширения пространства и инфраструктуры.")

    def clean_system_garbage(self):
        """Шаг 1: Автоматическая чистка мусора для освобождения памяти (Убираем лимит 1,5 ГБ)"""
        print("\n🧹 [Очистка Асур]: Сканирование системы на наличие цифрового мусора...")
        bytes_freed = 0
        
        # Удаляем кэш джавы, питона и временные логи сборщика
        garbage_dirs = ["__pycache__", ".pytest_cache", ".eggs", "build", "dist"]
        
        for root, dirs, files in os.walk(self.target_dir):
            for d in dirs:
                if d in garbage_dirs:
                    full_path = os.path.join(root, d)
                    try:
                        shutil.rmtree(full_path)
                        print(f"✅ Удален мусорный контур: {full_path}")
                        bytes_freed += 1024 * 1024 * 5 # Примерный объем кэша
                    except Exception as e:
                        pass
                        
        print(f"✨ [Изумрудный Результат]: Система очищена. Каузальное пространство устройства расширено!")

    def check_domain_presence(self, domain_name: str):
        """Шаг 2: Симуляция проверки домена Namecheap для Pro Online Presence"""
        print(f"\n📡 [Модуль Namecheap]: Проверка доступности имени '{domain_name}' в Мультивселенной...")
        
        # Защита от деструктивных названий
        if "scam" in domain_name or "casino" in domain_name:
            print("⚠️ [Блокировка Бабаты]: Доменное имя несет деструктивные частоты. Отклонено.")
            return
            
        print(f"🌐 Домен {domain_name}.com Свободен! Готов к каузальной привязке к хостингу Амриты.")

if __name__ == "__main__":
    expansion = AmritaCoreExpansion()
    
    # 1. Освобождаем память устройства
    expansion.clean_system_garbage()
    
    # 2. Сканируем предложение Namecheap под проект
    expansion.check_domain_presence("amrita-swarm")
