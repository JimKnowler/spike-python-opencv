import numpy as np
import cv2

def get_contours(img, img_contours):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        
        if area > 100:
            cv2.drawContours(img_contours, cnt, -1, (255,0,0), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            obj_corners = len(approx)
            x, y, w, h = cv2.boundingRect(approx)
            cv2.rectangle(img_contours, (x,y), (x+w, y+h), (0,0,255), 3)

            if obj_corners == 3:
                object_type = 'Tri'
            elif obj_corners == 4:
                aspect_ratio = w/float(h)
                if aspect_ratio > 0.95 and aspect_ratio < 1.05:
                    object_type = 'Square'
                else:
                    object_type = 'Rect'
            else:
                object_type = 'Circle'
            
            cv2.putText(img_contours, object_type, (x+(w//2)-10, y+(h//2)+10), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,0,0), 1)

img = cv2.imread('shapes.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (7,7), 1)
img_canny = cv2.Canny(img_blur, 50, 50)

img_contours = img.copy()
get_contours(img_canny, img_contours)

img_blank = np.zeros_like(img_gray)

def gray_to_bgr(img):
    return cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

horizontal1 = np.hstack((img, gray_to_bgr(img_gray), gray_to_bgr(img_blur)))
horizontal2 = np.hstack((gray_to_bgr(img_canny), img_contours, gray_to_bgr(img_blank)))
vertical = np.vstack((horizontal1, horizontal2))
vertical = cv2.resize(vertical, (int(vertical.shape[1]/2), int(vertical.shape[0]/2)))
cv2.imshow('image',vertical)
cv2.waitKey(0)
cv2.destroyAllWindows()


