# скачиваем библиотеку pip install pytelegrambotapi
import telebot
from telebot import types

bot = telebot.TeleBot("6108342756:AAGci6lokj3LYzBmb_q3n_iC0F0fh9863H4")


@bot.message_handler(commands=['start'])  # вызов функции по команде в списке
def start(message):    # отправка сообщения (кому отправляем, что отправляем(str))
    bot.send_message(message.chat.id, f"/button")


def summa(message):
    summ = sum(list(map(int, message.text.split())))
    bot.send_message(message.chat.id, str(summ))
    button(message)


@bot.message_handler(commands=["button"])
def button(message):
    markup = types.ReplyKeyboardMarkup(
        resize_keyboard=True)  # создание клавиатуры
    but1 = types.KeyboardButton("сумма")  # создание кнопок
    but2 = types.KeyboardButton("разность")
    markup.add(but1)  # добавление кнопок
    markup.add(but2)  # добавление кнопок
    # вызов функции если тип сообщения - текст
    bot.send_message(message.chat.id, "Выбери ниже", reply_markup=markup)


@bot.message_handler(content_types=["text"])
def controller(message):
    if message.text == "сумма":
        # вызов функции на ответ пользователя
        bot.send_message(message.chat.id, "введи два числа для суммы")
        bot.register_next_step_handler(message, summa)
    elif message.text == "разность":
        pass


bot.infinity_polling()
