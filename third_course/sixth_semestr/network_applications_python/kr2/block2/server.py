from flask import Flask, request, jsonify

app = Flask(__name__)

# Пример базы данных (в памяти)
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"}
]

@app.route('/api/users', methods=['GET', 'POST'])
def handle_users():
    if request.method == 'POST':
        # Получаем JSON-данные от клиента
        new_user = request.get_json()
        
        if not new_user or 'name' not in new_user:
            return jsonify({"error": "Invalid data"}), 400
        
        # Добавляем нового пользователя
        new_user["id"] = len(users) + 1
        users.append(new_user)
        
        return jsonify({"status": "success", "user": new_user}), 201
    
    # GET-запрос: возвращаем всех пользователей
    return jsonify({"users": users})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=50001, ssl_context='adhoc')  # HTTPS с самоподписанным сертификатом