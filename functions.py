import json
import os
from time import ctime
from status import Status

def delete_task(id, j_tasks):
    del j_tasks[id]
    return j_tasks

def read_file_to_json(path):
    if os.path.exists(path):
        with open(path, "r") as file:
            j_tasks = json.loads(file.read())
        return j_tasks
    else:
        return {}

def write_json_file(path, j_tasks):
    with open(path, "w") as file:
        file.write(json.dumps(j_tasks, sort_keys=True))

def update_task(id, description, j_tasks):
    j_tasks[id]["description"] = description
    j_tasks[id]["updateAt"] = ctime()
    return j_tasks

def add_task(task, j_tasks):
    time = ctime()
    id = str(create_id(j_tasks))
    j_tasks[id] = {
        "id": id,
        "description": task,
        "status": Status.TODO,
        "createdAt": time,
        "updateAt": time
    }
    return j_tasks

def create_id(j_task):
    list_of_ids = list(map(lambda x: int(x), j_task.keys()))
    new_id = max(list_of_ids) + 1
    return new_id