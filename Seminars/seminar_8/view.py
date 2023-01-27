def get_operation():
    operation = int(input(
        "Введите 0 - добавить студента,\n 1 - добавить предмет,\n 2 - добавить оценку ученика по предмету,\n 3 - показать список учеников,\n 4 - показать список оценок ученика, \n 5 - выйти из программы: \n"))
    return operation


students = {}
tasks = []
names = []


def get_student():
    Name = input('Введите имя и фамилию: ')
    return Name


def get_class():
    getclass = input('Введите предмет: ')
    return getclass


def get_mark():
    mark = input('Введите оценку по предмету: ')
    return mark


def add_student(student):
    global students
    if student not in names:
        names.append(student)
        students[student] = {}


def add_class(task):
    global students
    if task not in tasks:
        tasks.append(task)
        for name in names:
            students[name][task] = []


def add_mark(student, task, mark):
    global students
    students[student][task].append(mark)
