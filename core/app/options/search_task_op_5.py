from punq import Container

from core.logic.commands.task_manager_commands import SearchTaskCommand
from core.logic.container import init_container
from core.logic.mediator import Mediator


def search_task_option_5():
    title = input("Заголовок задачи для поиска (Enter - оставить пустым):")
    category = input("Категория для поиска (Enter - оставить пустым): ")
    status = input('Введите статус для поиска "Выполнена"/"Не выполнена" (Enter - оставить пустым): ')
    kwargs = {}
    if title:
        kwargs['title'] = title
    if category:
        kwargs['category'] = category
    if status:
        kwargs['status'] = status
    container: Container = init_container()
    mediator: Mediator = container.resolve(Mediator)
    tasks = mediator.handle_command(SearchTaskCommand(**kwargs))
    print(tasks)
