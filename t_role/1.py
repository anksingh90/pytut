def log_task():
    task = input("Enter your daily task: ")
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print("✅ Task added to tasks.txt")

def view_tasks():
    try:
        with open("tasks.txt", "r") as file:
            lines = file.readlines()
            print("\n📋 Your Tasks:")
            for idx, line in enumerate(lines, start=1):
                print(f"{idx}. {line.strip()}")
        return lines
    except FileNotFoundError:
        print("❌ No tasks found yet.")
        return []

def edit_task():
    tasks = view_tasks()
    if not tasks:
        return
    try:
        index = int(input("\nEnter task number to edit: ")) - 1
        if 0 <= index < len(tasks):
            new_task = input("Enter new task description: ")
            tasks[index] = new_task + "\n"
            with open("tasks.txt", "w") as file:
                file.writelines(tasks)
            print("✅ Task updated.")
        else:
            print("❗ Invalid task number.")
    except ValueError:
        print("❗ Enter a valid number.")

while True:
    print("\n--- Task Manager Menu ---")
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Edit a Task")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        log_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        edit_task()
    elif choice == '4':
        print("Exiting Task Manager.")
        break
    else:
        print("❗ Invalid choice. Try again.")
