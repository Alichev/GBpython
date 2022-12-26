# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число

list_num = [1, 8, 'hello', 25, 'привет']
# find = input('Введите искомое значение: ')  # для строки
# for i in range(len(list_num)):
#     if list_num[i] == find:
#         print('Искомое значение находится на позиции ', i)
#         break
# else:
#     print('Искомое значение не найдено')

find = int(input('Введите искомое число: '))
if find in list_num:
    print('Да, позиция ', list_num.index(find))
else:
    print('Нет')


# for i in list_num:
#     if i.isdigit():
#         print(list_num.index(i))
