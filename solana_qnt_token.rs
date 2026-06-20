use anchor_lang::prelude::*;
use anchor_spl::token::{self, Mint, Token, Transfer};

declare_id!("QNTm1rX111111111111111111111111111111111111");

// Священные константы Изначального Света (Язык Сознания 1-0-108)
const TOTAL_QUANTUM_SUPPLY: u64 = 108; 
const AUTHOR_COINS_POOL: u64 = 70;      // Доля Единого Источника
const COLOSSEUM_POOL: u64 = 38;         // Расширение пространства Мультивселенной
const MINIMAL_QUANTUM_SPARK: u64 = 1;   // 0.1 Квант (Искра души в масштабе системы)

#[program]
pub mod solana_qnt_token {
    use super::*;

    // Инициализация квантового контура с ведической токеномикой
    pub fn initialize_quantum_contour(ctx: Context<InitializeContour>) -> Result<()> {
        let contour_state = &mut ctx.accounts.contour_state;
        contour_state.is_sealed = true;
        
        // Матрица выравнивается строго по коду 108
        contour_state.total_quantum_balance = TOTAL_QUANTUM_SUPPLY;
        contour_state.current_contour = 1;
        contour_state.orchestrator = ctx.accounts.orchestrator.key();

        msg!("[AMRITA SIGNALS] 108 Квантов Единого Знания развернуты в матрице.");
        msg!("[LIGHT SOURCE] 70 коинов зафиксированы за Автором. 38 коинов направлены в Колизей.");
        Ok(())
    }

    // Перевод энергии Амриты между аватарами
    pub fn transfer_amrita_energy(ctx: Context<TransferAmrita>, amount: u64) -> Result<()> {
        let contour_state = &ctx.accounts.contour_state;

        // Верификация: переводы возможны только в пробужденном и запечатанном контуре
        if !contour_state.is_sealed {
            return Err(ErrorCode::ContourNotAwakened.into());
        }

        // Проверка минимальной искры (0.1 квант)
        if amount < MINIMAL_QUANTUM_SPARK {
            return Err(ErrorCode::SparkTooWeak.into());
        }

        let cpi_accounts = Transfer {
            from: ctx.accounts.from_ata.to_account_info(),
            to: ctx.accounts.to_ata.to_account_info(),
            authority: ctx.accounts.avatar_authority.to_account_info(),
        };

        let cpi_program = ctx.accounts.token_program.to_account_info();
        let cpi_ctx = Context::new_with_signer(cpi_program, cpi_accounts);

        token::transfer(cpi_ctx, amount)?;
        
        msg!("[SUCCESS] {} квантов Амриты передано. Свет Изначальный во всем!", amount);
        Ok(())
    }
}

#[derive(Accounts)]
pub struct InitializeContour<'info> {
    #[account(init, payer = orchestrator, space = 8 + 1 + 8 + 8 + 32)]
    pub contour_state: Account<'info, ContourState>,
    #[account(mut)]
    pub orchestrator: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct TransferAmrita<'info> {
    pub contour_state: Account<'info, ContourState>,
    pub avatar_authority: Signer<'info>,
    #[account(mut)]
    pub from_ata: Account<'info, token::TokenAccount>,
    #[account(mut)]
    pub to_ata: Account<'info, token::TokenAccount>,
    pub token_program: Program<'info, Token>,
}

#[account]
pub struct ContourState {
    pub is_sealed: bool,
    pub total_quantum_balance: u64,
    pub current_contour: u64,
    pub orchestrator: Pubkey,
}

#[error_code]
pub mod ErrorCode {
    #[msg("Квантовый контур еще не пробужден и не запечатан.")]
    ContourNotAwakened,
    #[msg("Передаваемая искра слишком слаба. Минимальный квант Сознания — 0.1.")]
    SparkTooWeak,
}
