# **************************************************************************** #
# Air Hockey Table Project

# Author: Ricardo Valverde
# -------------------------

#This Code is Created for UCR's EE175 Senior Design Project

# This Code contains The Timing Aspect

#For Pygame Documentation please see:
#https://www.pygame.org/docs/index.html

# **************************************************************************** #
import math
import pygame
from pygame.math import Vector2
import numpy as np

def distance(point1 , point2):
    x1 = point1[0]
    x2 = point2[0]
    y1 = point1[1]
    y2 = point2[1]

    xval = (x1 - x2)**2
    yval = (y1 - y2)**2
    disx = math.isqrt(int(xval))
    disy = math.isqrt(int(yval))

    return Vector2(disx,disy)



def sometime(vel,dis):
    try:
        xtime = dis[0]/vel[0]
    except:
        xtime = 0

    try:
        ytime = dis[1]/vel[1]
    except:
        ytime = 0

    return Vector2(xtime,ytime)

def calculateVelocity(dis,time):
    xvel = round( dis[0]/time[0])
    yvel = round(dis[1]/time[1])

    return Vector2(xvel,yvel)

pointss = [10,1]

point1 = [5,5]
point2 = [10,10]

#print(distance(point1,point2))

vel = [4 ,5]
dis = distance(point1,point2)
diss = distance(pointss,point2)


#print(sometime(vel,dis))
tim = sometime(vel,dis)

print(calculateVelocity(diss,tim))
