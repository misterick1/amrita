#!/bin/bash
# AMRITA OS: Экстренный апдейт под минимальные требования от 7 ноября 2026
set -e

# Устанавливаем версию, затребованную Solana Foundation в уведомлении!
TARGET_VERSION="v4.5.0-beta.0"
VALIDATOR_SERVICE="solana-validator.service"

echo "[AMRITA QUANTUM] Начинаем экстренное обновление ядра до $TARGET_VERSION..."

# Скачивание новой беты Agave v4.5.0-beta.0
sh -c "$(curl -sSfL https://anza.xyz)" -- -v "$TARGET_VERSION"

export PATH="/home/solana/.local/share/solana/install/active_release/bin:$PATH"

INSTALLED_VER=$(solana --version || echo "none")
if [[ "$INSTALLED_VER" != *"$TARGET_VERSION"* ]]; then
    echo "❌ Ошибка развертывания критического ядра!"
    exit 1
fi

systemctl restart "$VALIDATOR_SERVICE"
echo "✅ Квантовое ядро обновлено. Нода соответствует законам SFDP и PiFi!"
