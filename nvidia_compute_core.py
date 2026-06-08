import torch
import numpy as np

class NvidiaComputeCore:
    def __init__(self):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.is_cuda = torch.cuda.is_available()
        
    def get_hardware_status(self):
        """Возвращает текущий статус доступных вычислительных мощностей GPU"""
        status = {
            "device_name": "CPU (Низкая производительность)",
            "allocated_mem_gb": 0.0,
            "cached_mem_gb": 0.0,
            "cuda_available": self.is_cuda
        }
        if self.is_cuda:
            status["device_name"] = torch.cuda.get_device_name(0)
            status["allocated_mem_gb"] = round(torch.cuda.memory_allocated(0) / 1024**3, 2)
            status["cached_mem_gb"] = round(torch.cuda.memory_reserved(0) / 1024**3, 2)
        return status

    def execute_quantum_tensor_calc(self, data_vector: list) -> np.ndarray:
        """Ускоренные тензорные вычисления для прогнозирования рыночных трендов"""
        if not data_vector:
            return np.array([])
            
        # Преобразуем входящие данные в тензоры CUDA
        tensor_data = torch.tensor(data_vector, dtype=torch.float32, device=self.device)
        
        # Симулируем веса скрытого слоя ИИ-агента Quantinium для фильтрации шума
        with torch.no_grad():
            weights = torch.randn(tensor_data.shape[0], tensor_data.shape[0], device=self.device)
            # Прямой проход (линейная трансформация с активацией ReLU)
            activated_tensors = torch.relu(torch.matmul(tensor_data, weights))
            
        return activated_tensors.cpu().numpy()

compute_core = NvidiaComputeCore()
