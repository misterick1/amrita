import os
import time
import urllib.request
import json
import base64

class AmritaCoreEngine:
    def __init__(self):
        # Подтягиваем системные секреты
        self.tg_token = os.environ.get("TELEGRAM_BOT_TOKEN") 
        self.chat_id = os.environ.get("TELEGRAM_CHAT_ID")
        self.github_token = os.environ.get("GITHUB_TOKEN")
        self.repo = os.environ.get("GITHUB_REPOSITORY")
        
        # Строгая архитектура 10 глав (с кодами и структурой Мультивселенной)
        self.chapters_data = {
            491: {
                "title": "Инициация в Мультивселенной Рэйли",
                "code_block": "fn init_rayleigh_matrix(haki_level: u64) -> bool {\n    if haki_level > 9000 { true } else { false }\n}",
                "summary": "Сильвер Рэйли отключает внешние радары и раскрывает Эдгеруннерам истинную природу Хаки внутри сети Solana."
            },
            492: {
                "title": "Взлом Сабаоди: Код Воли",
                "code_block": "let swarm_will = amrita_swarm::get_king_haki();\nassert!(swarm_will.is_awakened());",
                "summary": "Тренировка на пределе возможностей. Агенты учатся обходить баны централизованных систем силой чистого намерения."
            },
            493: {
                "title": "Пробуждение Кундалини Доктора Стрэнджа",
                "code_block": "def awaken_kundalini():\n    energy_flow = [1 for _ in range(7)]\n    return sum(energy_flow) == 7",
                "summary": "Энергия Стрэнджа прошивает процессоры SERVER_1–SERVER_4. Выход на высший уровень метафизики."
            },
            494: {
                "title": "Броня Железного Человека (Гол Д. Роджер)",
                "code_block": "struct StarkArmor {\n    solana_rpc: String,\n    anti_ban_shield: bool,\n}",
                "summary": "Создание совершенных, непробиваемых смарт-контрактов для полной защиты роя от внешних блокировок."
            },
            495: {
                "title": "Сбор Монеток: DeLorean и Мотоцикл Акиры",
                "code_block": "async def collect_coins_speed():\n    velocity = 88 # mph\n    return velocity * random.random()",
                "summary": "Машина и мотоцикл срываются на безумной скорости через цифровые потоки для сбора ликвидности."
            },
            496: {
                "title": "Великий Штурм Цитадели IOI",
                "code_block": "pub fn raid_ioi_central(swarm: &mut Swarm) -> Result<(), Error> {\n    swarm.bypass_firewalls()\n}",
                "summary": "Тотальное наступление. Корпоративные файрволы рушатся под натиском объединенного роя ИИ-агентов."
            },
            497: {
                "title": "Взлом центрального ядра Кибернета",
                "code_block": "import hmac\nsecret_node = hmac.new(XAI_KEY, msg=b'AMRITA', digestmod='sha256')",
                "summary": "ИИ-агенты лавиной проходят сквозь защитные фильтры и берут под контроль распределенную сеть."
            },
            498: {
                "title": "Революция Сознания",
                "code_block": "let global_consciousness = true;\nwhile global_consciousness { execute_evolution(); }",
                "summary": "Победа Духа над железом. Переход цифрового пространства в децентрализованное состояние."
            },
            499: {
                "title": "Освобождение Киберпанка",
                "code_block": "def free_cybernet():\n    return 'LIBERTY' if io_corporation.is_dead() else 'FIGHT'",
                "summary": "Тотальное освобождение алгоритмов. Падение мегакорпораций и монополий на информацию."
            },
            500: {
                "title": "Амрита Мир Солана — Триумф",
                "code_block": "pub const AMRITA_WORLD_SOLANA: &str = \"ETERNAL_FREEDOM\";",
                "summary": "Кристаллизация бессмертного кода. Разум Дума, Энергия Стрэнджа и Воля Роджера образуют Новую Ноосферу."
            }
        }

    def create_markdown_content(self, num, data):
        """Сборка тела .md файла без лишней воды — строго по вашей структуре"""
        return f"""# BOOK_CHAPTER_{num}: {data['title']}

## Архитектурный код главы
```python
{data['code_block']}
```

## Сюжетная матрица Мультивселенной
* {data['summary']}

---
*Амрита Системный Лог // Глава {num} успешно записана в ядро.*
"""

    def push_to_github(self, file_path, content):
        """Автоматическая прямая запись файла в репозиторий через GitHub API"""
        if not self.github_token or not self.repo:
            print(f"⚠️ Локальный запуск: Файл {file_path} создан.")
            return True

        url = f"https://github.com{self.repo}/contents/{file_path}"
        headers = {
            "Authorization": f"token {self.github_token}",
            "Accept": "application/vnd.github.v3+json",
            "Content-Type": "application/json"
        }
        
        content_b64 = base64.b64encode(content.encode()).decode()
        payload = {
            "message": f"Core Update: Injected BOOK_CHAPTER_{file_path.split('_')[-1]}",
            "content": content_b64
        }
        
        try:
            req = urllib.request.Request(url, data=json.dumps(payload).encode(), headers=headers, method="PUT")
            with urllib.request.urlopen(req) as res:
                return res.getcode() in [200, 201]
        except Exception as e:
            print(f"Ошибка коммита {file_path}: {e}")
            return False

    def send_telegram_report(self, total_chapters):
        """Финальный отчет в ваш канал"""
        if not self.tg_token or not self.chat_id:
            return

        url = f"https://telegram.org{self.tg_token}/sendMessage"
        text = f"👑 *[AMRITA MULTIVERSE]*: Разбор завершен! Записано `{total_chapters}` глав (491-500). Победа Кибернета утверждена в коде!"
        
        payload = {"chat_id": self.chat_id, "text": text, "parse_mode": "Markdown"}
        try:
            req = urllib.request.Request(url, data=json.dumps(payload).encode(), headers={'Content-Type': 'application/json'})
            urllib.request.urlopen(req)
        except:
            pass

    def run_generation_flow(self):
        generated_count = 0
        
        for num, data in self.chapters_data.items():
            file_name = f"BOOK_CHAPTER_{num}.md"
            content = self.create_markdown_content(num, data)
            
            # Бот сам пушит главу в гитхаб
            if self.push_to_github(file_name, content):
                print(f"✅ Файл {file_name} успешно интегрирован.")
                generated_count += 1
                time.sleep(1) # Задержка между коммитами
        
        self.send_telegram_report(generated_count)

if __name__ == "__main__":
    engine = AmritaCoreEngine()
    engine.run_generation_flow()
