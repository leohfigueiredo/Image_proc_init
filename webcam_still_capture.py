import cv2
import matplotlib.pyplot as plt


cap = cv2.VideoCapture(0)

if cap.isOpened():
    ret, frame = cap.read()
    print(ret)
    print(frame)
else:
    ret = False

print(type(frame))


img1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #convert color


plt.imshow(img1)
windowName = 'IMAGE WEBCAM'
plt.title('Webcam snapshot')
plt.show()

cap.release()
