import view


def start():
    oper = view.get_operation()
    if oper == 0:
        view.get_person_info()
    elif oper == 1:
        view.print_all_data()
    elif oper == 2:
        view.sort_names()
    elif oper == 3:
        view.print_names()
    else:
        print("Нет такого варианта")
