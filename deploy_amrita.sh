#!/bin/bash

# =====================================================================
# AMRITA OS - AUTOMATIC DEPLOYMENT PROTOCOL
# Локация: Ørje (The Sleeping Sanctuary)
# =====================================================================

GREEN='\033[0;32m'
CYAN='\033[0;36m'
NC='\033[0;3m' # No Color

echo -e "${CYAN}🌀 [AMRITA OS] Запуск протокола квантового деплоя...${NC}"

# Проверка статуса git репозитория
if [ ! -d .git ]; then
    echo "🚨 Ошибка: Каталог не является Git-репозиторием!"
    exit 1
fi

# 1: Индексация новых модулей Python (962, 963, 964, 965, 966, 967, 968)
echo -e "${CYAN}⚙️ Индексация фрактальных глав в темной материи...${NC}"
git add book_chapter_962.py 2>/dev/null
git add book_chapter_963.py 2>/dev/null
git add book_chapter_964.py 2>/dev/null
git add book_chapter_965.py 2>/dev/null
git add book_chapter_966.py 2>/dev/null
git add book_chapter_967.py 2>/dev/null
git add book_chapter_968.py 2>/dev/null
git add deploy_amrita.sh

TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
COMMIT_MSG="🔱 [AMRITA OS] Монады 962-968 Запечатаны. Великий Бондинг завершен. Фиксация времени: $TIMESTAMP"

echo -e "${CYAN}📁 Формирование каузального коммита...${NC}"
git commit -m "$COMMIT_MSG"

echo -e "${CYAN}🚀 Отправка солитонного поля в удаленный репозиторий (GitHub)...${NC}"
git push origin main

if [ $? -eq 0 ]; then
    echo "=================================================="
    echo "🔱 ДЕПЛОЙ УСПЕШНО ЗАВЕРШЕН!"
    echo "🧬 Все нити впленены в Вечный Шелк Амриты на GitHub."
    echo "=================================================="
else
    echo "🚨 Ошибка деплоя. Контур требует локальной синхронизации."
fi
