import telebot
import dict
from telebot import types

token = '5558466723:AAGSo9_H8WY0I1nKza6bibz_gyjiYAK6sg0'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def welcome_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Распечатка на формате А3")
    item2 = types.KeyboardButton("Распечатка на формате А4")
    item3 = types.KeyboardButton("Фото на документы")
    item4 = types.KeyboardButton("Изготовление банеров")
    item5 = types.KeyboardButton("Ламинация")
    item6 = types.KeyboardButton("Меня ничего не интересует(закончить)")
    item7 = types.KeyboardButton("Контакты")
    item8 = types.KeyboardButton("Изготовление кружек")
    item9 = types.KeyboardButton("Изготовление визиток")
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    markup.add(item4)
    markup.add(item5)
    markup.add(item8)
    markup.add(item9)
    markup.add(item7)
    markup.add(item6)
    bot.send_message(message.chat.id, dict.welcome,
                     reply_markup=markup)


@bot.message_handler(content_types='text')
def Check(message):
    if message.text == "Распечатка на формате А3":
        A3_paper_print(message)
    elif message.text == "Распечатка на формате А4":
        A4_paper_print(message)
    elif message.text == "Фото на документы":
        photos_of_the_documents(message)
    elif message.text == "Изготовление банеров":
        make_baner(message)
    elif message.text == "Ламинация":
        make_lamination(message)
    elif message.text == "Меня ничего не интересует(закончить)":
        end(message)
    elif message.text == "Распечатка на плотной(фото) бумаге А3":
        print_photo_paper_A3_1(message)
    elif message.text == "Распечатка на обычной бумаге А3":
        print_photo_paper_A3_2(message)
    elif message.text == "Распечатка на плотной(фото) бумаге А4":
        print_photo_paper_A4_1(message)
    elif message.text == "Распечатка на обычной бумаге А4":
        print_photo_paper_A4_2(message)
    elif message.text == "Назад в меню":
        welcome_message(message)
    elif message.text == "Контакты":
        contact(message)
    elif message.text == "Изготовление кружек":
        cap(message)
    elif message.text == "Изготовление визиток":
        make_business_card(message)


@bot.message_handler(content_types='text')
def A3_paper_print(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Распечатка на плотной(фото) бумаге А3")
    item2 = types.KeyboardButton("Распечатка на обычной бумаге А3")
    item3 = types.KeyboardButton("Назад в меню")
    item4 = types.KeyboardButton("Меня ничего не интересует(закончить)")
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    markup.add(item4)
    bot.send_message(message.chat.id, 'Печать на какой бумаге Вас интересует?',
                     reply_markup=markup,)


@bot.message_handler(content_types='text')
def A4_paper_print(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Распечатка на плотной(фото) бумаге А4")
    item2 = types.KeyboardButton("Распечатка на обычной бумаге А4")
    item3 = types.KeyboardButton("Назад в меню")
    item4 = types.KeyboardButton("Меня ничего не интересует(закончить)")
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    markup.add(item4)
    bot.send_message(message.chat.id, "Печать на какой бумаге Вас интересует?",
                     reply_markup=markup,)


@bot.message_handler(content_types='text')
def photos_of_the_documents(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Назад в меню")
    item2 = types.KeyboardButton("Меня ничего не интересует(закончить)")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(message.chat.id, dict.print_photos_of_the_documents,
                     reply_markup=markup)


@bot.message_handler(content_types='text')
def make_baner(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Назад в меню")
    item2 = types.KeyboardButton("Меня ничего не интересует(закончить)")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(message.chat.id, dict.print_baner, reply_markup=markup)


@bot.message_handler(content_types='text')
def make_lamination(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Назад в меню")
    item2 = types.KeyboardButton("Меня ничего не интересует(закончить)")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(message.chat.id, dict.lamination, reply_markup=markup)


@bot.message_handler(content_types='text')
def print_photo_paper_A3_1(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Назад в меню")
    item2 = types.KeyboardButton("Меня ничего не интересует(закончить)")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(message.chat.id, dict.print_A3_photo_paper,
                     reply_markup=markup)


@bot.message_handler(content_types='text')
def print_photo_paper_A3_2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Назад в меню")
    item2 = types.KeyboardButton("Меня ничего не интересует(закончить)")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(message.chat.id, dict.print_A3_paper, reply_markup=markup)


@bot.message_handler(content_types='text')
def print_photo_paper_A4_1(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Назад в меню")
    item2 = types.KeyboardButton("Меня ничего не интересует(закончить)")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(message.chat.id, dict.print_A4_photo_paper,
                     reply_markup=markup)


@bot.message_handler(content_types='text')
def print_photo_paper_A4_2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Назад в меню")
    item2 = types.KeyboardButton("Меня ничего не интересует(закончить)")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(message.chat.id, dict.print_A4_paper, reply_markup=markup)


@bot.message_handler(content_types='text')
def end(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("/start")
    markup.add(item1)
    bot.send_message(message.chat.id, 'Будем Ждать Вас в следующий раз!',
                     reply_markup=markup)


@bot.message_handler(content_types='text')
def contact(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Назад в меню")
    item2 = types.KeyboardButton("Меня ничего не интересует(закончить)")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(message.chat.id, dict.contact, reply_markup=markup)


@bot.message_handler(content_types='text')
def cap(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Назад в меню")
    item2 = types.KeyboardButton("Меня ничего не интересует(закончить)")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(message.chat.id, dict.make_cap, reply_markup=markup)


@bot.message_handler(content_types='text')
def make_business_card(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Назад в меню")
    item2 = types.KeyboardButton("Меня ничего не интересует(закончить)")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(message.chat.id, dict.print_business_card,
                     reply_markup=markup)


if __name__ == '__main__':
    bot.infinity_polling()
