import cv2

imgpath = "/home/pi/Dataset/brandyrose.tif"
img = cv2.imread(imgpath, 0)

cv2.namedWindow('kROSE', cv2.WINDOW_AUTOSIZE)

cv2.imshow('ROSE', img)
cv2.waitKey(0)
cv2.destroyWindow('ROSE')
