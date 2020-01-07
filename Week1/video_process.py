"""
Read and Process the Video File forward and backward.
"""
import cv2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("video_path", help=": Path of input video")
parser.add_argument("output_path", help=": Path of output video")
args = parser.parse_args()

capture = cv2.VideoCapture(args.video_path)
if not capture.isOpened():
    print("Error. Video not opened")

while capture.isOpened():
    ret, frame = capture.read()
    if ret:
        cv2.imshow("Original Frame", frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Original Gray Frame", gray)

        if cv2.waitKey(10)&0xFF == ord('q'):
            break
    else:
        break

# FourCC is a 4-byte code for video codec
# ex: XVID codec for .avi format file
#     mp4v codec for .mp4 format file
# PS: It is platform Dependent. So, confirm it, if not working.
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = int(capture.get(cv2.CAP_PROP_FPS))
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))

# Last argument True for Color and False for Grayscale
out = cv2.VideoWriter(args.output_path, fourcc, fps,(width,height), True)
print("Showing and saving video in backwards")

frame_index = capture.get(cv2.CAP_PROP_FRAME_COUNT) - 1
print(f"Starting in frame:{frame_index}")

while capture.isOpened() and frame_index >= 0:
    capture.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
    ret, frame = capture.read()

    if ret:
        print(f"Current index:{frame_index}")
        print(f"Current Frame in Milliseconds:{capture.get(cv2.CAP_PROP_POS_MSEC)}")
        cv2.imshow("Original Frame", frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Gray Frame", gray)
        out.write(frame)
        frame_index -= 1
        print()

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    else:
        break

capture.release()
out.release()
cv2.destroyAllWindows()
