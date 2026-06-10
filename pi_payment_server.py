import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# ТВОИ НАСТРОЙКИ ИЗ ПАНЕЛИ РАЗРАБОТЧИКА PI
# Ключ API нужно сгенерировать в кабинете Pi Develop
PI_API_KEY = "ТВОЙ_API_КЛЮЧ_ИЗ_КАБИНЕТА_PI" 
PI_API_URL = "https://minepi.com"

headers = {
    "Authorization": f"Key {PI_API_KEY}"
}

# 1. МАРШРУТ ДЛЯ ОДОБРЕНИЯ ПЛАТЕЖА СЕРВЕРОМ (Approve)
@app.route('/approve-payment', methods=['POST'])
def approve_payment():
    payment_id = request.json.get("paymentId")
    if not payment_id:
        return jsonify({"error": "Missing paymentId"}), 400

    print(f"[СЕРВЕР] Одобрение платежа в блокчейне Pi: {payment_id}")
    
    # Отправляем официальный сигнал одобрения на сервера Pi Network
    response = requests.post(
        f"{PI_API_URL}/payments/{payment_id}/approve", 
        headers=headers
    )
    
    if response.status_code == 200:
        return jsonify({"status": "approved"}), 200
    else:
        return jsonify({"error": response.text}), response.status_code

# 2. МАРШРУТ ДЛЯ ЗАВЕРШЕНИЯ ПЛАТЕЖА СЕРВЕРОМ (Complete)
@app.route('/complete-payment', methods=['POST'])
def complete_payment():
    payment_id = request.json.get("paymentId")
    txid = request.json.get("txid") # Хэш транзакции из блокчейна
    
    if not payment_id or not txid:
        return jsonify({"error": "Missing data"}), 400

    print(f"[СЕРВЕР] Фиксация завершения платежа {payment_id} с TXID: {txid}")
    
    # Отправляем финальный сигнал завершения в Pi Network
    response = requests.post(
        f"{PI_API_URL}/payments/{payment_id}/complete", 
        json={"txid": txid}, 
        headers=headers
    )
    
    if response.status_code == 200:
        return jsonify({"status": "completed"}), 200
    else:
        return jsonify({"error": response.text}), response.status_code

if __name__ == '__main__':
    # Запуск сервера на порту 5000 (или другом порту твоего хостинга)
    app.run(host='0.0.0.0', port=5000)
