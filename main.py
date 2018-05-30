import numpy as np
import cv2
# import imutils
# from imutils.object_detection import non_max_suppression
import time


def search(filepath):
    img = cv2.imread(filepath)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    classifier = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
    rects = classifier.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=4, minSize=(30, 30),
                                        flags=cv2.CASCADE_SCALE_IMAGE)
    for (x, y, w, h) in rects:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.imwrite(filepath[:(len(filepath) - 4)] + '_result.png', img)
    return len(rects)


filename = input('input name(path) of photo: ')
try:
    f = search(filename)
except Exception:
    f = 0
if f == 0:
    print('i found 0 faces')
else:
    if f == 1:
        print('i found 1 face')
    else:
        print('i found ' + str(f) + ' faces')
img = cv2.imread(filename[:(len(filename) - 4)] + '_result.png')
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
