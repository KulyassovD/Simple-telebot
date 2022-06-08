import telebot
from telebot import types
import random
from main2 import music, lst

token = '5245735845:AAFYdOEm_CiUKf1APvII6v7H476gZxz2roU'
bot = telebot.TeleBot(token)




@bot.message_handler(commands=['start'])
def welcome_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Развлеки меня")
    item2 = types.KeyboardButton("У меня все хорошо)")
    item4 = types.KeyboardButton("Ничего, я тут случайно)")
    markup.add(item1)
    markup.add(item2)
    markup.add(item4)
    bot.send_message(message.chat.id, 'Привет. Что я могу для тебя сделать? ',
                     reply_markup=markup)

@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text == "Развлеки меня":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Ссылка была удалена из-за личной инфы")
        item2 = types.KeyboardButton("Держи песенку")
        item3 = types.KeyboardButton("Нашу фоточку хочешь посмотреть?")
        item4 = types.KeyboardButton("Назад в меню")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        markup.add(item4)
        bot.send_message(message.chat.id, 'Давай посмотрим что я умею)', reply_markup=markup,)
    elif message.text == "У меня все хорошо)":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item = types.KeyboardButton("Назад в меню")
        markup.add(item)
        bot.send_message(message.chat.id, f'Я рад, что у тебя все хорошо. Но у меня'
                                           'пока тут ограниченный функционал', reply_markup=markup,)
    elif message.text == "Ничего, я тут случайно)":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("/start")
        markup.add(item1)
        bot.send_message(message.chat.id, 'Хорошо, до встречи!',
                         reply_markup=markup)
    else:
        message_reply_1(message)


@bot.message_handler(content_types='text')
def message_reply_1(message):
    if message.text == "Ссылка была удалена из-за личной инфы":
        random_slt = random.choices(lst)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.InlineKeyboardButton("Ещё! Хочу еще!",)
        item2 = types.KeyboardButton("Приятно) На сегодня хватит)")
        item3 = types.KeyboardButton("Назад в меню")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        bot.send_message(message.chat.id, random_slt, reply_markup=markup,)
    elif message.text == "Ничего не хочу, давай закончим":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("/start")
        markup.add(item1)
        bot.send_message(message.chat.id, 'Хорошо, до встречи!',
                         reply_markup=markup)
    elif message.text == "Держи песенку":
        random_music = random.choices(music)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.InlineKeyboardButton("Еще песенок в студию!",)
        item2 = types.KeyboardButton("Послушали и хватит")
        item3 = types.KeyboardButton("Назад в меню")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        bot.send_message(message.chat.id, random_music, reply_markup=markup)
    elif message.text == "Назад в меню":
        welcome_message(message)
    else:
        message_reply_2(message)


def message_reply_2(message):
    if message.text == "Ещё! Хочу еще!":
        a = random.choices(lst)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.InlineKeyboardButton("Ещё! Хочу еще!",)
        item2 = types.KeyboardButton("Приятно) На сегодня хватит)")
        item3 = types.KeyboardButton("Назад в меню")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        bot.send_message(message.chat.id, a, reply_markup=markup)
    elif message.text == "Приятно) На сегодня хватит)":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("/start")
        markup.add(item1)
        bot.send_message(message.chat.id, 'Мило поболтали) Приходи еще!',
                         reply_markup=markup)
    elif message.text == "Еще песенок в студию!":
        random_music = random.choices(music)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.InlineKeyboardButton("Еще песенок в студию!",)
        item2 = types.KeyboardButton("Послушали и хватит")
        item3 = types.KeyboardButton("Назад в меню")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        bot.send_message(message.chat.id, random_music, reply_markup=markup)
    elif message.text == "Послушали и хватит":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("/start")
        markup.add(item1)
        bot.send_message(message.chat.id, 'Мило поболтали) Приходи еще!',
                         reply_markup=markup)

    


if __name__ == '__main__':
    bot.infinity_polling()
