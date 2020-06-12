import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()
   
    greyscale=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    laplacian = cv2.Laplacian(greyscale,cv2.CV_64F)
    solbex=cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=5)
    solbey=cv2.Sobel(frame,cv2.CV_64F,0,1,ksize=5)
    edge=cv2.Canny(frame,100,100)
    cv2.imshow('Original',frame)
    cv2.imshow('edges',edge)
    #cv2.imshow('solbex',solbex)
    #cv2.imshow('solbey',solbey)
 

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()