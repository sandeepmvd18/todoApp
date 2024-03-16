class TodoList:
    def __init__(self):
        self.tasks = []
    def add_task(self, task):
        self.tasks.append(task)
    def delete_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
        else:
            print("Task not found!")
    def view_tasks(self):
        if self.tasks:
            print("Todo List:")
            for idx, task in enumerate(self.tasks, 1):
                print(f"{idx}. {task}")
        else:
            print("Todo List is empty!")
        
if __name__ == "__main__":
    todo_list = TodoList()
    while True:
        print("\n1. Add Task")
        print("2. Delete Task")
        print("3. View Tasks")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == "2":
            task = input("Enter task to delete: ")
            todo_list.delete_task(task)
        elif choice == "3":
            todo_list.view_tasks()
        elif choice == "4":
            break
        else:
            print("Invalid choice!")






