from dataclasses import dataclass


@dataclass
class Task:
    id: int
    title: str
    description: str
    category: str
    due_date: str
    priority: str
    status: str

    def convert_task_to_cli_view(self):
        return f'\n\nID:{self.id}\nЗаголовок:{self.title}\nОписание:{self.description}\nКатегория:{self.category}\nСрок выполнения:{self.due_date}\nПриоритет:{self.priority}\nСтатус:{self.status}'
