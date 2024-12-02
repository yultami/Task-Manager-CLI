from punq import Container

from core.logic.commands.task_manager_commands import EditTaskCommand
from core.logic.container import init_container
from core.logic.mediator import Mediator


def edit_task_option_3():
    id = int(input("Введите ID задачи для изменения: "))
    print("Вы можете изменить задачу по заголовку, описанию, категории, сроку выполнения, приоритету и статусу!")
    title = input("Новое название задачи (Enter - пропустить):")
    description = input("Новое описание задачи (Enter - пропустить):")
    category = input("Новая категория задачи (Enter - пропустить):")
    due_date = input("Новый срок выполнения (YYYY-MM-DD) (Enter - пропустить):")
    priority = input("Новый приоритет задачи (Enter - пропустить):")
    status = input("Новый статус задачи (Enter - пропустить):")
    kwargs = {}

    kwargs.update({'title': title}) if title else kwargs
    kwargs.update({'description': description}) if description else kwargs
    kwargs.update({'category': category}) if category else kwargs
    kwargs.update({'due_date': due_date}) if due_date else kwargs
    kwargs.update({'priority': priority}) if priority else kwargs
    kwargs.update({'status': status}) if status else kwargs

    container: Container = init_container()
    mediator: Mediator = container.resolve(Mediator)
    mediator.handle_command(EditTaskCommand(id=id, kwargs=kwargs))
    print("Задача отредактирована!")
