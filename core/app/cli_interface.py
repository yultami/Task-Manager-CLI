from core.app.options.add_task_op_2 import add_task_option_2
from core.app.options.edit_task_op_3 import edit_task_option_3
from core.app.options.remove_task_op_4 import remove_task_option_4
from core.app.options.search_task_op_5 import search_task_option_5
from core.app.options.watch_task_op_1 import watch_task_option_1


def cli_interface():
    while True:
        print("\nДобро поажловать в Менеджер задач!\nВыберите нужную опцию по цифре:\n\n1. Просмотр задач\n2. Добавление задачи\n3. Изменение задачи\n4. Удаление задачи\n5. Поиск задачи\n6. Выход\n")

        [watch_task_option_1, add_task_option_2, edit_task_option_3, remove_task_option_4, search_task_option_5, exit][int(input('Выберите опцию: ')) - 1]()