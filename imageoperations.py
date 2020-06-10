import cv2
import numpy as np
img=cv2.imread("watch.jpeg",1)
px=img[55,55]
px=[0,0,0]
print(px)
cv2.imshow('image',img)
#ROI region of rthe iumage
roi=img[359:385,200:300]
img[:26,:100]=roi
cv2.imwrite("image_operation.jpg",img)
cv2.imshow("roi",img)
cv2.waitKey(0)
cv2.destroyAllWindows()