import numpy as np
import cv2

img = cv2.imread(r'project\openCV\openCV for xiaolin\hzxc.jpg', 1)
b, g, r = cv2.split(img)
cv2.namedWindow('Source Image')
cv2.namedWindow('Blue Channel')
cv2.namedWindow('Green Channel')
cv2.namedWindow('Red Channel')
cv2.imshow('Source Image', img)
cv2.imshow('Blue Channel', b)
cv2.imshow('Green Channel', g)
cv2.imshow('Red Channel', r)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)
cv2.namedWindow('HSV')
cv2.namedWindow('H')
cv2.namedWindow('S')
cv2.namedWindow('V')
cv2.imshow('HSV', hsv)
cv2.imshow('H', h)
cv2.imshow('S', s)
cv2.imshow('V', v)

cv2.waitKey(0)
cv2.destroyAllWindows()
