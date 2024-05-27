import cv2


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
nose_cascade = cv2.CascadeClassifier('haarcascade_mcs_nose.xml')
mouth_cascade = cv2.CascadeClassifier('haarcascade_mcs_mouth.xml')
eyes_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')


img = cv2.imread('photo.jpg')


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


faces = face_cascade.detectMultiScale(gray, 1.1, 4)
mouth = mouth_cascade.detectMultiScale(gray, 1.1, 4)
eyes = eyes_cascade.detectMultiScale(gray, 1.1, 4)
nose = nose_cascade.detectMultiScale(gray, 1.1, 4)


for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)


cv2.imshow('img', img)
cv2.waitKey()
