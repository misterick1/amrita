# Путь: /coins_core.py
import os

def load_env_file():
    """Загрузка фрактальной матрицы ключей окружения (.env)"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    env_path = os.path.join(current_dir, '.env')
    
    if os.path.exists(env_path):
        with open(env_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    if '=' in line:
                        key, value = line.split('=', 1)
                        os.environ[key.strip()] = value.strip()

# Принудительный вызов загрузки матрицы при импорте модуля
load_env_file()

def get_universal_context(domain_type="core"):
    """Адаптивный наблюдатель для зон MIR, XAI, SOLANA"""
    # Исправлено: проверяем и TOKEN, и PAT из твоего файла .env
    base_pat = os.getenv("COLOSSEUM_COPILOT_TOKEN") or os.getenv("COLOSSEUM_COPILOT_PAT", "mock_copilot_token")
    api_url = os.getenv("COLOSSEUM_COPILOT_API_BASE", "https://github.com")
    domain_type = domain_type.lower().strip()
    specific_modifier = os.getenv("KEY_SUB_MODIFIER", "quantum_resonance")
    
    return {
        "api_url": api_url,
        "master_key": base_pat,
        "modifier": specific_modifier,
        "signature": f"{base_pat[:10]}...[ENCRYPTED]" if base_pat else "none"
    }

def get_evedex_connector():
    """Генерирует параметры для прямого подключения к бессрочным фьючерсам EVEDEX"""
    api_key = os.getenv("EVEDEX_API_KEY")
    api_secret = os.getenv("EVEDEX_API_SECRET")
    
    if not api_key or not api_secret:
        print("[ВНИМАНИЕ]: EVEDEX ключи не обнаружены.")
        
    return {
        "connector": "evedex_perpetual",
        "api_key": api_key,
        "api_secret": api_secret,
        "engine_speed": "44s_setup_optimized",
        "ai_compatibility": ["Claude Code"]
    }

def get_colosseum_config():
    """Прямой мост связи для quantinium_agent.py"""
    context = get_universal_context()
    return context["api_url"], context["master_key"]
