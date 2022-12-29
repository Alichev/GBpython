# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов

data1 = open('file1.txt', 'w')
data1.writelines('5*x**3+12*x**2+2*x')
data1.close()
data2 = open('file2.txt', 'w')
data2.writelines('11*x**2+74*x')
data2.close()
data3 = open('file1.txt', 'r')
first = str((data3.readline()).split())
data3.close()
data4 = open('file2.txt', 'r')
second = str((data4.readline()).split())
data4.close()

print(f'{first} + {second}')

data5 = open('final_file.txt', 'w')
data5.writelines(f'{first}+{second}')
data5.close()
