# Путь: /coins_core.py
import os

def load_env_file():
    """Загрузка фрактальной матрицы ключей проекта amrita"""
    env_path = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(env_path):
        with open(env_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    os.environ[key.strip()] = value.strip().strip('"').strip("'")

load_env_file()

def get_universal_context(domain_type="com"):
    """Адаптивный наблюдатель для зон MIR, RU, COM"""
    base_pat = os.getenv("COLOSSEUM_COPILOT_PAT", "")
    api_url = os.getenv("COLOSSEUM_COPILOT_API_BASE", "")
    domain_type = domain_type.lower().strip()
    specific_modifier = os.getenv(f"KEY_SUFIX_{domain_type.upper()}", "DEFAULT_MODIFIER")
    
    return {
        "api_url": api_url,
        "master_key": base_pat,
        "modifier": specific_modifier,
        "signature": f"{base_pat[:10]}...[{domain_type.upper()}]"
    }

def get_evedex_connector():
    """
    Генерирует параметры для прямого подключения Hummingbot
    к бессрочным фьючерсам EVEDEX (поддерживает Claude Code, Codex, Gemini)
    """
    api_key = os.getenv("EVEDEX_API_KEY", "")
    api_secret = os.getenv("EVEDEX_API_SECRET", "")
    
    if not api_key or not api_secret:
        print("[ВНИМАНИЕ]: EVEDEX ключи не найдены. Агенты работают в режиме симуляции рынка (Paper Trading).")
        
    return {
        "connector": "evedex_perpetual",
        "api_key": api_key,
        "api_secret": api_secret,
        "engine_speed": "44s_setup_optimized", # Оптимизация по официальному гайду
        "ai_compatibility": ["Claude Code", "Codex", "Gemini"]
    }
