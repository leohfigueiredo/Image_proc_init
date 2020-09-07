import cv2
import matplotlib.pyplot as plt

imgpath = "/home/pi/Dataset/bear.tif"
img = cv2.imread(imgpath, 0)

plt.imshow(img)
plt.title('Greyscale Image - Default Colormap')
plt.show()

plt.imshow(img, cmap='gray')
plt.title('Greyscale Image - Gray Colormap')
plt.show()

imgpath = "/home/pi/Dataset/bear.tif"
img = cv2.imread(imgpath, 1) #RGB mode

plt.imshow(img)
plt.title('Color Image(BGR) - Default Colormap')
plt.show()

img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(img1)
plt.title('Color Image(RGB) - Default Colormap')
plt.show()

j = 0
for filename in dir(cv2):
    if filename.startswith('COLOR_'):
        print(filename)
        j = j + 1

print('There are '+ str((j+1)) + ' color conversion flags in OpenCV ' + cv2.__version__)


