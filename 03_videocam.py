import numpy as np
import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)     # width
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)     # height
#cap.set(cv2.CAP_PROP_BRIGHTNESS, 100)    # brightness

FRAME_DELAY = int(1)

while True:
    success, img = cap.read()
    cv2.imshow('Video',img)

    if cv2.waitKey(FRAME_DELAY) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

