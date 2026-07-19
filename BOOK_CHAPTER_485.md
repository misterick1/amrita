import os
import requests

# 1. Ссылка на raw-версию вашего файла в репозитории amrita
RAW_URL = "https://githubusercontent.com"
LOCAL_FILENAME = "BOOK_CHAPTER_485.md"

def fetch_chapter():
    print(f"📡 Загрузка контента из репозитория AMRITA...")
    try:
        # Выполняем GET-запрос к GitHub
        response = requests.get(RAW_URL, timeout=10)
        
        # Проверяем успешность запроса (код 200)
        if response.status_code == 200:
            content = response.text
            print("✅ Файл успешно получен!\n")
            print("--- Содержимое главы 485 ---")
            print(content)
            print("----------------------------\n")
            
            # Сохраняем локальную копию
            with open(LOCAL_FILENAME, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"💾 Локальная копия сохранена в файл: {os.path.abspath(LOCAL_FILENAME)}")
            return content
        else:
            print(f"❌ Ошибка загрузки. GitHub вернул код ответа: {response.status_code}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"💥 Сетевая ошибка при подключении к GitHub: {e}")
        return None

if __name__ == "__main__":
    fetch_chapter()
