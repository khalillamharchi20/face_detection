import cv2
trained_face_data=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
webcam=cv2.VideoCapture(0)
while True:
    succes , frame =webcam.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face_det=trained_face_data.detectMultiScale(gray)
    for k in face_det:
        (x,y,w,h)=k
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow('khalil',frame)
    cv2.waitKey(1)