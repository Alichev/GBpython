import telebot

bot = telebot.TeleBot("6185995644:AAGqPN3xhB2R1oemO9EbvwwNV0hS3GJz7Nc")


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id, f"Привет, это калькулятор!")
    mrk = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    key1 = telebot.types.KeyboardButton("Рациональные числа")
    key2 = telebot.types.KeyboardButton("Комплексные числа")
    mrk.add(key1)
    mrk.add(key2)
    bot.send_message(
        message.chat.id, "Выбери ниже, с какими числами будем работать", reply_markup=mrk)
    bot.register_next_step_handler(message, choose_type)


def choose_type(message):
    global num_type
    if message.text == "Рациональные числа":
        num_type = True
    else:
        num_type = False
    input1number(message)


def input1number(message):
    bot.send_message(message.chat.id, f"Введите первое число")
    bot.register_next_step_handler(message, num1new)


def num1new(message):
    global num1
    num1 = message.text
    bot.send_message(
        message.chat.id, f"Введите второе число")
    bot.register_next_step_handler(message, num2new)


def num2new(message):
    global num2
    num2 = message.text
    if num_type == True:
        bot.send_message(
            message.chat.id, f"Вы выбрали рациональные числа. Доступные операции: + - * / % //")
        mrk = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        key1 = telebot.types.KeyboardButton("+")
        key2 = telebot.types.KeyboardButton("-")
        key3 = telebot.types.KeyboardButton("*")
        key4 = telebot.types.KeyboardButton("/")
        key5 = telebot.types.KeyboardButton("%")
        key6 = telebot.types.KeyboardButton("//")
        mrk.add(key1)
        mrk.add(key2)
        mrk.add(key3)
        mrk.add(key4)
        mrk.add(key5)
        mrk.add(key6)
        bot.send_message(
            message.chat.id, "Выбери операцию ниже", reply_markup=mrk)
        bot.register_next_step_handler(message, operation)
    else:
        bot.send_message(
            message.chat.id, f"Вы выбрали комплексные числа. Доступные операции: + - * /")
        mrk = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        key1 = telebot.types.KeyboardButton("+")
        key2 = telebot.types.KeyboardButton("-")
        key3 = telebot.types.KeyboardButton("*")
        key4 = telebot.types.KeyboardButton("/")
        mrk.add(key1)
        mrk.add(key2)
        mrk.add(key3)
        mrk.add(key4)
        bot.send_message(
            message.chat.id, "Выбери операцию ниже", reply_markup=mrk)
        bot.register_next_step_handler(message, operation)


def operation(message):
    global op
    op = message.text
    if num_type == True:
        if op == "+":
            res = int(num1) + int(num2)
            bot.send_message(message.chat.id, f'Результат: {res}')
        elif op == "-":
            res = int(num1) - int(num2)
            bot.send_message(message.chat.id, f'Результат: {res}')
        elif op == "*":
            res = int(num1) * int(num2)
            bot.send_message(message.chat.id, f'Результат: {res}')
        elif op == "/":
            res = int(num1) / int(num2)
            bot.send_message(message.chat.id, f'Результат: {res}')
        elif op == "%":
            res = int(num1) % int(num2)
            bot.send_message(message.chat.id, f'Результат: {res}')
        elif op == "//":
            res = int(num1) // int(num2)
            bot.send_message(message.chat.id, f'Результат: {res}')
    else:
        if op == "+":
            res = complex(num1) + complex(num2)
            bot.send_message(message.chat.id, f'Результат: {res}')
        elif op == "-":
            res = complex(num1) - complex(num2)
            bot.send_message(message.chat.id, f'Результат: {res}')
        elif op == "*":
            res = complex(num1) * complex(num2)
            bot.send_message(message.chat.id, f'Результат: {res}')
        elif op == "/":
            res = complex(num1) / complex(num2)
            bot.send_message(message.chat.id, f'Результат: {res}')


bot.infinity_polling()
