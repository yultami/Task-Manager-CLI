from dataclasses import dataclass
from typing import List

from core.domain.entities.task import Task
from core.infra.filters.task_filter import TaskFilter
from core.infra.repositories.task_manager_repository.base import BaseTaskManagerRepository
from core.logic.commands.base import BaseCommand, BaseCommandHandler


@dataclass(frozen=True)
class GetTasksCommand(BaseCommand):
    category: str | None


@dataclass(frozen=True)
class AddTaskCommand(BaseCommand):
    id: int
    title: str
    description: str
    category: str
    due_date: str
    priority: str
    status: str


@dataclass(frozen=True)
class EditTaskCommand(BaseCommand):
    id: int
    kwargs: dict


@dataclass(frozen=True)
class DelTaskCommand(BaseCommand):
    id: int


@dataclass(frozen=True)
class SearchTaskCommand(BaseCommand):
    kwargs: dict


@dataclass(frozen=True)
class GetTasksCommandHandler(BaseCommandHandler[GetTasksCommand, List[Task]]):
    task_manager_repository: BaseTaskManagerRepository

    def handle(self, command: GetTasksCommand) -> List[Task]:
        task_filter = TaskFilter(
            category=command.category
        )
        return self.task_manager_repository.get_tasks(task_filter)


@dataclass(frozen=True)
class AddTaskCommandHandler(BaseCommandHandler[AddTaskCommand, None]):
    task_manager_repository: BaseTaskManagerRepository

    def handle(self, command: AddTaskCommand) -> None:
        task = Task(
            id=command.id,
            title=command.title,
            description=command.description,
            category=command.category,
            due_date=command.due_date,
            priority=command.priority,
            status=command.status,
        )

        return self.task_manager_repository.add_task(task)


@dataclass(frozen=True)
class EditTaskCommandHandler(BaseCommandHandler[EditTaskCommand, None]):
    task_manager_repository: BaseTaskManagerRepository

    def handle(self, command: EditTaskCommand) -> None:
        self.task_manager_repository.edit_task(command.id, **command.kwargs)


@dataclass(frozen=True)
class DelTaskCommandHandler(BaseCommandHandler[DelTaskCommand, None]):
    task_manager_repository: BaseTaskManagerRepository

    def handle(self, command: DelTaskCommand) -> None:
        self.task_manager_repository.del_task(command.id)


@dataclass(frozen=True)
class SearchTaskCommandHandler(BaseCommandHandler[SearchTaskCommand, List[Task]]):
    task_manager_repository: BaseTaskManagerRepository

    def handle(self, command: SearchTaskCommand):
        self.task_manager_repository.search_task(**command.kwargs)
