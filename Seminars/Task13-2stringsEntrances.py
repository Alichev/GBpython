# Напишите программу, в которой пользователь будет задавать две строки, а программа -
# определять количество вхождений одной строки в другой.
# Пример:
# Строка - "dabccabccabcc"
# Подстрока - "ab"
# Количество вхождений - 3

text = input('Введите текст: ')
findtext = input('Введите текст, который будем искать: ')
i = 0
# чтобы не доходил до последнего эл-та строки (т.к. может вылететь из диапазона)
for char in range(0, len(text)-len(findtext)+1):
    if text[char: char+len(findtext)] == findtext:
        i = i+1
print(i)


# print('Количество вхождений - ', text.count(findtext))
