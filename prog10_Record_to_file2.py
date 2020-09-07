import cv2

windowName = "Live Video Feed"
cv2.namedWindow(windowName)
cap = cv2.VideoCapture(0)

filename = 'output.avi'

# http://www.fourcc.org/codecs.php
codec = cv2.VideoWriter_fourcc('M', 'P', 'E', 'G') #fourcc codec - cc - 4 caracter code

framerate = 120
resolution = (2592, 1944)

Output = cv2.VideoWriter(filename, codec, framerate, resolution)

if cap.isOpened():
    ret, frame = cap.read()
else:
    ret = False

while ret:

    ret, frame = cap.read()
    output = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    Output.write(frame)

    cv2.imshow(windowName, frame)

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
cap.release()










    










    
