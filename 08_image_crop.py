import numpy as np
import cv2

img = cv2.imread('babyyoda.jpg')

print(img.shape)

crop_y = 100
crop_y2 = 400
crop_x = 200
crop_x2 = 600
img_cropped = img[crop_y:crop_y2, crop_x:crop_x2]

cv2.imshow('image',img)
cv2.imshow('image_cropped', img_cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()

