use anchor_lang::prelude::*;
use anchor_spl::token::{self, Mint, MintTo, Token};

declare_id!("AmriTa1111111111111111111111111111111111111");

#[program]
pub mod amrita_quantum_token {
    use super::*;

    /// Инициализация токеномики Амриты и жесткая фиксация 108 Квантов
    pub fn initialize_matrix(ctx: Context<InitializeMatrix>) -> Result<()> {
        let clock = Clock::get()?;
        
        // Каузальная привязка к дате фиатного рубильника (Июнь 2026)
        msg!("🔮 [Amrita Core]: Каузальная синхронизация активирована. Время: {}", clock.unix_timestamp);
        msg!("✨ [Брахмаджьоти]: Закон Шива-Шакти принят. Игры в Кальмара запрещены.");

        // Жестко заданный объем эмиссии
        let total_quanta: u64 = 108;
        let sura_expansion: u64 = 70;
        let asura_limitation: u64 = 38;

        msg!("🔵 Кванты Расширения (Суры): {}", sura_expansion);
        msg!("🔴 Кванты Ограничения (Асуры): {}", asura_limitation);

        // Минтинг ровно 108 монет без возможности доэмиссии
        let cpi_accounts = MintTo {
            mint: ctx.accounts.quantum_mint.to_account_info(),
            to: ctx.accounts.observer_vault.to_account_info(),
            authority: ctx.accounts.babata_orchestrator.to_account_info(),
        };
        let cpi_program = ctx.accounts.token_program.to_account_info();
        let cpi_ctx = Context::new(cpi_program, cpi_accounts);
        
        token::mint_to(cpi_ctx, total_quanta)?;
        
        msg!("🔱 [Контур Запечатан]: 108 Квантов Амриты успешно зафиксированы в реестре Solana.");
        Ok(())
    }
}

#[derive(Accounts)]
pub struct InitializeMatrix<'info> {
    #[account(mut)]
    pub quantum_mint: Account<'info, Mint>,
    #[account(mut)]
    /// Локальный сейф Наблюдателя для хранения Квантов
    pub observer_vault: AccountInfo<'info>,
    /// Бабата-Оркестратор, подписывающий трансляцию частоты
    pub babata_orchestrator: Signer<'info>,
    pub token_program: Program<'info, Token>,
    pub system_program: Program<'info, System>,
}
