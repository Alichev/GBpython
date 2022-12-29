# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.

# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
from random import randint

k = int(input('Введите значение степени k: '))
arr = []
if k > 0:
    while k >= 2:
        arr.append(f'{randint(0,100)}*x**{k}+')
        k -= 1
    arr.append(f'{randint(0,100)}*x+{randint(0,100)}=0')
    arr_final = [''.join(arr)]
    print(arr_final)
elif k == 0:
    print('Корней нет')
data = open('file.txt', 'w')
data.writelines(arr_final)
data.close()
