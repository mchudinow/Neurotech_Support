'''
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Перейти на сайт')
    markup.row(btn1)
    btn2 = types.KeyboardButton('Удалить фото')
    btn3 = types.KeyboardButton('Изменить текст')
    markup.row(btn2, btn3)
    file = open('./Compact_Neuro.png', 'rb')
    bot.send_photo(message.chat.id, file, reply_markup=markup)
    #bot.send_photo(message.chat.id, 'Привет', reply_markup=markup)
    #bot.send_message(message.chat.id, 'Привет', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)
def on_click(message):
    if message.text =='Перейти на сайт':
        bot.send_message(message.chat.id, 'Web open!')
    elif message.text == 'Удалить фото':
        bot.send_message(message.chat.id, 'Was deleted')


@bot.message_handler(commands=['site', 'web', 'website'])
def site(message):
    webbrowser.open('https://neurotech.ru/')


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Перейти на сайт', url='https://google.com'))
    markup.add(types.InlineKeyboardButton('Удалить фото', callback_data='delete'))
    markup.add(types.InlineKeyboardButton('Изменить текст', callback_data='edit'))
    bot.reply_to(message, 'Ашалееть', reply_markup=markup)

@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1=types.InlineKeyboardButton('Перейти на сайт', url='https://google.com')
    markup.row(btn1)
    btn2=types.InlineKeyboardButton('Удалить фото', callback_data='delete')
    btn3=types.InlineKeyboardButton('Изменить текст', callback_data='edit')
    markup.row(btn2, btn3)
    bot.reply_to(message, 'Какого...', reply_markup=markup)
@bot.message_handler(commands=['hope'])
def main(message):
    bot.send_message(message.chat.id,'Все получится, братик')
@bot.message_handler(commands=['star', 'hello', 'poop'])
def main(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}')

@bot.message_handler()
def main(message):
    if message.text.lower()=='help':
        bot.send_message(message.chat.id, 'Support Neurotech +79085602460')
    elif message.text.lower()=='id':
        bot.send_message(message.chat.id, f'Номер идентификатора: {message.from_user.id}')


import telebot
from telebot import types, callback_data

bot = telebot.TeleBot('7103302089:AAHjQgCYSMtaU_qtTMpuCC_zsjroJJRHnVg')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton('Ответы на вопросы', callback_data='questions')
    btn2 = types.InlineKeyboardButton('Документация по приборам', callback_data='docs')
    btn3 = types.InlineKeyboardButton('Технический специалист', callback_data='tech',
                                      url='https://web.telegram.org/k/#@NeuroSupportTeam')
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id,
                     "Добрый день, вы обратились к службе технической поддержки Нейротех. Данный бот содержит ответы частые вопросы пользователей, решения проблем с эксплуатацией и ПО, а такеже возможностью обращения к техническому персоналу научно-медицинской фирмы для оказания помощи.",
                     reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'questions')
def questions_handler(call):
    message = call.message
    chat_id = message.chat.id
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton('Компакт Нейро', callback_data='call1')
    btn2 = types.InlineKeyboardButton('Нейрополиграф', callback_data='call2')
    btn3 = types.InlineKeyboardButton('Синапсис', callback_data='call3')
    btn4 = types.InlineKeyboardButton('БОС Кинезис', callback_data='call4')
    btn5 = types.InlineKeyboardButton('Кинезис Brainbit', callback_data='call5')
    btn6 = types.InlineKeyboardButton('Кинезис Callibri', callback_data='call6')
    btn7 = types.InlineKeyboardButton('БОС Колибри Стоматологический', callback_data='call7')
    btn8 = types.InlineKeyboardButton('БОС Колибри Стоматологический', callback_data='call8')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
    if callback_data != 'call8':
        bot.send_message(chat_id, "Выберите тип продукта из списка", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "Вы вернулись в меню", reply_markup=None)


@bot.callback_query_handler(func=lambda call: call.data == 'docs')
def button_handler(call):
    message = call.message
    chat_id = message.chat.id
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton('У енота', callback_data='call4')
    btn2 = types.InlineKeyboardButton('В голове', callback_data='call5')
    btn3 = types.InlineKeyboardButton('Сделать дыру', callback_data='call6')
    markup.add(btn1, btn2, btn3)
    bot.send_message(chat_id, "Можно", reply_markup=markup)


bot.polling(none_stop=True)
'''
import telebot
from telebot import types, callback_data

bot = telebot.TeleBot('7103302089:AAHjQgCYSMtaU_qtTMpuCC_zsjroJJRHnVg')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton('Ответы на вопросы', callback_data='questions')
    btn2 = types.InlineKeyboardButton('Документация по приборам', callback_data='docs')
    btn3 = types.InlineKeyboardButton('Технический специалист', callback_data='tech',
                                      url='https://web.telegram.org/k/#@NeuroSupportTeam')
    markup.add(btn1, btn2, btn3)
    text = (f"Добрый день, {message.chat.first_name} !\n\n"\
            f"Вы обратились к службе технической поддержки Нейротех.\n\n"\
            f"Данный бот содержит ответы частые вопросы пользователей, решения проблем с эксплуатацией и ПО,\n"\
            f"а такеже возможностью обращения к техническому персоналу научно-медицинской фирмы для оказания помощи.")
    file = open('./logo.png', 'rb')
    #bot.send_message(message.chat.id, text, reply_markup=markup,  parse_mode="HTML")
    bot.send_photo(message.chat.id, file, caption=text, reply_markup=markup,  parse_mode="HTML")

@bot.callback_query_handler(func=lambda call: True)
def menu_back(call):
    if call.data == 'questions': #Вопросы по продуктам
        message = call.message
        chat_id = message.chat.id
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton('Компакт Нейро', callback_data='call1')
        btn2 = types.InlineKeyboardButton('Нейрополиграф', callback_data='call2')
        btn3 = types.InlineKeyboardButton('Синапсис', callback_data='call3')
        btn4 = types.InlineKeyboardButton('БОС Кинезис', callback_data='call4')
        btn5 = types.InlineKeyboardButton('Кинезис Brainbit', callback_data='call5')
        btn6 = types.InlineKeyboardButton('Кинезис Callibri', callback_data='call6')
        btn7 = types.InlineKeyboardButton('БОС Колибри Стоматологический', callback_data='call7')
        btn8 = types.InlineKeyboardButton('Вернуться в меню', callback_data='menu')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(chat_id, "Выберите тип продукта из списка", reply_markup=markup)

    if call.data == 'call1': #Вопросы по Компакт нейро
        message = call.message
        chat_id = message.chat.id
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton('Вопросы по работе с программой', callback_data='call14')
        btn2 = types.InlineKeyboardButton('Наложение электродов', callback_data='call15')
        btn3 = types.InlineKeyboardButton('Не подключается прибор', callback_data='call16')
        btn4 = types.InlineKeyboardButton('Ошибка доступа к БД', callback_data='call17')
        btn5 = types.InlineKeyboardButton('Не рабоатет фотостимулятор', callback_data='call18')
        btn6 = types.InlineKeyboardButton('Помеховый сигнал', callback_data='call19')
        btn7 = types.InlineKeyboardButton('Вопросы по работе с программой', callback_data='call20')
        btn8 = types.InlineKeyboardButton('Вернуться в меню', callback_data='menu')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        file = open('./Compact_Neuro.png', 'rb')
        text = ('Частые вопросы по прибору:\n\n '
                '<b>Компакт Нейро</b>')
        bot.send_photo(chat_id, file,caption=text, reply_markup=markup,  parse_mode="HTML")
    if call.data == 'call2': #Вопросы по прибору: Нейрополиграф
        message = call.message
        chat_id = message.chat.id
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton('Вопросы по работе с программой', callback_data='call14')
        btn2 = types.InlineKeyboardButton('Наложение электродов', callback_data='call15')
        btn3 = types.InlineKeyboardButton('Не подключается прибор', callback_data='call16')
        btn4 = types.InlineKeyboardButton('Ошибка доступа к БД', callback_data='call17')
        btn5 = types.InlineKeyboardButton('Не рабоатет фотостимулятор', callback_data='call18')
        btn6 = types.InlineKeyboardButton('Помеховый сигнал', callback_data='call19')
        btn7 = types.InlineKeyboardButton('Вопросы по работе с программой', callback_data='call20')
        btn8 = types.InlineKeyboardButton('Прибор не видит Bleutooth', callback_data='call21')
        btn8 = types.InlineKeyboardButton('Вернуться в меню', callback_data='menu')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(message.chat.id,"Наиболее часто задаваемые вопросы пользователей по прибору Компакт Нейро:", reply_markup=markup)


    if call.data == 'menu': #Стартовое меню
        message = call.message
        chat_id = message.chat.id
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton('Ответы на вопросы', callback_data='questions')
        btn2 = types.InlineKeyboardButton('Документация по приборам', callback_data='docs')
        btn3 = types.InlineKeyboardButton('Технический специалист', callback_data='tech',
                                          url='https://web.telegram.org/k/#@NeuroSupportTeam')
        markup.add(btn1, btn2, btn3)
        text = f"Главное меню: \n\n" \
           f"Если у вас возникли вопросы по использованию прибора или программного обеспечения компании Нейротех нажмите кнопку: \n\n <b>Ответы на вопросы</b>\n\n" \
           f"Для ознакомления с документацией по продуктам компании нажмите кнопку: \n\n <b>Документация по приборам</b>\n\n" \
            f"Если Бот не смог решить вашу проблему или у вас остались вопросы нажмите кнопку: \n\n <b>Техническая поддержка</b>\n\n"
        file = open('./logo.png', 'rb')

        bot.send_photo(chat_id, file, caption=text, reply_markup=markup,  parse_mode="HTML")

    if call.data == 'docs': #Приборы с документацией
        message = call.message
        chat_id = message.chat.id
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton('Компакт Нейро', callback_data='call8')
        btn2 = types.InlineKeyboardButton('Нейрополиграф', callback_data='call9')
        btn3 = types.InlineKeyboardButton('Синапсис', callback_data='call10')
        btn4 = types.InlineKeyboardButton('БОС Кинезис', callback_data='call11')
        btn5 = types.InlineKeyboardButton('Кинезис Brainbit', callback_data='call12')
        btn6 = types.InlineKeyboardButton('Кинезис Callibri', callback_data='call13')
        btn7 = types.InlineKeyboardButton('БОС Колибри Стоматологический', callback_data='call14')
        btn8 = types.InlineKeyboardButton('Вернуться в меню', callback_data='menu')
        markup.add(btn1, btn2, btn3, btn4, btn4, btn5, btn6, btn7, btn8)
        bot.send_message(chat_id, "Выберите программный продукт", reply_markup=markup)
    # Теперь можно просто писать через if call.data=="Название колбэка кнопки и отображать то что надо"

    if call.data == 'call8': #комментарий к док копакт
        message = call.message
        chat_id = message.chat.id
        bot.send_message(message.chat.id, "манюнянямонюнени")

    if call.data == 'call17': #ошибка бд комп
        message = call.message
        chat_id = message.chat.id
        doc = open('Instuction.pdf', 'rb')
        text = 'Нажмите на файл. чтобы скачать инструкцию'
        bot.send_document(chat_id, doc, caption=text, parse_mode="HTML")



bot.polling(none_stop=True)