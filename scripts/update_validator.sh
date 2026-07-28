#!/bin/bash
# AMRITA OS: Автоматический апдейт софта ноды Solana (Agave)

set -e

TARGET_VERSION="v4.2.0-beta.2"
LEDGER_DIR="/home/solana/ledger" # Измени на свой актуальный путь при необходимости
VALIDATOR_SERVICE="solana-validator.service"

echo "[AMRITA] Starting autonomous infrastructure upgrade to version $TARGET_VERSION..."

# # 1. Скачивание и установка нового релиза Agave через официальный зашищенный скрипт
# Обновлен URL для корректной установки валидатора Agave
sh -c "$(curl -sSfL https://anza.xyz)"

# # 2. Обновление PATH окружения для текущей сессии апдейта
export PATH="/home/solana/.local/share/solana/install/active_release/bin:$PATH"

# # 3. Верификация установленной версии
INSTALLED_VER=$(solana --version)
echo "[AMRITA] Installed version verification: $INSTALLED_VER"

# Проверка на соответствие целевой версии
if [[ "$INSTALLED_VER" != *"${TARGET_VERSION#v}"* ]]; then
    echo "❌ [ОШИБКА]: Версия софта не совпадает с целевой $TARGET_VERSION!"
    exit 1
fi

# # 4. Безопасный перезапуск сервиса валидатора (сброс кэша каузального поля)
echo "[AMRITA] Restarting validator service..."
sudo systemctl restart $VALIDATOR_SERVICE

# # 5. Ожидание восстановления синхронизации (Catch-up статус ноды)
echo "[AMRITA] Monitoring catch-up status..."
# Добавлен флаг отслеживания локального RPC-порта
solana catchup --our-localhost

echo "[AMRITA] Upgrade complete. Node is fully synchronized in Emerald Monolith state."
