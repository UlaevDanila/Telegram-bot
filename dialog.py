from bot import bot

@bot.message_handler(commands=["dialog"])
def startDialog(message):
    bot.send_message(message.chat.id, "Давай начнём с простого. Как тебя зовут?")
    bot.register_next_step_handler(message, getName)

def getName(message):
    if message.text.find(" ") == -1: 
        stringToSend = "Привет," + " " + message.text
        bot.send_message(message.chat.id, stringToSend)
        bot.register_next_step_handler(message, checkNegativeMessage)
    else:
        bot.send_message(message.chat.id, "Я тебя не понимаю. давай ещё раз")
        startDialog(message)


def checkNegativeMessage(message):
    if message.text == "Нет":
        bot.send_message(message.chat.id, "Нового года нет")
    bot.register_next_step_handler(message, checkOpositeMessage)

def checkOpositeMessage(message):
    if message.text == "Ты врёшь":
        bot.send_message(message.chat.id, "Есть такое")
