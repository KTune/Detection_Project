#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import telebot
import time

from effects.photo_invert import apply_invert
from effects.big_eyes import apply_big_eyes
from effects.face_swap import apply_face_swap

from useful_lists import meme_files


TOKEN = '<bot_token>'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет! Я Photo Booth Bot - Фотобудка!\n"
                                      "Хочешь узнать, что я могу? Кидай мне /help")


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, "Сейчас я умею:\n" "/invert - инвертировать изображение(делать негатив)\n" 
                                      "/eyes - увеличивать глаза на фотке(немножко страшно)\n"
                                      "/meme - присылать свои любимые мемы :)\n"
                                      "А ещё я могу менять лица на фотках местами - делать face swap. Это так весело!\n"
                                      "Для этого просто отправь мне фото, на котором 2 и больше лиц :)")


@bot.message_handler(commands=['meme'])
def send_meme(message):

    with open(random.choice(meme_files), 'rb') as meme:
        bot.send_photo(message.chat.id, meme)


@bot.message_handler(commands=['invert'])
def start_invert(message):
    msg = bot.send_message(message.chat.id, "Хорошо. Пришли мне фотку :)")
    bot.register_next_step_handler(msg, send_invert)


def send_invert(message):
    if bot.message_handler(content_types=['photo']):
        try:
            file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
            downloaded_file = bot.download_file(file_info.file_path)

            with open("photos/inving" + str(message.message_id) + ".jpg", 'wb') as new_file:
                new_file.write(downloaded_file)
            apply_invert("photos/inving" + str(message.message_id) + ".jpg", message, bot)
        except Exception as e:
            print(e)
            bot.send_message(message.chat.id, "Ой, шарики за ролики заехали. Что-то не так.")
    else:
        bot.send_message(message.chat.id, "Моя магия почему-то не сработала. Попробуй снова /invert")


@bot.message_handler(commands=['eyes'])
def start_invert(message):
    msg = bot.send_message(message.chat.id, "Присылай фотку, я готов :)")
    bot.register_next_step_handler(msg, send_eyes)


def send_eyes(message):
    if bot.message_handler(content_types=['photo']):
        try:
            file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
            downloaded_file = bot.download_file(file_info.file_path)

            with open("photos/eyeing" + str(message.message_id) + ".jpg", 'wb') as new_file:
                new_file.write(downloaded_file)
            apply_big_eyes("photos/eyeing" + str(message.message_id) + ".jpg", message, bot)
        except Exception as e:
            print(e)
            bot.send_message(message.chat.id, "Ой, шарики за ролики заехали. Что-то не так.")
    else:
        bot.send_message(message.chat.id, "Ничччего не понимаю. Давай начнём сначала - /eyes")


@bot.message_handler(content_types=['photo'])
def handle_face_swap(message):
    try:
        file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        with open("photos/swapping" + str(message.message_id) + ".jpg", 'wb') as new_file:
            new_file.write(downloaded_file)
        apply_face_swap("photos/swapping" + str(message.message_id) + ".jpg", message, bot)
    except Exception as e:
        print(e)
        bot.send_message(message.chat.id, "Ой, шарики за ролики заехали. Что-то не так.")


@bot.message_handler(func=lambda message: True)
def send_dialog(message):
    bot.send_message(message.chat.id, "Щёлк")


bot.polling(interval=0, timeout=10)


