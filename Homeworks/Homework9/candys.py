# Создайте программу для игры с конфетами человек против человека.
# Реализовать игру игрока против игрока в терминале. Игроки ходят друг за другом,
# вписывая желаемое количество конфет. Первый ход определяется жеребьёвкой.
# В конце вывести игрока, который победил

# Условие задачи: На столе лежит 221 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.

# В качестве дополнительного усложнения можно:
# a) Добавьте игру против бота ( где бот берет рандомное количество конфет от 0 до 28)

# b) Подумайте как наделить бота ""интеллектом""
# (есть алгоритм, позволяющий выяснить какое количесвто конфет необходимо брать,
# чтобы гарантированно победить, соответственно внедрить этот алгоритм боту )

import telebot
from telebot import types
import random
from random import randint

sweets = 221
max_sweets = 30
flag = None
bot = telebot.TeleBot("6034925377:AAGF84sNp_VVwrVnXIegfFRqFVN6bSfh8sQ")


@bot.message_handler(commands=['start'])
def start(message):
    global flag
    bot.send_message(
        message.chat.id, f'Добро пожаловать в игру в конфетки )))')
    bot.send_message(
        message.chat.id, f'На столе {sweets} конфет в начале игры')
    flag = random.choice(["user", "bot"])
    if flag == "user":
        bot.send_message(message.chat.id, 'Первый ход ваш!')
    else:
        bot.send_message(message.chat.id, 'Первым ходит бот!')
    controller(message)


def controller(message):
    global flag
    if sweets > 0:
        if flag == "user":
            bot.send_message(
                message.chat.id, f'Введите количество конфет от 0 до {max_sweets}')
            # должна быть последней командой в функции, чтобы дождался ответа пользователя
            bot.register_next_step_handler(message, user_input)
        else:
            bot_input(message)
    else:
        flag = "user" if flag == "bot" else "bot"
        if flag == "user":
            bot.send_message(
                message.chat.id, 'Игра окончена, вы победили, поздравляем!')
        else:
            bot.send_message(
                message.chat.id, 'Победил бот, а Вам повезет в другой раз!')


def user_input(message):
    global sweets, flag
    user_turn = int(message.text)
    sweets = sweets-user_turn
    bot.send_message(message.chat.id, f'Осталось {sweets} конфет')
    flag = "user" if flag == "bot" else "bot"
    controller(message)


def bot_input(message):
    global sweets, flag
    if sweets <= max_sweets:
        bot_turn = randint(0, sweets)
    else:
        bot_turn = randint(0, max_sweets)
    sweets = sweets-bot_turn
    bot.send_message(message.chat.id, f'Бот забирает {bot_turn} конфет')
    bot.send_message(message.chat.id, f'Осталось {sweets} конфет')
    flag = "user" if flag == "bot" else "bot"
    controller(message)


bot.infinity_polling()
