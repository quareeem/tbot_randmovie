import os
from dotenv import load_dotenv
import telebot as tb
from main import get_random

load_dotenv()
API_KEY = os.getenv('API_KEY')
bot = tb.TeleBot(API_KEY)


@bot.message_handler(commands=['random'])
def random_film(msg):
    res = get_random()
    bot.send_message(msg.chat.id, f'{res}')

@bot.message_handler(commands=['close'])
def close(msg):
    markup = tb.types.ReplyKeyboardRemove()
    bot.send_message(msg.chat.id, 'menu has closed', reply_markup=markup)

@bot.message_handler(commands=['start'])
def menu(msg):
    markup = tb.types.ReplyKeyboardMarkup(row_width=2)
    btn1 = tb.types.KeyboardButton(f'/random')
    btn2 = tb.types.KeyboardButton(f'/close')
    markup.add(btn1, btn2)
    bot.send_message(msg.chat.id, text='type /random to decide what film to watch', reply_markup=markup)

bot.polling()
