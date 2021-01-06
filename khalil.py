import cv2
trained_face_data=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img=cv2.imread('khalil.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
face=trained_face_data.detectMultiScale(gray)
cv2.rectangle(img,(277,101),(277+394,101+394),(0,0,255),2)
cv2.imshow('khalil',img)
cv2.waitKey()
print('stop')
