import telebot

bot = telebot.TeleBot('5804376761:AAE2BcTI1FJf1kWrY3Et50pr3NMhqvIoL6s')

@bot.message_handler(commands=['start'])
def start(message):
    #mess = f'>Здравствуй 😉, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, 'Приступим 😉', parse_mode='html')

@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == "Привет":
        mess = f'>Здравствуй 😉, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
        bot.send_message(message.chat.id, mess, parse_mode='html')
    elif message.text == "id":
        bot.send_message(message.chat.id, f"Твой ID: {message.from_user.id}", parse_mode='html')
    elif message.text == "photo":
        photo = open('фильтер.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == "абв":
        bot.send_message(message.chat.id, 'Мне нечего Вам ответить, так как я отфильтровал сочетание "абв" и ничего не осталось', parse_mode='html')
    else:
        find_txt = "абв"
        lst = [i for i in message.text.split() if find_txt not in i]
        bot.send_message(message.chat.id, " ".join(lst), parse_mode='html')

bot.polling()
