import telebot
from telebot.types import Message

TOKEN = '895248757:AAH7tjGZjkiRSyAOCInlSn4F0auuaqD55XE'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Привет! Я Bot the Face Swapper! Пришли мне свою фотку.')


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, 'Я ещё учусь, но рад с тобой поболтать :)')




@bot.message_handler(content_types=['photo'])
def handle_face_swap(message):
    try:
        file_info = bot.get_file(message.photo[len(message.photo)-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        src = file_info.file_path;
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)
        bot.reply_to(message, "Фото добавлено")
    except Exception as e:
        bot.reply_to(message, e)

# #@bot.message_handler(commands=['meme'])
# #def send_meme(message):
#    # bot.send_chat_action(message.chat.id, 'typing')
#     #meme = open('sonic.png', 'rb')
#    # bot.send_photo(message.chat.id, open('sonic.png', 'rb'))
#     meme.close()


#@bot.message_handler(commands=['meme'])
#def send_meme(message):
   # photo = open('sonic.png' in glob.glob('meme/*png'), 'rb')
  #  bot.reply_to(message, photo)

@bot.message_handler(func=lambda message: True)
def send_dialog(message: Message):
    bot.reply_to(message, 'Салют!')

meme = open('sonic.png', 'rb')
bot.send_photo(260747339, meme)

bot.polling(interval=0, timeout=10)