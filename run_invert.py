#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2


def apply_invert(photo, message):
    '''
    Inverts the message given
    :param photo: path to an image file
    :param message:
    :return: inverted image
    '''
    opened_photo = cv2.imread(photo)
    inved_photo = cv2.bitwise_not(opened_photo)
    cv2.imwrite("photos/inved" + str(message.message_id) + ".jpg", inved_photo)
    cv2.destroyAllWindows()


# apply_invert(photo)

# inverted = apply_invert(photo)
#
# cv2.imshow("inverted", inverted)
# cv2.waitKey(0)
# cv2.destroyAllWindows()