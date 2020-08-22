import numpy as np
import cv2

img = cv2.imread('babyyoda.jpg')
cv2.imshow('image', img)
img_blur = cv2.GaussianBlur(img, (15,15), 0)
cv2.imshow('image blurred',img_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()

