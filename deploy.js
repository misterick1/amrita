const { execSync } = require('child_process');
const fs = require('fs');

console.log("🚀 [Оркестратор] Запуск автоматического обновления и перезапуска контура Amrita...");

// Функция для безопасного выполнения системных команд
function runCommand(command) {
    try {
        console.log(`Executing: ${command}`);
        execSync(command, { stdio: 'inherit' });
    } catch (error) {
        console.error(`❌ Ошибка при выполнении: ${command}`);
        // Не выходим при ошибке удаления PM2, так как процесса может не существовать
        if (!command.includes('delete')) {
            process.exit(1);
        }
    }
}

// 1. Проверяем наличие файла конфигурации локального окружения
if (!fs.existsSync('.env')) {
    console.error("❌ КРИТИЧЕСКАЯ ОШИБКА: Файл конфигурации .env отсутствует в корне каталога!");
    process.exit(1);
}

// 2. Обновляем и синхронизируем зависимости Python
console.log("📦 Установка и обновление зависимостей ядра из requirements.txt...");
runCommand("pip install --upgrade pip");
runCommand("pip install -r requirements.txt --upgrade");

// 3. Перезапуск сервисов через менеджер процессов PM2
console.log("🔄 Перезапуск модулей в PM2 для очищения частот матрицы...");

// --- Перезапуск платежного сервера Pi на FastAPI ---
runCommand("pm2 delete pi_payment_server || true");
runCommand("pm2 start 'uvicorn pi_payment_server:app --host 0.0.0.0 --port 8000' --name 'pi_payment_server'");

// --- Перезапуск асинхронного моста Pump.fun (Solana Stream) ---
runCommand("pm2 delete pump_fun_bridge || true");
runCommand("pm2 start python3 -- pump_fun_bridge.py --name 'pump_fun_bridge'");

// --- Перезапуск ИИ-Оркестратора Эволюции Сознания (Новый модуль) ---
runCommand("pm2 delete consciousness_evolution_core || true");
runCommand("pm2 start python3 -- consciousness_evolution_core.py --name 'consciousness_evolution_core'");

// 4. Сохраняем конфигурацию процессов PM2 для защиты от перезагрузки сервера
console.log("💾 Сохранение конфигурации активного роя в PM2...");
runCommand("pm2 save");

console.log("✅ [УСПЕХ] Все компоненты успешно развернуты, запущены и зафиксированы в PM2!");
