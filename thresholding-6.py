import cv2
import numpy as np
img=cv2.imread("bookpage.jpg",1)
greysacle=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval,threshold=cv2.threshold(img,12,255,cv2.THRESH_BINARY)

retval2,bg_threshold=cv2.threshold(greysacle,12,255,cv2.THRESH_BINARY)
gaus=cv2.adaptiveThreshold(greysacle,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
cv2.imshow("test",bg_threshold)
cv2.imshow("test",threshold)
cv2.imshow("Bookpage Before",img)
cv2.imshow("FGaus adaptive thress",gaus)

cv2.waitKey(0)
cv2.destroyAllWindows()