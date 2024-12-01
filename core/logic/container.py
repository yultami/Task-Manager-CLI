from functools import lru_cache

from punq import Container, Scope

from core.infra.repositories.task_manager_repository.base import BaseTaskManagerRepository
from core.infra.repositories.task_manager_repository.task_manager_repository import TaskManagerRepository
from core.logic.commands.task_manager_commands import GetTasksCommandHandler, AddTaskCommandHandler, \
    DelTaskCommandHandler, GetTasksCommand, AddTaskCommand, \
    DelTaskCommand, EditTaskCommandHandler, EditTaskCommand, SearchTaskCommandHandler, SearchTaskCommand
from core.logic.mediator import Mediator


@lru_cache(1)
def init_container():
    return _init_container()


def _init_container() -> Container:
    container = Container()

    container.register(GetTasksCommandHandler)
    container.register(AddTaskCommandHandler)
    container.register(EditTaskCommandHandler)
    container.register(DelTaskCommandHandler)
    container.register(SearchTaskCommandHandler)

    def init_task_manager_repository() -> BaseTaskManagerRepository:
        return TaskManagerRepository()

    def init_mediator() -> Mediator:
        mediator = Mediator()

        mediator.register_command(GetTasksCommand, [container.resolve(GetTasksCommandHandler)])
        mediator.register_command(AddTaskCommand, [container.resolve(AddTaskCommandHandler)])
        mediator.register_command(EditTaskCommand, [container.resolve(EditTaskCommandHandler)])
        mediator.register_command(DelTaskCommand, [container.resolve(DelTaskCommandHandler)])
        mediator.register_command(SearchTaskCommand, [container.resolve(SearchTaskCommandHandler)])

        return mediator

    container.register(BaseTaskManagerRepository, factory=init_task_manager_repository, scope=Scope.singleton)

    container.register(Mediator, factory=init_mediator, scope=Scope.singleton)

    return container


