import cv2

# photo = cv2.imread("sonic.png")

def apply_invert(img):
    return cv2.bitwise_not(img)

# inverted = apply_invert(photo)
#
# cv2.imshow("inverted", inverted)
# cv2.waitKey(0)
# cv2.destroyAllWindows()