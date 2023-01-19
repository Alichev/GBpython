# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Модуль сжатия:
# Для чисел:
# Входные данные: 111112222334445
# Выходные данные: 5142233415
# Также должно работать и для букв:
# Входные данные: AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE
# Выходные данные: 6A1F2D7C1A17E
# (5 - количество единиц, далее сама единица, 4 - количество двоек, далее сама двойка и т.д)
# Модуль восстановления работет в обратную сторону - из строки выходных данных, получить строку входных данных.

def rle(text):
    result = ""
    count = 0
    prev_symb = text[0]
    for symb in text:
        if symb != prev_symb:
            result += f'{count}{prev_symb}'
            prev_symb = symb
            count = 1
        else:
            count += 1
    result += f'{count}{prev_symb}'
    return result


def rleback(text):
    result = ""
    digit = True
    count = 0
    for symb in text:
        if digit:
            count = int(symb)
            digit = False
        else:
            result += count*symb
            digit = True
    return result


text = '1111112223333334555'
print(f'Оригинальный текст: {text}')
rle_text = rle(text)
print(f'Сжатый текст: {rle_text}')

orig_text = rleback(rle_text)
print(f'Восстановленный текст: {orig_text}')
