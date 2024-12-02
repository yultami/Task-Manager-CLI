from core.domain.entities.task import Task


def convert_task_to_dict(task: Task) -> dict:
    return {'id': task.id, 'title': task.title, 'description': task.description, 'category': task.category,
                'due_date': task.due_date, 'priority': task.priority, 'status': task.status}


def convert_dict_to_task(task_dict: dict) -> Task:
    return Task(
        id=task_dict["id"],
        title=task_dict["title"],
        description=task_dict["description"],
        category=task_dict["category"],
        due_date=task_dict["due_date"],
        priority=task_dict["priority"],
        status=task_dict["status"]
    )

