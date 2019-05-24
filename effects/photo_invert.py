#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import os


def apply_invert(photo, message, bot):
    '''
    Inverts the message given
    :param photo: path to an image file
    :param message: the message sent to the bot
    :param bot: telegram bot
    :return: inverted image
    '''
    opened_photo = cv2.imread(photo)
    inved_photo = cv2.bitwise_not(opened_photo)
    cv2.imwrite("photos/inved" + str(message.message_id) + ".jpg", inved_photo)

    result = "photos/inved" + str(message.message_id) + ".jpg"
    bot.send_message(message.chat.id, "Вжух!!!")
    bot.send_photo(message.chat.id, (open(result, "rb")))
    os.remove("photos/inving" + str(message.message_id) + ".jpg")
    os.remove(result)