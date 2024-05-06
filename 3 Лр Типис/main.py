import telebot
from telebot import types
import random

bot = telebot.TeleBot('7165030002:AAESdPWJI7Kf6KJ-BxDuEltveJlNaMm4hqc')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Рассказать факт', callback_data='fact')
    btn2 = types.InlineKeyboardButton('Посмотреть картинку', callback_data='pic')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}! Что тебе интересно?', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'pic')
def send_random_pic(query):
    images = ['cat.jpg', 'cat1.jpg', 'cat2.jpg']
    random_image = random.choice(images)

    markup = types.InlineKeyboardMarkup()
    btn_menu = types.InlineKeyboardButton('Меню', callback_data='menu')
    markup.add(btn_menu)

    with open(random_image, 'rb') as file:
        bot.send_photo(query.message.chat.id, file, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'fact')
def send_fact(query):
    with open('facts.txt', 'r', encoding='utf-8') as file:
        facts = file.read().splitlines()
        random_fact = random.choice(facts)

    markup = types.InlineKeyboardMarkup()
    btn_menu = types.InlineKeyboardButton('Меню', callback_data='menu')
    markup.add(btn_menu)

    bot.send_message(query.message.chat.id, random_fact, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'menu')
def handle_menu_button(query):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Рассказать факт', callback_data='fact')
    btn2 = types.InlineKeyboardButton('Посмотреть картинку', callback_data='pic')
    markup.add(btn1, btn2)
    bot.send_message(query.message.chat.id, 'Что еще тебе интересно?', reply_markup=markup)

@bot.message_handler(commands=['pic'])
def send_random_pic(message):
    images = ['cat.jpg', 'cat1.jpg', 'cat2.jpg']
    random_image = random.choice(images)

    markup = types.InlineKeyboardMarkup()
    btn3 = types.InlineKeyboardButton('Меню', callback_data='menu')
    markup.row(btn3)

    with open(random_image, 'rb') as file:
        bot.send_photo(message.chat.id, file, reply_markup=markup)

@bot.message_handler(commands=['fact'])
def send_random_fact(message):
    with open('facts.txt', 'r', encoding='utf-8') as file:
        facts = file.read().splitlines()
        random_fact = random.choice(facts)

    bot.send_message(message.chat.id, random_fact)

bot.polling(none_stop=True)