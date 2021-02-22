# **************************************************************************** #
# Air Hockey Table Project

# Author: Oscar Carreon
# -------------------------

#This Code is Created for UCR's EE175 Senior Design Project

# This Code contains The Open CV Files

#For Pygame Documentation please see:
#https://www.pygame.org/docs/index.html

#For Pygame Documentation please see:
#https://docs.opencv.org/master/d6/d00/tutorial_py_root.html

# **************************************************************************** #


#packages for opencv lib
import numpy as np
import argparse
import cv2
import time
import imutils

## list like date structures.  Hold past locations and create tail
from collections import deque
from imutils.video import VideoStream
import serial

## packages from pygames code
from pygame.math import Vector2
import pygame
## packages from TableObjcets/ Prediction code
from Constants import* #
from linex import*
from Puck import*
from Border import*
from Striker import*
#from Filtertest import*




#from Prediction import*
global predictlinepoint
global newstrikerlocation
predictlinepoint = (250,100) #check if removing global break it
print(predictlinepoint)
newstrikerlocation =[0,0]






ap = argparse.ArgumentParser()
## Buffer to define the size of deque shorter buffer shorter tail
ap.add_argument("-b", "--buffer", type=int, default=64, help="max buffer size")
args = vars(ap.parse_args())

## HSV vaules for color tracking
LowerColor = (35, 40, 0)
UpperColor = (102, 255, 255)

## intialize to the size of buffer
bufferpts = deque(maxlen=args["buffer"])
counter = 0
(dX, dY) = (0, 0)           # current spot
(deltaX, deltaY) = (0, 0)   # previous spot
(X_v, Y_v) = (0, 0)         # velocity

##pulling up webcam
vs = VideoStream(src=1).start()     #  1 sets it for extrenal cam
time.sleep(2.0)                     #  0 sets it for built it cam


#  **************** INSTANIATE BORDER OBJECTS ************************
#Declares Starting Postions for table Objects
border = Border(BORDER_POSITION[0],BORDER_POSITION[1])
puck = Puck(PUCK_POSITION[0],PUCK_POSITION[1])
striker = Striker(STRIKER_POSITION[0],STRIKER_POSITION[1])
#For test purposes
puck.addSpeed(0,0)
#*********************************************************




#  **************** Arduino Stuff  ************************
data_out = serial.Serial('COM5',9600)
data_out.timeout = 1
send2Arduino_x = 0
send2Arduino_y = 0
already_sent = False
# already_sent = input("reset, press 0")
#*********************************************************

#Deprecated Code
#a = Prediction((11,252),(16,131))



##loop to keep webcam open till q is pressed
while True:

    ##getting the current frame
    frame = vs.read()
    frame = frame[1] if args.get("video", False) else frame
    #not grabbing a frame --> break out
    if frame is None:
        break

    ##converting frame size to 600px
    ##getting rid of noise and blur video and changing to hsv values
    frame = imutils.resize(frame, width=600)
    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)


    #Mask configurations
    mask = cv2.inRange(hsv, LowerColor, UpperColor)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask,None, iterations=2)

    #locating the contours in mask and finding position x and y
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    middle = None
    #*************   Doing camera object dect stuff (magic) *********************
    if len(cnts) > 0:  #a conture was found
        outlineC = max(cnts, key=cv2.contourArea)  #outline
        ((x,y), radius) = cv2.minEnclosingCircle(outlineC)
        M = cv2.moments(outlineC)
        middle = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        if radius > 10:  ##check the radius size
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)


            # print(radius)


            cv2.circle(frame, middle, 5, (0, 0, 255), -1)
   # ********************** (Magic ^ )  *************************************


            bufferpts.appendleft(middle)  ##adding points to buffer, buffer holds the points

    #******************** Building buffer (Magic) ***************************
    	# loop over the set of tracked points
    for i in np.arange(1, len(bufferpts)):
		# if either of the tracked points are None, ignore
		# them
        if bufferpts [i - 1] is None or bufferpts [i] is None:
            continue
		# check to see if enough points have been accumulated in
		# the buffer
        if counter >=10 and i== 1 and len(bufferpts) >= 10 and bufferpts[-10] is not None:

            dX = bufferpts[i][0]
            dY = bufferpts[i][1]
            deltaX = bufferpts[i-5][0]
            deltaY = bufferpts[i-5][1]

            X_v = dX - deltaX
            Y_v = dY - deltaY

            #  **************** Prediction Stuff  ************************
            striker.StrikerEyes()
            puck.updatePosition(dY,dX)
            # print(predictlinepoint)
            predictlinepoint = puck.coordinate(border)
            # print(predictlinepoint)
            
            puck.getTrajectory() #might not be needed
            newstrikerlocation = puck.strikercorr(striker) #should be a list[x,y]
            puck.addSpeed(0,0) #probally does nothing remove

            puck.declareVelocity((X_v,Y_v))
            
            # updatedrawpos() #Might do nothing/ Might mess up code #test Removal
            
            # puck.bounceb(border) # Might not be necessary #test removal
            #depreciated Code
            #predectedpoint =  a.getPredictionLine((dX,dY),(191,16),(X_v,Y_v))
            #*********************************************************


		# draw the connecting lines
        thickness = int(np.sqrt(args["buffer"] / float(i + 1)) * 2.5)
        cv2.line(frame, bufferpts[i - 1], bufferpts[i], (0, 0, 255), thickness)

#************************** Arduino stuff *****************************
        if ( (newstrikerlocation[0] < 60 and newstrikerlocation[0] > 0) ) and ( (newstrikerlocation[1]) > 131 and ( newstrikerlocation[1] < 256)) :
            if newstrikerlocation[1] >= 150 and newstrikerlocation[1] <= 183:
                if send2Arduino_x != 1:
                    send2Arduino_x = 1
                    #data_out.write(str(send2Arduino).encode())
                    # print("fourth loop s2A = ", send2Arduino_x)

            if newstrikerlocation[1] > 183 and newstrikerlocation[1] <= 217:
                if send2Arduino_x != 2:
                    send2Arduino_x = 2
                    #data_out.write(str(send2Arduino).encode())
                    # print("fifth loop s2A = ", send2Arduino_x)
            if newstrikerlocation[1] > 217 and newstrikerlocation[1] <= 253:
                if send2Arduino_x != 3:
                    send2Arduino_x = 3
                    #data_out.write(str(send2Arduino).encode())
                    # print("sixth loop s2A = ", send2Arduino_x)
            if newstrikerlocation[1] > 253 and newstrikerlocation[1] <= 285:
                if send2Arduino_x != 4:
                    send2Arduino_x = 4
                    #data_out.write(str(send2Arduino).encode())
                    # print("Seventh loop s2A = ", send2Arduino)
            if newstrikerlocation[0] >= 20 and newstrikerlocation[0] <= 43 :
                if send2Arduino_y != 5:
                    send2Arduino_y = 5
                    #data_out.write(str(send2Arduino).encode())
                    # print("first loop s2A = ", send2Arduino_y)
            if newstrikerlocation[0] > 43 and newstrikerlocation[0] <= 66:
                if send2Arduino_y != 6:
                    send2Arduino_y = 6
                    #data_out.write(str(send2Arduino).encode())
                    # print("Second loop s2A = ", send2Arduino_y)
            if newstrikerlocation[0] > 66 and newstrikerlocation[0] <= 90 :
                if send2Arduino_y != 7:
                    send2Arduino_y = 7
                    #data_out.write(str(send2Arduino).encode())
                    # print("Third loop s2A = ", send2Arduino_y)
        if( dX >500 and dX < 600):
            already_sent = False
        if (dX < 300  and already_sent == False) and (send2Arduino_x !=0 and send2Arduino_y != 0):
            print("x coor sent: ",send2Arduino_x)
            print("y coor sent: ",send2Arduino_y)
         
            data_out.write(str(send2Arduino_x).encode())    
            data_out.write(str(send2Arduino_y).encode())
            # data_out.close()
            already_sent = True;    
                    
                    
                    
                    
        # if dX<300:
        #     data_out.write(str(dX).encode())   ##sending it to arduino encoding it to bytes


        # print(data_out.readline().decode('ascii'))

            # time.sleep(0.001)
    # print(data_out.readline().decode('ascii')) #decoding from bytes to dec


    # print(data_out.readline().decode('ascii'))
    # print(dX)

#**************************************************************************
    #predicted_x = int(predectedpoint[0])
    #predicted_y = int(predectedpoint[1])

#******************************* (Debuging code printing to frame  and terminal ************************
    #print(predicted_y)
    #print(predicted_x)

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, "X: {}, y: {}".format(dX, dY), (10, frame.shape[0] -10), font, 1, (255,255,255), 2)
    # cv2.putText(frame, "dX: {}, dy: {}".format(deltaX, deltaY), (100, frame.shape[0] -100), font, 1, (255,255,255), 2)
    # cv2.putText(frame, "v_x: {}, v_y: {}".format(X_v, Y_v), (150, frame.shape[0] -150), font, 1, (255,255,255), 2)
    # cv2.putText(frame, "predictedlinepoint: {}".format(predictlinepoint), (125, frame.shape[0] -125), font, 1, (255,255,255), 2)
    # #cv2.putText(frame, "predicted point: {}".format(predectedpoint[1]), (125, frame.shape[0] -125), font, 1, (255,255,255), 2)

    #cv2.line(frame,(dX,dY),(predicted_x,predicted_y),(255,0,0),3)

#*******************************************BORDER LINES*********************************************************
    cv2.line(frame,(border.x,border.y),(border.x + 1,border.y +FACE_WIDTH+1),(0,0,255),3)
    cv2.line(frame,(border.x,border.y),(border.x + FACE_LENGTH,border.y + 1),(0,0,255),3)
    cv2.line(frame,(border.x + FACE_LENGTH,border.y),(border.x + FACE_LENGTH,border.y +FACE_WIDTH+1),(0,0,255),3)
    cv2.line(frame,(border.x,border.y+ FACE_WIDTH) ,(border.x + FACE_LENGTH + 1,border.y +FACE_WIDTH+1),(0,0,255),3)

    #TRAJEcTORY LINE
    cv2.line(frame,(dX,dY),(int(predictlinepoint[0]),int(predictlinepoint[1])),(255,0,0),3)
    #STRIKER EYES
    cv2.line(frame,(striker.centerxline[0]) ,(striker.centerxline[1]),(STRIKER_LINE_COLOR),3)
    cv2.line(frame,(striker.centeryline[0]) ,(striker.centeryline[1]),(STRIKER_LINE_COLOR),3)
    cv2.circle(frame, (int(newstrikerlocation[0]),int(newstrikerlocation[1])), 4,(255,0,0),3 )

    #print(predectedpoint)

#******************************************************************************************************************

 # show the frame to our screen


    cv2.imshow("Stryker's Eye", frame)
    key = cv2.waitKey(1) & 0xFF
    counter += 1
	# if the 'q' key is pressed, stop the loop
    if key == ord("q"):
        break

# if we are not using a video file, stop the camera video stream

if not args.get("video", False):
    vs.stop()
# otherwise, release the camera
else:
    vs.release()
# close all windows
cv2.destroyAllWindows()
