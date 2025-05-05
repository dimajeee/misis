from flask import Blueprint, request, jsonify
from data import (
    get_all_tasks, get_task_by_id, add_task, 
    update_task, delete_task, get_task_stats
)

tasks_blueprint = Blueprint('tasks', __name__)

@tasks_blueprint.route('/tasks', methods=['GET'])
def list_tasks():
    status_filter = request.args.get('status')
    search_query = request.args.get('q')
    sort_by = request.args.get('sort')
    
    tasks = get_all_tasks(status_filter)
    
    # Поиск по заголовку (регистронезависимый)
    if search_query:
        tasks = [task for task in tasks 
                if search_query.lower() in task['title'].lower()]
    
    # Сортировка по дате создания
    if sort_by == 'created_at':
        tasks = sorted(tasks, key=lambda x: x['created_at'])
    elif sort_by == '-created_at':
        tasks = sorted(tasks, key=lambda x: x['created_at'], reverse=True)
    
    return jsonify(tasks)

@tasks_blueprint.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({"error": "Title is required"}), 400
    
    try:
        task = add_task(
            title=data['title'],
            description=data.get('description'),
            status=data.get('status', 'pending')
        )
        return jsonify(task), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@tasks_blueprint.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = get_task_by_id(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    return jsonify(task)

@tasks_blueprint.route('/tasks/<int:task_id>', methods=['PUT'])
def modify_task(task_id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    try:
        updated_task = update_task(
            task_id=task_id,
            title=data.get('title'),
            description=data.get('description'),
            status=data.get('status')
        )
        if not updated_task:
            return jsonify({"error": "Task not found"}), 404
        return jsonify(updated_task)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@tasks_blueprint.route('/tasks/<int:task_id>', methods=['DELETE'])
def remove_task(task_id):
    if delete_task(task_id):
        return jsonify({"message": "Task deleted"}), 200
    return jsonify({"error": "Task not found"}), 404

@tasks_blueprint.route('/tasks/stats', methods=['GET'])
def task_statistics():
    stats = get_task_stats()
    return jsonify(stats)

@tasks_blueprint.route('/tasks/search', methods=['GET'])
def search_tasks():
    search_query = request.args.get('q')
    if not search_query:
        return jsonify({"error": "Search query parameter 'q' is required"}), 400
    
    tasks = get_all_tasks()
    results = [task for task in tasks 
              if search_query.lower() in task['title'].lower()]
    
    return jsonify(results)