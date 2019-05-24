import cv2
import os


def apply_big_eyes(img, message, bot):
    opened_img = cv2.imread(img)
    haar_eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    gray_img = cv2.cvtColor(opened_img, cv2.COLOR_BGR2GRAY)
    eyes = haar_eye_cascade.detectMultiScale(gray_img, scaleFactor=1.3, minNeighbors=6)

    if len(eyes) == 0:
        os.remove("photos/eyeing" + str(message.message_id) + ".jpg")
        bot.send_message(message.chat.id, "Никаких глаз не нашёл, нужен кто-то, кто больше глазеет.")

    elif len(eyes) >= 1:
        crops = []
        for (x, y, w, h) in eyes:
            crop_img = opened_img[y:y + h, x:x + w].copy()
            crop_img = cv2.resize(crop_img, (2 * w, 2 * h))
            crops.append(crop_img)

            # print(x, y, w, h)

        for i in range(len(crops)):

            for (x, y, w, h), i in zip(eyes, range(len(crops))):
                # crops[i] = cv2.resize(crops[i],(2*w,2*h))
                opened_img[y:y + 2 * h, x:x + 2 * w] = crops[i].copy()

        cv2.imwrite("photos/eyed" + str(message.message_id) + ".jpg", opened_img)

        bot.send_message(message.chat.id, f"Я нашёл {len(eyes)} глаз(а)")
        result = "photos/eyed" + str(message.message_id) + ".jpg"
        bot.send_photo(message.chat.id, (open(result, "rb")))
        os.remove("photos/eyeing" + str(message.message_id) + ".jpg")
        os.remove(result)

