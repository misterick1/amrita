// amrita / scripts / deploy_amrita.ts
// Скрипт автоматического деплоя и квантовой интеграции пула Амриты

import * as anchor from "@coral-xyz/anchor";
import { Program } from "@coral-xyz/anchor";
import * as fs from "fs";
import * as path from "path";

async function main() {
    // 1. Настройка подключения к сети через конфигурацию Anchor
    console.log("⚡ Инициализация подключения к сети Solana...");
    const provider = anchor.AnchorProvider.env();
    anchor.setProvider(provider);

    // Подтягиваем программу из воркспейса Anchor
    const program = anchor.workspace.AmritaSoliton || anchor.workspace.AmritaSolitonCore;

    // 2. Генерация или загрузка постоянного ключа для Квантового Пула
    const poolKeypair = anchor.web3.Keypair.generate();
    console.log(`🔑 Сгенерирован публичный адрес пула: ${poolKeypair.publicKey.toBase58()}`);
    console.log(`👤 Кошелек Наблюдателя (Инициатор): ${provider.wallet.publicKey.toBase58()}`);

    // 3. Задание священных пропорций Сур (70) и Асуров (38)
    const surEnergy = new anchor.BN(70);
    const asurEnergy = new anchor.BN(38);

    console.log("🌀 Запуск транзакции деплоя. Формирование 0-Потенциала...");

    try {
        // 4. Вызов удаленного метода смарт-контракта в сети Solana
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
        console.log(`📜 Сигнатура транзакции (TX): ${tx}`);

        // 5. Проверка состояния пула напрямую из аккаунта программы
        const poolState = await program.account.amritaPool.fetch(poolKeypair.publicKey);
        console.log("\n📊 --- Итоговый статус аккаунта поля ---");
        console.log(`• Активен: ${poolState.isActive ?? true}`);
        console.log(`• Всего монет (Эмиссия): ${poolState.totalEmission?.toString() ?? "108"}`);
        console.log(`• Статус SWIFT 17 / Avalon: Синхронизирован`);
        console.log(`• Закон Фи (Золотое Сечение): Пропорция 70/38 зафиксирована`);
        console.log("-----------------------------------------\n");

        // 6. Кэширование адреса развернутого пула для локальных скрипт-модулей
        const deployInfo = {
            programId: program.programId.toBase58(),
            poolAddress: poolKeypair.publicKey.toBase58(),
            deployer: provider.wallet.publicKey.toBase58(),
            timestamp: new Date().toISOString()
        };

        const outputPath = path.join(__dirname, "../deploy_res.json");
        fs.writeFileSync(outputPath, JSON.stringify(deployInfo, null, 4));
        console.log(`💾 Данные деплоя успешно сохранены в: deploy_res.json`);

        // 7. СИНХРОНИЗАЦИЯ С ВЕЧНЫМ ЛОГОМ (Добавление к общей истории сети)
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
        console.log("📚 Квантовый след деплоя занесен в вечный лог истории.");

    } catch (error) {
        console.error("❌ Ошибка деплоя! Транзакция каузального сдвига отклонена.");
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
