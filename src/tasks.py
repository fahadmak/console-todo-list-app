# --- tasks.py ---
# This file contains code that manages your todo_list
todo_list = {}

def search_task_by_name(task):
    if not todo_list:
        return 0
    for k, v in todo_list.items():
        if task == v:
            return task
    return 0


def search_task_by_id(task_id):
    if not todo_list:
        return 0
    for k in todo_list:
        if task_id == k:
            return task_id
    return 0


def create_task(task):
    if not task:
        return "please input task"
    if task.isdigit():
        return "Please input proper name for task"
    if not isinstance(task, str):
        print("Please input proper name for task")
        return "Please input proper name for task"
    searched_task = search_task_by_name(task)
    if not searched_task:
        task_number = str(len(todo_list) + 1)
        todo_list[task_number] = task
        print("{} has been added and new Todo list".format(task))
        return "{} has been added and new Todo list".format(task)
    print("{} already exists in the Todo list".format(task))
    return "{} already exists in the Todo list".format(task)


# Write a function deletes a task


# @view_tasks
# @retry
def delete_task(task_number):
    """
    Removes the specified task from the todo_list
    """
    if not todo_list:
        print("They are currently no task to delete")
        return "They are currently no task to delete"
    if not task_number.isdigit():
        print("Please fill in correct number")
        return "Please fill in correct number"
    task = todo_list.get(task_number, None)
    if not task:
        print(task)
        return "This task number does not exist"
    deleted_task = todo_list.pop(task_number)
    print("{} has been deleted".format(deleted_task))
    get_tasks()
    return "{} has been deleted".format(deleted_task)


# Write a function that marks a task finished

#
# @view_tasks
# @retry
def mark_as_finished(task_number):
    """
    Append the string label '[finished]' at the end of the task
    if it does not already have the label appended.
    It should remain in the todo_list
    """
    if not task_number.isdigit():
        print("Please fill in correct number")
        return
    task = todo_list.get(task_number, None)
    if not task:
        print("This task number does not exist")
        return "This task number does not exist"
    if '[finished]' in task:
        print("{} has already been marked as Finished".format(todo_list[task_number].replace('[finished]', '')))
        return "{} has already been marked as Finished".format(todo_list[task_number].replace('[finished]', ''))
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
        return "There are currently no tasks"
    todo_list.clear()
    print("All tasks successfully deleted")
    return "All tasks successfully deleted"


def get_tasks():
    """
        Get the tasks in the todo_list
    """
    print("-------  Tasks  -------")
    if not todo_list:
        print("There are currently no tasks")
    for k, v in todo_list.items():
        print("{}.  {}".format(k, v))


