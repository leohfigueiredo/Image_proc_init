import cv2

cv2.namedWindow('Live Video Feed', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Live Video Feed', 640,640)
windowName = "Live Video Feed"
cv2.namedWindow(windowName)
cap = cv2.VideoCapture(0)

if cap.isOpened():
    ret, frame = cap.read()
else:
    ret = False

while ret:

    ret, frame = cap.read()
    output = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.namedWindow('gray', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('gray', 640,640)
    cv2.imshow('gray', output)

    
    cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('frame', 640,640)
    cv2.imshow(windowName, frame)

    if cv2.waitKey(1) == 27: # esc press
        break

cv2.destroyAllWindows()
cap.release()
