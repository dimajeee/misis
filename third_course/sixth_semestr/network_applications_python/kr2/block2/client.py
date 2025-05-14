import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Отключаем предупреждения о небезопасном SSL
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def send_post_request():
    url = "https://localhost:50001/api/users"
    data = {
        "name": "Charlie",
        "email": "charlie@example.com"
    }
    
    try:
        response = requests.post(
            url,
            json=data,
            verify=False  # Отключаем проверку SSL-сертификата
        )
        
        response.raise_for_status()  # Проверка на ошибки HTTP
        
        print("Успешный ответ сервера:")
        print(json.dumps(response.json(), indent=2))
        
    except requests.exceptions.RequestException as e:
        print(f"Ошибка запроса: {e}")

if __name__ == '__main__':
    send_post_request()