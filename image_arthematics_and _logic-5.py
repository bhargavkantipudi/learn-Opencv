import cv2
import numpy as np
img1=cv2.imread("img1.png",1)
img2=cv2.imread("img2.png",1)
pyimg=cv2.imread("mainlogo.png",1)
#add=img1+img2
#add=cv2.add(img1,img2)
#weighted=cv2.addWeighted(img1,0.6,img2,0.4,0)
rows,cols,channels=pyimg.shape
roi=img1[:rows,:cols]
img2gray=cv2.cvtColor(pyimg,cv2.COLOR_BGR2GRAY)
ret,mask=cv2.threshold(img2gray,220,255,cv2.THRESH_BINARY_INV)
maskinv=cv2.bitwise_not(mask)
img1_bg=cv2.bitwise_and(roi,roi,mask=maskinv)
img2_fg=cv2.bitwise_and(pyimg,pyimg,mask=mask)
dsk=cv2.add(img1_bg,img2_fg)
img1[:rows,:cols]=dsk
cv2.imshow("Mask",mask)
cv2.imshow("Mask Inv",maskinv)
cv2.imshow("img1bg",img1_bg)
cv2.imshow("img2  fg ",img2_fg)
cv2.imshow("Final img",img1)
cv2.imwrite("final_img.png",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()