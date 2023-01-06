from keyboardHandler import sayHello, spamCommand
from lists import memeList
from telebot import types


from bot import bot

import random

@bot.message_handler(commands=["start"])
def startCommand(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Поздороваться")
    button2 = types.KeyboardButton("Спам")
    markup.add(button1,button2)
    bot.send_message(message.chat.id, "Привет", reply_markup=markup)

@bot.message_handler(commands=["meme"])
def sendMeme(message):
    randomMemeIndex = random.randint(0,len(memeList) - 1)
    bot.send_photo(message.chat.id, photo = memeList[randomMemeIndex], caption="Рандомный мем")

@bot.message_handler(commands=["help"])
def helpCommand(message):
    bot.send_message(message.chat.id, "Для начала работы напиши /start\n Для диалога с ботом напишите /dialog\n Для спам атаки напишите /spam\n Для получения дозы мемов напишите /meme\n"  )


@bot.message_handler(content_types=["text"])
def messageHandler(message):
    if message.text == "Поздороваться":
        sayHello(message)
    elif message.text == "Спам":
        spamCommand(message)    






