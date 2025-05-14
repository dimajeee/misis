from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Создаем БД
def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                      (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')
    conn.commit()
    conn.close()

init_db()

# Create
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", 
                   (data['name'], data['email']))
    conn.commit()
    conn.close()
    return jsonify({"status": "user created"}), 201

# Read (All)
@app.route('/users', methods=['GET'])
def get_users():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    return jsonify({"users": users})

# Update
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET name=?, email=? WHERE id=?", 
                   (data['name'], data['email'], user_id))
    conn.commit()
    conn.close()
    return jsonify({"status": "user updated"})

# Delete
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id=?", (user_id,))
    conn.commit()
    conn.close()
    return jsonify({"status": "user deleted"})

if __name__ == '__main__':
    app.run(debug=True)