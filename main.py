from commands import sendMeme, helpCommand, startCommand
from keyboardHandler import messageHandler
from telebot import types
from dialog import startDialog
from bot import bot

import random

bot.polling(non_stop=True)
