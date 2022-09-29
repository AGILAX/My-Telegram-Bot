from cgitb import html
import telebot
from telebot import types

bot = telebot.TeleBot('5412971012:AAED2iKNBl9tdCzRuDwHh0dKDMAjUBHpZ9s')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Hello, <b>{message.from_user.first_name} {message.from_user.last_name}</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == 'Hello':
        bot.send_message(message.chat.id, 'Hi', parse_mode='html')
    elif message.text == 'id':
        bot.send_message(message.chat.id, f'Твой ID: {message.from_user.id}', parse_mode='html')
    elif message.text == 'photo':
        photo = open('Types of data Python.PNG', 'rb')
        bot.send_photo(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id, 'i dont understand you (', parse_mode='html')


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Wow, nice one')


@bot.message_handler(commands=['Resume'])
def Resume(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('View Resume', url='https://hh.ru/resume/deb664b6ff0b1edeec0039ed1f704369684e68'))
    bot.send_message(message.chat.id, 'Go to site', reply_markup=markup)


@bot.message_handler(commands=['help'])
def Resume(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    resume = types.KeyboardButton('Resume')
    start = types.KeyboardButton('Start')
    markup.add(resume, start, )
    bot.send_message(message.chat.id, 'Boom', reply_markup=markup)



bot.polling(none_stop=True)
