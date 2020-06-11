from imutils.video import FPS
import numpy as np
import argparse
import imutils
import cv2


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt2.xml')
cap = cv2.VideoCapture("rtsp://admin:ThaiRun1234@192.168.1.104:554/Streaming/channels/101") #"rtsp://admin:ThaiRun1234@192.168.1.104:554/Streaming/channels/101"
fps = cap.get(cv2.CAP_PROP_FPS)
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))


while (True):
    ret, frame = cap.read()
    frame = imutils.resize(frame, width= 720)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for(x,y,w,h) in faces:
        print(x,y,w,h)
        roi_gray = gray[y:y+h, x:x+w] #(ycoord_start - ycoord_end)
        roi_color = frame[y:y+h, x:x+w]
     
            
    
        color = (255,0,0) #BGR 
        stroke = 2
        end_cord_x = x + w
        end_cord_y = y + h
        cv2.rectangle(frame, (x,y),(end_cord_x, end_cord_y), color, stroke)


    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
