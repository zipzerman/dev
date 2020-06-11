import dlib
import cv2
from imutils import face_utils
from imutils.video import VideoStream
import imutils
import time

cnn_face_detector = dlib.cnn_face_detection_model_v1(r"C:\Users\junecsnp\dev\mmod_human_face_detector.dat")

print("->Starting Face Dectection")
c= VideoStream(src="rtsp://admin:ThaiRun1234@192.168.1.104:554/Streaming/channels/101").start()
time.sleep(2.0)

while True:
    frame = c.read()
    frame = imutils.resize(frame, width=720)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces_cnn = cnn_face_detector(gray, 0)

    for face in faces_cnn:
        x1 = face.rect.left()
        y1 = face.rect.top()
        x2 = face.rect.right()
        y2 = face.rect.bottom()
        frame = cv2.rectangle(frame, (x1,y1), (x2,y2), (255,0,0),2)
    cv2.imshow("Frame",frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break