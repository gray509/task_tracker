from functions.does_task_exist import does_task_exist
def delete_task(list, j_tasks):
    does_task_exist(list[1] ,j_tasks)
    del j_tasks[list[1]]
    print("Task successfully deleted")
    return j_tasks