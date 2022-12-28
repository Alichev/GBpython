# Задайте строку из набора чисел.
# Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.


nums = input('Введите числа через пробел: ')
list_nums = nums.split(" ")
print(list_nums)   # list_nums = list(map(int, list_nums))
max = int(list_nums[0])
min = int(list_nums[0])

for i in range(len(list_nums)):   # print(max(list_nums, min(list_nums))
    if int(list_nums[i]) > max:
        max = int(list_nums[i])
    if int(list_nums[i]) < min:
        min = int(list_nums[i])
print(f'Максимум: {max}, минимум: {min}')
