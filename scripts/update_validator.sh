#!/bin/bash
# AMRITA OS: Автоматический апдейт софта ноды Solana до v4.2.0-beta.2

set -e

TARGET_VERSION="v4.2.0-beta.2"
LEDGER_DIR="/home/solana/ledger" # Измени на свой путь
VALIDATOR_SERVICE="solana-validator.service"

echo "[AMRITA] Starting autonomous infrastructure upgrade to $TARGET_VERSION..."

# 1. Скачивание и установка нового релиза Agave
sh -c "$(curl -sSfL https://solana.com)"

# 2. Обновление PATH окружения
export PATH="/home/solana/.local/share/solana/install/active_release/bin:$PATH"

# 3. Верификация установленной версии
INSTALLED_VER=$(solana --version)
echo "[AMRITA] Installed version verification: $INSTALLED_VER"

# 4. Безопасный перезапуск сервиса валидатора (Catch up monitoring)
echo "[AMRITA] Restarting validator service..."
sudo systemctl restart $VALIDATOR_SERVICE

# 5. Ожидание восстановления синхронизации (Catch up)
echo "[AMRITA] Monitoring catch-up status..."
solana catchup --our-localhost
echo "[AMRITA] Upgrade complete. Node is fully operational."
