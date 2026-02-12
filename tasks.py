from google.colab import drive
drive.mount('/content/drive')

def show_menu():
    print("\n=== Task Manager ===")
    print("1. Add new task")
    print("2. View all tasks")
    print("3. Mark task as done")
    print("4. Save tasks to file")
    print("5. Load tasks from file")
    print("6. Edit a task")
    print("7. Delete a task")
    print("8. Exit")

tasks = []
def add_task():
    title = input("Enter task title: ").strip()

    if title == "":
        print("Task title cannot be empty!")
        return

    task = {
        "title": title,
        "done": False
    }

    tasks.append(task)
    print("Task added successfully!")

def list_tasks():
    if len(tasks) == 0:
        print("No tasks found.")
        return

    print("\nYour tasks:")
    for i, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Not done"
        print(f"{i}. {task['title']} [{status}]")

def mark_task_done():
    if len(tasks) == 0:
        print("No tasks to mark as done.")
        return

    list_tasks()

    choice = input("Enter task number to mark as done: ")

    if not choice.isdigit():
        print("Please enter a valid number.")
        return

    task_num = int(choice)

    if task_num < 1 or task_num > len(tasks):
        print("Invalid task number.")
        return

    task = tasks[task_num - 1]

    if task["done"]:
        print("Task is already marked as done!")
    else:
        task["done"] = True
        print("Task marked as done!")

# for edit
def edit_task():
    if len(tasks) == 0:
        print("No tasks to edit.")
        return

    list_tasks()
    choice = input("Enter task number to edit: ")

    if not choice.isdigit():
        print("Please enter a valid number.")
        return

    task_num = int(choice)

    if task_num < 1 or task_num > len(tasks):
        print("Invalid task number.")
        return

    new_title = input("Enter the new title for the task: ").strip()

    if new_title == "":
        print("Task title cannot be empty!")
        return

    tasks[task_num - 1]["title"] = new_title
    print("Task updated successfully!")

# for delete
def delete_task():
    if len(tasks) == 0:
        print("No tasks to delete.")
        return

    list_tasks()
    choice = input("Enter task number to delete: ")

    if not choice.isdigit():
        print("Please enter a valid number.")
        return

    task_num = int(choice)

    if task_num < 1 or task_num > len(tasks):
        print("Invalid task number.")
        return

    deleted_task = tasks.pop(task_num - 1)
    print(f"Task '{deleted_task['title']}' deleted successfully!")

import json
def save_tasks():
    try:
        with open("/content/drive/MyDrive/Colab Notebooks/quantum/tasks.json", "w", encoding="utf-8") as f:
            json.dump(tasks, f, indent=4, ensure_ascii=False)
        print("Tasks saved to tasks.json successfully!")
    except Exception as e:
        print("Error while saving tasks:", e)

def load_tasks():
    global tasks
    try:
        with open("/content/drive/MyDrive/Colab Notebooks/quantum/tasks.json", "r", encoding="utf-8") as f:
            tasks = json.load(f)
        print("Tasks loaded from tasks.json successfully!")
    except FileNotFoundError:
        print("tasks.json file not found.")
    except json.JSONDecodeError:
        print("tasks.json is empty or corrupted.")
    except Exception as e:
        print("Error while loading tasks:", e)

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-8): ").strip()


        if choice == "1":
            add_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            mark_task_done()
        elif choice == "4":
            save_tasks()
        elif choice == "5":
            load_tasks()
        elif choice == "6":
            edit_task()
        elif choice == "7":
            delete_task()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
