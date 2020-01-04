"""
1. Accessing and Manipulating Pixels in OpenCV with BGR(COLOR) and Grayscale Images:
"""
import cv2
## 1.
# Read the COLOR Image
img = cv2.imread("sasuke.jpg")

# Read properties of image like shape which gives row, col and channels
dimensions = img.shape
print("Dimensions:",dimensions)
# for height*width*channels
elements = img.size
print("Elements:",elements)
# for image datatype or type of image
img_dtype = img.dtype
print("Image Type:",img_dtype)
# Show the image
cv2.imshow("Title of window",img)
# binding function to wait till keyboard button event
# 0 means indefinite time or till a keystroke
cv2.waitKey(0)

# OpenCV uses BGR format
# Hence while extracting the pixel values from image, maintain the
# following order. pixel coordinates are img[x=width ,y=height, ChannelIndex].
# This gives all channel values of a pixel
(b,g,r) = img[dimensions[0]//2,dimensions[1]//2]
print(f"B:{b} G:{g} R:{r}")
# If we need specific color channel value of particular pixel
# For example, Blue (index 0)
# In image, channels can be accessed through their index
# In Following command, third parameter is the channel Index
blue = img[dimensions[0]//2,dimensions[1]//2,0]
print("Blue Pixel Value:",blue)
# We can manipulate and replace the pixel value
img[dimensions[0]//2,dimensions[1]//2] = (0,0,255)   # This will make that pixel red colored

# We can also access the region of image instead of just a pixel.
top_left_corner = img[0:dimensions[0]//2, 0:dimensions[1]//2]
cv2.imshow("Top left corner",top_left_corner)
cv2.waitKey(0)

###################################################

# For Grayscale Image
# Second argument is to read the image in the particular color type.
gray_img = cv2.imread("selfie.jpg",cv2.IMREAD_GRAYSCALE)

g_dimensions = gray_img.shape
print("Gray Image dimensions",g_dimensions)

# Most of the things are same as above
# Replace the color of pixel with black
gray_img[g_dimensions[0]//2,g_dimensions[0]//2] = 0     # 0 means black

###################################################
