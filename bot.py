import os
from dotenv import load_dotenv
import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from request import dados_brasileirao

load_dotenv(dotenv_path='C:/Users/539555318/Desktop/API-NBA/.venv/.env')
token = os.getenv('TOKEN_TELEGRAM')
brasileirao = dados_brasileirao()

bot = telebot.TeleBot(token)
bot.remove_webhook()

@bot.message_handler(['start', 'help'])
def start(msg:telebot.types.Message):
    bot.reply_to(msg,'Olá!')


@bot.message_handler(['opcoes'])
def botao(mensagem: telebot.types.Message):
    markup = InlineKeyboardMarkup()
    brasileirao = InlineKeyboardButton('Brasileirão', callback_data='botao1')
    markup.add(brasileirao)
    bot.send_message(mensagem.chat.id, 'Escolha uma opção. ', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'botao1':
        dicionario = dados_brasileirao()
        resposta = ""
        for posicao, info in dicionario.items():
            resposta += f"{posicao} {info}\n"
        bot.send_message(call.message.chat.id, resposta)






bot.infinity_polling()