import cv2

imgpath = "/home/pi/Dataset/pills.tif"
img = cv2.imread(imgpath)

cv2.namedWindow('PILLS', cv2.WINDOW_AUTOSIZE)

cv2.imshow('PILLS', img)
cv2.waitKey(0)
cv2.destroyWindow('PILLS')
