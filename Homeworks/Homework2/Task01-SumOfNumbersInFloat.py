# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

N = input('Введите вещественное число: ')
sum = 0
for i in N:
    if i.isdigit():
        sum = sum+int(i)
print('Сумма цифр введенного числа: ', sum)
