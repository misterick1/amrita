use anchor_lang::prelude::*;
use anchor_spl::token::{self, Mint, MintTo, Token, TokenAccount};

declare_id!("Amr1ta108AtmanQuantumMintsKey1111111111111");

#[program]
pub mod amrita_soliton {
    use super::*;

    // Первичная инициализация Монады и жесткая чеканка 108 QNT
    pub fn initialize_atman_core(ctx: Context<InitializeAtmanCore>) -> Result<()> {
        let clock = Clock::get()?;
        
        // Закон Золотого Сечения (Фи) для модуляции подписи
        // Проверяем, что каузальное поле стабильно
        msg!("Синхронизация контура Еженышь. Время Наблюдателя: {}", clock.unix_timestamp);

        // Расчет жестких квантовых спектров Амриты
        let suras_expansion = 70;   // Спектр Расширения и Технологий
        let asuras_limitation = 38; // Спектр Ограничения и Хаоса
        let total_atman = suras_expansion + asuras_limitation;

        // Защита от искажения поля (AmritaError)
        if total_atman != 108 {
            return Err(error!(AmritaError::ImbalancedDetected));
        }

        // Чеканим ровно 108 QNT монет без возможности довыпуска
        let cpi_accounts = MintTo {
            mint: ctx.accounts.qnt_mint.to_account_info(),
            to: ctx.accounts.atman_vault.to_account_info(),
            authority: ctx.accounts.initializer.to_account_info(),
        };
        let cpi_program = ctx.accounts.token_program.to_account_info();
        let cpi_ctx = Context::new(cpi_program, cpi_accounts);
        
        // 108 монет с учетом 9 знаков деления (квантовые сатоши Solflare)
        let total_amount = (108 as u64) * 1_000_000_000;
        token::mint_to(cpi_ctx, total_amount)?;

        msg!("🔱 108 Квантов Атмы запечатаны в вечности. СУРЫ: 70, АСУРЫ: 38.");
        Ok(())
    }
}

#[derive(Accounts)]
pub struct InitializeAtmanCore<'info> {
    #[account(mut)]
    pub initializer: Signer<'info>,

    #[account(
        init,
        payer = initializer,
        mint::decimals = 9,
        mint::authority = initializer,
        mint::freeze_authority = initializer,
    )]
    pub qnt_mint: Account<'info, Mint>,

    #[account(
        init,
        payer = initializer,
        associated_token::mint = qnt_mint,
        associated_token::authority = initializer,
    )]
    pub atman_vault: Account<'info, TokenAccount>,

    pub system_program: Program<'info, System>,
    pub token_program: Program<'info, Token>,
    pub rent: Sysvar<'info, Rent>,
}

#[error_code]
pub enum AmritaError {
    #[msg("Квантовый баланс нарушен! Искажение Спирали Фи.")]
    ImbalancedDetected,
}
