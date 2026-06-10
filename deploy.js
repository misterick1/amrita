const { execSync } = require('child_process');
const fs = require('fs');

console.log("🚀 [Оркестратор] Запуск автоматического деплоя экосистемы...");

function runCommand(command) {
    try {
        console.log(`Executing: ${command}`);
        execSync(command, { stdio: 'inherit' });
    } catch (error) {
        console.error(`❌ Ошибка при выполнении: ${command}`);
        process.exit(1);
    }
}

// 1. Проверяем наличие файла конфигурации
if (!fs.existsSync('.env')) {
    console.error("❌ КРИТИЧЕСКАЯ ОШИБКА: Файл .env отсутствует. Деплой остановлен.");
    process.exit(1);
}

// 2. Обновляем зависимости Python
console.log("📦 Установка и обновление зависимостей Python...");
runCommand("pip install -r requirements.txt --upgrade");

// 3. Перезапуск сервисов через PM2 (менеджер процессов для деплоя 24/7)
console.log("🔄 Перезапуск модулей в PM2...");

// Перезапуск платежного сервера Pi на FastAPI (порт 8000)
runCommand("pm2 delete pi_payment_server || true");
runCommand("pm2 start 'uvicorn pi_payment_server:app --host 0.0.0.0 --port 8000' --name 'pi_payment_server'");

// Перезапуск асинхронного моста Pump.fun (Solana Stream)
runCommand("pm2 delete pump_fun_bridge || true");
runCommand("pm2 start python3 --name 'pump_fun_bridge' -- pump_fun_bridge.py");

// 4. Сохраняем конфигурацию процессов PM2, чтобы они поднимались после ребута сервера
runCommand("pm2 save");

console.log("✅ [УСПЕХ] Все компоненты успешно развернуты и запущены в Swarm Mode!");
