import cv2
import numpy as np
img1=cv2.imread("main_img_template.jpg",1)
img1grey=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
template=cv2.imread("template.jpg",0)
w,h=template.shape
res = cv2.matchTemplate(img1grey,template,cv2.TM_CCOEFF_NORMED)
threshould=0.8
loc=np.where(res>=threshould)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img1,pt,(pt[0]+w,pt[1]+h),(0,255,255),2)
cv2.imshow("template",im)
cv2.waitKey(0)
cv2.destroyAllWindows()