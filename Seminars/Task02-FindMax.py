# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# Примеры: 1, 4, 8, 7, 5 -> 8    78, 55, 36, 90, 2 -> 90

# print('Введите первое число: ')
# a = int(input())
# print('Введите второе число: ')
# b = int(input())
# print('Введите третье число: ')
# c = int(input())
# print('Введите четвертое число: ')
# d = int(input())
# print('Введите пятое число: ')
#e = int(input())
# if a >= b and a >= c and a >= d and a >= e:
#     print('Максимальное число ', a)
# elif b >= a and b >= c and b >= d and b >= e:
#     print('Максимальное число ', b)
# elif c >= a and c >= b and c >= d and c >= e:
#     print('Максимальное число ', c)
# elif d >= a and d >= b and d >= c and d >= e:
#     print('Максимальное число ', d)
# elif e >= a and e >= b and e >= c and e >= d:
#     print('Максимальное число ', e)
# else:
#     print('Ошибка')

# a = input('Введите 5 чисел через пробел: ')
# list = a.split()
# print(max(list))

a = int(input('Введите первое число: '))
max = a
for i in range(4):
    a = int(input('Введите следующее число: '))
    if a > max:
        max = a
print('Максимальное число:', max)
