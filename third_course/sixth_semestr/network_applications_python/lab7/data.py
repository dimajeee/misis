from typing import Dict, List, Optional

tasks = []
current_id = 1

class Task:
    def __init__(self, title: str, description: Optional[str] = None, status: str = "pending"):
        global current_id
        self.id = current_id
        self.title = title
        self.description = description
        self.status = status
        current_id += 1

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status
        }

def get_all_tasks(status_filter: Optional[str] = None) -> List[Dict]:
    if status_filter:
        return [task.to_dict() for task in tasks if task.status == status_filter]
    return [task.to_dict() for task in tasks]

def get_task_by_id(task_id: int) -> Optional[Dict]:
    for task in tasks:
        if task.id == task_id:
            return task.to_dict()
    return None

def add_task(title: str, description: Optional[str] = None, status: str = "pending") -> Dict:
    if not title:
        raise ValueError("Title cannot be empty")
    task = Task(title, description, status)
    tasks.append(task)
    return task.to_dict()

def update_task(task_id: int, title: Optional[str] = None, 
               description: Optional[str] = None, status: Optional[str] = None) -> Optional[Dict]:
    for task in tasks:
        if task.id == task_id:
            if title is not None:
                if not title:
                    raise ValueError("Title cannot be empty")
                task.title = title
            if description is not None:
                task.description = description
            if status is not None:
                task.status = status
            return task.to_dict()
    return None

def delete_task(task_id: int) -> bool:
    global tasks
    initial_length = len(tasks)
    tasks = [task for task in tasks if task.id != task_id]
    return len(tasks) != initial_length

def get_task_stats() -> Dict[str, int]:
    stats = {"pending": 0, "done": 0}
    for task in tasks:
        stats[task.status] += 1
    return stats