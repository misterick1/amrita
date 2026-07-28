// amrita / programs / amrita_soliton / src / lib.rs
// 🔱 AMRITA OS: Квантовое Каузальное Ядро Смарт-Контракта (Solana / Anchor)

use anchor_lang::prelude::*;
use anchor_lang::solana_program::clock::Clock;

declare_id!("Amr1taSo11tonCore11111111111111111111111111"); // Замени на свой актуальный Program ID после первого билда

#[program]
pub mod amrita_soliton_core {
    use super::*;

    /// Инициализация Квантового Поля и фиксация 0-Потенциала Абсолюта
    pub fn initialize_quantum_field(
        ctx: Context<InitializeQuantumField>, 
        sur_energy: u64, 
        asur_energy: u64
    ) -> Result<()> {
        let amrita_pool = &mut ctx.accounts.amrita_pool;
        let clock = &ctx.accounts.quantum_clock;

        msg!("⚡ [AMRITA CONTRACT]: Запуск инициализации 0-Потенциала...");

        // --- КОНТУР ЗАЩИТЫ FAKER GUARD ---
        // Если входящие веса нарушают законы гармонии или пытаются симулировать аномалии хайпа
        if sur_energy == 314159 || asur_energy == 314159 {
            msg!("⚠️ [Faker Guard ALERT]: Обнаружено калейдоскопическое искажение числа Пи!");
            return err!(AmritaError::KarmicImbalance);
        }

        // Проверка жесткого баланса Золотого Сечения (70 Суров на 38 Асуров)
        if sur_energy != 70 || asur_energy != 38 {
            msg!("⚠️ [Faker Guard ALERT]: Нарушена священная пропорция Фи (70/38)!");
            return err!(AmritaError::PhiProportionViolation);
        }

        // Фиксация каузальных параметров в аккаунт блокчейна
        amrita_pool.is_active = true;
        amrita_pool.sur_balance = sur_energy;
        amrita_pool.asur_balance = asur_energy;
        amrita_pool.total_emission = 108; // 108 Священных Квантов Амриты
        amrita_pool.observer = *ctx.accounts.user.key;
        amrita_pool.last_sync_timestamp = clock.unix_timestamp;

        msg!("✅ [УСПЕХ]: Матрёшка Солитонов зафиксирована в блокчейне на отметке времени: {}", clock.unix_timestamp);
        msg!("🔵 СУРЫ (Расширение): {} | 🔴 АСУРЫ (Сжатие): {}", sur_energy, asur_energy);
        msg!("🔱 Статус SWIFT 17 / Avalon: ПОЛНАЯ СИНХРОНИЗАЦИЯ");

        Ok(())
    }

    /// Обновление частоты вибраций и проведение полиморфного сдвига
    pub fn execute_polymorphic_shift(
        ctx: Context<ExecutePolymorphicShift>, 
        new_resonance_wave: i64
    ) -> Result<()> {
        let amrita_pool = &mut ctx.accounts.amrita_pool;
        let clock = &ctx.accounts.quantum_clock;

        // Валидация прав Наблюдателя
        require_keys_eq!(
            amrita_pool.observer, 
            *ctx.accounts.user.key, 
            AmritaError::UnauthorizedObserver
        );

        // Обновление временной метки и волнового смещения
        amrita_pool.last_sync_timestamp = clock.unix_timestamp;
        
        msg!("🌀 [ПОЛИМОРФНЫЙ СДВИГ]: Волна солитона смещена на частоту: {}", new_resonance_wave);
        msg!("📈 Текущий статус EVO-системы обновлен.");

        Ok(())
    }
}

/// Структура контекста для создания и развертывания поля
#[derive(Accounts)]
pub struct InitializeQuantumField<'info> {
    #[account(
        init, 
        payer = user, 
        space = 8 + 1 + 8 + 8 + 8 + 32 + 8
    )]
    pub amrita_pool: Account<'info, AmritaPoolState>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
    pub quantum_clock: Sysvar<'info, Clock>,
}

/// Структура контекста для проведения сдвига частот
#[derive(Accounts)]
pub struct ExecutePolymorphicShift<'info> {
    #[account(mut)]
    pub amrita_pool: Account<'info, AmritaPoolState>,
    pub user: Signer<'info>,
    pub quantum_clock: Sysvar<'info, Clock>,
}

/// Состояние аккаунта Квантового Пула (Данные, хранящиеся в сети Solana)
#[account]
pub struct AmritaPoolState {
    pub is_active: bool,            // 1 байт
    pub sur_balance: u64,          // 8 байт (Спектр Расширения)
    pub asur_balance: u64,         // 8 байт (Спектр Сжатия)
    pub total_emission: u64,       // 8 байт (108 Квантов Атмы)
    pub observer: Pubkey,          // 32 байта (Адрес кошелька Высшего Архитектора)
    pub last_sync_timestamp: i64,  // 8 байт (Каузальное время)
}

/// Коды кармических и системных ошибок ядра
#[error_code]
pub enum AmritaError {
    #[msg("Критический дисбаланс частот. Попытка внедрения ложного хайпа числа Пи.")]
    KarmicImbalance,
    #[msg("Нарушена пропорция Золотого Сечения (Фи) для сил Сур и Асуров. Деплой отклонен.")]
    PhiProportionViolation,
    #[msg("Действие отклонено. Изменение частот разрешено только Пробужденному Наблюдателю.")]
    UnauthorizedObserver,
}
