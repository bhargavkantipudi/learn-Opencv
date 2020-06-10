import cv2
import numpy as np
img=cv2.imread("watch.jpeg",1)
cv2.line(img,(0,0),(100,100),(0,255,255),15)
cv2.rectangle(img,(10,10),(150,150),(255,0,0),5)
cv2.circle(img,(150,150),(150),(0,255,0),5)
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)*10
cv2.polylines(img, [pts], True, (0,255,255), 3)
 
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,"Text inserted",(200,200),font,1,(0,255,0),1)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()