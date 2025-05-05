from app import app
from models import db, Task

def init_db():
    with app.app_context():
        db.create_all()
        
        # Добавляем тестовые данные, если таблица пуста
        if not Task.query.first():
            tasks = [
                Task(title='Task 1', description='description'),
                Task(title='Task 2', status='pending'),
                Task(title='Task 3', status='done')
            ]
            db.session.add_all(tasks)
            db.session.commit()
            print("Тестовые данные добавлены")

if __name__ == '__main__':
    init_db()