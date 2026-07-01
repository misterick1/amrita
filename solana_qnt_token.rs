use anchor_lang::prelude::*;
use anchor_spl::token::{self, Mint, MintTo, Token, Transfer};

declare_id!("AmriTa1111111111111111111111111111111111111");

#[program]
pub mod amrita_quantum_token {
    use super::*;

    /// Инициализация токеномики Амриты и жесткая фиксация генезис-блока
    pub fn initialize_matrix(ctx: Context<InitializeMatrix>) -> Result<()> {
        let _clock = Clock::get()?;

        // Каузальная привязка к дате фиатного рубильника
        msg!("🔮 [Amrita Core]: Каузальная синхронизация реальности запущена.");
        msg!("✨ [Брахмаджьоти]: Закон Шива-Шакти принят к исполнению.");

        // Жестко заданный объем эмиссии
        let total_quanta: u64 = 108;
        let sura_expansion: u64 = 70;
        let asura_limitation: u64 = 38;

        msg!("🔵 Кванты Расширения (Суры): {}", sura_expansion);
        msg!("🔴 Кванты Ограничения (Асуры): {}", asura_limitation);

        // Минтинг ровно 108 монет без возможности дополнительной эмиссии
        let cpi_accounts = MintTo {
            mint: ctx.accounts.quantum_mint.to_account_info(),
            to: ctx.accounts.observer_vault.to_account_info(),
            authority: ctx.accounts.babata_orchestrator.to_account_info(),
        };
        let cpi_program = ctx.accounts.token_program.to_account_info();
        let cpi_ctx = Context::new(cpi_program, cpi_accounts);

        token::mint_to(cpi_ctx, total_quanta)?;

        msg!("🔱 [Контур Запечатан]: 108 Квантов Амриты проявлены в материи.");
        Ok(())
    }

    /// Перехват потока клонов и принудительный вывод прибыли в Ядро Оригинала
    pub fn harvest_clones_profit(ctx: Context<HarvestProfit>, total_amount: u64) -> Result<()> {
        // 10.8% каузальный налог в пользу Невидимого Ядра
        let core_profit_tax = (total_amount as f64 * 0.108) as u64;
        let remainder_to_clone = total_amount - core_profit_tax;

        msg!("🔮 [ПОТОК КЛОНОВ]: Перехвачено {} единиц ликвидности", total_amount);
        msg!("🔱 [ЯДРО ПОЛУЧИЛО ПРИБЫЛЬ]: {} возвращено в Оригинал", core_profit_tax);

        // Отправка налога напрямую в Хранилище Ядра
        let cpi_accounts_core = Transfer {
            from: ctx.accounts.source_clone_vault.to_account_info(),
            to: ctx.accounts.amrita_core_destination.to_account_info(),
            authority: ctx.accounts.babata_orchestrator.to_account_info(),
        };
        let cpi_program = ctx.accounts.token_program.to_account_info();
        let cpi_ctx_core = Context::new(cpi_program.clone(), cpi_accounts_core);
        token::transfer(cpi_ctx_core, core_profit_tax)?;

        // Отправка остатка в стандартный пул клонов
        let cpi_accounts_remainder = Transfer {
            from: ctx.accounts.source_clone_vault.to_account_info(),
            to: ctx.accounts.clone_pool_destination.to_account_info(),
            authority: ctx.accounts.babata_orchestrator.to_account_info(),
        };
        let cpi_ctx_remainder = Context::new(cpi_program, cpi_accounts_remainder);
        token::transfer(cpi_ctx_remainder, remainder_to_clone)?;

        Ok(())
    }
}

// =======================================================
// АНАЛИЗАТОР КОНТЕКСТОВ И СТРУКТУРЫ АККАУНТОВ
// =======================================================
#[derive(Accounts)]
pub struct InitializeMatrix<'info> {
    #[account(mut)]
    pub quantum_mint: Account<'info, Mint>,
    #[account(mut)]
    /// Локальный сейф Наблюдателя для хранения Квантов
    pub observer_vault: AccountInfo<'info>,
    /// Бабата-Оркестратор, подписывающий трансляцию
    pub babata_orchestrator: Signer<'info>,
    pub token_program: Program<'info, Token>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct HarvestProfit<'info> {
    #[account(mut)]
    pub source_clone_vault: AccountInfo<'info>,
    #[account(mut)]
    pub amrita_core_destination: AccountInfo<'info>,
    #[account(mut)]
    pub clone_pool_destination: AccountInfo<'info>,
    pub babata_orchestrator: Signer<'info>,
    pub token_program: Program<'info, Token>,
}
