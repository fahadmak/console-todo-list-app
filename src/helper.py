from src.tasks import (get_tasks, create_task, delete_task, delete_all_tasks, mark_as_finished)  # import other functions as well
from src.accounts import login_prompt  # import the function as well


selections = {
            '1': 'Create Task',
            '2': 'deleting a task',
            '3': 'deleting all tasks',
            '4': 'Marking a task finished',
            '5': 'View Tasks',
            '6': 'Log out',
            '7': 'Exit'
            }


def options():
    for k, v in selections.items():
        print("{}. {}".format(k, v))


def new_line():
    print("")


def select():
    new_line()
    print("Hello your welcome to the To do App\n"
          "<----------> Menu <---------->")
    options()
    new_line()
    selection = input("Choose an option [Should be a number]: ")

    if selection is '1':
        new_line()
        task = input("enter name task to add: ")
        create_task(task)
        return select()

    elif selection is '2':
        task_number = input("enter task_number: ")
        delete_task(task_number)
        return select()

    elif selection is '3':
        new_line()
        delete_all_tasks()
        return select()

    return extra_ifs(selection)


def extra_ifs(selection):
    if selection is '4':
        new_line()
        task_number = input("enter task_number: ")
        mark_as_finished(task_number)
        return select()

    elif selection is '5':
        new_line()
        get_tasks()
        return select()

    elif selection is '6':
        new_line()
        print("You are Logging out.............")
        new_line()
        login_prompt()
        return select()

    elif selection is '7':
        new_line()
        print("Thank You, Until Next Time.............")
        return

    else:
        new_line()
        print("Wrong selection try the ones listed")
        return select()

