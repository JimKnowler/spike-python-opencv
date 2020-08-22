import cv2
import numpy as np

img = cv2.imread('babyyoda.jpg')

horizontal = np.hstack((img, img))
vertical = np.vstack((img, img))

cv2.imshow("horiztonal", horizontal)
cv2.imshow('vertical', vertical)

cv2.waitKey(0)