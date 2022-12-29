# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности

import collections
list_str = input('Введите последовательность чисел через пробел: ')
list_num = list(map(int, list_str.split()))
print(list_num)
final_list = []
for i in list_num:
    if i not in final_list:
        final_list.append(i)
print('Список уникальных элементов последовательности: ', final_list)

# ИЛИ (если речь о списке элементов последовательности, представленных в единственном экземпляре)

# list_str = input('Введите последовательность чисел через пробел: ')
# list_num = list(map(int, list_str.split()))
# print(list_num)
# final2_list = []
# list_counter = collections.Counter(list_num)
# print(list_counter)
# for number, count in list_counter.items():
#     if count == 1:
#         final2_list.append(number)
# print('Список элементов, не имеющих повторов: ', final2_list)
