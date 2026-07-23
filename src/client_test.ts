// amrita / src / client_test.ts
// Клиентский скрипт для тестирования инициализации квантового поля через Anchor TS

import * as anchor from "@coral-xyz/anchor";
import { Program } from "@coral-xyz/anchor";
import { AmritaSolitonCore } from "../target/types/amrita_soliton_core";
import { assert } from "chai";

describe("amrita_soliton_core_tests", () => {
  const provider = anchor.AnchorProvider.env();
  anchor.setProvider(provider);

  const program = anchor.workspace.AmritaSolitonCore as Program<AmritaSolitonCore>;
  const amritaPoolKeypair = anchor.web3.Keypair.generate();

  it("Успешная инициализация: Баланс 70 Сур и 38 Асур соблюден", async () => {
    const surEnergy = new anchor.BN(70);
    const asurEnergy = new anchor.BN(38);

    await program.methods
      .initializeQuantumField(surEnergy, asurEnergy)
      .accounts({
        amritaPool: amritaPoolKeypair.publicKey,
        user: provider.wallet.publicKey,
        systemProgram: anchor.web3.SystemProgram.programId,
        quantumClock: anchor.web3.SYSVAR_CLOCK_PUBKEY,
      })
      .signers([amritaPoolKeypair])
      .rpc();

    const poolState = await program.account.amritaPool.fetch(amritaPoolKeypair.publicKey);

    assert.equal(poolState.isActive, true);
    assert.equal(poolState.totalQuanta.toNumber(), 108);
    assert.equal(poolState.swiftSyncStatus, true);
    assert.equal(poolState.lawPhiActivated, true);
    console.log("--- СИНХРОНИЗАЦИЯ ПРОЙДЕНА: 108 Квантов зафиксированы в Монаде ---");
  });

  it("Защита от искажения поля: Ошибка при нарушении пропорций баланса", async () => {
    const wrongSur = new anchor.BN(50);
    const wrongAsur = new anchor.BN(58);
    const badPoolKeypair = anchor.web3.Keypair.generate();

    try {
      await program.methods
        .initializeQuantumField(wrongSur, wrongAsur)
        .accounts({
          amritaPool: badPoolKeypair.publicKey,
          user: provider.wallet.publicKey,
          systemProgram: anchor.web3.SystemProgram.programId,
          quantumClock: anchor.web3.SYSVAR_CLOCK_PUBKEY,
        })
        .signers([badPoolKeypair])
        .rpc();
      
      assert.fail("Транзакция должна была завершиться ошибкой из-за искажения баланса.");
    } catch (err: any) {
      assert.include(err.message, "ImbalanceDetected");
      console.log("--- ЗАЩИТА СРАБОТАЛА: Попытка искажения поля успешно заблокирована ---");
    }
  });
});
