import numpy as np
import cv2

def empty(arg):
    pass

TRACKBARS = 'TrackBars'
cv2.namedWindow(TRACKBARS)
cv2.resizeWindow(TRACKBARS, 640,240)
cv2.createTrackbar('Hue Min', TRACKBARS, 20, 179, empty)
cv2.createTrackbar('Hue Max', TRACKBARS, 80, 179, empty)
cv2.createTrackbar('Sat Min', TRACKBARS, 0, 255, empty)
cv2.createTrackbar('Sat Max', TRACKBARS, 62, 255, empty)
cv2.createTrackbar('Val Min', TRACKBARS, 45, 255, empty)
cv2.createTrackbar('Val Max', TRACKBARS, 255, 255, empty)

img = cv2.imread('babyyoda.jpg')
cv2.imshow('image',img)

imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('hsv', imgHSV)

while True:
    h_min = cv2.getTrackbarPos('Hue Min', TRACKBARS)
    h_max = cv2.getTrackbarPos('Hue Max', TRACKBARS)
    s_min = cv2.getTrackbarPos('Sat Min', TRACKBARS)
    s_max = cv2.getTrackbarPos('Sat Max', TRACKBARS)
    v_min = cv2.getTrackbarPos('Val Min', TRACKBARS)
    v_max = cv2.getTrackbarPos('Val Max', TRACKBARS)

    #print(h_min, h_max, s_min, s_max, v_min, v_max)

    

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    cv2.imshow('mask', mask)

    img_green = cv2.bitwise_and(img, img, mask=mask)
    cv2.imshow('green', img_green)
    
    cv2.waitKey(1)


cv2.destroyAllWindows()

