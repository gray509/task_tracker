def does_task_exist(id ,j_task):
    if not id in j_task.keys():
        raise ValueError(f"This id: {id} does not exists")