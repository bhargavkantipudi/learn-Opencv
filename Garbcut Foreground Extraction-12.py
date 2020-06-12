import cv2
import numpy as np
import matplotlib.pyplot as plt
cap=cv2.VideoCapture(0)
_,frame=cap.read()
mask=np.zeros(frame.shape[:2],np.uint8)
bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)
while True:
    _,frame=cap.read()
  
    rect = (270,150,200,200)
    cv2.imshow("frame",frame)
    cv2.grabCut(frame,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
    mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
    img = frame*mask2[:,:,np.newaxis]
    cv2.imshow("masked",img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()