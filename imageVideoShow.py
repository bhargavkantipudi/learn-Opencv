import cv2
import numpy as np
import matplotlib.pyplot as plt
cap=cv2.VideoCapture(0)
w=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc=cv2.VideoWriter_fourcc(*'MJPG')
out=cv2.VideoWriter("output.avi",fourcc,20.0,(w,h))
while True:
    ret,frame=cap.read()
    grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    out.write(frame)
    cv2.imshow("frame",frame)
    cv2.imshow("grey",grey)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()