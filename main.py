import sys, os
from functions.add import add_task
from functions.change_status import change_status
from functions.delete import delete_task
from functions.list_tasks import list_tasks
from functions.read_write import write_json_file, read_file_to_json
from functions.update import update_task

def main():
    args = sys.argv[1:]
    if not args:
        print("Please enter commands to add, delete, update, list ... tasks")
        exit(1)

    path = os.path.abspath("tasks.json")

    j_tasks = read_file_to_json(path)
    match(args[0]):
        case "add":
            if len(args) < 2:
                raise ValueError("Wrong amount of commands was passed")
            write_json_file(path, add_task(args, j_tasks))
        case "update":
            if len(args) < 3: 
                raise ValueError("Wrong amount of commands was passed")
            write_json_file(path, update_task(args, j_tasks))
        case "delete":
            if len(args) < 2:
                raise ValueError("Wrong amount of commands was passed")
            write_json_file(path, delete_task(args, j_tasks))
        case "mark-in-progress" | "mark-done":
            if len(args) < 2:
                raise ValueError("Wrong amount of commands was passed")
            write_json_file(path, change_status(args, j_tasks))
        case "list":
            list_tasks(args, j_tasks)
        case _:
            raise ValueError("Wrong command argument passed")

main()