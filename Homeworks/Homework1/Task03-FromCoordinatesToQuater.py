# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится)
x = int(input('Введите координаты точки по оси X: '))
y = int(input('Введите координаты точки по оси Y: '))
if x > 0 and y > 0:
    print('Точка находится в I четверти')
elif x < 0 and y > 0:
    print('Точка находится во II четверти')
elif x < 0 and y < 0:
    print('Точка находится в III четверти')
elif x > 0 and y < 0:
    print('Точка находится в IV четверти')
elif x == 0 and y != 0:
    print('Точка находится на оси Y')
elif x != 0 and y == 0:
    print('Точка находится на оси X')
else:
    print('Ваша точка - начало координат')