import telebot
import webbrowser
from telebot import types
bot = telebot.TeleBot('7103302089:AAHjQgCYSMtaU_qtTMpuCC_zsjroJJRHnVg')
@bot.message_handler(commands=['site', 'web', 'website'])
def site(message):
    webbrowser.open('https://neurotech.ru/')

@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Перейти на сайт', url='https://google.com'))
    bot.reply_to(message, 'Ашалееть', reply_markup=markup)

@bot.message_handler(commands=['start', 'hello', 'poop'])
def main(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}')

@bot.message_handler()
def main(message):
    if message.text.lower()=='help':
        bot.send_message(message.chat.id, '<h3> Support Neurotech +79085602460 </h3>')
    elif message.text.lower()=='id':
        bot.send_message(message.chat.id, f'Номер идентификатора: {message.from_user.id}')

bot.polling(none_stop=True)