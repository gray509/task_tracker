import sys
from functions import *

def main():
    args = sys.argv[1:]
    if not args:
        print("Please enter commands to add, delete, update, list ... tasks")
        exit(1)

    path = os.path.abspath("task.json")

    j_tasks = read_file_to_json(path)
    match(args[0]):
        case "add":
            write_json_file(path, add_task(args[1], j_tasks))
        case "update":
            write_json_file(path, update_task((args[1]), args[2], j_tasks))
        case "delete":
            pass
        case "mark-in-progress":
            pass
        case "mark-in-done":
            pass
        case "list":
            pass
        case _:
            raise ValueError("Worng command argument passed")

main()