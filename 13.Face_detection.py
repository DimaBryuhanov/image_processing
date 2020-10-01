import numpy as np
import cv2
import random

img = cv2.imread('./images/faces copy.jpeg', 1)

grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
path = './haarcascade_frontalface_default.xml'

face_cascade = cv2.CascadeClassifier(path)
faces = face_cascade.detectMultiScale(grey, scaleFactor=1.05, minNeighbors=5, minSize=(40, 40))
print(len(faces))

for (x,y, w, h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,255, 0), 2)

cv2.imshow("Faces", img)
cv2.waitKey(0)
cv2.destroyAllWindows()