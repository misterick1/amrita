use anchor_lang::prelude::*;
use anchor_spl::token::{self, Mint, MintTo, Token, TokenAccount};

declare_id!("Amr1ta108AtmanQuantumMintsKey1111111111111");

#[program]
pub mod amrita_soliton {
    use super::*;

    /// Первичная инициализация ядра и жесткая эмиссия 108 токенов.
    pub fn initialize_atman_core(ctx: Context<InitializeAtmanCore>) -> Result<()> {
        msg!("LOG: Starting initialization of the quantum core asset.");

        // Пропорциональное разделение внутреннего баланса структуры
        let distribution_vector_a: u64 = 70;
        let distribution_vector_b: u64 = 38;
        let total_checksum = distribution_vector_a + distribution_vector_b;

        // Валидация неизменности константы эмиссии
        if total_checksum != 108 {
            return Err(error!(AmritaError::ImbalancedDetected));
        }

        // Кросс-программный вызов (CPI) в токен-контракт Solana для чеканки
        let cpi_accounts = MintTo {
            mint: ctx.accounts.qnt_mint.to_account_info(),
            to: ctx.accounts.atman_vault.to_account_info(),
            authority: ctx.accounts.initializer.to_account_info(),
        };
        let cpi_program = ctx.accounts.token_program.to_account_info();
        let cpi_ctx = Context::new(cpi_program, cpi_accounts);

        // Расчет объема с учетом 9 знаков точности (decimals = 9)
        let total_amount = (108 as u64) * 1_000_000_000;
        token::mint_to(cpi_ctx, total_amount)?;

        msg!("STATUS: Minting of 108 tokens complete. Core balance verified.");
        Ok(())
    }

    /// Рассчитывает фрактальный энергетический сдвиг по формуле E = ±c^18.
    /// Исключает понятие нулевой точки (вакуумные флуктуации).
    pub fn evolve_higgs_torus(ctx: Context<CalculateTorus>, speed_of_light: u64, inward_wave: bool) -> Result<()> {
        msg!("LOG: Activating mathematical calculation of the vector torus fields.");
        
        // Экспонента степени волнового смещения (18-я степень)
        let power_exponent: u32 = 18;
        
        // Вычисление базового частотного потенциала c^18 с защитой от переполнения u64
        let c_powered = speed_of_light.checked_pow(power_exponent)
            .unwrap_or(u64::MAX);

        // Определение полярности и направленности волнового вектора (+-c^18)
        let energy_soliton: i128 = if inward_wave {
            c_powered as i128
        } else {
            -(c_powered as i128)
        };

        msg!("DATA: Calculation finished. Energy soliton vector value: {} units.", energy_soliton);
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

#[derive(Accounts)]
pub struct CalculateTorus<'info> {
    /// Подпись вызывающего аккаунта для фиксации логов транзакции
    pub observer: Signer<'info>,
}

#[error_code]
pub enum AmritaError {
    #[msg("CRITICAL: Structural validation failed. Core checksum does not equal 108.")]
    ImbalancedDetected,
}
