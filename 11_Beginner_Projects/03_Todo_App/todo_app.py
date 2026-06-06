"""
Project 3: To-Do List App

A command-line task manager with file persistence.
Tasks are saved to a JSON file.
"""

import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def add_task(tasks, title, priority="medium"):
    task = {
        "id": max((t["id"] for t in tasks), default=0) + 1,
        "title": title,
        "done": False,
        "priority": priority,
        "created": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"✅ Task added: '{title}'")

def list_tasks(tasks, show_done=False):
    visible = [t for t in tasks if show_done or not t["done"]]
    
    if not visible:
        print("No tasks!" + (" (all done! 🎉)" if not show_done and tasks else ""))
        return
    
    priority_icons = {"high": "🔴", "medium": "🟡", "low": "🟢"}
    
    print(f"\n{'ID':3} {'✓':2} {'Priority':10} {'Title':30} {'Created':16}")
    print("-" * 65)
    
    for task in visible:
        status = "✓" if task["done"] else " "
        icon = priority_icons.get(task["priority"], "⚪")
        title = task["title"][:28] + ".." if len(task["title"]) > 30 else task["title"]
        print(f"{task['id']:3} [{status}] {icon} {task['priority']:8} {title:30} {task['created']}")

def complete_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            save_tasks(tasks)
            print(f"✅ Completed: '{task['title']}'")
            return
    print(f"Task #{task_id} not found.")

def delete_task(tasks, task_id):
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            removed = tasks.pop(i)
            save_tasks(tasks)
            print(f"🗑️  Deleted: '{removed['title']}'")
            return
    print(f"Task #{task_id} not found.")

def show_stats(tasks):
    total = len(tasks)
    done = sum(1 for t in tasks if t["done"])
    pending = total - done
    print(f"\n📊 Stats: {total} total | {done} done | {pending} pending")

def main():
    tasks = load_tasks()
    
    print("=" * 50)
    print("        📝 TO-DO LIST APP")
    print("=" * 50)
    
    while True:
        print("\nOptions:")
        print("  1. Add task")
        print("  2. List pending tasks")
        print("  3. List all tasks")
        print("  4. Complete a task")
        print("  5. Delete a task")
        print("  6. Stats")
        print("  7. Quit")
        
        choice = input("\nChoice: ").strip()
        
        if choice == "1":
            title = input("Task title: ").strip()
            if not title:
                print("Title cannot be empty!")
                continue
            priority = input("Priority (high/medium/low) [medium]: ").strip() or "medium"
            if priority not in ("high", "medium", "low"):
                priority = "medium"
            add_task(tasks, title, priority)
        
        elif choice == "2":
            list_tasks(tasks)
        
        elif choice == "3":
            list_tasks(tasks, show_done=True)
        
        elif choice == "4":
            list_tasks(tasks)
            try:
                task_id = int(input("Task ID to complete: "))
                complete_task(tasks, task_id)
            except ValueError:
                print("Please enter a valid ID.")
        
        elif choice == "5":
            list_tasks(tasks, show_done=True)
            try:
                task_id = int(input("Task ID to delete: "))
                confirm = input(f"Delete task #{task_id}? (y/n): ")
                if confirm.lower() == "y":
                    delete_task(tasks, task_id)
            except ValueError:
                print("Please enter a valid ID.")
        
        elif choice == "6":
            show_stats(tasks)
        
        elif choice == "7":
            print("Goodbye! 👋")
            break
        
        else:
            print("Invalid choice. Try 1-7.")

if __name__ == "__main__":
    main()
