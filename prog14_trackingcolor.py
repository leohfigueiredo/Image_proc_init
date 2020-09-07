from picamera.array import PiRGBArray
from picamera import PiCamera
import time

import cv2
import numpy as np

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
# allow the camera to warmup
time.sleep(0.1)



# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image - this array
	# will be 3D, representing the width, height, and # of channels
	frame = frame.array
	
cap = cv2.VideoCapture(0)
if cap.isOpened():
    ret, frame = cap.read()
else:
    ret = False         

while ret:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    low = np.array([0, 50, 50])
    high = np.array([179, 255, 255])

    image_mask = cv2.inRange(hsv, low, high)
    output = cv2.bitwise_and(frame, frame, mask = image_mask)


    cv2.imshow('Original', frame)


    cv2.imshow('Mask', image_mask)


    cv2.imshow('RED Objects', output)


           
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
cap.release()
