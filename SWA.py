class Observer:
    def update(self, action):
        pass
class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self, action):
        for observer in self.observers:
            observer.update(action)

    def complete(self):
        self.completed = True
        self.notify_observers("completed")
        return self

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"[{status}] {self.description}"


class SimpleTask(Task):
    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"[Simple Task] [{status}] {self.description}"


class TimedTask(Task):
    def __init__(self, description, due_date):
        super().__init__(description)
        self.due_date = due_date

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"[Timed Task] [{status}] (Due: {self.due_date}) {self.description}"
        
class TaskFactory:
    @staticmethod
    def create_task(task_type, description, *args):
        if task_type == "Simple":
            return SimpleTask(description)
        elif task_type == "Timed":
            return TimedTask(description, *args)
        else:
            raise ValueError(f"Unknown task type: {task_type}")

class TaskManager:
    _instance = None  # Class variable to hold the singleton instance

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance.tasks = []  # Initialize tasks list only once
        return cls._instance

    def add_task(self, task_type, description, *args):
        task = TaskFactory.create_task(task_type, description, *args)
        self.tasks.append(task)
        print(f'Task added: "{description}"')

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for idx, task in enumerate(self.tasks, 1):
                print(f"{idx}. {task}")

    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].complete()
            print(f'Task {task_index + 1} marked as completed.')
        else:
            print("Invalid task index.")

def main():
    task_manager = TaskManager()

    while True:
        print("\nTask Manager")
        print("1. Add Simple Task")
        print("2. Add Timed Task")
        print("3. View Tasks")
        print("4. Complete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Enter the task description: ")
            task_manager.add_task("Simple", description)
        elif choice == '2':
            description = input("Enter the task description: ")
            due_date = input("Enter the due date: ")
            task_manager.add_task("Timed", description, due_date)
        elif choice == '3':
            task_manager.view_tasks()
        elif choice == '4':
            task_index = int(input("Enter the task number to complete: ")) - 1
            task_manager.complete_task(task_index)
        elif choice == '5':
            print("Exiting the Task Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
