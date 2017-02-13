/* http://www.pyimagesearch.com/2015/11/09/pedestrian-detection-opencv/

COMMAND LINE
# import the necessary packages
from __future__ import print_function
from imutils.object_detection import non_max_suppression
from imutils import paths
import numpy as np
import argparse
import imutils
import cv2
 
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", required=True, help="path to images directory")
args = vars(ap.parse_args())
 
# initialize the HOG descriptor/person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

$ pip install imutils
$ pip install --upgrade imutils */

// ------------------------------------

#!/usr/bin/env python


import cv2
import time
import os
import time

count = 0
while(count < 1):

	cam = cv2.VideoCapture(0)
	#cam.set(3, 4608.)
	#cam.set(4, 3072.)

	cam.set(3, 1920.)
	cam.set(4, 1080.)
	#cam.set(15, 0.20)

	s, im = cam.read() # captures image
	cv2.namedWindow('image',cv2.WINDOW_NORMAL)
	cv2.resizeWindow('image', 600,600)
	cv2.imshow("image", im)
	
	cv2.waitKey(3000)
	#cv2.imshow("Test Picture", im) # displays captured image
	count = count + 1
	cv2.destroyAllWindows()
	del(cam)
#cv2.waitKey(500)

img = time.strftime("%d-%m-%Y") + "_" + time.strftime("%I:%M:%S") + ".bmp"

cv2.imwrite(img,im) # writes image test.bmp to disk

mvimg = "mv "+ img +" ~/Desktop/detect/images"

os.system(mvimg)
  
  // ------------------------------------
  
// $ python detect.py --images images
