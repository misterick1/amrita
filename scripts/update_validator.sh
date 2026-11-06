#!/bin/bash
# AMRITA OS: Автоматический апдейт софта ноды под стандарты SFDP
set -e

TARGET_VERSION="v4.2.0-beta.2"
LEDGER_DIR="/home/solana/ledger"
VALIDATOR_SERVICE="solana-validator.service"
RPC_URL="http://127.0.0.1:8899"

echo "[AMRITA] Starting autonomous infrastructure update..."

# 1. Скачивание и установка конкретной целевой версии релизов Anza/Agave
echo "[AMRITA] Fetching Solana/Anza installer..."
# Передаем флаг -v для установки именно TARGET_VERSION, а не последнего релиза
sh -c "$(curl -sSfL https://anza.xyz)" -- -v "$TARGET_VERSION"

# 2. Обновление PATH окружения для текущей сессии
export PATH="/home/solana/.local/share/solana/install/active_release/bin:$PATH"

# 3. Верификация установленной версии
INSTALLED_VER=$(solana --version || echo "none")
echo "[AMRITA] Installed version verification: $INSTALLED_VER"

# Проверка на частичное соответствие целевой версии
if [[ "$INSTALLED_VER" != *"$TARGET_VERSION"* ]]; then
    echo "❌ [ОШИБКА]: Версия софта не совпадает с целевой ($TARGET_VERSION)!"
    exit 1
fi

# 4. Безопасный перезапуск сервиса валидатора
echo "[AMRITA] Restarting validator service..."
# Используем sudo только если скрипт запущен не от root
if [ "$EUID" -ne 0 ]; then
    sudo systemctl restart "$VALIDATOR_SERVICE"
else
    systemctl restart "$VALIDATOR_SERVICE"
fi

# 5. Ожидание восстановления синхронизации (Catch-up)
echo "[AMRITA] Monitoring catch-up status via local RPC..."
# Добавим цикл, пока нода полностью не догонит сеть, чтобы бот в Discord выдал финальный статус
until solana catchup --our-localhost --url "$RPC_URL"; do
    echo "[AMRITA] Still catching up to the cluster... Retrying in 30 seconds."
    sleep 30
done

echo "[AMRITA] Upgrade complete. Node is fully synced and generating blocks!"
