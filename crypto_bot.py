import telebot
import config
import random
import dictionary

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, dictionary.hello)

@bot.message_handler(content_types=['audio', 'document', 'photo', 'sticker',
'video', 'voice', 'location', 'contact', 'new\_chat\_participant',
'left\_chat\_participant', 'new\_chat\_title', 'new\_chat\_photo',
'delete\_chat\_photo', 'group\_chat\_created'])
def error(message):
    rnd_msg = random.choice(dictionary.msg_list)
    bot.send_message(message.chat.id, rnd_msg + dictionary.letter_err)

    
@bot.message_handler(content_types=["text"])
def crypting(message):
    data = message.text
    crypted_pass = ''
    
    for i in range(len(data)):        
        if (ord(data[i]) >= 48) and (ord(data[i]) <= 57):
            crypted_pass += data[i]
        elif (ord(data[i]) >= 65 and ord(data[i]) <= 90):
            j = chr(ord(data[i]) + 32)
            crypted_pass += dictionary.Leet_EN[j]
        elif (ord(data[i]) >= 97 and ord(data[i]) <= 122):
            crypted_pass += dictionary.Leet_EN[data[i]]
        else:
            crypted_pass = 'Ввод недопустимых символов! Попробуйте еще раз'
            break
       
    bot.send_message(message.chat.id, crypted_pass)

bot.polling()

