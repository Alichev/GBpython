# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint

list_num = [randint(0, 10) for i in range(randint(5, 10))]
print(list_num)

list_final = []
middle = len(list_num)//2+len(list_num) % 2
for i in range(middle):
    list_final.append(list_num[i]*(list_num[-i-1]))
print(list_final)
