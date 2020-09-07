import cv2

imgpath = "/home/pi/Dataset/pills.tif"
img = cv2.imread(imgpath)

outpath = "/home/pi/test.png"
cv2.imwrite(outpath, img)
