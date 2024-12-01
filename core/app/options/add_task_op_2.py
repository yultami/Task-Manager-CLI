from punq import Container

from core.logic.commands.task_manager_commands import AddTaskCommand
from core.logic.container import init_container
from core.logic.mediator import Mediator


def add_task_option_2():
    title = input("Введите название задачи: ")
    description = input("Введите описание задачи: ")
    category = input("Введите категорию задачи: ")
    due_date = input("Введите срок выполнения (YYYY-MM-DD): ")
    priority = input("Введите приоритет (низкий, средний, высокий): ")
    container: Container = init_container()
    mediator: Mediator = container.resolve(Mediator)
    mediator.handle_command(AddTaskCommand(
        id=0,
        title=title,
        description=description,
        category=category,
        due_date=due_date,
        priority=priority,
        status='Не выполнена'
    ))
    print("Задача добавлена в список!")