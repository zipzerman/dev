from imutils.video import FPS
import numpy as np
import argparse
import imutils
import cv2
@vectorize(['float32(float32, float32)'], target='cuda')

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt2.xml')

#rtsp://admin:ThaiRun1234@192.168.1.104:554/Streaming/channels/101
0
stream = cv2.VideoCapture("rtsp://admin:ThaiRun1234@192.168.1.104:554/Streaming/channels/101")
fps = FPS().start()

while (True):
    (grabbed, frame) = stream.read()

    if not grabbed :
        break
    frame = imutils.resize(frame, width= 720)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = np.dstack([frame,frame,frame])
    
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.5, minNeighbors = 5)
    for(x,y,w,h) in faces:
        #print(x,y,w,h)
        roi_gray = gray[y:y+h, x:x+w] #(ycoord_start - ycoord_end)
        roi_color = frame[y:y+h, x:x+w]
        img_item = "my-image.png"
        cv2.imwrite(img_item, roi_color)

        color = (255,0,0) #BGR 
        stroke = 2
        end_cord_x = x + w
        end_cord_y = y + h
        cv2.rectangle(frame, (x,y),(end_cord_x, end_cord_y), color, stroke)

    cv2.putText(frame,"Slow method",(10,30),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,255,0),2)
    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()