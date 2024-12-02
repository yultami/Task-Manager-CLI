import json

from typing import List

from core.domain.entities.task import Task
from core.infra.converters.task import convert_task_to_dict, convert_dict_to_task
from core.infra.filters.task_filter import TaskFilter
from core.infra.repositories.task_manager_repository.base import BaseTaskManagerRepository


class TaskManagerRepository(BaseTaskManagerRepository):
    def __init__(self):
        self.data_task = self._load_data()

    def _load_data(self) -> list[Task]:
        with open('static/tasks_list.json', 'r') as file:
            try:
                return [convert_dict_to_task(task) for task in json.load(file)]
            except:
                return []

    def _save_data(self):
        try:
            with open('static/tasks_list.json', 'w') as file:
                data = [convert_task_to_dict(task) for task in self.data_task]
                json.dump(data, file, indent=4)

        except IOError as e:
            print (f"Ошибка записи в файл: {e}")

    def get_tasks(self, task_filter: TaskFilter) -> str:
        if task_filter.category is not None:
            return ''.join([task.convert_task_to_cli_view() for task in self._load_data() if task.category == task_filter.category])
        return ''.join([task.convert_task_to_cli_view() for task in self._load_data()])

    def add_task(self, task: Task) -> None:
        task.id = len(self.data_task) + 1
        self.data_task.append(task)
        self._save_data()

    def edit_task(self, id: int, **kwargs) -> None:
        for task in self.data_task:
            if task.id == id:
                for key, value in kwargs.items():
                    setattr(task, key, value)
                self._save_data()
                return

    def del_task(self, id: int) -> None:
        self.data_task = [task for task in self.data_task if task.id != id]
        self._save_data()

    def search_task(self, **kwargs) -> str:
        for key, value in kwargs.items():
            return ''.join([task.convert_task_to_cli_view() for task in self._load_data() if getattr(task, key) == value])