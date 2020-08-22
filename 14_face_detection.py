import cv2

# haar cascade - fast, but not the most accurate
face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

img = cv2.imread('lena.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(img_gray, 1.1, 4)
for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,255,0), 2)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

