#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import os


def apply_face_swap(img, message, bot):
    opened_img = cv2.imread(img)
    gray_img = cv2.cvtColor(opened_img, cv2.COLOR_BGR2GRAY)
    haar_face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    faces = haar_face_cascade.detectMultiScale(gray_img, scaleFactor=1.3, minNeighbors=5)

    if len(faces) == 0:
        os.remove("photos/swapping" + str(message.message_id) + ".jpg")
        bot.send_message(message.chat.id, "Я не нашёл лиц :( Попробуй кинуть другую фотку.")
    elif len(faces) == 1:
        os.remove("photos/swapping" + str(message.message_id) + ".jpg")
        bot.send_message(message.chat.id, "Нашёл только одно лицо,\n а один в поле - не воин.")
    elif len(faces) > 1:
        crops = []
        for (x, y, w, h) in faces:
            crop_img = opened_img[y:y + h, x:x + w].copy()
            crops.append(crop_img)
            print(x, y, w, h)

        for (x, y, w, h) in faces:
            coords = {'A': x, 'B': y, 'C': w, 'D': h}
            co = []
            co += [coords[key] for key in sorted(coords)]

            if co == faces[0].tolist():
                print(co)
                crop1 = cv2.resize(crops[1], (w, h))  # TODO
                opened_img[y:y + h, x:x + w] = crop1.copy()
            else:
                crop2 = cv2.resize(crops[0], (w, h))
                opened_img[y:y + h, x:x + w] = crop2.copy()

        cv2.imwrite("photos/swapped" + str(message.message_id) + ".jpg", opened_img)

        result = "photos/swapped" + str(message.message_id) + ".jpg"
        bot.send_photo(message.chat.id, (open(result, "rb")))

        os.remove("photos/swapping" + str(message.message_id) + ".jpg")
        os.remove(result)
