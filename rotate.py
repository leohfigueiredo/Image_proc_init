import cv2
import matplotlib.pyplot as plt

# read the image in grayscale
img = cv2.imread("Lenna.png", 0)
rows, cols = img.shape

# rotate for 45 degree counter-clockwise respect to the center of the image
M = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 1)
dst = cv2.warpAffine(img, M, (cols, rows))

# display image
plt.figure()
plt.imshow(dst, cmap="gray")
plt.show()
