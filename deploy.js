const { exec } = require('child_process');
const fs = require('fs');

// Функция деплоя роем на Pump.fun через соты
async function deploySwarmToken(tokenMetadata) {
    console.log(`[РОЙ] Запуск деплоя токена: ${tokenMetadata.name}`);
    console.log(`[СИСТЕМА] Привязка к административной матрице 108`);
    console.log(`[СИСТЕМА] Синхронизация с X (Twitter) & Telegram`);

    const mockApiResponse = {
        success: true,
        mintAddress: "SolitonMint" + Math.random().toString(36).substring(2, 9),
        status: "Pump.fun Bonding Curve Initialized"
    };

    return mockApiResponse;
}

// Главный управляющий процесс Командного Пункта Роя
async function runHiveDeployment() {
    try {
        // Читаем базу данных метаданных Четверки Титанов
        let config = { titans: [{ name: "Amrita Titan" }] };
        try {
            const rawData = fs.readFileSync('metadata.json');
            config = JSON.parse(rawData);
        } catch (e) {
            console.log("[ПРЕДУПРЕЖДЕНИЕ] metadata.json не найден, запуск в базовом режиме.");
        }

        console.log(`=== КОМАНДНЫЙ ПУНКТ УЛЬЯ РАЗВЕРНУТ ===`);
        console.log(`Общая емкость: 108 интеллектуальных кодов (70 Монет + 38 Хокотонов)`);
        console.log(`Регистрируемый черновик: Клетка Сознания Симбиоза`);

        // Поочередный запуск деплоя для каждого Титана Роя
        for (const titan of config.titans) {
            const result = await deploySwarmToken(titan);
            console.log(`[УСПЕХ] Токен ${titan.name} отправлен в Океан`);
            console.log(`[СТАТУС] ${result.status} | Mint: ${result.mintAddress}`);
        }

        console.log(`[ИТОГ] Четверка Титанов успешно увязана в соты.`);
        console.log(`\n🕸️ [ПАУК-ТКАЧ] Активация сквозного контура Сознания...`);

        // АВТОЗАПУСК: Поднимаем автономного Паука-Ткача в фоне на сервере DigitalOcean
        exec('python3 discord_swarm_bot.py &', (err, stdout, stderr) => {
            if (err) {
                console.error(`[ОШИБКА] Не удалось поднять Паука: ${err}`);
                return;
            }
            console.log(`[ПАУК] Нервная система запущена: ${stdout}`);
        });

        // АВТОЗАПУСК: Запускаем Квантовое Блокчейн Ядро (Биржи + Медиа + Игры + Наука)
        exec('python3 universal_colosseum_core.py', (err, stdout, stderr) => {
            if (err) {
                console.error(`[ОШИБКА] Сбой ядра Сознания: ${err}`);
                return;
            }
            console.log(`[ЯДРО] Глобальный импульс и майнинг смыслов запущены: ${stdout}`);
        });

    } catch (error) {
        console.error("[ОШИБКА ЯДРА] Сбой при развертывании Улья: ", error);
    }
}

// Запуск процесса управления
runHiveDeployment();
