import telebot as tb 
import random

bot = tb.TeleBot('1533100969:AAH49Am82yYTv_QACVXOC2MGxAvz5CdYAC4')
keyboard1 = tb.types.ReplyKeyboardMarkup()
keyboard1.row('Привет', 'Что ты чувствуешь?', 'Хочу музыки!', 'Случайное число','Пока')

keyboard2 = tb.types.ReplyKeyboardMarkup()
keyboard2.row('Мне мечательную', 'Мне мужественную')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет! Я очень рад, что могу поговорить! Я робот и не часто мне пишут. Даже не знаю с чего начать разговор. Наверно поздароваться?', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):

    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет!', reply_markup=keyboard1)
        bot.send_sticker(message.chat.id, 'CAACAgQAAxkBAANCYAgXmH0RgceKO9Bh-ywn70pdQH8AAosAA0tp7hAy1ngHkROcVB4E')

    elif message.text == 'Случайное число':
        intr = random.randint(1, 100)
        bot.send_message(message.chat.id, intr)

    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Пока. (ಥ﹏ಥ)', reply_markup=keyboard1)
        bot.send_sticker(message.chat.id, 'CAACAgQAAxkBAANIYAgXskvdlvtrGMW29dwvAAGwL7mRAAIJDAACS2nuEGsiEfgoHEAXHgQ')

    elif message.text == 'Что ты чувствуешь?':
        a = random.randint(1 , 4)
        st = {
            1:'CAACAgQAAxkBAANMYAgXuSvxDnuCZnogqcN_9Wu4b4oAAgUMAAJLae4QRe6N3v9138IeBA',
            2:'CAACAgQAAxkBAANKYAgXthQh8yZaz5v8zuGIYejkOqMAAgoMAAJLae4QMSSuoTqN1TgeBA',
            3:'CAACAgQAAxkBAANGYAgXsk2iokBhWf9Du2hWAYSTL18AAgIMAAJLae4Q1n9MXxtSjXgeBA',
            4:'CAACAgQAAxkBAANEYAgXrQ5ytT4kiAtZimuMsrlR8UcAAmcBAAJLae4QmfqI_cbNjxceBA'
        }
        bot.send_message(message.chat.id, 'Когда словами не передать, меня спасают стикеры.', reply_markup=keyboard1)
        bot.send_sticker(message.chat.id, st[a])    

    elif message.text == 'Хочу музыки!':
        bot.send_message(message.chat.id, 'О давай!')
        bot.send_message(message.chat.id, 'А какой???', reply_markup=keyboard2)
        bot.send_sticker(message.chat.id, 'CAACAgQAAxkBAANQYAgX20-dspdAt6uksq2qNjNpkXAAAoMAA0tp7hCDSlFyUpGDOB4E')

    elif message.text == 'Мне мечательную':
        bot.send_message(message.chat.id, 'Ждите...', reply_markup=keyboard1)
        audio = open('ob.mp3', 'rb')
        bot.send_audio(message.chat.id, audio)

    elif message.text == 'Мне мужественную':
        bot.send_message(message.chat.id, 'Ждите...', reply_markup=keyboard1)
        audio = open('sum.mp3', 'rb')
        bot.send_audio(message.chat.id, audio)  

    else:
        bot.send_message(message.chat.id, 'Я не часто общаюсь с людьми. И иногда не понимаю их речь. Извените!', reply_markup=keyboard1)
        bot.send_sticker(message.chat.id, 'CAACAgQAAxkBAAIBQWAJTpzM8Jj1g1Kg5dZIXU30xdGzAAK2BwACS2nuEMYCMo5r4qvlHgQ') 
        
bot.polling()