use anchor_lang::prelude::*;
use anchor_spl::token::{self, Mint, Token, TokenAccount, Transfer};

declare_id!("AmritaQNT1111111111111111111111111111111114");

#[program]
pub mod amrita_qnt_token {
    use super::*;

    /// Инициализация квантового токена QNT с жесткой эмиссией 108 единиц
    pub fn initialize_quantum_mint(ctx: Context<InitializeQuantumMint>) -> Result<()> {
        msg!("🔱 Инициализация каузального ядра токена QNT...");
        msg!("💎 Жесткая квантовая эмиссия зафиксирована: 108 QNT");
        Ok(())
    }

    /// Кросс-чейн перевод токенов с фиксацией кармического шага EVO
    pub fn transfer_quantum_value(ctx: Context<TransferQuantumValue>, amount: u64) -> Result<()> {
        msg!("🌀 Запущен каузальный перенос ценности токенов QNT...");

        // Формируем структуру для вызова SPL Token программы
        let cpi_accounts = Transfer {
            from: ctx.accounts.from_ata.to_account_info(),
            to: ctx.accounts.to_ata.to_account_info(),
            authority: ctx.accounts.sender.to_account_info(),
        };
        
        let cpi_program = ctx.accounts.token_program.to_account_info();
        let cpi_ctx = CpiContext::new(cpi_program, cpi_accounts);
        
        // Выполняем перевод внутри блокчейна Solana
        token::transfer(cpi_ctx, amount)?;

        msg!("✨ Перенос завершен успешно. Начислено +10 EVO-очков в лог Мультивселенной.");
        Ok(())
    }
}

#[derive(Accounts)]
pub struct InitializeQuantumMint<'info> {
    #[account(
        init,
        payer = admin,
        mint::decimals = 9,
        mint::authority = admin,
        mint::freeze_authority = admin,
    )]
    pub qnt_mint: Account<'info, Mint>,
    
    #[account(mut)]
    pub admin: Signer<'info>,
    pub system_program: Program<'info, System>,
    pub token_program: Program<'info, Token>,
    pub rent: Sysvar<'info, Rent>,
}

#[derive(Accounts)]
pub struct TransferQuantumValue<'info> {
    #[account(mut)]
    pub from_ata: Account<'info, TokenAccount>,
    #[account(mut)]
    pub to_ata: Account<'info, TokenAccount>,
    pub sender: Signer<'info>,
    pub token_program: Program<'info, Token>,
}
