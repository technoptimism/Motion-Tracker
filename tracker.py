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

def selectROI(event, x, y, flags, param):
    
    # grab the reference to the current frame, list
    # of ROI points, and weather or not it is ROI selection
    # mode

    global frame, roiPts, inputMode

    # If we are in ROI selection mode, the mouse was clicked,
    # and we do not already have four points, then update 
    # the list of ROI ppoints within the (x, y) location
    # of the click and draw the circle
    if inputMode and event == cv2.EVENT_LBUTTON and len(roiPoints) < 4:
        roiPoints.append((x, y))
        cv2.circle(frame, (x, y), 4, (0, 255, 0), 2)
        cv2.imshow("frame", frame)

def main():
    # Construct the argument oarser and parse the argument
    ap = argparse.ArgumantParser()
    ap.add_argument("-v", "--video",
                    help = "path to the (optional) video file")
    args = vars(ap.parse_args())

    # Grab the reference to the current frame, list of ROI points, and whether or not 
    # we are in ROI selection mode

    global frame, roiPts, inputMode

    # If the video path was not supplied, grab the reference to the camera
    
    if not args.get("video", False):
        camera = cv2.VideoCapture(0)
    
    # Otherwise load the video
    else:
        camera = cv2.VideoCapture(args["video"])

    # Setup the mouse callback
    cv2.namesWindow("frame")
    cv2.setMouseCallback("frame", selectROI)

    # Initialize the termination criteria for cam shift, indicating a maximum of ten iterations of movement by atleast one pixel
    # Along with the bounding box of the ROI
    
    termination = (cv2.TERM_CRITERIA_EPS) | cv2.TERM_CRITERIA_COUNT, 10, 1)
    roiBox = None

    
