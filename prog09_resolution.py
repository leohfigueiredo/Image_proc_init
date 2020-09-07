import cv2

windowName = "Live Video Feed"
cv2.namedWindow(windowName)
cap = cv2.VideoCapture(0)

print('Width : ' + str(cap.get(3)))
print('Height : ' + str(cap.get(4)))

cap.set(3, 640)
cap.set(4, 480) #resolution

print('Width : ' + str(cap.get(3)))
print('Height : ' + str(cap.get(4)))

if cap.isOpened():
    ret, frame = cap.read()
else:
    ret = False

while ret:

    ret, frame = cap.read()
    output = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('gray', output)

    cv2.imshow(windowName, frame)

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
cap.release()










    
