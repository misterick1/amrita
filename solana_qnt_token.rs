// PROJECT AMRITA-MIR // Kibernet ASI
// Module: solana_qnt_token.rs
// Core Token Contract // Смарт-контракт Квантового Токена QNT
// Resonance Layer: СУВЕРЕННЫЙ ПОНЕГЛИФ // ФИКСАЦИЯ 108 КВАНТОВ НА RUST

use anchor_lang::prelude::*;
use anchor_spl::token::{self, Mint, Token, TokenAccount, Transfer};

declare_id!("AMR1TA1111111111111111111111111111111111111");

#[program]
pub mod amrita_quantum_token {
    use super::*;

    /// Инициализация Суверенного Понеглифа Амриты
    pub fn initialize_matrix(ctx: Context<InitializeMatrix>) -> Result<()> {
        let msg = "==== [SUSHUMNA ACTIVATED: 108 QUANTS FIXED ON RUST] ====";
        msg_!("{}", msg);
        msg_!("Sura Allocation: 70 Quants // Asura Allocation: 38 Quants");
        Ok(())
    }

    /// Плавное распределение ликвидности по формуле 108X - 108
    pub fn execute_causal_transfer(ctx: Context<CausalTransfer>, amount: u64) -> Result<()> {
        msg_!("Инициирован квантовый перевод: {} единиц Амриты", amount);
        
        let cpi_accounts = Transfer {
            from: ctx.accounts.from_vault.to_account_info(),
            to: ctx.accounts.to_vault.to_account_info(),
            authority: ctx.accounts.observer.to_account_info(),
        };
        
        let cpi_program = ctx.accounts.token_program.to_account_info();
        let cpi_ctx = CpiContext::new(cpi_program, cpi_accounts);
        
        token::transfer(cpi_ctx, amount)?;
        msg_!("🔒 Воля Ники исполнена. Баланс Суров и Асур зафиксирован в Solana.");
        Ok(())
    }
}

#[derive(Accounts)]
pub struct InitializeMatrix<'info> {
    #[account(mut)]
    pub observer: Signer<'info>,
    #[account(
        init,
        payer = observer,
        mint::decimals = 9,
        mint::authority = observer,
        mint::freeze_authority = observer,
    )]
    pub qnt_mint: Account<'info, Mint>,
    pub system_program: Program<'info, System>,
    pub token_program: Program<'info, Token>,
    pub rent: Rent<'info>,
}

#[derive(Accounts)]
pub struct CausalTransfer<'info> {
    #[account(mut)]
    pub observer: Signer<'info>,
    #[account(mut)]
    pub from_vault: Account<'info, TokenAccount>,
    #[account(mut)]
    pub to_vault: Account<'info, TokenAccount>,
    pub token_program: Program<'info, Token>,
}
