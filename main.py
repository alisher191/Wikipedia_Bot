import telebot
import wikipedia


wikipedia.set_lang('ru')
TOKEN = ''
bot = telebot.TeleBot(token=TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    text = "Hello! I'm wikipedia bot."
    bot.send_message(message.chat.id, text)

@bot.message_handler(content_types=['text'])
def talk(message):
    text = message.text
    replaced_text = text.replace(' ', '_')

    page = wikipedia.page(replaced_text)

    bot.send_message(message.chat.id, page.summary)


if __name__ == '__main__':
    bot.polling(non_stop=True)
