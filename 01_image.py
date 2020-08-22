import numpy as np
import cv2

img = cv2.imread('babyyoda.jpg')

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# image output
#cv2.imwrite('output_babyyoda_gray.png', img)

