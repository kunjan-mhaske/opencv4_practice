"""
3. Handle Files and Images using argparse library of python
"""
import cv2
import argparse

# This parser will contain the information about arguments
# needed while running this program.
parser = argparse.ArgumentParser()
parser.add_argument("input_path", help=": path of input image")
parser.add_argument("output_path",help=": path of output image")
args = parser.parse_args()

# Load image using argument from parser
image_input = cv2.imread(args.input_path)

cv2.imshow("BGR Image",image_input)
cv2.waitKey(0)

# Convert input image to GRAY
gray_image = cv2.cvtColor(image_input, cv2.COLOR_BGR2GRAY)

cv2.imshow("Gray Image", gray_image)
cv2.waitKey(0)

# Save image to the disk
cv2.imwrite(args.output_path,gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

