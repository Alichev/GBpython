# Напишите программу, которая сортирует отдельно элементы массива с четными и нечетными значениями.
# Все элементы с нечетными значениями нужно отсортировать по возрастанию, а элементы с четными значениями - по убыванию.
# При этом элементы каждой из групп(как четные, так и нечетные) должны занимать то же множество позиций в массиве,
# что и до сортировки.
# Входные данные
# 6
# 3 1 2 5 4 6
# Первая строка содержит размер массива N. Во второй строке через пробел задаются N чисел - элементы массива.
# Гарантируется, что 0 < N <= 100000

# Выходные данные
# 1 3 6 5 4 2
# Программа должна вывести все элементы отсортированного массива в одну строку, разделив их пробелами.
import random

num = int(input('Введите размер массива: '))
a = [random.randint(1, 1000) for i in range(num)]
print(a)
odd_ind = [i for i, v in enumerate(a) if v % 2 != 0]
even_ind = [i for i, v in enumerate(a) if v % 2 == 0]
indexes = odd_ind + even_ind
odd_elem = [v for i, v in enumerate(a) if v % 2 != 0]
even_elem = [v for i, v in enumerate(a) if v % 2 == 0]
odd_sort = sorted(odd_elem)
even_sort = sorted(even_elem, reverse=True)
elements = odd_sort + even_sort
index_elem = list(zip(indexes, elements))
index_elem_sorted = sorted(index_elem, key=lambda x: x[0])
result = [i[1] for i in index_elem_sorted]
print(result)

# Более быстрое решение:
# создаем список из 0 и 1, на позициях четных элементов будет 1, нечетных - 0
# h = [1 if i % 2 == 0 else 0 for i in a]   можно даже без h, а сразу проверять не на 0 и 1, а на четность
# even = [i for i in a if i%2==0]
# odd = [i for i in a if i%2!=0]
# even.sort(reverse=True)
# odd.sort()
# for indx, value in enumerate(h):
#    if value = 1:
#       h[indx] = even.pop(0)    метод pop позоляет удалить элемент после обращения к нему
#    else:
#       h[indx] = odd.pop(0)
# print(h)
