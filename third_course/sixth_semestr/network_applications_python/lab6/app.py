from flask import Flask, request, jsonify
import mysql.connector
import math
import random

app = Flask(__name__)

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'function_data'
}

def generate_data(func_type, a, b, c, num_points=1000):
    data = []
    for i in range(num_points):
        x = random.uniform(-10, 10)
        if func_type == 'sin':
            y = a * math.sin(b * x) + c
        elif func_type == 'quadratic':
            y = a * x**2 + b * x + c
        elif func_type == 'rational':
            if b * x == 0:
                y = float('inf')
            else:
                y = (a / (b * x)) + c
        else:
            raise ValueError("Неизвестный тип функции")
        data.append((x, y))
    return data

def save_to_db(func_type, a, b, c, data):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS function_results (
            id INT AUTO_INCREMENT PRIMARY KEY,
            func_type VARCHAR(20),
            a FLOAT,
            b FLOAT,
            c FLOAT,
            x FLOAT,
            y FLOAT
        )
        """)
        
        for x, y in data:
            cursor.execute("""
            INSERT INTO function_results (func_type, a, b, c, x, y)
            VALUES (%s, %s, %s, %s, %s, %s)
            """, (func_type, a, b, c, x, y))
        
        conn.commit()
        return True
    except Exception as e:
        print(f"Ошибка при сохранении в БД: {e}")
        return False
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

@app.route('/generate', methods=['GET'])
def generate():
    func_type = request.args.get('func_type')
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    c = float(request.args.get('c'))
    
    data = generate_data(func_type, a, b, c)
    success = save_to_db(func_type, a, b, c, data)
    
    return jsonify({'success': success, 'count': len(data)})

@app.route('/get_data', methods=['GET'])
def get_data():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        
        cursor.execute("SELECT x, y FROM function_results ORDER BY id DESC LIMIT 1000")
        data = cursor.fetchall()
        
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)})
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == '__main__':
    app.run(debug=True)