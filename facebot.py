import telebot
from telebot.types import Message

TOKEN = 'TELEGRAM BOT TOKEN'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Привет! Я Bot the Face Swapper! Спроси, что я умею командой /help.')


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, 'Я ещё учусь, но рад с тобой поболтать :)')


#@bot.message_handler(commands=['meme'])
#def send_meme(message):
   # photo = open('sonic.png' in glob.glob('meme/*png'), 'rb')
  #  bot.reply_to(message, photo)


@bot.message_handler(func=lambda message: True)
def send_dialog(message: Message):
    bot.reply_to(message, 'Салют!')


bot.polling(interval=0, timeout=10)
