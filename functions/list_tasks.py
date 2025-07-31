
def list_tasks(list, j_tasks):
    if not j_tasks:
        print("You have no tasks")
    list_of_tasks = [
        ["ID", "DESCRIPTION", "STATUS", "CREATED AT", "UPDATED AT"]
    ]
    if len(list) < 2:
        #print all tasks
        for taks_key in j_tasks:
            row = [j_tasks[taks_key]["id"], j_tasks[taks_key]["description"],j_tasks[taks_key]["status"],
                   j_tasks[taks_key]["createdAt"], j_tasks[taks_key]["updateAt"]]
            list_of_tasks.append(row)
    else:
        for taks_key in j_tasks:
            if j_tasks[taks_key]["status"] == list[1]:
                row = [j_tasks[taks_key]["id"], j_tasks[taks_key]["description"],j_tasks[taks_key]["status"],
                    j_tasks[taks_key]["createdAt"], j_tasks[taks_key]["updateAt"]]
                list_of_tasks.append(row)
    print_tasks(list_of_tasks)

def print_tasks(list_of_tasks):
    col_widths = [max(len(str(item)) for item in col) for col in zip(*list_of_tasks)]
    for row in list_of_tasks:
        formatted_row = " | ".join(f"{str(item):<{col_widths[i]}}" for i, item in enumerate(row))
        print(formatted_row)