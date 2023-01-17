# Напишите программу на Python для поиска пересечения двух заданных массивов с помощью Lambda.
# [1, 2, 3, 5, 7, 8, 9, 10]
# [1, 2, 4, 8, 9]

list1 = [1, 2, 3, 5, 7, 8, 9, 10]
list2 = [1, 2, 4, 8, 9]
# a = list(filter((lambda x: True if x in list1) else False, list2))
a = list(filter((lambda x: x in list1), list2))
print(a)
