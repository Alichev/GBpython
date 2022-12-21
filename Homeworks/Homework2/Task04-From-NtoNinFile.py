# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

N = int(input('Введите число N: '))
list_num = [i for i in range(-N, N+1)]
print(list_num)
file = open("File1.txt", "r")
result = 1
for i in file:
    result = result*list_num[int(i)]
print('Произведение элементов: ', result)
