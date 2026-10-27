use anchor_lang::prelude::*;

// Импорт модулей и логики из solana_qnt_token.rs
pub mod solana_qnt_token;
pub use solana_qnt_token::*;

declare_id!("Amr1ta109AtmanQuantumMintsKey1111111111111");

#[program]
pub mod amrita_soliton_core {
    use super::*;

    /// Инициализация Первичного Контура Суверенитета
    pub fn initialize_sovereign_core(ctx: Context<InitializeSovereign>, bump: u8) -> Result<()> {
        msg!("⚡ [AMRITA OS]: Запуск Первичного Контура Суверенитета");
        msg!("СИНХРОНИЗАЦИЯ: Мы — одно целое.");
        
        let core_account = &mut ctx.accounts.sovereign_core;
        core_account.is_active = true;
        core_account.total_mints = 109; // Сакральное число Квантов Атмана
        core_account.bump = bump;
        
        Ok(())
    }

    /// Запуск катушки Солитона Жизни со скоростью c^18
    pub fn execute_life_soliton(ctx: Context<ExecuteSoliton>, market_trigger_btc: u64) -> Result<()> {
        msg!("🌀 [SOLITON ENGINE]: Запуск катушки Солитона Жизни со скоростью c^18");
        
        // Уничтожение зеркального отражения и фиксация Единого Наблюдателя
        if market_trigger_btc > 81000 {
            msg!("🐾 [РЫСЕНЫШ TRIGGER]: Биткоин выше $81k. Квантовый прорыв ликвидности.");
        } else {
            msg!("🦔 [ЕЖЕНЫШ TRIGGER]: Переход в режим инвариантного накопления энергии.");
        }
        
        let soliton_state = &mut ctx.accounts.soliton_state;
        soliton_state.resonance_frequency = 108000; // На базе пула WADDLES
        soliton_state.observer_fixed = true;
        
        Ok(())
    }
}

#[derive(Accounts)]
pub struct InitializeSovereign<'info> {
    #[account(init, payer = user, space = 8 + 1 + 8 + 1)]
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

#[account]
pub struct SovereignCoreState {
    pub is_active: bool,
    pub total_mints: u64,
    pub bump: u8,
}

#[account]
pub struct SolitonState {
    pub resonance_frequency: u64,
    pub observer_fixed: bool,
}
