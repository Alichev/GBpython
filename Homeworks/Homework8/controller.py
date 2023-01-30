import view

students = {}
tasks = []
names = []


def start():
    while True:
        print(students)
        operation = view.get_operation()
        if operation == 0:
            name = view.get_student()
            if name not in names:
                names.append(name)
                students[name] = {}
                for task in tasks:
                    students[name][task] = []
        elif operation == 1:
            task = view.get_task()
            if task not in tasks:
                tasks.append(task)
                for name in names:
                    students[name][task] = []
        elif operation == 2:
            name = view.get_student()
            task = view.get_task()
            mark = view.get_mark()
            students[name][task].append(mark)
        elif operation == 3:
            print(students)
        elif operation == 4:
            name, task = view.choice_student()
            print(students[name][task])
        elif operation == 5:
            break
        else:
            print('Введите значение от 0 до 5')
