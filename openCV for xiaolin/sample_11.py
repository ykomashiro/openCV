import numpy as np
import cv2

cap = cv2.VideoCapture(0)
i = 0
cv2.namedWindow('Camera')
cv2.namedWindow('Thresh Window')

while(True):
    i += 1
    ret, img = cap.read()
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    threshImg = cv2.adaptiveThreshold(
        grayImg, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 49, 0)
    cv2.imshow('Camera', img)
    if i == 5:
        i = 0
        cv2.imshow('Thresh Window', threshImg)
    if cv2.waitKey(25) & 0xff is ord('q'):
        break
cv2.destroyAllWindows()
