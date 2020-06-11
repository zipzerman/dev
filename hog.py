import dlib
import cv2
from imutils import face_utils
from imutils.video import VideoStream
import imutils
import time

detector = dlib.get_frontal_face_detector()

print("->Starting Face Dectection")
c= VideoStream(src="rtsp://admin:ThaiRun1234@192.168.1.104:554/Streaming/channels/101").start()
time.sleep(2.0)

while True:
    frame = c.read()
    frame = imutils.resize(frame, width=720)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    rects = detector(gray, 0)

    for rect in rects:
        x1 = rect.left()
        y1 = rect.top()
        x2 = rect.right()
        y2 = rect.bottom()
        frame = cv2.rectangle(frame, (x1,y1), (x2,y2), (255,0,0),2)
    cv2.imshow("Frame",frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break