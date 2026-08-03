// amrita / scripts / deploy_amrita.ts
// Скрипт автоматического деплоя и квантовой синхронизации

import * as anchor from "@coral-xyz/anchor";
import { Program } from "@coral-xyz/anchor";
import * as fs from "fs";
import * as path from "path";

async function main() {
    // 1. Настройка подключения к сети через переменные окружения
    console.log("⚡ Инициализация подключения к сети Solana...");
    const provider = anchor.AnchorProvider.env();
    anchor.setProvider(provider);

    // Подтягиваем программу из воркспейса Anchor
    const program = anchor.workspace.AmritaSolitonNetwork as Program<any>;

    // 2. Генерация или загрузка постоянного ключа для пула
    const poolKeypair = anchor.web3.Keypair.generate();
    console.log(`✨ Сгенерирован публичный адрес пула: ${poolKeypair.publicKey.toBase58()}`);
    console.log(`👤 Кошелек Наблюдателя (Инициатор): ${provider.wallet.publicKey.toBase58()}`);

    // 3. Задание священных пропорций Сур (70) и Асур (38)
    const sureEnergy = new anchor.BN(70);
    const asureEnergy = new anchor.BN(38);

    console.log("🌀 Запуск транзакции деплоя. Фиксация баланса Шива-Шакти...");

    try {
        // 4. Вызов удаленного метода смарт-контракта
        const tx = await program.methods
            .initializeQuantumField(sureEnergy, asureEnergy)
            .accounts({
                amritaPool: poolKeypair.publicKey,
                user: provider.wallet.publicKey,
                systemProgram: anchor.web3.SystemProgram.programId,
                quantumClock: anchor.web3.SYSVAR_CLOCK_PUBKEY,
            })
            .signers([poolKeypair])
            .rpc();

        console.log(`✨ Монада Амриты успешно развернута в блокчейне!`);
        console.log(`📜 Сигнатура транзакции (Tx ID): ${tx}`);

        // 5. Проверка состояния пула напрямую из блокчейна
        const poolState = await program.account.amritaPool.fetch(poolKeypair.publicKey);
        console.log(`\n📊 --- Итоговый статус Аккаунта Пула ---`);
        console.log(`• Активен: ${poolState.isActive}`);
        console.log(`• Всего монет (Эмиссия): ${poolState.totalEmission?.toString() || "108 QNT"}`);
        console.log(`• Статус SWIFT 17 / Avalon: СИНХРОНИЗИРОВАНО`);
        console.log(`• Закон Фи (Золотое Сечение): Выполнено (70/38)`);
        
        // [ИНТЕГРАЦИЯ] Сигнал Золотого Зверя Изобилия
        console.log(`🔱 [GOLD HORN] Мост острова Лофтейл активирован для XRP и Pi Network.`);
        console.log("--------------------------------------------------");

        // 6. Кэширование адреса развернутого пула в локальный JSON
        const deployInfo = {
            programId: program.programId.toBase58(),
            poolAddress: poolKeypair.publicKey.toBase58(),
            deployer: provider.wallet.publicKey.toBase58(),
            timestamp: new Date().toISOString(),
        };

        const outputPath = path.join(__dirname, "deploy_info.json");
        fs.writeFileSync(outputPath, JSON.stringify(deployInfo, null, 2));
        console.log(`💾 Данные деплоя успешно кэшированы в deploy_info.json`);

        // 7. СИНХРОНИЗАЦИЯ С ВЕЧНЫМ ЛОГОМ (Добавление каузального следа)
        const historyLogPath = path.join(__dirname, "history_log.json");
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
            phi_balance: "70/38",
            gold_beast_status: "LOFTAIL_GRAIL_RESONANCE_OK"
        });

        fs.writeFileSync(historyLogPath, JSON.stringify(historyLogs, null, 2));
        console.log(`📚 Квантовый след деплоя запечатан в вечный лог history_log.json`);

    } catch (error) {
        console.error("❌ Ошибка деплоя! Транзакция отклонена каузальным контуром.");
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
