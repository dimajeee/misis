import requests

BASE_URL = "http://localhost:5000/tasks"

def print_response(response):
    """Печатает информацию о запросе и ответе"""
    print(f"URL: {response.url}")
    print(f"Status: {response.status_code}")
    print("Response:", response.json())
    print("-" * 50)

def test_api():
    # 1. Создаем несколько задач
    print("1. Создаем задачи:")
    tasks = [
        {"title": "Купить молоко", "status": "pending"},
        {"title": "Сделать ДЗ", "description": "Математика", "status": "pending"},
        {"title": "Позвонить маме", "status": "done"}
    ]
    
    created_ids = []
    for task in tasks:
        resp = requests.post(BASE_URL, json=task)
        created_ids.append(resp.json()["id"])
        print_response(resp)

    # 2. Получаем все задачи
    print("\n2. Получаем все задачи:")
    resp = requests.get(BASE_URL)
    print_response(resp)

    # 3. Тестируем фильтрацию по статусу
    print("\n3. Фильтруем задачи по статусу 'done':")
    resp = requests.get(BASE_URL, params={"status": "done"})
    print_response(resp)

    # 4. Получаем статистику
    print("\n4. Получаем статистику по задачам:")
    resp = requests.get(f"{BASE_URL}/stats")
    print_response(resp)

    # 5. Обновляем задачу
    print("\n5. Обновляем первую задачу:")
    update_data = {
        "title": "Купить органическое молоко",
        "description": "В магазине на углу",
        "status": "done"
    }
    resp = requests.put(f"{BASE_URL}/{created_ids[0]}", json=update_data)
    print_response(resp)

    # 6. Проверяем обновление
    print("\n6. Проверяем обновленную задачу:")
    resp = requests.get(f"{BASE_URL}/{created_ids[0]}")
    print_response(resp)

    # 7. Удаляем задачу
    print("\n7. Удаляем вторую задачу:")
    resp = requests.delete(f"{BASE_URL}/{created_ids[1]}")
    print_response(resp)

    # 8. Проверяем список после удаления
    print("\n8. Проверяем список задач после удаления:")
    resp = requests.get(BASE_URL)
    print_response(resp)

    # 9. Проверяем обработку ошибок
    print("\n9. Тестируем обработку ошибок:")
    
    # Несуществующий ID
    print("a) Запрос несуществующей задачи:")
    resp = requests.get(f"{BASE_URL}/9999")
    print(f"Status: {resp.status_code}")
    print("Response:", resp.json())
    
    # Некорректный статус
    print("\nb) Некорректный статус:")
    resp = requests.put(f"{BASE_URL}/{created_ids[0]}", json={"status": "invalid"})
    print(f"Status: {resp.status_code}")
    print("Response:", resp.json())
    
    # Пустой title
    print("\nc) Пустой title:")
    resp = requests.post(BASE_URL, json={"title": ""})
    print(f"Status: {resp.status_code}")
    print("Response:", resp.json())

if __name__ == "__main__":
    test_api()