import cv2
import numpy as np
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while(cap.isOpened):
    ret, frame = cap.read()
    if ret == True:
        out.write(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(100) & 0xFF is ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()
