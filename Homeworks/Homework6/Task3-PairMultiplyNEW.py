# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint

list_num = [randint(0, 10) for i in range(randint(5, 15))]
print(list_num)

list_final = [list_num[indx]*list_num[-indx-1]
              for indx in range(len(list_num)//2+len(list_num) % 2)]

print(list_final)
