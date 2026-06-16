use anchor_lang::prelude::*;
use anchor_spl::token::{self, Mint, TokenAccount, Transfer};

declare_id!("QNT1111111111111111111111111111111111111116");

#[program]
pub mod quantum_neuro_token {
    use super::*;

    // Инициализация Квантового Генезиса (108 монет)
    pub fn initialize_genesis(ctx: Context<InitializeGenesis>) -> Result<()> {
        let state = &mut ctx.accounts.quantum_state;
        state.total_supply = 108;
        state.author_allocation = 70;
        state.colosseum_allocation = 38;
        state.colosseum_distributed = 0;
        state.authority = ctx.accounts.author.key();
        
        msg!("Квантовая матрица инициализирована. Всего: 108 монет. 38 заблокировано под Колизей.");
        Ok(())
    }

    // Выдача гранта из пула 38 монет для участников Хакатона Colosseum
    pub fn distribute_colosseum_grant(ctx: Context<DistributeGrant>, amount: u64, patent_hash: String) -> Result<()> {
        let state = &mut ctx.accounts.quantum_state;
        
        // Жесткая проверка ограничений
        require!(state.colosseum_distributed + amount <= state.colosseum_allocation, QuantumError::ColosseumPoolExceeded);
        
        state.colosseum_distributed += amount;
        
        msg!("Абсолютный патент {} вшит в блокчейн. Выделен грант: {} QNT", patent_hash, amount);
        Ok(())
    }
}

#[derive(Account)]
pub struct QuantumState {
    pub total_supply: u64,
    pub author_allocation: u64,
    pub colosseum_allocation: u64,
    pub colosseum_distributed: u64,
    pub authority: Pubkey,
}

#[derive(Accounts)]
pub struct InitializeGenesis<'info> {
    #[account(init, payer = author, space = 8 + 64)]
    pub quantum_state: Account<'info, QuantumState>,
    #[account(mut)]
    pub author: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct DistributeGrant<'info> {
    #[account(mut, has_one = authority)]
    pub quantum_state: Account<'info, QuantumState>,
    pub authority: Signer<'info>,
}

#[error_code]
pub enum QuantumError {
    #[msg("Превышен жесткий лимит в 38 монет, выделенный для хакатонов Colosseum.")]
    ColosseumPoolExceeded,
}
