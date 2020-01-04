## 2. View images using Matplotlib

import cv2
import matplotlib.pyplot as plt
import numpy as np

img_opencv = cv2.imread("sasuke.jpg")   # This loads image in BGR
b,g,r = cv2.split(img_opencv)           # This will split the channels
# cv2.split() is time consuming method. One should use Numpy arrays
# to perform image matrix manipulation.
# merge channel for matplotlib
img_matplotlib = cv2.merge([r,g,b])

# We can see multiple images in one window using subplot(m,n,p)
# m*n = rows*cols grid, p = where to put the image in grid

# Wrong representation of image using matplotlib (Opencv BGR)
plt.subplot(121)
plt.imshow(img_opencv)
plt.title("OpenCV Image")

# Right representation of image ( RGB )
plt.subplot(122)
plt.imshow(img_matplotlib)
plt.title("Matplotlib Image")

plt.show()

# Show images using OpenCV
cv2.imshow("BGR image",img_opencv)      # True color
cv2.imshow("RGB image",img_matplotlib)  # Wrong Color
cv2.waitKey(0)
cv2.destroyAllWindows()

# We can concatenate two images by concatenating two image matrices
# using numpy arrays concatenate method
# Axis = 0 means stack vertically, 1 means horizontally
img_concat = np.concatenate((img_opencv, img_matplotlib), axis=1)
cv2.imshow("BGR and RGB images",img_concat)
cv2.waitKey(0)
cv2.destroyAllWindows()

# We can use Numpy to manipulate the Image matrix
# Get the three channels
B = img_opencv[:,:,0]
G = img_opencv[:,:,1]
R = img_opencv[:,:,2]

# Transform the BGR to RGB using Numpy
img_RGB = img_opencv[:,:,::-1]

cv2.imshow("RGB image (wrong Colors)",img_RGB)
cv2.waitKey(0)
cv2.destroyAllWindows()
