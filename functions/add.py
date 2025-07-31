from time import ctime
def add_task(list, j_tasks):
    for tasks_key in j_tasks:
        if j_tasks[tasks_key]["description"] == list[1]:
            print("Task same description already exist")
            print(f"Here is its ID: {j_tasks[tasks_key]["id"]}")
            return None
    if not j_tasks:
        id = "1"
    else:
        id = str(create_id(j_tasks))
    time = ctime()
    j_tasks[id] = {
        "id": id,
        "description": list[1],
        "status": "todo",
        "createdAt": time,
        "updateAt": time
    }
    print(f"Task added successfully (ID: {id})")
    return j_tasks

def create_id(j_task):
    list_of_ids = list(map(lambda x: int(x), j_task.keys()))
    new_id = max(list_of_ids) + 1
    return new_id