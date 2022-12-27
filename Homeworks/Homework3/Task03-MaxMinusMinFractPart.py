# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import random


def fract(N):
    return round(N % 1, 2)


list_num = [round(random.uniform(0, 100), 2)
            for i in range(random.randint(5, 10))]
print(list_num)
fract_list = list(map(fract, list_num))
print(fract_list)
print('Максимум: ', max(fract_list))
print('Минимум: ', min(fract_list))
print('Разница: ', round(max(fract_list)-min(fract_list), 2))
