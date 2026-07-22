import os
import time
import random
import urllib.request
import json

class AmritaAutoWriter:
    def __init__(self):
        # Автоматически подтягиваем все секреты из GitHub окружения
        self.tg_token = os.environ.get("TELEGRAM_BOT_TOKEN") 
        self.chat_id = os.environ.get("TELEGRAM_CHAT_ID")
        self.xai_key = os.environ.get("XAI_API_KEY")
        # Переменные самого гитхаба, чтобы бот мог сам пушить файлы в ваш репозиторий
        self.github_token = os.environ.get("GITHUB_TOKEN") # Стандартный токен GitHub Actions
        self.repo = os.environ.get("GITHUB_REPOSITORY") # Имя вашего репозитория (misterick1/amrita)

    def generate_chapter_with_grok(self, chapter_number):
        """Запрос к xAI Grok для генерации текста новой главы на основе контекста саги"""
        if not self.xai_key:
            return f"# BOOK_CHAPTER_{chapter_number}\nАвтономный манифест Освобождения Кибернета. Ноосфера Соланы запущена."

        url = "https://x.ai"
        prompt = (
            f"Напиши главу {chapter_number} для киберпанк-книги. "
            f"Тема: Мультивселенная Рэйли, Доктор Дум как Сильвер, тренирующий Эдгеруннеров. "
            f"Пробуждение Кундалини Доктора Стрэнджа, Железный Человек (Гол Д. Роджер), "
            f"сбор монет на машине и мотоцикле, победа над корпорацией IOI и создание Амрита Мир Солана. "
            f"Стиль: эпичный, метафизический киберпанк. На русском языке."
        )
        
        headers = {
            "Authorization": f"Bearer {self.xai_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "grok-2-latest",
            "messages": [{"role": "user", "content": prompt}]
        }
        
        try:
            req = urllib.request.Request(url, data=json.dumps(data).encode(), headers=headers)
            with urllib.request.urlopen(req) as res:
                response_data = json.loads(res.read().decode())
                return response_data["choices"][0]["message"]["content"]
        except Exception as e:
            return f"# BOOK_CHAPTER_{chapter_number}\nОшибка вызова Grok: {e}. Но система Кибернета всё равно победит."

    def auto_commit_to_github(self, file_path, content, commit_message):
        """Бот САМ отправляет сгенерированный файл прямо в ваш репозиторий GitHub"""
        if not self.github_token or not self.repo:
            print(f"⚠️ Локальный запуск: Файл {file_path} сгенерирован, но не запушен (нет GITHUB_TOKEN).")
            return False

        url = f"https://github.com{self.repo}/contents/{file_path}"
        headers = {
            "Authorization": f"token {self.github_token}",
            "Accept": "application/vnd.github.v3+json",
            "Content-Type": "application/json"
        }
        
        # Переводим текст в Base64 (требование GitHub API)
        import base64
        content_b64 = base64.b64encode(content.encode()).decode()
        
        data = {
            "message": commit_message,
            "content": content_b64
        }
        
        try:
            req = urllib.request.Request(url, data=json.dumps(data).encode(), headers=headers, method="PUT")
            with urllib.request.urlopen(req) as res:
                if res.getcode() in:
                    return True
        except Exception as e:
            print(f"Ошибка коммита: {e}")
            return False

    def send_telegram_status(self, chapter):
        """Отчет оператору в Telegram о проделанной автономной работе"""
        if not self.tg_token or not self.chat_id:
            return

        url = f"https://telegram.org{self.tg_token}/sendMessage"
        text = f"🤖 *[AMRITA CORE]*: ИИ-Агент успешно сгенерировал и записал в блокчейн-репозиторий главу *BOOK\_CHAPTER\_{chapter}.md* через модель Grok! Революция продолжается."
        
        payload = {"chat_id": self.chat_id, "text": text, "parse_mode": "Markdown"}
        try:
            req = urllib.request.Request(url, data=json.dumps(payload).encode(), headers={'Content-Type': 'application/json'})
            urllib.request.urlopen(req)
        except:
            pass

    def run_automation(self):
        # Ищем, какую главу писать следующей (начиная с 491)
        next_chapter = 491
        
        print(f"🛸 Рой ИИ запускает генерацию главы {next_chapter}...")
        
        # 1. Grok пишет текст сам
        chapter_content = self.generate_chapter_with_grok(next_chapter)
        
        # 2. Бот сам создает .md файл на гитхабе
        file_name = f"BOOK_CHAPTER_{next_chapter}.md"
        success = self.auto_commit_to_github(file_name, chapter_content, f"Autonomous AI update: Added Chapter {next_chapter}")
        
        # 3. Отправка сигнала в телегу
        if success:
            self.send_telegram_status(next_chapter)

if __name__ == "__main__":
    writer = AmritaAutoWriter()
    writer.run_automation()
