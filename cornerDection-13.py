import cv2
import numpy as np
img=cv2.imread("corner.jpg",1)
imggrey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imggrey=np.float32(imggrey)
corners=cv2.goodFeaturesToTrack(imggrey,20000,0.01,8)
corners=np.int0(corners)
for corner in corners:
    x,y=corner.ravel()
    cv2.circle(img,(x,y),3,255,-1)
cv2.imshow("Original",img)
cv2.waitKey(0)
cv2.destroyAllWindows()