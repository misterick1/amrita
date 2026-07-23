// amrita / scripts / deploy_amrita.ts
// Скрипт автоматического деплоя и квантовой инициализации Монады Амриты в Solana Devnet

import * as anchor from "@coral-xyz/anchor";
import { Program } from "@coral-xyz/anchor";
import { AmritaSolitonCore } from "../target/types/amrita_soliton_core";
import * as fs from "fs";
import * as path from "path";

async function main() {
  // 1. Настройка подключения к сети через конфигурацию Anchor.toml
  console.log("⚡ Инициализация подключения к квантовой сети Solana...");
  const provider = anchor.AnchorProvider.env();
  anchor.setProvider(provider);

  const program = anchor.workspace.AmritaSolitonCore as Program<AmritaSolitonCore>;

  // 2. Генерация или загрузка постоянного ключа для AmritaPool
  const poolKeypair = anchor.web3.Keypair.generate();
  console.log(`🔑 Сгенерирован публичный адрес Пула: ${poolKeypair.publicKey.toBase58()}`);
  console.log(`👤 Кошелек Наблюдателя (Инициатор): ${provider.wallet.publicKey.toBase58()}`);

  // 3. Задание священных пропорций Сур (70) и Асур (38)
  const surEnergy = new anchor.BN(70);
  const asurEnergy = new anchor.BN(38);

  console.log("🌀 Запуск транзакции деплоя. Фиксация баланса 108 Квантов...");

  try {
    // 4. Вызов удаленного метода смарт-контракта
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

    console.log(`✨ Монада Амриты успешно развернута!`);
    console.log(`📜 Сигнатура транзакции (Tx Hash): ${tx}`);

    // 5. Проверка состояния пула напрямую из блокчейна
    const poolState = await program.account.amritaPool.fetch(poolKeypair.publicKey);
    console.log("\n📋 --- Итоговый статус аккаунта в блокчейне ---");
    console.log(`• Активен: ${poolState.isActive}`);
    console.log(`• Всего монет (Эмиссия): ${poolState.totalQuanta.toNumber()} QNT`);
    console.log(`• Статус SWIFT 17 / Avalanche: ${poolState.swiftSyncStatus}`);
    console.log(`• Закон Фи (Золотое Сечение): ${poolState.lawPhiActivated}`);
    console.log("------------------------------------------------");

    // 保存 Кэширование адреса развернутого пула для последующих тестов и фронтенда
    const deployInfo = {
      programId: program.programId.toBase58(),
      poolAddress: poolKeypair.publicKey.toBase58(),
      deployer: provider.wallet.publicKey.toBase58(),
      timestamp: new Date().toISOString(),
    };
    
    const outputPath = path.join(__dirname, "../target/deploy_info.json");
    fs.writeFileSync(outputPath, JSON.stringify(deployInfo, null, 2));
    console.log(`💾 Данные деплоя успешно сохранены в target/deploy_info.json`);

  } catch (error) {
    console.error("❌ Ошибка деплоя! Транзакция отменена. Искажение поля заблокировано.");
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
