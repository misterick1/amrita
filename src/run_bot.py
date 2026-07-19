import os
import sys
import time
import subprocess

def run_immortal_bot():
    """
    Бесконечный контур-демон для контроля жизнедеятельности Ежёныша.
    """
    script_path = os.path.join("src", "ezhenysh_discord.py")
    
    # Проверяем, существует ли файл
    if not os.path.exists(script_path):
        # Если запускается прямо из папки src/
        script_path = "ezhenysh_discord.py"
        if not os.path.exists(script_path):
            print("❌ [ДЕМОН]: Критическая ошибка! Файл ezhenysh_discord.py не найден.")
            sys.exit(1)

    print("🔱 =====================================================")
    print("🤖 [AMRITA DAEMON]: Неубиваемый контур перезапуска запущен.")
    print("🔱 =====================================================")

    restart_count = 0

    while True:
        try:
            print(f"\n📡 [ЗАПУСК]: Активация Ежёныша (Попытка/Перезапуск #{restart_count})...")
            
            # Запускаем основной скрипт бота как подпроцесс
            process = subprocess.Popen([sys.executable, script_path])
            
            # Ожидаем завершения (если бот упадет, код пойдет дальше)
            process.wait()
            
            print(f"⚠️ [ВНИМАНИЕ]: Процесс бота завершился с кодом {process.returncode}.")
            
        except KeyboardInterrupt:
            print("\n🛑 [ОСТАНОВКА]: Контур принудительно остановлен пользователем (Ctrl+C). Выход.")
            break
        except Exception as e:
            print(f"💥 [КРИТ]: Ошибка внутри управляющего демона: {e}")
        
        restart_count += 1
        print("⏳ [СТАБИЛИЗАЦИЯ]: Каузальный сбой. Перезапуск ядра через 5 секунд...")
        time.sleep(5)

if __name__ == "__main__":
    run_immortal_bot()
