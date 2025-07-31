from time import ctime
from functions.does_task_exist import does_task_exist
def update_task (list, j_tasks):
    id, description = list[1], list[2]
    does_task_exist(id, j_tasks)
    j_tasks[id]["description"] = description
    j_tasks[id]["updateAt"] = ctime()
    print("Task successfully updated")
    return j_tasks