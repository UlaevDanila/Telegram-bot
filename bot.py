import telebot  
import pytz


TOKEN = "5674764733:AAEWr8-DDP3zkRkoXcASJacRrEcBFMaTOiA"
TIMEZONE = "Europe/Moscow"
TIMEZONE_COMMON_NAME = "Moscow"

P_TIMEZONE = pytz.timezone(TIMEZONE)

bot = telebot.TeleBot(TOKEN)