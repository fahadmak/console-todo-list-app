# --- tasks.py ---
# This file contains code that manages your todo_list
todo_list = {'1': 'fight win', '2': 'lose'}

# Write a function creates a task


def retry(func):
    def continue_func():
        while True:
            prompt = input("Choose to yes or no to continue or start: ")
            if prompt == 'yes':
                func()
            elif prompt == 'no':
                break
            else:
                print("Try 'YES' or 'NO' !")
    return continue_func


def view_tasks(func):
    """
        Get the tasks in the todo_list
    """
    def continue_func():
        print("-------  Tasks  -------")
        if not todo_list:
            print("There are currently no tasks")
            func()
        for k, v in todo_list.items():
            print("{}.  {}".format(k, v))
        func()
    return continue_func


@view_tasks
@retry
def create_task():
    task = input("enter name task to add: ")
    if not task.isalpha():
        print("Please input proper name for task")
        return
    for item in list(todo_list.values()):
        if task in item:
            print("{} already exists in the Todo list".format(task))
            return
    task_number = str(len(todo_list) + 1)
    todo_list[task_number] = task
    print("{} has been added and new Todo list".format(task))
    get_tasks()
    return

# Write a function deletes a task


@view_tasks
@retry
def delete_task():
    """
    Removes the specified task from the todo_list
    """
    if not todo_list:
        print("They are currently no task to delete")
        return
    task_number = input("enter task_number: ")
    if not task_number.isdigit():
        print("Please fill in correct number")
        return
    task = todo_list.get(task_number, "This task number does not exist")
    if task is "This task number does not exist":
        print(task)
        return
    deleted_task = todo_list.pop(task_number)
    print("{} has been deleted".format(deleted_task))
    get_tasks()
    return


# Write a function that marks a task finished


@view_tasks
@retry
def mark_as_finished():
    """
    Append the string label '[finished]' at the end of the task
    if it does not already have the label appended.
    It should remain in the todo_list
    """
    task_number = input("enter task number: ")
    if not task_number.isdigit():
        print("Please fill in correct number")
        return
    task = todo_list.get(task_number, "This task number does not exist")
    if task is "This task number does not exist":
        print(task)
        return
    if '[finished]' in task:
        print("{} has already been marked as Finished".format(todo_list[task_number].replace('[finished]', '')))
        return
    todo_list[task_number] = task + '[finished]'
    print("{} has been marked as Finished".format(todo_list[task_number].replace('[finished]', '')))
    get_tasks()
    return



# Write a function deletes all tasks


def delete_all_tasks():
    """
    Empty the the todo_list
    """
    if not todo_list:
        print("There are currently no tasks")
        return
    todo_list.clear()
    print("All tasks successfully deleted")
    return


def get_tasks():
    """
        Get the tasks in the todo_list
    """
    print("-------  Tasks  -------")
    if not todo_list:
        print("There are currently no tasks")
    for k, v in todo_list.items():
        print("{}.  {}".format(k, v))


