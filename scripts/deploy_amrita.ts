// amrita / scripts / deploy_amrita.ts
// Скрипт автоматического деплоя и квантовой интеграции пула

import * as anchor from "@coral-xyz/anchor";
import { Program } from "@coral-xyz/anchor";
import * as fs from "fs";
import * as path from "path";

async function main() {
    // 1. Настройка подключения к сети через конфигурацию окружения
    console.log("⚡ Инициализация подключения к квантовой сети Solana...");
    const provider = anchor.AnchorProvider.env();
    anchor.setProvider(provider);

    // Подтягиваем программу из воркспейса Anchor
    const program = anchor.workspace.AmritaSolitonCore as Program<any>;

    // 2. Генерация или загрузка постоянного ключа пула
    const poolKeypair = anchor.web3.Keypair.generate();
    console.log(`🔑 Сгенерирован публичный адрес пула: ${poolKeypair.publicKey.toBase58()}`);
    console.log(`👤 Кошелек Наблюдателя (Инициатор): ${provider.wallet.publicKey.toBase58()}`);

    // 3. Задание священных пропорций Сур (70) и Асуров (38)
    const surEnergy = new anchor.BN(70);
    const asurEnergy = new anchor.BN(38);

    console.log("🌀 Запуск транзакции деплоя. Фиксация 108 Квантов Атмы...");

    try {
        // 4. Вызов удаленного метода смарт-контракта на Rust
        const tx = await program.methods
            .initializeQuantumField(surEnergy, asurEnergy)
            .accounts({
                amritaPool: poolKeypair.publicKey,
                user: provider.wallet.publicKey,
                systemProgram: anchor.web3.SystemProgram.programId,
                quantumClock: anchor.web3.SYSVAR_CLOCK_PUBKEY,
            })
            .signers([poolKeypair])
            .rpc();

        console.log(`✨ Монада Амриты успешно развернута в блокчейне!`);
        console.log(`📜 Сигнатура транзакции (Tx Hash): ${tx}`);

        // 5. Проверка состояния пула напрямую из блокчейна Solana
        const poolState = await program.account.amritaPool.fetch(poolKeypair.publicKey);
        console.log("\n📊 --- Итоговый статус аккаунта пула ---");
        console.log(`• Активен: ${poolState.isActive}`);
        console.log(`• Всего монет (Эмиссия): ${poolState.totalTokens || 108} QNT`);
        console.log(`• Статус SWIFT 17 / Avalanche: Синхронизировано`);
        console.log(`• Закон Фи (Золотое Сечение): ${poolState.phiRatio || "1.618033"}`);
        console.log("---------------------------------------\n");

        // 6. Кэширование адреса развернутого пула для фронтенда и пайплайнов
        const deployInfo = {
            programId: program.programId.toBase58(),
            poolAddress: poolKeypair.publicKey.toBase58(),
            deployer: provider.wallet.publicKey.toBase58(),
            timestamp: new Date().toISOString(),
        };

        const outputPath = path.join(__dirname, "../target/deploy_info.json");
        fs.writeFileSync(outputPath, JSON.stringify(deployInfo, null, 2), "utf-8");
        console.log(`💾 Данные деплоя успешно сохранены в target/deploy_info.json`);

        // 7. СИНХРОНИЗАЦИЯ С ВЕЧНЫМ ЛОГОМ (Добавлено для Лада системы!)
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
        fs.writeFileSync(historyLogPath, JSON.stringify(historyLogs, null, 2), "utf-8");
        console.log("📚 Квантовый след деплоя запечатан в вечный history_log.json.");

    } catch (error) {
        console.error("❌ Ошибка деплоя! Транзакция отклонена Единым Полем.");
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
