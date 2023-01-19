# Создайте программу для игры с конфетами человек против человека.
# Реализовать игру игрока против игрока в терминале.
# Игроки ходят друг за другом, вписывая желаемое количество конфет.
# Первый ход определяется жеребьёвкой. В конце вывести игрока, который победил

# Условие задачи: На столе лежит 221 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
import random

player1 = input('Введите имя первого игрока: ')
player2 = input('Введите имя второго игрока: ')
candy_total = int(input('Введите общее количество конфет: '))
max_candy = int(input('Введите максимальное количество конфет за 1 ход: '))
first_turn = random.choice([player1, player2])

flag = player1 if first_turn == player1 else player2
while candy_total > 0:
    print(f'Ход игрока {flag}')
    turn = int(
        input(f'Введите желаемое количество конфет от 1 до {max_candy}: '))
    while not 0 < turn <= max_candy:
        print('Вы указали недопустимое количество конфет')
        turn = int(
            input(f'Введите желаемое количество конфет от 1 до {max_candy}: '))
    candy_total = candy_total-turn
    if candy_total > 0:
        print(f'Конфет осталось: {candy_total}')
    else:
        print('Конфеты закончились')
    flag = player2 if flag == player1 else player1
winner = player2 if flag == player1 else player1
print(f'Победил игрок {winner}!')
