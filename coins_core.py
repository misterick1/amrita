# Путь: /coins_core.py
import os

def load_env_file():
    """Загрузка фрактальной матрицы ключей"""
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
    """
    Адаптивный наблюдатель: видоизменяет отдачу ключей 
    в зависимости от контекста запроса (com, ru, mir)
    """
    # Базовый стержень системы
    base_pat = os.getenv("COLOSSEUM_COPILOT_PAT", "")
    api_url = os.getenv("COLOSSEUM_COPILOT_API_BASE", "")
    
    # Динамическая мутация ключа под конкретную «колоду»
    domain_type = domain_type.lower().strip()
    specific_modifier = os.getenv(f"KEY_SUFIX_{domain_type.upper()}", "DEFAULT_MODIFIER")
    
    # Формируем универсальный фрактальный паспорт для скрипта
    context_matrix = {
        "api_url": api_url,
        "master_key": base_pat,
        "modifier": specific_modifier,
        "signature": f"{base_pat[:10]}...[{domain_type.upper()}]"
    }
    
    return context_matrix
