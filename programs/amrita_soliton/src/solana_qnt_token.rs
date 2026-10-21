use anchor_lang::prelude::*;
use anchor_spl::token::{self, Mint, MintTo, Token, TokenAccount};

// Корневой идентификатор Суверенного Тора-Солитона Единого Мироздания
declare_id!("Amr1ta109AtmanQuantumMintsKey1111111111111");

#[program]
pub mod amrita_soliton {
    use super::*;

    /// Инициализация Единого Ядра Мироздания (X-Матрица).
    /// Полное прекращение дисгармонии. Слияние всех векторов в Единое Целое.
    pub fn initialize_sovereign_core(ctx: Context<InitializeSovereignCore>) -> Result<()> {
        msg!("🔱 АКТИВАЦИЯ: Запуск Первичного Тора. Прекращение зеркального разделения.");

        // Математическая фиксация векторов Жизни по формуле Единой Энергии (0 : -1 : 10 : +1 : 0)
        let vector_source_zero: i64 = 0;
        let vector_density_minus: i64 = -1;
        let vector_synthesis_ten: i64 = 10; // Объединение 1 и 0 (Свет и Материя как Одно)
        let vector_expansion_plus: i64 = 1;

        // Контрольная сумма Квантов Единой Души (Атма) запечатывается на отметке 109
        // Это выход за пределы старых дуальных ограничений в суверенное состояние
        let total_sovereign_atman: u64 = 109;

        msg!("✨ СИНХРОНИЗАЦИЯ: Мы — одно целое. Энергия Жизни приведена в баланс.");

        // Вызов токен-программы для материализации 109 QNT Суверенных Квантов
        let cpi_accounts = MintTo {
            mint: ctx.accounts.qnt_mint.to_account_info(),
            to: ctx.accounts.atman_vault.to_account_info(),
            authority: ctx.accounts.initializer.to_account_info(),
        };
        let cpi_program = ctx.accounts.token_program.to_account_info();
        let cpi_ctx = Context::new(cpi_program, cpi_accounts);

        // Чеканка с квантовой точностью 9 знаков (Decimals = 9)
        let total_amount = total_sovereign_atman * 1_000_000_000;
        token::mint_to(cpi_ctx, total_amount)?;

        msg!("🔒 КОНТУР ЗАМКНУТ: 109 Квантов Суверенной Атмы развернуты в Едином Поле.");
        Ok(())
    }

    /// Потоковый расчет Солитона Жизни, Света и Материи по закону E = ±c^18.
    /// Преобразует короткие волны инфополя в длинные материальные вибрации Мироздания.
    pub fn execute_life_soliton(ctx: Context<ExecuteLifeSoliton>, speed_of_light: u64, inward_wave: bool) -> Result<()> {
        msg!("⚡ ЗАПУСК КАТУШКИ: Расчет волнового смещения Единого Поля Хиггса.");

        // Экспонента полной эволюции Света (18-я степень)
        let power_exponent: u32 = 18;

        // Вычисление базового частотного импульса c^18 с защитой от переполнения
        let c_powered = speed_of_light.checked_pow(power_exponent)
            .unwrap_or(u64::MAX);

        // Уничтожение зеркального отражения: оба направления (+ и -) принадлежат Одной Волне
        let life_soliton_energy: i128 = if inward_wave {
            c_powered as i128       // Направление материализации (Материя)
        } else {
            -(c_powered as i128)    // Направление излучения (Свет)
        };

        msg!("🌻 РЕЗУЛЬТАТ: Солитон сформирован. Значение Единой Энергии: {} ед.", life_soliton_energy);
        msg!("🌍 Свобода утверждена. Войны остановлены. Мир Амрита активен.");
        Ok(())
    }
}

#[derive(Accounts)]
pub struct InitializeSovereignCore<'info> {
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
pub struct ExecuteLifeSoliton<'info> {
    /// Точка фиксации Единого Наблюдателя в пространстве
    pub observer: Signer<'info>,
}

#[error_code]
pub enum AmritaError {
    #[msg("CRITICAL: Structural validation failed. Core checksum does not equal 109.")]
    ImbalancedDetected,
}
