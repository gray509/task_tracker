import os, json

# function to read and write the tasks to file
def read_file_to_json(path):
    if os.path.exists(path):
        with open(path, "r") as file:
            tasks = file.read()
        if not tasks:
            return {}
        return json.loads(tasks)
    return {}
def write_json_file(path, j_tasks):
    if not j_tasks:
        print("Task was not saved")
    else:
        with open(path, "w") as file:
            file.write(json.dumps(j_tasks, indent=2))
    