from abc import ABC, abstractmethod
from typing import List

from core.domain.entities.task import Task
from core.infra.filters.task_filter import TaskFilter


class BaseTaskManagerRepository(ABC):
    @abstractmethod
    def get_tasks(self, task_filter: TaskFilter) -> str:
        ...

    @abstractmethod
    def add_task(self, task: Task) -> None:
        ...

    @abstractmethod
    def edit_task(self, id: int, **kwargs) -> None:
        ...

    @abstractmethod
    def del_task(self, id: int) -> None:
        ...

    @abstractmethod
    def search_task(self, **kwargs) -> str:
        ...