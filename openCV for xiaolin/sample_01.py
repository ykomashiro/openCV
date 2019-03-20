import cv2
import numpy as np
index = 0
imgname = 0
cap = cv2.VideoCapture(0)
while True:
    index += 1
    ret, img = cap.read()
    cv2.imshow('camera', img)
    if index == 100:
        imgname += 1
        if imgname >= 50:
            imgname = 0
        fname = str(imgname)+'.jpg'
        cv2.imwrite(fname, img)
        print(fname+' saved')
        index = 0
    if cv2.waitKey(100) & 0xFF is ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
