"""
4. Handle camera frames and video files using cv2.VideoCapture
"""
import cv2
import argparse

# Reading camera frames:
parser = argparse.ArgumentParser()
parser.add_argument("camera_index", help=": Index of camera")
args = parser.parse_args()

capture = cv2.VideoCapture(int(args.camera_index))
# Default index will be 0 for connected webcam

frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = capture.get(cv2.CAP_PROP_FPS)

print(f"Frame_Width:{frame_width} Frame_Height:{frame_height}")
print("FPS :",fps)

if capture.isOpened()is False:
    print("Error while opening the camera")
frame_index = 0
while capture.isOpened():
    ret, frame = capture.read()

    if ret:
        cv2.imshow("Input from camera",frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Grayscale Input camera", gray)

        if cv2.waitKey(10)&0xFF == ord('c'):
            frame_name = "cam_{}.jpg".format(frame_index)
            gray_frame = "gray_cam_{}.jpg".format(frame_index)
            cv2.imwrite(frame_name, frame)
            cv2.imwrite(gray_frame, gray)
            frame_index += 1

        if cv2.waitKey(10)&0xFF == ord('q'):
            break
    else:
        break

capture.release()
cv2.destroyAllWindows()