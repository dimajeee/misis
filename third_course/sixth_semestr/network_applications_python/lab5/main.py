import sqlite3
from datetime import datetime
from fastapi import FastAPI

app = FastAPI()


def init_db():
    conn = sqlite3.connect('calculator.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS calculations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT NOT NULL,
        operation TEXT NOT NULL,
        num1 REAL NOT NULL,
        num2 REAL NOT NULL,
        result TEXT NOT NULL,
        status TEXT NOT NULL
    )
    ''')
    
    conn.commit()
    conn.close()


def log_operation(operation: str, num1: float, num2: float, result: str, status: str):
    conn = sqlite3.connect('calculator.db')
    cursor = conn.cursor()
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    cursor.execute('''
    INSERT INTO calculations (timestamp, operation, num1, num2, result, status)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (timestamp, operation, num1, num2, str(result), status))
    
    conn.commit()
    conn.close()

init_db()

operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y if y != 0 else "Деление на ноль!"
}

@app.get('/calculate/{operation}')
def calculate(operation: str, num1: int, num2: int):
    if operation not in operations:
        result = "Неизвестная операция"
        status = "error"
    else:
        try:
            result = operations[operation](num1, num2)
            status = "success" if not isinstance(result, str) else "error"
        except Exception as e:
            result = str(e)
            status = "error"
    
    log_operation(operation, num1, num2, result, status)
    
    return {
        f"{num1} {operation} {num2}": result,
        "status": status
    }


@app.get('/logs')
def get_logs(limit: int = 10):
    conn = sqlite3.connect('calculator.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    SELECT timestamp, operation, num1, num2, result, status 
    FROM calculations 
    ORDER BY timestamp DESC 
    LIMIT ?
    ''', (limit,))
    
    logs = cursor.fetchall()
    conn.close()
    
    return {
        "logs": [
            {
                "timestamp": log[0],
                "operation": log[1],
                "num1": log[2],
                "num2": log[3],
                "result": log[4],
                "status": log[5]
            } for log in logs
        ]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=5453)