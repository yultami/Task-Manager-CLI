from punq import Container

from core.logic.commands.task_manager_commands import EditTaskCommand
from core.logic.container import init_container
from core.logic.mediator import Mediator


def edit_task_option_3():
    id = int(input("Введите ID задачи для изменения: "))
    title = input("Новое название задачи (Enter - пропустить):")
    description = input("Новое описание задачи (Enter - пропустить):")
    category = input("Новая категория задачи (Enter - пропустить):")
    due_date = input("Новый срок выполнения (YYYY-MM-DD) (Enter - пропустить):")
    priority = input("Новый приоритет задачи (Enter - пропустить):")
    status = input("Новый статус задачи (Enter - пропустить):")
    kwargs = {}

    if title:
        kwargs['title'] = title
    if description:
        kwargs['description'] = description
    if category:
        kwargs['category'] = category
    if due_date:
        kwargs['due_date'] = due_date
    if priority:
        kwargs['priority'] = priority
    if status:
        kwargs['status'] = status

    container: Container = init_container()
    mediator: Mediator = container.resolve(Mediator)
    mediator.handle_command(EditTaskCommand(id=id, kwargs=kwargs))
    print("Задача отредактирована!")
