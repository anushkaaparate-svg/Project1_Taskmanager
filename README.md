# 🗂️ CLI Task Manager

A lightweight, fully command-line-based Task Manager built with Python. Tasks are stored persistently in a local JSON file — no database or external dependencies required.

---

## 📋 Features

- Add tasks with title and priority (low / medium / high)
- List pending or all tasks
- Mark tasks as completed
- Delete tasks
- Persistent storage via JSON file
- Unit tested with Python's built-in `unittest` module

---

## 🖥️ Requirements

- Python 3.7 or higher
- No external packages required (uses standard library only)

---

## ⚙️ Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/cli-task-manager.git
cd cli-task-manager
```

### 2. (Optional) Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

No external dependencies. Nothing to install beyond Python itself.

```bash
# Verify Python version
python3 --version
```

---

## ▶️ Running the Application

```bash
python3 task_manager.py
```

You will see an interactive prompt:

```
🗂️  Welcome to CLI Task Manager!
Type 'help' for available commands.

task-manager>
```

---

## 📖 Available Commands

| Command                     | Description                         |
|-----------------------------|-------------------------------------|
| `add <title> [priority]`    | Add a task (priority: low/medium/high) |
| `list`                      | Show all pending tasks              |
| `list all`                  | Show all tasks including completed  |
| `done <id>`                 | Mark a task as completed            |
| `delete <id>`               | Delete a task                       |
| `help`                      | Show help menu                      |
| `exit`                      | Exit the application                |

---

## 💡 Example Usage

```
task-manager> add "Buy groceries" low
✅ Task added: [1] Buy groceries (Priority: low)

task-manager> add "Submit assignment" high
✅ Task added: [2] Submit assignment (Priority: high)

task-manager> list
📋 Task List:
-------------------------------------------------------
  [1] ○ [LOW] Buy groceries
        Created: 2025-03-31 10:00
  [2] ○ [HIGH] Submit assignment
        Created: 2025-03-31 10:01
-------------------------------------------------------

task-manager> done 1
✔ Task [1] marked as completed: Buy groceries

task-manager> list all
📋 Task List:
-------------------------------------------------------
  [1] ✔ [LOW] Buy groceries
        Created: 2025-03-31 10:00
  [2] ○ [HIGH] Submit assignment
        Created: 2025-03-31 10:01
-------------------------------------------------------

task-manager> delete 2
🗑️  Task [2] deleted: Submit assignment

task-manager> exit
👋 Goodbye!
```

---

## 🧪 Running Tests

```bash
python3 -m unittest test_task_manager.py -v
```

Expected output:

```
test_add_multiple_tasks ... ok
test_add_task_default_priority ... ok
test_add_task_high_priority ... ok
test_complete_nonexistent_task ... ok
test_complete_task ... ok
test_delete_nonexistent_task ... ok
test_delete_task ... ok
test_load_tasks_empty ... ok
test_save_and_load_tasks ... ok

Ran 9 tests in 0.002s
OK
```

---

## 📁 Project Structure

```
cli-task-manager/
├── task_manager.py        # Main application
├── test_task_manager.py   # Unit tests
├── requirements.txt       # Dependencies (none external)
├── tasks.json             # Auto-created on first use
└── README.md              # This file
```

---

## 📄 License

MIT License. Free to use and modify.
