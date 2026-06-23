const { execSync } = require('child_process');
const fs = require('fs');

console.log("🚀 [Оркестратор] Запуск автоматического обновления контура Amrita...");

function runCommand(command) {
    try {
        console.log(`Executing: ${command}`);
        execSync(command, { stdio: 'inherit' });
    } catch (error) {
        console.error(`❌ Ошибка при выполнении: ${command}`);
        // Не останавливаем скрипт, если PM2 просто не нашел старый процесс для удаления
        if (!command.includes('delete')) {
            process.exit(1);
        }
    }
}

// 1. Проверяем наличие файла конфигурации
if (!fs.existsSync('.env')) {
    console.error("❌ КРИТИЧЕСКАЯ ОШИБКА: Файл конфигурации .env отсутствует!");
    process.exit(1);
}

// 2. Обновляем зависимости Python
console.log("📦 Установка и обновление зависимостей...");
runCommand("pip install -r requirements.txt --upgrade");

// 3. Перезапуск сервисов через PM2
console.log("🔄 Перезапуск модулей в PM2...");

// Перезапуск платежного сервера Pi на FastAPI
runCommand("pm2 delete pi_payment_server || true");
runCommand("pm2 start 'uvicorn pi_payment_server:app --host 0.0.0.0 --port 8000' --name 'pi_payment_server'");

// Перезапуск асинхронного моста Pump.fun (Solana Stream)
runCommand("pm2 delete pump_fun_bridge || true");
runCommand("pm2 start 'python3 pump_fun_bridge.py' --name 'pump_fun_bridge'");

// 4. Сохраняем конфигурацию процессов PM2
runCommand("pm2 save");

console.log("✅ [УСПЕХ] Все компоненты успешно перезапущены в PM2!");
