import numpy as np
import cv2

img = cv2.imread('cards.jpg')

# from inspecting the image
# TL 553, 248
# TR 813, 204
# BL 666, 585
# BR 967, 539

pts1 = np.float32([
    [553, 245], 
    [813, 204], 
    [666, 585], 
    [967, 539]
])

width, height = 250, 350

pts2 = np.float32([
    [0,0],
    [width,0],
    [0,height],
    [width,height]
])

matrix = cv2.getPerspectiveTransform(pts1, pts2)

img_warped = cv2.warpPerspective(img, matrix, (width,height))

cv2.imshow('image',img)
cv2.imshow('image warped', img_warped)
cv2.waitKey(0)
cv2.destroyAllWindows()
