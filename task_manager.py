#!/usr/bin/env python3
"""
CLI Task Manager - A simple command-line to-do application.
Tasks are stored persistently in a JSON file.
"""

import json
import os
import sys
from datetime import datetime


TASKS_FILE = "tasks.json"


def load_tasks():
    """Load tasks from the JSON file."""
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return json.load(f)


def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def add_task(title, priority="medium"):
    """Add a new task."""
    tasks = load_tasks()
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "priority": priority,
        "completed": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"✅ Task added: [{task['id']}] {title} (Priority: {priority})")


def list_tasks(show_all=False):
    """List all tasks or only pending ones."""
    tasks = load_tasks()
    if not tasks:
        print("📋 No tasks found.")
        return

    print("\n📋 Task List:")
    print("-" * 55)
    for task in tasks:
        if not show_all and task["completed"]:
            continue
        status = "✔" if task["completed"] else "○"
        print(f"  [{task['id']}] {status} [{task['priority'].upper()}] {task['title']}")
        print(f"        Created: {task['created_at']}")
    print("-" * 55)


def complete_task(task_id):
    """Mark a task as completed."""
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            if task["completed"]:
                print(f"ℹ️  Task [{task_id}] is already completed.")
            else:
                task["completed"] = True
                save_tasks(tasks)
                print(f"✔ Task [{task_id}] marked as completed: {task['title']}")
            return
    print(f"❌ Task with ID {task_id} not found.")


def delete_task(task_id):
    """Delete a task by ID."""
    tasks = load_tasks()
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            removed = tasks.pop(i)
            save_tasks(tasks)
            print(f"🗑️  Task [{task_id}] deleted: {removed['title']}")
            return
    print(f"❌ Task with ID {task_id} not found.")


def show_help():
    """Display help menu."""
    print("""
🗂️  CLI Task Manager - Commands:
─────────────────────────────────────────────
  add    <title> [priority]  Add a new task
                             Priority: low | medium | high (default: medium)
  list                       List pending tasks
  list   all                 List all tasks (including completed)
  done   <id>                Mark task as completed
  delete <id>                Delete a task
  help                       Show this help menu
  exit                       Exit the program
─────────────────────────────────────────────
Examples:
  add "Buy groceries"
  add "Submit report" high
  list
  done 1
  delete 2
""")


def main():
    """Main interactive loop."""
    print("🗂️  Welcome to CLI Task Manager!")
    print("Type 'help' for available commands.\n")

    while True:
        try:
            user_input = input("task-manager> ").strip()
            if not user_input:
                continue

            parts = user_input.split(maxsplit=2)
            command = parts[0].lower()

            if command == "exit":
                print("👋 Goodbye!")
                break

            elif command == "help":
                show_help()

            elif command == "add":
                if len(parts) < 2:
                    print("❌ Usage: add <title> [priority]")
                else:
                    title = parts[1].strip('"\'')
                    priority = parts[2].lower() if len(parts) == 3 else "medium"
                    if priority not in ("low", "medium", "high"):
                        print("❌ Priority must be: low, medium, or high")
                    else:
                        add_task(title, priority)

            elif command == "list":
                show_all = len(parts) > 1 and parts[1].lower() == "all"
                list_tasks(show_all)

            elif command == "done":
                if len(parts) < 2 or not parts[1].isdigit():
                    print("❌ Usage: done <id>")
                else:
                    complete_task(int(parts[1]))

            elif command == "delete":
                if len(parts) < 2 or not parts[1].isdigit():
                    print("❌ Usage: delete <id>")
                else:
                    delete_task(int(parts[1]))

            else:
                print(f"❓ Unknown command: '{command}'. Type 'help' for options.")

        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break


if __name__ == "__main__":
    main()
