import os
import telebot
from telebot import types
from telebot.types import Message
import cv2
from invert import apply_invert
import requests

TOKEN = '895248757:AAH7tjGZjkiRSyAOCInlSn4F0auuaqD55XE'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Привет! Я Bot the Face Swapper! Пришли мне свою фотку.')


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, 'Сейчас я могу:\n''/meme - прислать свой любимый мем :)\n')


@bot.message_handler(commands=['meme'])
def send_meme(message):
    # meme = open('sonic.png', 'rb')

    with open('sonic.png', 'rb') as meme:
        bot.send_photo(message.chat.id, meme)


@bot.message_handler(commands=['invert'])
def start_invert(message):
    msg = bot.send_message(message.chat.id, 'Хорошо. Пришли мне фотку :)')
    bot.register_next_step_handler(msg, send_invert)


def send_invert(message):
    if bot.message_handler(content_types=['photo']):
        try:
            file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
            # filePath = file_info.file_path
            downloaded_file = bot.download_file(file_info.file_path)

            # src = file_info.file_path
            with open("photos/inving" + str(message.chat.id) + ".jpg", 'wb') as new_file:
                new_file.write(downloaded_file)
            apply_invert("photos/inving" + str(message.chat.id) + ".jpg", message)
            result = "results/inved" + str(message.chat.id) + ".jpg"
            bot.send_photo(message.chat.id, (open(result, "rb")))

            #     inverted_photo = apply_invert(str(message.chat.id) + ".jpg")
            #     bot.send_photo(message.chat.id, inverted_photo)
            # os.remove(str(message.chat.id) + ".jpg")
            # src = file_info.file_path
            # with open(src, 'wb') as new_file:
            #     photo = new_file.write(downloaded_file)
                # opened_photo = cv2.imread(photo)
                # inverted_photo = apply_invert(opened_photo)

    #         file_info = bot.get_file(message.photo[len(message.photo)-1].file_id)
    #         downloaded_file = bot.download_file(file_info.file_path)
    #
    #         src = file_info.file_path;
    #         with open(downloaded_file, 'wb') as new_photo:
    #         photo = cv2.imread(new_photo)
    #         inverted_photo1 = cv2.bitwise_not(new_photo)
    #         inverted_photo2 = cv2.imwrite("inverted_photo1", inverted_photo1)
    #         # inverted_photo = apply_invert(new_photo)
    #         inverted_photo = apply_invert(downloaded_file)
    #         bot.send_photo(message.chat.id, inverted_photo)
        except Exception as e:
            bot.send_message(message.chat.id, e)
    else:
        bot.send_message(message.chat.id, "Что-то я не понял...")


@bot.message_handler(content_types=['photo'])
def handle_face_swap(message):
    try:
        file_info = bot.get_file(message.photo[len(message.photo)-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        with open("photos/new_file.jpg", 'wb') as new_file:
            new_file.write(downloaded_file)
        bot.send_message(message.chat.id, "Фото добавлено")
    except Exception as e:
        bot.send_message(message.chat.id, e)


@bot.message_handler(func=lambda message: True)
def send_dialog(message: Message):
    bot.send_message(message.chat.id, 'Салют!')


# def apply_invert(img):
#     photo = cv2.imread(src)
#     return cv2.bitwise_not(photo)

bot.polling(interval=0, timeout=10)
