from picamera.array import PiRGBArray #Comandos para pi Camera
from picamera import PiCamera

import time
import cv2
import numpy as np


camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 3
rawCaputre = PiRGBArray(camera, size=(640, 480))

time.sleep(0.1)

for frame in camera.capture_continuous(rawCaputre, format="bgr", use_video_port=True): #bgr pi camera format
    image = frame.array
    frame = image
    rawCaputre.truncate(0)


    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #Hue, Saturation and Value

    low = np.array([100, 150, 0], np.uint8)
    high = np.array([140, 255, 255], np.uint8)

    image_mask = cv2.inRange(hsv, low, high)
    output = cv2.bitwise_and(frame, frame, mask = image_mask)

    cv2.namedWindow('Original', cv2.WINDOW_NORMAL)
    cv2.namedWindow('Mask', cv2.WINDOW_NORMAL)
    cv2.namedWindow('Blue Objects', cv2.WINDOW_NORMAL)

    cv2.resizeWindow('Original', 320,320)
    cv2.imshow('Original', frame)

    cv2.resizeWindow('Mask', 320,320) 
    cv2.imshow('Mask', image_mask)

    cv2.resizeWindow('Blue Objects', 320,320)
    cv2.imshow('Blue Objects', output)

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()

