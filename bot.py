import os
from dotenv import load_dotenv
import telebot


load_dotenv(dotenv_path='C:/Users/539555318/Desktop/API-NBA/.venv/.env')
token = os.getenv('TOKEN_TELEGRAM')


bot = telebot.TeleBot(token)
bot.remove_webhook()

@bot.message_handler(['start', 'help'])
def start(msg:telebot.types.Message):
    bot.reply_to(msg,'Olá!')









bot.infinity_polling()