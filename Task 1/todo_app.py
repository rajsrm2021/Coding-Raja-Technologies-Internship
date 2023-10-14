import pickle
import os
from datetime import datetime

# Define Task class
class Task:
    def __init__(self, description, priority, due_date=None):
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.completed = False

# Define ToDoList class
class ToDoList:
    def __init__(self, filename):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'rb') as file:
                self.tasks = pickle.load(file)

    def save_tasks(self):
        with open(self.filename, 'wb') as file:
            pickle.dump(self.tasks, file)

    def add_task(self, description, priority, due_date=None):
        new_task = Task(description, priority, due_date)
        self.tasks.append(new_task)
        self.save_tasks()
        print("Task added successfully!")

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save_tasks()
            print("Task removed successfully!")
        else:
            print("Invalid task index.")

    def mark_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
            self.save_tasks()
            print("Task marked as completed!")
        else:
            print("Invalid task index.")

    def list_tasks(self):
        for index, task in enumerate(self.tasks):
            status = "Completed" if task.completed else "Pending"
            due_date = task.due_date.strftime("%Y-%m-%d") if task.due_date else "N/A"
            print(f"{index}. {task.description} - Priority: {task.priority} - Due Date: {due_date} - Status: {status}")

# Main function
def main():
    todo_list = ToDoList("tasks.pkl")

    while True:
        print("\nTodo List Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. List Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            priority = input("Enter task priority (high, medium, low): ")
            due_date_str = input("Enter due date (YYYY-MM-DD) or leave empty: ")
            due_date = datetime.strptime(due_date_str, "%Y-%m-%d") if due_date_str else None
            todo_list.add_task(description, priority, due_date)
        elif choice == "2":
            index = int(input("Enter task index to remove: "))
            todo_list.remove_task(index)
        elif choice == "3":
            index = int(input("Enter task index to mark as completed: "))
            todo_list.mark_completed(index)
        elif choice == "4":
            todo_list.list_tasks()
        elif choice == "5":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
