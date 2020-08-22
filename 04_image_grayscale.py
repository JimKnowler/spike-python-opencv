import numpy as np
import cv2

img = cv2.imread('babyyoda.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('image',img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

