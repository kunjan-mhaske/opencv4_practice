"""
Calculate FPS from Video Input
"""

import cv2
import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument("camera_index", help=": Index of camera input")
args = parser.parse_args()

capture = cv2.VideoCapture(int(args.camera_index))

if not capture.isOpened():
    print("Error in camera opening")

while capture.isOpened():
    ret, frame = capture.read()
    if ret:
        processing_start = time.time()
        cv2.imshow("Input frame from camera", frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Gray frame from camera", gray)

        if cv2.waitKey(10)&0xFF == ord('q'):
            break
        processing_stop = time.time()
        print("FPS:",1.0/(processing_stop-processing_start))
    else:
        break
capture.release()
cv2.destroyAllWindows()
