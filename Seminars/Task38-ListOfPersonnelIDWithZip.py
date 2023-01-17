# Имеется список id сотрудников из 10 элементов, каждый id - случайное число от 1 до 100
# Имеется список имен сотрудников из 10 элементов
# Сопоставьте каждому имени сотрудника его id, и выведите получившийся список.
# Выведете имена сотрудников, получившие нечетное id. Решить с помощью zip,filter,lambda

import random
id = [random.randint(1, 100) for i in range(10)]
names = ['ivanov', 'petrov', 'sidorov', 'kovalev', 'sergeev',
         'borzov', 'buzova', 'efremov', 'ivleeva', 'kirienko']
lst = list(zip(id, names))
print(lst)

# lst_odd = list(filter(lambda x: x[0]%2==1,lst))
lst_odd = [elem[1] for elem in lst if elem[0] % 2 != 0]
print(lst_odd)
