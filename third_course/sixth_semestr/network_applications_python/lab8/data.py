from models import db, Task
from typing import Dict, List, Optional

def get_all_tasks(status_filter: Optional[str] = None) -> List[Dict]:
    query = Task.query
    if status_filter:
        query = query.filter_by(status=status_filter)
    return [task.to_dict() for task in query.all()]

def get_task_by_id(task_id: int) -> Optional[Dict]:
    task = Task.query.get(task_id)
    return task.to_dict() if task else None

def add_task(title: str, description: Optional[str] = None, status: str = "pending") -> Dict:
    if not title:
        raise ValueError("Title cannot be empty")
    task = Task(title=title, description=description, status=status)
    db.session.add(task)
    db.session.commit()
    return task.to_dict()

def update_task(task_id: int, title: Optional[str] = None, 
               description: Optional[str] = None, status: Optional[str] = None) -> Optional[Dict]:
    task = Task.query.get(task_id)
    if not task:
        return None
    
    if title is not None:
        if not title:
            raise ValueError("Title cannot be empty")
        task.title = title
    if description is not None:
        task.description = description
    if status is not None:
        task.status = status
    
    db.session.commit()
    return task.to_dict()

def delete_task(task_id: int) -> bool:
    task = Task.query.get(task_id)
    if not task:
        return False
    db.session.delete(task)
    db.session.commit()
    return True

def get_task_stats() -> Dict[str, int]:
    stats = {"pending": 0, "done": 0}
    for status in stats.keys():
        stats[status] = Task.query.filter_by(status=status).count()
    return stats