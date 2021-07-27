import cv2 as cv
import sys
img = cv.imread(cv.samples.findFile("IMG_002130.JPG"))
if img is None:
    sys.exit("Could not read the image.")

img[200:300,800:900]=0    
cv.imshow("Display window", img)
k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("starry_night.png", img)