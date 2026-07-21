import subprocess
import json
import re

class SolanaNodeController:
    def __init__(self, min_agave="4.2.0", min_firedancer="0.1102.40201"):
        self.min_agave = min_agave
        self.min_firedancer = min_firedancer

    def get_epoch_info(self):
        """Получает текущую эпоху через Solana CLI"""
        try:
            result = subprocess.run(["solana", "epoch-info", "--output", "json"], capture_output=True, text=True)
            return json.loads(result.stdout)
        except Exception as e:
            return {"error": f"Failed to get epoch: {str(e)}"}

    def check_node_version(self):
        """Проверяет запущенный клиент ноды"""
        try:
            # Проверяем стандартный софт (Agave/Solana)
            ver_output = subprocess.run(["solana", "--version"], capture_output=True, text=True).stdout
            current_version = re.search(r"solana-cli\s+([\d\.]+)", ver_output)
            
            if current_version:
                return {"client": "agave", "version": current_version.group(1)}
            return {"client": "unknown", "version": "0.0.0"}
        except FileNotFoundError:
            return {"error": "Solana CLI not installed"}

    def analyze_stake_risk(self, target_epoch=994):
        """Каузальный анализ AMRITA: риск потери делегирования"""
        epoch_data = self.get_epoch_info()
        node_data = self.check_node_version()
        
        if "error" in epoch_data or "error" in node_data:
            return "CRITICAL: Infrastructure check failed."

        current_epoch = epoch_data.get("epoch")
        remaining_slots = epoch_data.get("slotsInEpoch") - epoch_data.get("slotIndex")
        
        # Логика принятия решений Еженыша
        if current_epoch >= target_epoch - 2:  # За 2 эпохи до дедлайна
            if node_data["client"] == "agave" and node_data["version"] < self.min_agave:
                return f"ALERT: Low software version ({node_data['version']}). Risk of losing Solana Foundation stake at epoch {target_epoch}!"
        
        return "STATUS: Node is healthy and compliant."
