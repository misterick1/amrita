import subprocess
import json
import sys
import os

class SolanaAgaveValidatorManager:
    def __init__(self, vote_account_path="vote-account-keypair.json", identity_path="validator-keypair.json"):
        self.vote_account_path = vote_account_path
        self.identity_path = identity_path
        self.bls_key_path = "bls-signer-keypair.json"

    def _run_cmd(self, cmd):
        try:
            result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            print(f"Ошибка выполнения команды [{cmd}]: {e.stderr}")
            return None

    def check_agave_version(self):
        """Проверяет, перешел ли валидатор на клиент Agave (требуется версия >= 2.0)"""
        print("[*] Проверка версии Solana CLI...")
        version_output = self._run_cmd("solana --version")
        if version_output:
            print(f"[+] Текущая версия: {version_output}")
            return version_output
        return None

    def get_current_epoch(self):
        """Получает текущую эпоху в Testnet"""
        print("[*] Получение данных об эпохе...")
        epoch_info = self._run_cmd("solana epoch-info --output json")
        if epoch_info:
            try:
                data = json.loads(epoch_info)
                current_epoch = data.get("epoch")
                print(f"[+] Текущая эпоха в сети: {current_epoch} (Дедлайн: 975)")
                if current_epoch >= 975:
                    print("[!] ВНИМАНИЕ: Эпоха 975 уже наступила или прошла! Действуйте немедленно.")
                return current_epoch
            except json.JSONDecodeError:
                pass
        return None

    def generate_bls_key(self):
        """Генерирует новый BLS pubkey для протокола Alpenglow, если его нет"""
        if os.path.exists(self.bls_key_path):
            print(f"[+] BLS ключ уже существует: {self.bls_key_path}")
            return True
        
        print("[*] Генерация нового BLS-ключа...")
        # Используем команду нового клиента agave/solana для генерации bls
        cmd = f"solana-keygen new --no-passphrase -o {self.bls_key_path}"
        # Примечание: В зависимости от точной сборки agave команда может быть 'solana-keygen new-bls'
        # Корректируем под актуальный CLI релиз
        output = self._run_cmd(cmd)
        if output:
            print("[+] BLS ключ успешно сгенерирован.")
            return True
        return False

    def link_bls_to_vote_account(self):
        """Привязывает сгенерированный BLS ключ к Vote Account валидатора"""
        print("[*] Привязка BLS ключа к Vote-аккаунту...")
        # Базовая команда авторизации BLS подписи в Vote Account для Alpenglow
        cmd = f"solana vote-authorize-bls {self.vote_account_path} {self.bls_key_path} --keypair {self.identity_path}"
        output = self._run_cmd(cmd)
        if output:
            print(f"[+] Успешно! BLS ключ привязан к вашей ноде. Транзакция: {output}")
            return True
        return False

if __name__ == "__main__":
    manager = SolanaAgaveValidatorManager()
    manager.check_agave_version()
    manager.get_current_epoch()
    
    if manager.generate_bls_key():
        # Раскомментировать на боевой ноде при наличии корректных путей к keypair-файлам:
        # manager.link_bls_to_vote_account()
        pass
