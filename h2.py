from sys import flags
import numpy as np
import cv2 as cv
import time
from  drange import *
 
 
 
 
# Create a black image
w = 1500
h = w
# img = np.zeros((h,w,3), np.uint8)
# # cv.line(img,(0,0),(200,400),(255,0,0),5)
# cv.rectangle(img,(384,0),(510,128),(0,255,0),3)

     
# font
font = cv.FONT_HERSHEY_PLAIN
# org
org = (50, 50)
# fontScale
fontScale = 1.5
# Blue color in BGR
color = (255, 255, 0)
# Line thickness of 2 px
thickness = 1
   
name = 'HWindow'
cv.namedWindow(name, cv.WINDOW_KEEPRATIO)
# cv.namedWindow(name, cv.WINDOW_OPENGL)

cv.setWindowProperty(name, cv.WINDOW_GUI_EXPANDED, 1)

img = np.zeros((h,w,3), np.uint8)
to=time.time()
ts = 1

txt=""

for i in drange (50,1000,.5):
    # img = np.zeros((h,w,3), np.uint8)
    img = img*0

    cv.putText(img, txt, org, font, 
                   fontScale, color, thickness, cv.LINE_AA)
    q = int(w/2)
    ii = int(i)
    cv.rectangle(img,(q-ii,q-ii),(q+ii,q+ii),(0,255,200),3) 
    cv.imshow( name , img)
    k = cv.waitKey(ts)  
    t=time.time()
    # print( "Time Step : {0:8.3f}".format(t-to))
    txt = "Time Step : {0:8.3f}".format(t-to)
    to=t
    if k == 27 or k==32:
        break



# k = cv.waitKey(0)     
# if k == ord("s"):
#     cv.imwrite("starry_night.png", img)