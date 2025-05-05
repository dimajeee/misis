import requests
import pytest
from datetime import datetime

BASE_URL = 'http://localhost:5000'

@pytest.fixture
def test_task():
    # Создаем тестовую задачу и возвращаем её ID
    response = requests.post(
        f'{BASE_URL}/tasks',
        json={'title': 'Test task', 'description': 'Test description'}
    )
    yield response.json()['id']
    # После теста удаляем задачу
    requests.delete(f'{BASE_URL}/tasks/{response.json()["id"]}')

def test_crud_operations(test_task):
    task_id = test_task
    
    # Проверка создания (фикстура уже создала задачу)
    get_response = requests.get(f'{BASE_URL}/tasks/{task_id}')
    assert get_response.status_code == 200
    assert get_response.json()['title'] == 'Test task'

    # Обновление задачи
    updated_data = {
        'title': 'Updated title',
        'status': 'done',
        'description': 'Updated description'
    }
    update_response = requests.put(f'{BASE_URL}/tasks/{task_id}', json=updated_data)
    assert update_response.status_code == 200
    updated_task = update_response.json()
    assert updated_task['title'] == 'Updated title'
    assert updated_task['status'] == 'done'

def test_search_functionality():
    # Создаем задачу для поиска
    test_task = requests.post(
        f'{BASE_URL}/tasks',
        json={'title': 'УникальнаяЗадачаДляПоиска123'}
    ).json()

    try:
        # Тестируем поиск
        search_response = requests.get(f'{BASE_URL}/tasks/search?q=уник')
        assert search_response.status_code == 200
        results = search_response.json()
        assert any(task['id'] == test_task['id'] for task in results)
        
        # Поиск через основной эндпоинт
        search_main = requests.get(f'{BASE_URL}/tasks?q=Задач')
        assert search_main.status_code == 200
        assert len(search_main.json()) > 0
    finally:
        # Удаляем тестовую задачу
        requests.delete(f'{BASE_URL}/tasks/{test_task["id"]}')

def test_sort_functionality():
    # Создаем две задачи с разными временами
    task1 = requests.post(f'{BASE_URL}/tasks', json={'title': 'Task 1'}).json()
    task2 = requests.post(f'{BASE_URL}/tasks', json={'title': 'Task 2'}).json()

    try:
        # Тестируем сортировку по возрастанию
        sort_asc = requests.get(f'{BASE_URL}/tasks?sort=created_at')
        assert sort_asc.status_code == 200
        tasks_asc = sort_asc.json()
        if len(tasks_asc) > 1:
            assert datetime.fromisoformat(tasks_asc[0]['created_at']) <= datetime.fromisoformat(tasks_asc[1]['created_at'])

        # Тестируем сортировку по убыванию
        sort_desc = requests.get(f'{BASE_URL}/tasks?sort=-created_at')
        assert sort_desc.status_code == 200
        tasks_desc = sort_desc.json()
        if len(tasks_desc) > 1:
            assert datetime.fromisoformat(tasks_desc[0]['created_at']) >= datetime.fromisoformat(tasks_desc[1]['created_at'])
    finally:
        # Удаляем тестовые задачи
        requests.delete(f'{BASE_URL}/tasks/{task1["id"]}')
        requests.delete(f'{BASE_URL}/tasks/{task2["id"]}')

def test_task_stats():
    # Создаем задачу с известным статусом
    test_task = requests.post(
        f'{BASE_URL}/tasks',
        json={'title': 'Stats test', 'status': 'done'}
    ).json()

    try:
        # Проверяем статистику
        stats_response = requests.get(f'{BASE_URL}/tasks/stats')
        assert stats_response.status_code == 200
        stats = stats_response.json()
        assert 'done' in stats
        assert 'pending' in stats
        assert stats['done'] >= 1  # Как минимум наша тестовая задача
    finally:
        requests.delete(f'{BASE_URL}/tasks/{test_task["id"]}')

if __name__ == '__main__':
    pytest.main([__file__, '-v'])