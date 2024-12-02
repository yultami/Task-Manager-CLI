from punq import Container

from core.logic.commands.task_manager_commands import SearchTaskCommand
from core.logic.container import init_container
from core.logic.mediator import Mediator


def search_task_option_5():
    print("Вы можете найти задачу по заголовку, категории и статусу выполнения!")
    title = input("Заголовок (Enter - оставить пустым): ")
    category = input("Категория (Enter - оставить пустым): ")
    status = input("Статус (Выполнена/Не выполнена) (Enter - оставить пустым): ")
    kwargs = {}
    kwargs.update({"title": title}) if title else kwargs
    kwargs.update({"category": category}) if category else kwargs
    kwargs.update({"status": status}) if status else kwargs
    container: Container = init_container()
    mediator: Mediator = container.resolve(Mediator)
    tasks = mediator.handle_command(SearchTaskCommand(kwargs))
    print(*tasks)