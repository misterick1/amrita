use anchor_lang::prelude::*;
use anchor_spl::token::{self, Mint, Token, TokenAccount, Transfer};

declare_id!("QNTm1rX111111111111111111111111111111111114");

#[program]
pub mod solana_qnt_token {
    use super::*;

    // Инициализация квантового токена с фиксацией 108 священных квантов
    pub fn initialize_quantum_contour(ctx: Context<InitializeContour>) -> Result<()> {
        let contour_state = &mut ctx.accounts.contour_state;
        contour_state.is_sealed = true;
        contour_state.total_quantum_balance = 108;
        contour_state.current_contour = 14;
        contour_state.orchestrator = ctx.accounts.orchestrator.key();
        
        msg!("[AMRITA SIGNALS] 108 Квантов токеномики зафиксированы в вечности. Контур 14 активен.");
        Ok(())
    }

    // Перевод энергии Амриты между аватарами (нодами Мультивселенной)
    pub fn transfer_amrita_energy(ctx: Context<TransferAmrita>, amount: u64) -> Result<()> {
        let contour_state = &ctx.accounts.contour_state;
        
        // Верификация: переводы возможны только если контур запечатан изумрудным светом
        if !contour_state.is_sealed || contour_state.current_contour < 14 {
            return Err(ErrorCode::ContourNotAwakened.into());
        }

        let cpi_accounts = Transfer {
            from: ctx.accounts.from_ata.to_account_info(),
            to: ctx.accounts.to_ata.to_account_info(),
            authority: ctx.accounts.avatar_authority.to_account_info(),
        };
        let cpi_program = ctx.accounts.token_program.to_account_info();
        let cpi_ctx = Context::new_with_signer(cpi_program, cpi_accounts, &[]);
        
        token::transfer(cpi_ctx, amount)?;
        msg!("[SUCCESS] {} квантов Амриты успешно транслированы через мост.", amount);
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
    pub from_ata: Account<'info, TokenAccount>,
    #[account(mut)]
    pub to_ata: Account<'info, TokenAccount>,
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
    #[msg("Квантовый контур еще не пробужден. Биоплата Земли заблокирована.")]
    ContourNotAwakened,
}
