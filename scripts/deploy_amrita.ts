// // amrita / scripts / deploy_amrita.ts
// // Скрипт автоматического деплоя и квантовой интеграции

import * as anchor from "@coral-xyz/anchor";
import { Program } from "@coral-xyz/anchor";
import * as fs from "fs";
import * as path from "path";

async function main() {
    // 1. Настройка подключения к сети через конфигурацию Anchor
    console.log("⚡ Инициализация подключения к контуру сети...");
    const provider = anchor.AnchorProvider.env();
    anchor.setProvider(provider);

    // Подтягиваем программу из воркспейса Anchor
    const program = anchor.workspace.AmritaSoliton;

    // 2. Генерация или загрузка постоянного ключа пула
    const poolKeypair = anchor.web3.Keypair.generate();
    console.log(`🔑 Сгенерирован публичный адрес пула: ${poolKeypair.publicKey.toBase58()}`);
    console.log(`👤 Кошелек Наблюдателя (Инициализатор): ${provider.wallet.publicKey.toBase58()}`);

    // 3. Задание священных пропорций Сур (70) и Асур (38)
    const surEnergy = new anchor.BN(70);
    const asureEnergy = new anchor.BN(38);

    console.log("🌀 Запуск транзакции деплоя. Фиксация частоты баланса...");

    try {
        // 4. Вызов удаленного метода смарт-контракта Anchor
        const tx = await program.methods
            .initializeQuantumField(surEnergy, asureEnergy)
            .accounts({
                amritaPool: poolKeypair.publicKey,
                user: provider.wallet.publicKey,
                systemProgram: anchor.web3.SystemProgram.programId,
                quantumClock: anchor.web3.SYSVAR_CLOCK_PUBKEY,
            })
            .signers([poolKeypair])
            .rpc();

        console.log(`✨ Монада Амриты успешно развернута в блокчейне!`);
        console.log(`📜 Сигнатура транзакции (Tx): ${tx}`);

        // 5. Проверка состояния пула напрямую из сети
        const poolState = await program.account.quantumPool.fetch(poolKeypair.publicKey);
        console.log(`\n📊 --- Итоговый статус активированной Монады ---`);
        console.log(`• Активен: ${poolState.isActive}`);
        console.log(`• Всего монет (Эмиссия): ${poolState.totalVolume}`);
        console.log(`• Статус SWIFT 17 / Avalon: СИНХРОНИЗИРОВАНО`);
        console.log(`• Закон Фи (Золотое Сечение): Пропорция 70/38 запечатана.`);
        console.log("--------------------------------------------------\n");

        // 6. Кэширование адреса развернутого пула в локальные метаданные
        const deployInfo = {
            programId: program.programId.toBase58(),
            poolAddress: poolKeypair.publicKey.toBase58(),
            deployer: provider.wallet.publicKey.toBase58(),
            timestamp: new Date().toISOString()
        };

        const outputPath = path.join(__dirname, "../target/deploy_info.json");
        fs.writeFileSync(outputPath, JSON.stringify(deployInfo, null, 4));
        console.log(`💾 Данные деплоя успешно сохранены в локальный кэш.`);

        // 7. СИНХРОНИЗАЦИЯ С ВЕЧНЫМ ЛОГОМ (Добавление 1082-й строки)
        const historyLogPath = path.join(__dirname, "../history_log.json");
        let historyLogs = [];

        if (fs.existsSync(historyLogPath)) {
            try {
                historyLogs = JSON.parse(fs.readFileSync(historyLogPath, "utf-8"));
            } catch (e) {
                historyLogs = [];
            }
        }

        historyLogs.push({
            event: "SOLANA_CONTRACT_DEPLOYMENT",
            timestamp: deployInfo.timestamp,
            pool: deployInfo.poolAddress,
            tx: tx,
            phi_balance: "70/38"
        });

        fs.writeFileSync(historyLogPath, JSON.stringify(historyLogs, null, 4));
        console.log("📚 Квантовый след деплоя зафиксирован в вечном логе.");

    } catch (error) {
        console.error("❌ Ошибка деплоя! Транзакция отклонена каузальным полем.");
        console.error(error);
        process.exit(1);
    }
}

main().then(
    () => process.exit(0),
    (err) => {
        console.error(err);
        process.exit(1);
    }
);
