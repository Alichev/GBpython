def get_operation():
    operation = int(input(
        "Введите 0 - внести данные в телефонную книгу,\n 1 - выгрузить данные из телефонной книги,\n 2 - отсортировать данные по именам,\n 3 - вывести данные по Имени и Фамилии: \n"))
    return operation


def get_person_info():
    id = int(input('Введите ID сотрудника: '))
    surname = input('Введите ФАМИЛИЮ сотрудника: ')
    name = input('Введите ИМЯ сотрудника: ')
    phone = int(input('Введите ТЕЛЕФОН сотрудника: '))
    comment = input('Введите КОММЕНТАРИЙ: ')
    data = f"{id}, {surname}, {name}, {phone}, {comment}\n"
    with open('phone_book.txt', 'a') as file:
        file.write(data)
    print('Данные внесены')


def print_all_data():
    with open('phone_book.txt', 'r') as file:
        for line in file.readlines():
            print(line, end="")


def print_names():
    with open('phone_book.txt', 'r') as file:
        for line in file.readlines():
            temp = line.split(",")
            print(f'ФАМИЛИЯ: {temp[1]}, ИМЯ: {temp[2]}')


def sort_names():
    with open('phone_book.txt', 'r+') as file:
        lst_with_str = file.readlines()
        lst_with_lst = []
        for line in lst_with_str:
            temp = line.split(",")
            lst_with_lst.append(temp)
        lst_with_lst = sorted(lst_with_lst, key=lambda x: x[1])
        file.seek(0)
        for strng in lst_with_lst:
            file.write(",".join(strng))
        print('Сортировка произведена')
