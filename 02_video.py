import numpy as np
import cv2

VIDEO_FILENAME = 'babyyoda.gif'

cap = cv2.VideoCapture(VIDEO_FILENAME)

FRAME_DELAY = int(1000/20)

while True:
    success, img = cap.read()
    cv2.imshow('Video',img)

    if cv2.waitKey(FRAME_DELAY) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

