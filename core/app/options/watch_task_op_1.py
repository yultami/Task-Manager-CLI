from punq import Container

from core.logic.commands.task_manager_commands import GetTasksCommand
from core.logic.container import init_container
from core.logic.mediator import Mediator


def watch_task_option_1():
    category = input("Введите категорию / оставьте пустым для просмотра всех задач\n")
    container: Container = init_container()
    mediator: Mediator = container.resolve(Mediator)
    tasks = mediator.handle_command(GetTasksCommand(category if category else None))
    print(*tasks)

