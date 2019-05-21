import cv2
import telebot
from telebot.types import Message

# photo = "sonic.png"


def apply_invert(photo, message):
    opened_photo = cv2.imread(photo)
    inved_photo = cv2.bitwise_not(opened_photo)
    cv2.imwrite("results/inved" + str(message.chat.id) + ".jpg", inved_photo)
    cv2.destroyAllWindows()


# apply_invert(photo)

# inverted = apply_invert(photo)
#
# cv2.imshow("inverted", inverted)
# cv2.waitKey(0)
# cv2.destroyAllWindows()