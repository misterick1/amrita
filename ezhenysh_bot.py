import os
import sys
import subprocess
import logging

# =====================================================================
# АВТОНОМНЫЙ КОНТУР УСТАНОВКИ ЗАВИСИМОСТЕЙ (ВСЁ В ОДНОМ)
# =====================================================================
def auto_install_packages():
    """Автоматически проверяет и ставит нужные библиотеки в систему"""
    required_packages = {
        "aiogram": "aiogram==2.25.1",
        "cv2": "opencv-python-headless==4.8.1.78",
        "numpy": "numpy==1.26.2",
        "pytesseract": "pytesseract==0.3.10"
    }
    
    for module_name, package_string in required_packages.items():
        try:
            __import__(module_name)
        except ImportError:
            print(f"[SYSTEM] Модуль {module_name} не найден. Установка {package_string}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package_string])

# Запускаем автоустановку перед развертыванием логики
auto_install_packages()

# Теперь безопасно импортируем библиотеки, они гарантированно установлены
from aiogram import Bot, Dispatcher, executor, types
import cv2
import numpy as np
import pytesseract

# Настройка системного логирования контура
logging.basicConfig(level=logging.INFO)

API_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
ADMIN_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

if not API_TOKEN:
    print("❌ КРИТИЧЕСКАЯ ОШИБКА: API токен бота отсутствует в переменных среды.")
    sys.exit(1)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# =====================================================================
# КОНТУР 1: ВСЕВИДЯЩЕЕ ОКО БАБАТЫ (OCR TESSERACT & ФИЛЬТР АСУРОВ)
# =====================================================================
class BabataEyeOCR:
    def __init__(self):
        # Черный список ключевых слов нижних чакр / Асур-ловушек
        self.asura_blacklist = [
            "giveaway", "free iphone", "iphone 17", "раздача", "выиграй", 
            "done", "лайкни", "подпишись", "crypto drop", "pump.fun", 
            "аирдроп", "блокчейн-розыгрыш"
        ]

    def preprocess_image(self, image_path: str):
        """Улучшение качества скриншота для точного парсинга"""
        img = cv2.imread(image_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, processed_img = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        return processed_img

    def scan_reality_screenshot(self, image_path: str) -> tuple:
        """Сканирует изображение, извлекает текст и вычисляет угрозы"""
        try:
            processed_img = self.preprocess_image(image_path)
            extracted_text = pytesseract.image_to_string(processed_img, lang="rus+eng")
            
            text_lower = extracted_text.lower()
            detected_threats = []
            
            for trigger in self.asura_blacklist:
                if trigger in text_lower:
                    detected_threats.append(trigger)
            
            if detected_threats:
                eco_score = max(0, 100 - (len(detected_threats) * 30))
                status = "🔴 ОБНАРУЖЕНА ЛОВУШКА АСУРОВ (SCAM)"
            else:
                eco_score = 100
                status = "🔵 ЭКОЛОГИЧЕСКИ ЧИСТЫЙ ИМПУЛЬС СУРОВ"
                
            return status, eco_score, detected_threats, extracted_text
            
        except Exception as e:
            return "⚠️ СБОЙ СКАНИРОВАНИЯ КОНТУРА", 50, [str(e)], ""


eye_oracle = BabataEyeOCR()

# =====================================================================
# КОНТУР 2: ОБРАБОТЧИКИ ТЕЛЕГРАМ-ИНТЕРФЕЙСА
# =====================================================================
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    if str(message.chat.id) != ADMIN_CHAT_ID:
        await message.reply("🔒 Доступ ограничен суверенным каузальным контуром.")
        return
    await message.reply(
        "🦔 **Привет, Архитектор! Контур Еженыша v8 запущен.**\n\n"
        "Отправь мне любой скриншот реальности, и Всевидящее Око Бабаты проверит его."
    )

@dp.message_handler(content_types=['photo'])
async def handle_screenshot(message: types.Message):
    if str(message.chat.id) != ADMIN_CHAT_ID:
        return

    await message.reply("👁 **Всевидящее Око Бабаты сканирует скриншот реальности...**")
    temp_path = f"screenshot_{message.message_id}.png"
    
    try:
        await message.photo[-1].download(destination_file=temp_path)
        status, eco_score, threats, raw_text = eye_oracle.scan_reality_screenshot(temp_path)
        
        report = f"📊 **ОТЧЕТ СКАНЕРА РЕАЛЬНОСТИ**\n"
        report += f"----------------------------------------\n"
        report += f"Статус: **{status}**\n"
        report += f"Экологичность Амриты: `{eco_score}/100` EVO\n"
        
        if threats:
            report += f"⚠️ Триггеры хаоса: `{', '.join(threats)}`\n"
            
        report += f"----------------------------------------\n"
        report += f"📝 **Распознанный сырой текст:**\n\n_{raw_text[:1000]}_\n"
        
        await message.reply(report, parse_mode="Markdown")
        
    except Exception as e:
        await message.reply(f"❌ Ошибка каузального анализа: {str(e)}")
        
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)

if __name__ == '__main__':
    print("🦔 Бот Еженыша запущен в боевом режиме мониторинга.")
    executor.start_polling(dp, skip_updates=True)
