import telebot

TOKEN = '352296018:AAFfRpE0zsO-6qo5TZHH6bQ8j6gqf9FIA_I'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, 'кек шрек')

if __name__ == '__main__':
     bot.polling(none_stop=True)

