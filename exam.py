class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

class Observer:
    def update(self, subject):
        pass

class Task:
    def __init__(self, task_id, title, description, assigned_user=None):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.assigned_user = assigned_user
        self.comments = []
        self.status = "Нове"
        self.observers = []  

    def assign_to_user(self, user):
        if not isinstance(user, User):
            raise ValueError("Призначений користувач має бути екземпляром класу User")
        self.assigned_user = user
        self.notify_observers()

    def add_comment(self, comment):
        self.comments.append(comment)
        self.notify_observers()

    def update_status(self, status):
        self.status = status
        self.notify_observers()

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self)

class Project(Observer):
    def __init__(self, project_id, name):
        self.project_id = project_id
        self.name = name
        self.tasks = []

    def add_task(self, task):
        if not isinstance(task, Task):
            raise ValueError("Додаваний об'єкт має бути завданням (екземпляром класу Task)")
        self.tasks.append(task)
        task.add_observer(self)

    def update(self, task):
        print(f"Оновлено завдання '{task.title}' у проекті '{self.name}'")


try:
    dev1 = User(1, "Іван")
    dev2 = User(2, "Олена")

    task1 = Task(101, "Виправити баг", "Опис багу тут")
    task2 = Task(102, "Додати функціонал", "Опис функціоналу тут")

    project = Project(201, "Розробка Web-додатку")
    project.add_task(task1)
    project.add_task(task2)

    task1.assign_to_user(dev1)
    task2.assign_to_user(dev2)

    task1.add_comment("Перевірено, баг відтворюється")
    task2.add_comment("Починаю роботу над функціоналом")

    task1.update_status("В роботі")
    task2.update_status("Виконане")
except ValueError as e:
    print(e)