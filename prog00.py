import cv2

imgpath = "/home/pi/Dataset/bear.tif"
img = cv2.imread(imgpath)

print(type(img))

cv2.imshow('BEAR', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
