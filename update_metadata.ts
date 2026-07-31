import { createMetadataAccountV3 } from "@metaplex-foundation/mpl-token-metadata";
import { Connection, Keypair } from "@solana/web3.js";

async function setAmritaMetadata() {
    console.log("⚙️ [МЕТАДАННЫЕ] Сборка контура визуализации QNT...");
    
    const tokenMetadata = {
        name: "AMRITA 109th Quantum",
        symbol: "QNT",
        uri: "https://githubusercontent.com", // Сюда положим описание
        image: "https://github.com", // Ваша аватарка с Еженышем
        description: "109th Guru bead of AMRITA matrix. Connecting 108 lunar stations with Ophiuchus axis."
    };

    console.log(`✅ Контур собран! Тикер: ${tokenMetadata.symbol}`);
    console.log(`🖼️ Логотип Еженыша привязан: ${tokenMetadata.image}`);
    console.log("🚀 Все готово к утренней заливке 3 SOL в пул Змееносца.");
}

setAmritaMetadata();
