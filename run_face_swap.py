import cv2
import sys

for arg in sys.argv[1:]:
    test1 = cv2.imread(arg) #TODO rename, argparse, check path
    test0 = cv2.imread(arg)


def convertToRGB(img): #TODO в мэйн
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)



#gray_img = cv2.cvtColor(test1, cv2.COLOR_BGR2GRAY)



def face_swap(img):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
     #TODO rename и вынести в файл
    haar_face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    faces = haar_face_cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=5)




    crops = []
    for (x, y, w, h) in faces:
        crop_img = test1[y:y+h, x:x+w].copy()
        crops.append(crop_img)
        print(x, y, w, h)



    for (x, y, w, h) in faces:
        coords = {'A': x, 'B': y, 'C': w, 'D': h}
        co = []
        co += [coords[key] for key in sorted(coords)]

        if co == faces[0].tolist():
            print(co)
            crop1 = cv2.resize(crops[1], (w, h)) #TODO
            test1[y:y + h, x:x + w] = crop1.copy()
        else:
            crop2 = cv2.resize(crops[0], (w, h))
            test1[y:y + h, x:x + w] = crop2.copy()

        cv2.imwrite('swapped_faces.png', test1)




face_swap(test1)




#for (x, y, w, h) in faces:
#    cv2.rectangle(test0, (x, y), (x+w, y+h), (0, 0, 255), 10)



#cv2.imwrite('detected_faces.png', test0)