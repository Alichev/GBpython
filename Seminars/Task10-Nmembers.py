# Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# Каждый член последовательности больше предыдущего в 3 раза, знаки у элементов чередуются.
# *Пример:*

# - Для N = 5: 1, -3, 9, -27, 81

n = int(input('Введите число: '))
z = 1
for i in range(1, n+1):
    print(z, end='    ')
    z = z*-3