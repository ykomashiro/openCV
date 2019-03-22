import cv2
import numpy as np

img = cv2.imread('project\openCV\data\hand1.jpg')
# 首先进行高斯滤波 滤除干扰
blurImg = cv2.GaussianBlur(img, (9, 9), 0)

cannyImg = cv2.Canny(blurImg, 50, 130)

cv2.namedWindow('Canny')
cv2.namedWindow('Blur')
cv2.imshow('Canny', cannyImg)
cv2.imshow('Blur', blurImg)

cv2.waitKey()
cv2.destroyAllWindows()