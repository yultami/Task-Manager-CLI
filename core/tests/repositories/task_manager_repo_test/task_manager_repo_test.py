import json

from core.domain.entities.task import Task
from core.infra.converters.task import convert_task_to_dict, convert_dict_to_task
from core.tests.repositories.task_manager_repo_test.conftest import fake_task_data_1, fake_task_data_2


def load_json_file() -> list:
    with open('../../../../static/tasks_list_test.json', 'r') as file:
        try:
            return json.load(file)
        except:
            return []


def write_to_json_file(task):
    data = load_json_file()
    data.append(convert_task_to_dict(task))
    print(data)
    with open('../../../../static/tasks_list_test.json', 'w') as file:
        json.dump(data, file, indent=4)


def clear_json_file():
    with open('../../../../static/tasks_list_test.json', 'w') as file:
        json.dump([], file, indent=4)


def task_data_1() -> Task:
    return Task(
        id=0,
        title="First test task",
        description="first description",
        category="first category",
        due_date="2024-11-30",
        priority="High",
        status="Not finished"
    )


def task_data_2() -> Task:
    return Task(
        id=0,
        title="Second test task",
        description="second description",
        category="second category",
        due_date="2024-11-30",
        priority="High",
        status="Not finished"
    )

#print(write_to_json_file(task_data_1()))
#print(write_to_json_file(task_data_2()))
#clear_json_file()


def test_get_tasks_success_with_category(task_manager_repository, fake_task_data_1,
                                         fake_task_data_2, fake_task_filter_with_category, fake_task_filter_empty):
    clear_json_file()
    write_to_json_file(fake_task_data_1)
    write_to_json_file(fake_task_data_2)
    result_1 = task_manager_repository.get_tasks(fake_task_filter_with_category)
    result_2 = task_manager_repository.get_tasks(fake_task_filter_empty)

    assert len(result_1) == 1
    assert len(result_2) == 2


def test_add_task_success(task_manager_repository, fake_task_data_1, fake_task_filter_with_category):
    clear_json_file()
    task_manager_repository.add_task(fake_task_data_1)
    result, *_ = task_manager_repository.get_tasks(fake_task_filter_with_category)

    assert result.title == fake_task_data_1.title
    assert result.description == fake_task_data_1.description
    assert result.category == fake_task_data_1.category
    assert result.priority == fake_task_data_1.priority
    assert result.status == fake_task_data_1.status


def test_edit_task_success(task_manager_repository, fake_task_data_1, fake_kwargs):
    clear_json_file()
    write_to_json_file(fake_task_data_1)
    task_manager_repository.edit_task(fake_task_data_1.id, **fake_kwargs)
    result, *_ = task_manager_repository.search_task(**fake_kwargs)

    assert result.title == fake_kwargs["title"]
    assert result.description == fake_kwargs["description"]
    assert result.category == fake_kwargs["category"]
    assert result.priority == fake_kwargs["priority"]
    assert result.status == fake_kwargs["status"]


def test_del_task_success(task_manager_repository, fake_task_data_1, fake_kwargs):
    clear_json_file()
    write_to_json_file(fake_task_data_1)
    task_manager_repository.del_task(1)
    result = task_manager_repository.search_task(**fake_kwargs)

    assert result == []


