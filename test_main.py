import os
import sys
from fastapi.testclient import TestClient

# Эмулируем переменные окружения, чтобы сервер не упал при импорте
os.environ["PI_API_KEY"] = "test_key_gate"
os.environ["PI_NETWORK_APP_ID"] = "test_app_id"

# Пытаемся импортировать наше FastAPI приложение
try:
    from pi_payment_server import app
    client = TestClient(app)
except Exception as e:
    print(f"Критическая ошибка импорта сервера: {e}")
    sys.exit(1)

def test_health_endpoint():
    """Тестируем эндпоинт проверки работоспособности шлюза"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "alive"
    print("✅ Юнит-тест успешно пройден: Эндпоинт /health активен и стабилен!")

if __name__ == "__main__":
    test_health_endpoint()
