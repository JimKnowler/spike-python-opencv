import numpy as np
import cv2

img = cv2.imread('babyyoda.jpg')

print(img.shape)

img_resize = cv2.resize(img, (100,100))
print(img_resize.shape)

cv2.imshow('image',img_resize)
cv2.waitKey(0)
cv2.destroyAllWindows()

