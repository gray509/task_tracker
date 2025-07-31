from functions.does_task_exist import does_task_exist
def change_status(list, j_tasks):
    does_task_exist(list[1] ,j_tasks)
    if(list[0] == "mark-in-progress"):
        j_tasks[list[1]]["status"] = "in-progress"
    else:
        j_tasks[list[1]]["status"] = "done"
    return j_tasks