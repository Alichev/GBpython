# Вычислить число c заданной точностью d

# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
import math

d = input('Введите степень точности: ')
d_list = d.split(".")
print(d_list)
print(len(d_list[1]))
print("Значение числа ПИ с заданной точностью: ",
      round(math.pi, (len(d_list[1]))))
