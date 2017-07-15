import telebot
import config
import random

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, я бот который шифрует пароли' +
                     ' (пока поддерживается только латынь -> leet).' +
                     ' Отправь свой пароль сообщением и я его зашифрую!')

@bot.message_handler(content_types=['audio', 'document', 'photo', 'sticker',
'video', 'voice', 'location', 'contact', 'new\_chat\_participant',
'left\_chat\_participant', 'new\_chat\_title', 'new\_chat\_photo',
'delete\_chat\_photo', 'group\_chat\_created'])
def error(message):
    msg_list = ['Семь раз отмерь, но, ввод все равно неправильный',
                'Если гора не идет к Магомеду, значит ввод неправильный',
                'Ввод не волк, но он неправильный',
                'Труд человека кормит, а неправильный ввод портит',
                'Терпенье и труд все правильно введут',
                'Красна птица пером, а человек правильным вводом',
                'Одна голова хорошо, а правильный ввод еще лучше',
                'Купил мужик шляпу, а у вас ввод неправильный']
    rnd_msg = random.choice(msg_list)
    bot.send_message(message.chat.id, rnd_msg +
                     '. Нужны букаффки, а вы, извиняюсь, ввели что-то нечитаемое')

    
@bot.message_handler(content_types=["text"])
def crypting(message):
    data = message.text

    Leet_EN = ['4', '8', 'see', 'cl', '3', 'ph',
           '6', 'auch', 'ai', 'gei', 'IX', '1',
           'IVI', 'en', '0', 'q', '9', 'l2',
           'z', '7', 'IJ', 'U', 'VV', 'eks', 'uai', '2']

    crypted_pass = ''
    for i in range(len(data)):        
        if(ord(data[i]) >= 48) and (ord(data[i]) <= 57):
            crypted_pass += data[i]
        elif ((ord(data[i]) >= 65 and ord(data[i]) <= 90)
        or (ord(data[i]) >= 97 and ord(data[i]) <= 122)):
            for j in range(len(Leet_EN)):
                if (j == ord(data[i]) - 97) or (j == ord(data[i]) - 65):
                    crypted_pass += Leet_EN[j]
        else:
            crypted_pass = 'Ввод недопустимых символов! Попробуйте еще раз'
            break
        
    bot.send_message(message.chat.id, crypted_pass)

bot.polling()

