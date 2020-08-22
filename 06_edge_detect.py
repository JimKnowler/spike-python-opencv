import numpy as np
import cv2

img = cv2.imread('babyyoda.jpg')
img_canny = cv2.Canny(img, 150, 200)

kernel = np.ones((5,5), np.uint8)
img_dilation = cv2.dilate(img_canny, kernel, iterations=1)

img_eroded = cv2.erode(img_dilation, kernel, iterations=1)

cv2.imshow('image', img)
cv2.imshow('image edge', img_canny)
cv2.imshow('image dilation', img_dilation)
cv2.imshow('image eroded', img_eroded)
cv2.waitKey(0)
cv2.destroyAllWindows()

