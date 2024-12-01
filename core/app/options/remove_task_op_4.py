from punq import Container

from core.logic.commands.task_manager_commands import DelTaskCommand
from core.logic.container import init_container
from core.logic.mediator import Mediator


def remove_task_option_4():
    id = int(input("Введите ID задачи, которую хотите удалить: "))
    container: Container = init_container()
    mediator: Mediator = container.resolve(Mediator)
    mediator.handle_command(DelTaskCommand(id))
    print("Задача была успешно удалена")