import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)
img[:] = 255, 0, 0      # B, G, R

width = img.shape[1]
height = img.shape[0]
cv2.line(img, (0,0), (width, height), (0,255,255), 3)
cv2.rectangle(img, (100,100), (400,300), (0,0,255), cv2.FILLED)
cv2.circle(img, (400,50), 30, (255, 255, 0), 5)

cv2.putText(img, 'hello dave', (110,200), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 2)

cv2.imshow("Image", img)

cv2.waitKey(0)