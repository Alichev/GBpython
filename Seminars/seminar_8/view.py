def get_operation():
    operation = int(input(
        "Введите 0 - добавить студента,\n 1 - добавить предмет,\n 2 - добавить оценку ученика по предмету,\n 3 - показать список учеников,\n 4 - показать список оценок ученика, \n 5 - выйти из программы: \n"))
    return operation


def get_student():
    name = input('Введите имя и фамилию: ')
    return name


def get_task():
    task = input('Введите предмет: ')
    return task


def get_mark():
    mark = input('Введите оценку по предмету: ')
    return mark


def choice_student():
    name = input('Введите имя и фамилию: ')
    task = input('Введите предмет: ')
    return name, task
