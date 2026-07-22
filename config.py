import os

class CyberConfig:
    """Управление ключами и доступами экосистемы Amrita"""
    def __init__(self):
        # Настройки ИИ и Оракулов
        self.XAI_API_KEY = os.getenv("XAI_API_KEY", "mock_grok_key_for_test")
        self.SWARM_ORACLE = os.getenv("SWARM_ORACLE_ADDR")
        
        # Инфраструктура Solana
        self.SOLANA_RPC = os.getenv("SOLANA_RPC_URL", "https://solana.com")
        self.MINT_ADDRESS = os.getenv("MINT_ADDRESS")
        
        # Настройки связи (Логирование побед)
        self.TG_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "mock_bot_token")
        self.TG_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "mock_chat_id")
        self.DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK_URL")
        
        # Вычислительные кластеры (Сервера 1-4)
        self.SERVERS = [
            os.getenv("SERVER_1"), os.getenv("SERVER_2"), 
            os.getenv("SERVER_3"), os.getenv("SERVER_4")
        ]
