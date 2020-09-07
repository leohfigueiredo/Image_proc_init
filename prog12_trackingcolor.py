import cv2
import numpy as np


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
    cv2.namedWindow('Original', cv2.WINDOW_NORMAL)
    cv2.namedWindow('Mask', cv2.WINDOW_NORMAL)
    cv2.namedWindow('Blue Objects', cv2.WINDOW_NORMAL)


    cv2.resizeWindow('Original', 600,600)
    cv2.imshow('Original', frame)

    cv2.resizeWindow('Mask', 600,600)
    cv2.imshow('Mask', image_mask)

    cv2.resizeWindow('RED Objects', 600,600)
    cv2.imshow('RED Objects', output)


   
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
cap.release()
