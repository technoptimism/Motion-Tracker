# Import necessary packeges

import numpy as np 
import argparse
import cv2

# Initialize the current frame of the video, along
# with the list of ROI points along with whether or not
# this is input mode

frame = None
roiPoints = []
inputMode = False
