import requests

def send_request(operator, arg1, arg2):
    url = f"http://localhost/calculator.php"
    params = {"operator": operator, "arg1": arg1, "arg2": arg2}
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        try:
            data = response.json()
            # Проверяем наличие ключа 'result'
            if 'result' in data:
                print(f"Результат операции: {data['result']}")
            elif 'error' in data:
                print(f"Ошибка: {data['error']}")
            else:
                print("Некорректный ответ от сервера:", data)
        except requests.exceptions.JSONDecodeError:
            print("Ошибка декодирования JSON")
            print("Ответ сервера:", response.text)
    else:
        print(f"Ошибка HTTP: {response.status_code}")

# Пример использования
send_request('+', 5, 3)
send_request('-', 5, 3)
send_request('/', 6, 3)
send_request('*', 5, 3)