# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

# a = int(input('Введите число: '))
# if a > 0:
#     array = [i for i in range(-a, a+1)]
# else:
#     array = [i for i in range(a, -a+1)]
# print(array)

def func(N):
    if N > 0:
        for i in range(-N, N+1):
            print(i, end=' ')
    else:
        for i in range(N, -N+1):
            print(i, end=' ')


num = int(input('Введите число: '))
func(num)
