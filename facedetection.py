import numpy as np
import cv2
img=cv2.imread("test2.jpg",1)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        
cv2.imshow('img',img)
cv2.imwrite("output.jpg",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
