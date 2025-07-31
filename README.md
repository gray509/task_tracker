# Task Tracker
Task Tracker is a simple command-line tool built with Python that helps you manage your tasks efficiently. You can add, update, delete, and list tasks, as well as track their progress using different status labels.

## 🛠Features
- Add new tasks with descriptions
- Update existing tasks
- Mark tasks as in-progress or done
- List all tasks or filter by status
- Delete tasks by ID

## 💻 Technologies Used
- Python 3
- JSON for data storage

## 🚀 Getting Started
### Prerequisites
Make sure you have **Python 3** installed on your system.

### Installation & Usage
1. Clone or download this repository.
2. Navigate to the project directory.
3. Run the app using the following command format:

`python3 main.py <command> [arguments]`

### Example Commands
```
    # Add a new task
    python3 main.py add "description of your task here"

    # Update a task
    python3 main.py update <id> "new description of the selected task here"

    # Mark task as in-progress or done
    python3 main.py mark-in-progress <id>
    python3 main.py mark-done <id>

    # List all tasks
    python3 main.py list

    # List tasks by status (done, todo, in-progress)
    python3 main.py list <status>

    # Delete a task
    python3 main.py delete <id>
```
Note: Tasks are saved automatically in a JSON file.

## Features to add
delete function
- confirm with the user if they want to delete
- delete multiple tasks at once based on ID, status

list functions
- list with ID
- list based on date
