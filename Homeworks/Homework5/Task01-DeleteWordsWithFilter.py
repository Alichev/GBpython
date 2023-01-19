# Сделать с помощью filter, lambda
# Напишите программу, удаляющую из текста все слова, содержащие "абв".


str = 'апол прабвзз 78/7 3абв333 юю2рвд аб абв'
list1 = str.split()
# list2 = list(filter(lambda x: False if 'абв' in x.lower() else True, list1)) -учли регистр
list2 = list(filter(lambda x: 'абв' not in x, list1))
print(list2)
str2 = " ".join(list2)
print(str2)
