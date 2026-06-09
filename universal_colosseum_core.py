from coins_core import get_universal_context

# Наблюдатель активирует контекст для международной зоны com
matrix = get_universal_context(domain_type="com")

COPILOT_TOKEN = matrix["master_key"]
API_BASE = matrix["api_url"]
# Далее идет ваш стандартный код бота...
