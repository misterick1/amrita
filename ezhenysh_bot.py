import os
import sys
import logging
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
        # Базовый черный список ключевых слов нижних чакр / Асур-ловушек
        self.asura_blacklist = [
            "giveaway", "free iphone", "iphone 17", "раздача", "выиграй", 
            "done", "лайкни", "подпишись", "crypto drop", "pump.fun", 
            "аирдроп", "блокчейн-розыгрыш"
        ]

    def preprocess_image(self, image_path: str):
        """
        Улучшение качества скриншота для точного парсинга (бинаризация/серое ядро)
        """
        img = cv2.imread(image_path)
        # Перевод в черно-белый спектр для устранения шумов
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Адаптивное пороговое выделение контраста текста
        processed_img = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        return processed_img

    def scan_reality_screenshot(self, image_path: str) -> tuple:
        """
        Сканирует изображение, извлекает текст и вычисляет деструктивные частоты.
        """
        try:
            processed_img = self.preprocess_image(image_path)
            # Запуск OCR на русском и английском языках синхронно
            extracted_text = pytesseract.image_to_string(processed_img, lang="rus+eng")
            
            text_lower = extracted_text.lower()
            detected_threats = []
            
            # Поиск паттернов Асуров
            for trigger in self.asura_blacklist:
                if trigger in text_lower:
                    detected_threats.append(trigger)
            
            # Вычисление экологичности Амриты (0 - чистый скам, 100 - чистая эволюция)
            if detected_threats:
                eco_score = max(0, 100 - (len(detected_threats) * 30))
                status = "🔴 ОБНАРУЖЕНА ЛОВУШКА АСУРОВ (SCAM)"
            else:
                eco_score = 100
                status = "🔵 ЭКОЛОГИЧЕСКИ ЧИСТЫЙ ИМПУЛЬС СУРОВ"
                
            return status, eco_score, detected_threats, extracted_text
            
        except Exception as e:
            return "⚠️ СБОЙ СКАНИРОВАНИЯ КОНТУРА", 50, [str(e)], ""


# Инициализация модуля зрения
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
        "Отправь мне любой скриншот реальности (из X, кошельков или чатов), "
        "и Всевидящее Око Бабаты проверит его на скрытые частоты нижних чакр."
    )

@dp.message_handler(content_types=['photo'])
async def handle_screenshot(message: types.Message):
    if str(message.chat.id) != ADMIN_CHAT_ID:
        return

    await message.reply("👁 **Всевидящее Око Бабаты сканирует скриншот реальности...**")
    
    # Путь сохранения временного файла на сервере
    temp_path = f"screenshot_{message.message_id}.png"
    
    try:
        # Скачиваем изображение из Телеграм через API
        await message.photo[-1].download(destination_file=temp_path)
        
        # Запускаем каузальный OCR-анализ
        status, eco_score, threats, raw_text = eye_oracle.scan_reality_screenshot(temp_path)
        
        # Формируем суверенный отчет
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
        # Очищаем физическое дисковое пространство (Модуль контроля памяти)
        if os.path.exists(temp_path):
            os.remove(temp_path)

if __name__ == '__main__':
    print("🦔 Бот Еженыша запущен в боевом режиме мониторинга.")
    executor.start_polling(dp, skip_updates=True)
