import pytest

from core.domain.entities.task import Task
from core.infra.filters.task_filter import TaskFilter
from core.infra.repositories.task_manager_repository.base import BaseTaskManagerRepository
from core.infra.repositories.task_manager_repository.task_manager_repository import TaskManagerRepository


@pytest.fixture
def task_manager_repository() -> BaseTaskManagerRepository:
    return TaskManagerRepository()


@pytest.fixture
def fake_task_data_1() -> Task:
    return Task(
        id=1,
        title="First test task",
        description="first description",
        category="first category",
        due_date="2024-11-30",
        priority="High",
        status="Not finished"
    )


@pytest.fixture
def fake_task_data_2() -> Task:
    return Task(
        id=2,
        title="Second test task",
        description="second description",
        category="second category",
        due_date="2024-11-30",
        priority="High",
        status="Not finished"
    )


@pytest.fixture
def fake_task_filter_with_category() -> TaskFilter:
    return TaskFilter(
        category="first category"
    )


@pytest.fixture
def fake_task_filter_empty() -> TaskFilter:
    return TaskFilter(
        category=None
    )


@pytest.fixture
def fake_kwargs() -> dict:
    kwargs = {"title": "Измененный title", "description": "Измененное описание",
              "category": "Измененная категория", "due_date": "2025-01-01",
              "priority": "Не высокий", "status": "Выполнена"}

    return kwargs

