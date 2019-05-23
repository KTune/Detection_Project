import cv2

def convertToRGB(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

def big_eyes(img):
    haar_eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    eyes = haar_eye_cascade.detectMultiScale(gray_img, scaleFactor=1.3, minNeighbors=6)

    crops = []
    for (x, y, w, h) in eyes:
        crop_img = img[y:y + h, x:x + w].copy()
        crop_img = cv2.resize(crop_img, (2 * w, 2 * h))
        crops.append(crop_img)

        print(x, y, w, h)


    for i in range(len(crops)):

        for (x, y, w, h), i in zip(eyes, range(len(crops))):
            # crops[i] = cv2.resize(crops[i],(2*w,2*h))
            img[y:y + 2 * h, x:x + 2 * w] = crops[i].copy()

        cv2.imwrite('large_eyes.png', convertToRGB(img))
            