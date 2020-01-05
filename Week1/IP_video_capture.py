"""
Capture the IP camera frames
URL : http://video-relay.sinergiainformatica.net/mollE.m3u8
"""

import cv2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("ip_url", help=": URL of IP Camera")
args = parser.parse_args()

capture = cv2.VideoCapture(args.ip_url)

if not capture.isOpened():
    print("Error in opening IP Camera")

while capture.isOpened():
    ret, frame = capture.read()
    if ret:
        cv2.imshow("IP camera",frame)
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("Gray IP Camera", gray)

        if cv2.waitKey(10)&0xFF == ord('q'):
            break
    else:
        break

capture.release()
cv2.destroyAllWindows()
