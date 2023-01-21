# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
from random import randint

list_num = [randint(0, 100) for i in range(10)]
print(list_num)
list_final = [val for indx, val in enumerate(list_num) if indx % 2 != 0]
print(sum(list_final))
