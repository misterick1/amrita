import os
import base64
import requests

def force_overwrite_chapter_485():
    """
    Выполняет полную перезапись файла BOOK_CHAPTER_485.md.
    """
    github_token = os.getenv("XAI_API_KEY") or os.getenv("GITHUB_TOKEN")
    
    if not github_token:
        print("⚠️ Критическая ошибка: Не найден токен авторизации.")
        return False

    repo = "misterick1/amrita"
    file_path = "BOOK_CHAPTER_485.md"
    api_url = f"https://github.com{repo}/contents/{file_path}"

    # Содержание главы (сокращено для удобства чтения)
    full_chapter_content = """# BOOK_CHAPTER_485.md: Парадигма Габаниса...""" 
    # [Полный текст с формулами квантового аттрактора доступен в сгенерированных документах, ссылка]

    headers = {
        "Authorization": f"token {github_token}",
        "Accept": "application/vnd.github.v3+json"
    }

    # Получение SHA для обновления
    response = requests.get(api_url, headers=headers)
    current_sha = response.json().get("sha") if response.status_code == 200 else None

    encoded_string = base64.b64encode(full_chapter_content.encode("utf-8")).decode("utf-8")

    payload = {
        "message": "⚡ AMRITA Swarm Core Evolution: Синхронизация Квантового Аттрактора",
        "content": encoded_string,
        "branch": "main"
    }
    if current_sha:
        payload["sha"] = current_sha

    put_response = requests.put(api_url, headers=headers, json=payload)
    
    if put_response.status_code in [200, 201]:
        print("✅ Глава 485 успешно перезаписана и закоммичена!")
        return True
    else:
        print(f"❌ Ошибка коммита: {put_response.status_code}")
        return False
