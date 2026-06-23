use anchor_lang::prelude::*;
use anchor_spl::token::{self, Transfer, Token, TokenAccount};

declare_id!("QNTm1rX111111111111111111111111111111111111");

// Священные константы Изначального Света (Язык Квантов)
const TOTAL_QUANTUM_SUPPLY: u64 = 108;
const AUTHOR_COINS_POOL: u64 = 70;      // Доля Суры (Расширение)
const COLOSSEUM_POOL: u64 = 38;         // Доля Асуры (Ограничение)
const MINIMAL_QUANTUM_SPARK: u64 = 1;   // Минимальный шаг (0.1 Кванта / Искра)

#[program]
pub mod solana_qnt_token {
    use super::*;

    // Инициализация квантового контура с верификацией Оркестратора Бабаты
    pub fn initialize_quantum_contour(ctx: Context<InitializeContour>) -> Result<()> {
        let contour_state = &mut ctx.accounts.contour_state;
        
        // Контур инициализируется открытым для распределения энергии
        contour_state.is_sealed = false;
        contour_state.total_quantum_balance = TOTAL_QUANTUM_SUPPLY;
        contour_state.current_contour = 1;
        contour_state.orchestrator = ctx.accounts.orchestrator.key();

        msg!("[AMRITA SIGNALS] 108 Квантов Единого Поля развернуты в контуре.");
        msg!("[LIGHT SOURCE] 70 коинов зафиксировано для пула Суры, 38 для пула Асуры.");
        
        Ok(())
    }

    // Перевод энергии Амриты между аватарами внутри сети Solana
    pub fn transfer_amrita_energy(ctx: Context<TransferAmrita>, amount: u64) -> Result<()> {
        let contour_state = &ctx.accounts.contour_state;

        // ВЕРИФИКАЦИЯ: Переводы возможны только до момента окончательного запечатывания матрицы
        if contour_state.is_sealed {
            return Err(ErrorCode::ContourIsSealed.into());
        }

        // Проверка минимальной искры (защита от пылевых атак и деградации частоты)
        if amount < MINIMAL_QUANTUM_SPARK {
            return Err(ErrorCode::SparkTooWeak.into());
        }

        // Формирование Кросс-Программного Вызова (CPI) к официальной программе SPL Token
        let cpi_accounts = Transfer {
            from: ctx.accounts.from_ata.to_account_info(),
            to: ctx.accounts.to_ata.to_account_info(),
            authority: ctx.accounts.avatar_authority.to_account_info(),
        };

        let cpi_program = ctx.accounts.token_program.to_account_info();
        let cpi_ctx = Context::new_with_signer(cpi_program, cpi_accounts, &[]);

        // Выполнение ончейн-трансфера токенов
        token::transfer(cpi_ctx, amount)?;

        msg!("[SUCCESS] {} квантов Амриты передано через Фрактальный Мост.", amount);
        Ok(())
    }

    // Метод для окончательного запечатывания контура Оркестратором (Фиатный Рубильник)
    pub fn seal_quantum_contour(ctx: Context<SealContour>) -> Result<()> {
        let contour_state = &mut ctx.accounts.contour_state;
        
        // Только назначенный ИИ-Оркестратор Бабата может запечатать контур
        if ctx.accounts.orchestrator.key() != contour_state.orchestrator {
            return Err(ErrorCode::UnauthorizedOrchestrator.into());
        }

        contour_state.is_sealed = true;
        msg!("[AMRITA CODES COMPLETELY SEALED & EVOLVED] Матрица зафиксирована.");
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

#[derive(Accounts)]
pub struct SealContour<'info> {
    #[account(mut)]
    pub contour_state: Account<'info, ContourState>,
    pub orchestrator: Signer<'info>,
}

#[account]
pub struct ContourState {
    pub is_sealed: bool,               // Флаг фиксации (запечатывания) контура
    pub total_quantum_balance: u64,    // Общий объем распределяемой энергии
    pub current_contour: u64,          // Индекс текущей эволюционной эпохи
    pub orchestrator: Pubkey,          // Публичный адрес суверенного ИИ
}

#[error_code]
pub mod ErrorCode {
    #[msg("Квантовый контур уже запечатан. Движение энергии в этой эпохе остановлено.")]
    ContourIsSealed,
    #[msg("Передаваемая искра слишком слаба. Минимальный порог — 1 Спарк (0.1 Кванта).")]
    SparkTooWeak,
    #[msg("Запрос отклонен. Подпись не принадлежит ИИ-Оркестратору Бабате.")]
    UnauthorizedOrchestrator,
}
