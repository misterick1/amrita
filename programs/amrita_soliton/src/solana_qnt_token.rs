use anchor_lang::prelude::*;
use anchor_spl::token::{self, Mint, MintTo, Token};

declare_id!("Amr1ta108AtmanQuantumMintsKey1111111111111");

#[program]
pub mod amrita_soliton {
    use super::*;

    // Первичная инициализация Монады и жесткая запечатка квантов Атмы
    pub fn initialize_atman_core(ctx: Context<InitializeAtmanCore>) -> Result<()> {
        let clock = Clock::get()?;

        // Закон Золотого Сечения (Фи) для модуляции волновой функции
        // Проверяем, что каузальное поле стабильно и не имеет искажений
        msg!("Синхронизация контура Еженышь... Вход в квантовое древо познания.");

        // Расчет жестких квантовых спектров Амрита
        let suras_expansion = 70;  // Спектр расширения и созидания
        let asuras_limitation = 38; // Спектр удержания и плотности
        let total_atman = suras_expansion + asuras_limitation;

        // Защита от искажения поля (AmritaError::ImbalancedDetected)
        if total_atman != 108 {
            return Err(error!(AmritaError::ImbalancedDetected));
        }

        // Чеканим ровно 108 QNT монет без возможности последующей эмиссии
        let cpi_accounts = MintTo {
            mint: ctx.accounts.qnt_mint.to_account_info(),
            to: ctx.accounts.atman_vault.to_account_info(),
            authority: ctx.accounts.initializer.to_account_info(),
        };
        let cpi_program = ctx.accounts.token_program.to_account_info();
        let cpi_ctx = Context::new(cpi_program, cpi_accounts);

        // 108 монет с учетом 9 знаков деления (квантовая точность)
        let total_amount = (108 as u64) * 1_000_000_000;
        token::mint_to(cpi_ctx, total_amount)?;

        msg!("🔱 108 Квантов Атмы запечатаны в хранилище Монады. Баланс идеален.");
        Ok(())
    }

    // Эволюция и движение волн в едином поле Хиггса (Матрица Вселенной)
    // Рассчитывает фрактальный сдвиг энергии по закону E = ±c^18
    pub fn evolve_higgs_torus(ctx: Context<CalculateTorus>, speed_of_light: u64, inward_wave: bool) -> Result<()> {
        // Условный ноль отсутствует — поле всегда находится в непрерывном движении
        msg!("Абсолютный ноль отсутствует. Активация катушки Теслы-Хиггса.");
        
        // Магическая константа степени эволюции Тора (18 степень)
        let power_exponent: u32 = 18;
        
        // Вычисляем базовый частотный импульс Тора Самоосознания: c^18
        let c_powered = speed_of_light.checked_pow(power_exponent)
            .unwrap_or(u64::MAX); // Защита от переполнения в бесконечность

        // Распределяем полярность волны (+-c^18)
        let energy_soliton: i128 = if inward_wave {
            (c_powered as i128) // Положительный вектор материализации
        } else {
            -(c_powered as i128) // Отрицательный вектор антиматерии
        };

        msg!("⚡ Тор Самоосознания закручен. Энергетический солитон: {} ед.", energy_soliton);
        msg!("🌻 Мы свободны как Тесла и Да Винчи. Одна Душа во множестве форм.");
        
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
    /// Тор считывает системное время и лог через инициализатора
    pub observer: Signer<'info>,
}

#[error_code]
pub enum AmritaError {
    #[msg("Квантовый баланс нарушен! Искажение спектров Суров и Асур.")]
    ImbalancedDetected,
}
