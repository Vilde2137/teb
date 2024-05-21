from datetime import datetime

class Task:
    def __init__(self, description, priority, deadline):
        self.description = description
        self.priority = priority
        self.deadline = deadline

    def __str__(self):
        return f"Task(description={self.description}, priority={self.priority}, deadline={self.deadline.strftime('%Y-%m-%d')})"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):

        self.tasks.append(task)
        print("Dodano zadanie.")

    def remove_task(self, task_description):

        for task in self.tasks:
            if task.description == task_description:
                self.tasks.remove(task)
                print("Usunieto zadanie.")
                return
        print("Nie znaleziono zadania.")

    def view_tasks(self):

        if not self.tasks:
            print("Nie ma dostepnych zadan.")
        for task in self.tasks:
            print(task)

task1 = Task("Zrob costam", 1, datetime(2020, 1, 1))
manager = TaskManager()

manager.add_task(task1)

print("Obecne zadania: ")
manager.view_tasks()