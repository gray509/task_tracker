import json
import os
from time import ctime
from status import Status

def list_task(list, j_tasks):
    if not j_tasks:
        print("You have no tasks")
    
    match(list[1]):
        case Status.TODO:
            pass

def change_status(list, j_tasks):
    does_task_exist(list[1] ,j_tasks)
    if(list[0] == "mark-in-progress"):
        j_tasks[list[1]]["status"] = "mark-in-progress"
    else:
        j_tasks[list[1]]["status"] = "mark-in-done"
    return j_tasks

def delete_task(list, j_tasks):
    does_task_exist(list[1] ,j_tasks)
    del j_tasks[list[1]]
    return j_tasks

def update_task (list, j_tasks):
    id, description = list[1], list[2]
    does_task_exist(id, j_tasks)
    j_tasks[id]["description"] = description
    j_tasks[id]["updateAt"] = ctime()
    return j_tasks

def add_task(list, j_tasks):
    if not j_tasks:
        id = "1"
    else:
        id = str(create_id(j_tasks))
    time = ctime()
    j_tasks[id] = {
        "id": id,
        "description": list[1],
        "status": Status.TODO,
        "createdAt": time,
        "updateAt": time
    }
    return j_tasks

def create_id(j_task):
    list_of_ids = list(map(lambda x: int(x), j_task.keys()))
    new_id = max(list_of_ids) + 1
    return new_id

def does_task_exist(id ,j_task):
    if not id in j_task.keys():
        raise ValueError(f"This id: {id} does not exists")
    
# function to read and write the tasks to file
def read_file_to_json(path):
    if os.path.exists(path):
        with open(path, "r") as file:
            tasks = file.read()
        if not tasks:
            return {}
        return json.loads(tasks)

def write_json_file(path, j_tasks):
    with open(path, "w") as file:
        file.write(json.dumps(j_tasks, indent=2, sort_keys=True))
    