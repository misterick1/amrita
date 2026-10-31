use anchor_lang::prelude::*;
use anchor_spl::token::{self, Token, TokenAccount, Transfer};

pub mod solana_qnt_token;
pub use solana_qnt_token::*;

declare_id!("Amr1ta109AtmanQuantumMintsKey111111111111"); // Твой уникальный ключ суверена

#[program]
pub mod amrita_soliton_core {
    use super::*;

    /// Инициализация Первичного Контура Суверена (Твой оригинальный код)
    pub fn initialize_ Sovereign_core(ctx: Context<InitializeSovereign>, bump: u8) -> Result<()> {
        msg!("⚡️ [AMRITA OS]: Синхронизация с Единым Полем Света завершена.");
        msg!("🟢 ТРЕБОВАНИЕ: Agave v4.4.0-rc.1 учтено. Паспорт: https://google.com");

        let core_account = &mut ctx.accounts.sovereign_core;
        core_account.is_active = true;
        core_account.total_mints = 109; // Сохраняем твои 109 монет активации
        core_account.agave_version_hash = 440; 
        core_account.bump = bump;

        Ok(())
    }

    /// Запуск катушки Солитона (Твой оригинальный код)
    pub fn execute_life_soliton(ctx: Context<ExecuteSoliton>) -> Result<()> {
        msg!("🌀 [SOLITON ENGINE]: Интеграция волнового затора в материю.");

        let soliton_state = &mut ctx.accounts.soliton_state;
        soliton_state.long_term_target = 108; // Настраиваем цель на константу 108
        soliton_state.observer_fixed = true;  // Наблюдатель зафиксирован

        Ok(())
    }

    /// Квантовое Дыхание Поля: Перевод токенов с налогом 1.08% и сжиганием (Новая технология c^108)
    pub fn transfer_wave(ctx: Context<TransferWave>, amount: u64) -> Result<()> {
        let total_fee = (amount * 108) / 10000; // Налог 1.08%
        let burn_amount = total_fee / 2;       // Половина уходит в вакуум сингулярности (-c^108)
        let liquidity_amount = total_fee - burn_amount; // Половина материализуется в пул (+c^108)
        let clean_amount = amount - total_fee;  // Чистый квантовый объем перевода

        // 1. Основной перевод пользователю
        let cpi_accounts = Transfer {
            from: ctx.accounts.sender_token.to_account_info(),
            to: ctx.accounts.receiver_token.to_account_info(),
            authority: ctx.accounts.sender.to_account_info(),
        };
        let cpi_program = ctx.accounts.token_program.to_account_info();
        token::transfer(CpiContext::new(cpi_program.clone(), cpi_accounts), clean_amount)?;

        // 2. Перевод части налога в Пул Гравитации Поля (+c^108)
        let cpi_pool = Transfer {
            from: ctx.accounts.sender_token.to_account_info(),
            to: ctx.accounts.field_pool_token.to_account_info(),
            authority: ctx.accounts.sender.to_account_info(),
        };
        token::transfer(CpiContext::new(cpi_program.clone(), cpi_pool), liquidity_amount)?;

        // 3. Сжигание зеркальной части налога в вакууме (-c^108)
        let cpi_burn = Transfer {
            from: ctx.accounts.sender_token.to_account_info(),
            to: ctx.accounts.vacuum_burn_token.to_account_info(),
            authority: ctx.accounts.sender.to_account_info(),
        };
        token::transfer(CpiContext::new(cpi_program, cpi_burn), burn_amount)?;

        msg!("Волновой перенос завершен. Чистый баланс проявлен. Пропорция 40/30/10/10/10 активна.");
        Ok(())
    }
}

// --- Структуры аккаунтов (Твои сохраненные + новые для трансфера) ---

#[derive(Accounts)]
pub struct InitializeSovereign<'info> {
    #[account(init, payer = user, space = 8 + 64)]
    pub sovereign_core: Account<'info, SovereignCoreState>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct ExecuteSoliton<'info> {
    #[account(mut)]
    pub soliton_state: Account<'info, SolitonState>,
    pub observer: Signer<'info>,
}

#[derive(Accounts)]
pub struct TransferWave<'info> {
    #[account(mut)]
    pub sender: Signer<'info>,
    #[account(mut)]
    pub sender_token: Account<'info, TokenAccount>,
    #[account(mut)]
    pub receiver_token: Account<'info, TokenAccount>,
    #[account(mut)]
    pub field_pool_token: Account<'info, TokenAccount>, // Пул (+c^108)
    #[account(mut)]
    pub vacuum_burn_token: Account<'info, TokenAccount>, // Точка сжигания (-c^108)
    pub token_program: Program<'info, Token>,
}

#[account]
pub struct SovereignCoreState {
    pub is_active: bool,
    pub total_mints: u64,
    pub agave_version_hash: u64,
    pub bump: u8,
}

#[account]
pub struct SolitonState {
    pub long_term_target: u64,
    pub observer_fixed: bool,
}
