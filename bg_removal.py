## Check time required
import time
time_start = time.time()

## default
import sys
import argparse as ap

## opencv
import cv2

## moviepy
from moviepy.editor import *

import numpy as np

parser = ap.ArgumentParser()
parser.add_argument('-f', "--videoFile", help="Path to Video File")

args = vars(parser.parse_args())

if args["videoFile"] is not None:
    video_file_name = args["videoFile"]
else:
    print("You have to input videoFile name")
    sys.exit(1)

video_file_route = 'testset/' + video_file_name
video = cv2.VideoCapture(video_file_route)

if not video.isOpened():
    print("Video doesn't opened!")
    sys.exit(1)

video_width = int(video.get(3))
video_height = int(video.get(4))
video_fps = 1 / video.get(2)

fgbg = cv2.createBackgroundSubtractorMOG2()

frame_output_list = []

while(1):
    ret, frame = video.read()
    if ret == False:
        break

    frame_output = fgbg.apply(frame)

    frame_output_numpy = np.asarray(frame_output)

    frame_output_list.append(frame_output_numpy)

video_output = ImageSequenceClip(frame_output_list, fps=video_fps)
video_name = video_file_name.split('.')[0]
video_output.write_videofile("testset/" + video_name + "_bgrm.mp4", fps=video_fps, progress_bar=False)

print("Total time required(s): " + str(time.time() - time_start))
