import os

# Define the path to the to-do list file
TODO_FILE = "todo.txt"

# Function to display the to-do list
def display_todo_list():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            todo_list = file.readlines()
            if todo_list:
                print("To-Do List:")
                for index, item in enumerate(todo_list, start=1):
                    print(f"{index}. {item.strip()}")
            else:
                print("To-Do List is empty.")
    else:
        print("To-Do List file does not exist.")

# Function to add a task to the to-do list
def add_task(task):
    with open(TODO_FILE, "a") as file:
        file.write(task + "\n")
        print(f"Task '{task}' added to the to-do list.")

# Function to remove a task from the to-do list
def remove_task(task_number):
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            todo_list = file.readlines()

        if 1 <= task_number <= len(todo_list):
            removed_task = todo_list.pop(task_number - 1)
            with open(TODO_FILE, "w") as file:
                file.writelines(todo_list)
            print(f"Task '{removed_task.strip()}' removed from the to-do list.")
        else:
            print("Invalid task number. Please enter a valid task number.")
    else:
        print("To-Do List file does not exist.")

# Function to update a task in the to-do list
def update_task(task_number, new_task):
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            todo_list = file.readlines()

        if 1 <= task_number <= len(todo_list):
            updated_task = todo_list[task_number - 1]
            todo_list[task_number - 1] = new_task + "\n"
            with open(TODO_FILE, "w") as file:
                file.writelines(todo_list)
            print(f"Task '{updated_task.strip()}' updated to '{new_task.strip()}' in the to-do list.")
        else:
            print("Invalid task number. Please enter a valid task number.")
    else:
        print("To-Do List file does not exist.")

def main():
    """Simple To-Do List Application"""
    if not os.path.exists(TODO_FILE):
        open(TODO_FILE, "a").close()

    while True:
        print("\n1. Display To-Do List")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Update Task")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            display_todo_list()
        elif choice == "2":
            task = input("Enter the task: ")
            add_task(task)
        elif choice == "3":
            display_todo_list()
            task_number = int(input("Enter the task number to remove: "))
            remove_task(task_number)
        elif choice == "4":
            display_todo_list()
            task_number = int(input("Enter the task number to update: "))
            new_task = input("Enter the new task: ")
            update_task(task_number, new_task)
        elif choice == "5":
            print("Thank you for using this apllication!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
