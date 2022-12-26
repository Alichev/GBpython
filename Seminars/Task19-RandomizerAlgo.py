# Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.
# (пользователь вводит число N и нужно вывести случайное число в интервале от 0 до N, чтобы и N тоже могло выпасть)


import datetime


def random_int(num):
    rand = datetime.datetime.now().microsecond/10**6
    return int((num+1)*rand)


N = int(input('Введите число N: '))
print(random_int(N))
