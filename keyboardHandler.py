from lists import pictureSpamCaption, pictureSpamUrl
from bot import bot

import random

@bot.message_handler(content_types=["text"])
def messageHandler(message):
    if message.text == "Поздороваться":
        sayHello(message)
    elif message.text == "Спам":
        spamCommand(message) 


def sayHello(message):
    randomHelloValue = random.randint(0,1)
    if randomHelloValue:
        bot.send_message(message.chat.id, "Привет, я Гринч - похититель рождества")
    else:
        picture = "https://media-1obl-ru.storage.yandexcloud.net/resize_cache/664110/83132dad08c79bfbcc1d891fdcdbb658/iblock/23b/23bec37b72bb484e7333b414ba063ba5.jpg"
        bot.send_photo(message.chat.id, photo = picture , caption="Я Гринч")  

def spamCommand(message):          
    for i in range(0, len(pictureSpamUrl), 1):
        randomCaptionIndex = random.randint(0, len(pictureSpamCaption) - 1) 
        bot.send_photo(message.chat.id, photo=pictureSpamUrl[i], caption=pictureSpamCaption[randomCaptionIndex])
